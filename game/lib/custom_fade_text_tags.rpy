init python hide:
    def fade(tag, argument, contents):
        new = []
        tags = 0

        if ',' in argument:
            start, end = [float(x) for x in argument.split(',', 1)]
            delta = end - start
            new.append((renpy.TEXT_TAG, 'alpha={}'.format(start)))
            tags += 1
        else:
            delta = float(argument)

        amount = sum(len(s) for (t, s) in contents if t == renpy.TEXT_TEXT)
        step = delta / amount

        for (type, value) in contents:
            if type == renpy.TEXT_TEXT:
                for c in value:
                    new.append((renpy.TEXT_TAG, 'alpha=+{}'.format(step)))
                    new.append((renpy.TEXT_TEXT, c))
                    tags += 1
            else:
                new.append((type, value))

        for _ in range(tags):
            new.append((renpy.TEXT_TAG, '/alpha'))

        return new

    def fade_size(tag, argument, contents):
        new = []
        tags = 0

        if ',' in argument:
            start, end = [int(x) for x in argument.split(',', 1)]
            delta = float(end - start)
            new.append((renpy.TEXT_TAG, 'size={}'.format(start)))
            tags += 1
        else:
            delta = float(argument)

        amount = sum(len(s) for (t, s) in contents if t == renpy.TEXT_TEXT)
        step = delta / amount
        intermediate = 0

        for (type, value) in contents:
            if type == renpy.TEXT_TEXT:
                for c in value:
                    intermediate += step
                    if round(intermediate) >= 1:
                        increment = int(round(intermediate))
                        intermediate -= increment
                        new.append((renpy.TEXT_TAG, 'size=+{}'.format(increment)))
                        tags += 1
                    new.append((renpy.TEXT_TEXT, c))
            else:
                new.append((type, value))

        for _ in range(tags):
            new.append((renpy.TEXT_TAG, '/size'))

        return new

    config.custom_text_tags['fade'] = fade
    config.custom_text_tags['fadesize'] = fade_size
