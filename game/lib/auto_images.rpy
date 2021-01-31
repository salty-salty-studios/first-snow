init -1 python:
    ## Helper function to automatically define images from a folder.
    import re
    import itertools

    AUTO_IMAGE_REGEXP = re.compile('\.(jpe?g|png|gif|bmp|webp)$')

    # Load all images from a certain directory.
    def define_image(name, image, **transforms):
        if transforms:
            renpy.image(name, Transform(image, **transforms))
        else:
            renpy.image(name, image)

    def define_images(dir, base_name=None, variants={}, **transforms):
        if not base_name:
            base_name = []

        images = []

        for entry in renpy_listdir(dir):
            name = base_name + entry.split('_')
            path_ = renpy_join(dir, entry)

            if renpy_isdir(path_):
                images.extend(define_images(path_, name, variants=variants, **transforms))
            elif AUTO_IMAGE_REGEXP.search(path_):
                # Remove extension.
                id = AUTO_IMAGE_REGEXP.sub('', ' '.join(name))
                nid = name[0].rsplit('.', 2)[0]
                if nid in sprite_offsets.keys():
                    tf = transforms.copy()
                    tf['yoffset'] = sprite_offsets[nid]
                else:
                    tf = transforms

                define_image(id, path_, **tf)
                images.append(id)

                for variant_name, variant_func in variants.items():
                    variant_id = id + ' ' + variant_name
                    define_image(variant_id, variant_func(id, path_), **tf)
                    images.append(variant_id)
        
        return images

    def FittingComposite(parts):
        img = Fixed(xfit=True, yfit=True)
        for widget in parts:
            img.add(widget)
        return img

    def define_dynamic_images(dir, base_name=None, variants={}, **transforms):
        if not base_name:
            base_name = []

        images = []

        # iterate over all base folders...
        for base in renpy_listdir(dir):
            bpath = renpy_join(dir, base)
            if not renpy_isdir(bpath):
                continue

            bname = base_name + base.split('_')
            parts = []
            # iterate over all the attribute/parts/layer folders...
            for part in renpy_listdir(bpath):
                ppath = renpy_join(bpath, part)
                if not renpy_isdir(ppath):
                    continue

                # is part optional?
                if part.startswith('_'):
                    parts.append([None])
                    # make sure optionals sort last
                    part = 'z' + part
                else:
                    parts.append([])

                # find all the images!
                for x in renpy_listdir(ppath):
                    if AUTO_IMAGE_REGEXP.search(x):
                        name = AUTO_IMAGE_REGEXP.sub('', x)
                        parts[-1].append((part, name, renpy_join(ppath, x)))

                # no images found in this folder? don't count it at all
                if not parts[-1] or parts[-1] is None:
                    del parts[-1]

            if base in sprite_offsets.keys():
                tf = transforms.copy()
                tf['yoffset'] = sprite_offsets[base]
            else:
                tf = transforms

            # iterate over all possible cross-combinations and create the images!
            for combo in itertools.product(*parts):
                combo = sorted(v for v in combo if v is not None)
                pname = [name for (_, name, _) in combo]

                id = ' '.join(bname + pname)
                img = FittingComposite(file for (_, _, file) in combo)
                define_image(id, img, **tf)
                images.append(id)

                for vname, vfunc in variants.items():
                    vid = id + ' ' + vname
                    vimg = FittingComposite(vfunc(id, file) for (_, _, file) in combo)
                    define_image(vid, vimg, **tf)
                    images.append(vid)

        return images


    def apply_image_variants(name, func, base_name=None):
        for image_name in renpy.list_images():
            if base_name and not image_name.startswith(base_name):
                continue
            image = ImageReference(image_name)
            variant = func(image_name, image)
            renpy.image(image_name + ' ' + name, variant)
