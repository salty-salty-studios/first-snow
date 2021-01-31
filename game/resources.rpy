# resources.rpy
# Contains all resources: sprites, backgrounds, characters...

# Characters.
define adv = Character(None, ctc=DynamicDisplayable(ctc), ctc_position="fixed")
define narrator = Character(None, what_style='say_thought')

# Dynamically load sprites and backgrounds.
init python:
    sprite_offsets = {
        'rose': 410,
        'rose_right': 410,
        'eileen': 380,
        'eileen_right': 380,
        'caprice': 450,
        'millie': 420,
        'millie_right': 420,
        'michael': 380,
        'eve': 300,
        'wallace': 370,
        'wallace_right': 370
    }

    for package in [None] + store.dlc_packages:
        if package:
            pfx = 'dlc/' + package + '/'
        else:
            pfx = ''

        define_dynamic_images(pfx + 'sprites', yanchor=0.5, variants={'blur': vblur})
        define_images(pfx + 'sprites-static')

        define_images(pfx + 'bgs', ['bg'], xalign=0.5, yalign=0.5, variants={'blur': vblur})
        define_images(pfx + 'cgs', ['cg'], xalign=0.5, yalign=0.5)

        define_images(pfx + 'vfx', ['misc'])
        define_images(pfx + 'vfx/cutins', ['cutin'])
        define_images(pfx + 'vfx/title', ['title'])
        define_images(pfx + 'vfx/notes', ['note'])

# Sepia and blur filters
init python:
    sepia_images = [
        'bg downtown park',
        'bg colorado town HD',
        'bg colorado house ext',
        'bg colorado hiking2',
        'cg act2 kiss after',
        'cg act3 swings foreground',
        'cg act3 swings2',
        'cg act1 eileenpainting',
        'misc rendered eileen first meeting',
        'misc rendered eileen painting flashback',
        'misc rendered eileen physical flashback',
        'misc rendered eileen hiking flashback',
        'misc rendered eileen leaving colorado',
    ]

    blur_images = [
        ('bg aptallison outside', 1.0),
        ('bg aptallison outside night', 2.0),
        ('bg aptallison livingroom', 2.0),
        ('bg aptallison livingroom', 5.0),
        ('bg aptallison road dusk', 4.0),
        ('bg apteileen livingroom', 2.0),
        ('bg apteileen livingroom HD', 2.0),
        ('bg apteileen livingroom HD', 5.0),
        ('bg apteileen livingroom messy', 2.0),
        ('bg apteileen livingroom messy norabbit', 2.0),
        ('bg apteileen livingroom messy HD', 4.0),
        ('bg buildingmisc generichall', 2.0),
        ('bg buildingmisc library', 2.0),
        ('bg buildingmisc library HD', 2.0),
        ('bg buildingart art dusk', 2.0),
        ('bg buildingart art dusk siren', 1.0),
        ('bg buildingart art dusk womanwip', 1.0),
        ('bg buildingart art dusk bustsketch', 2.0),
        ('bg buildingart hallway2f dusk HD', 2.0),
        ('bg buildingunion outside snow', 2.0),
        ('bg cafe inside', 2.0),
        ('bg cafe inside HD', 2.0),
        ('bg campus outskirts snow', 2.0),
        ('bg colorado house ext', 4.0),
        ('bg colorado house livingroom fire', 2.0),
        ('bg colorado house livingroom night', 4.0),
        ('bg colorado house guestbedroom', 4.0),
        ('bg colorado colorado hiking loop', 2.0),
        ('bg colorado hiking2', 4.0),
        ('bg colorado town HD', 4.0),
        ('bg colorado park', 2.0),
        ('bg colorado town', 2.0),
        ('bg downtown city', 3.0),
        ('bg downtown park', 3.0),
        ('bg downtown pizzeria', 2.0),
        ('bg downtown square night', 2.0),
        ('bg misc zoo', 2.0),
        ('bg misc zoo HD', 2.0),
        ('cg act1 eileenpainting', 4.0),
        ('cg act1 eileenpainting eileen', 1.0),
        ('cg act2 balconychat talk 4', 2.0),
        ('cg act2 photo', 2.0),
        ('cg act2 nudepainting', 4.0),
        ('cg act3 roadtrip 1', 4.0),
        ('cg act3 snowmen', 4.0),
        ('cg act3 swings', 2.0),
        ('cg act3 swings foreground', 0.8),
        ('cg act3 hug end', 5.0)
    ]

init 2 python:
    # different init level to allow DLC to add images in init level 1

    def get_base_image(n):
        ref = ImageReference(n)
        if not ref.find_target():
            return None
        src = ref.target
        while True:
            if not isinstance(src, Transform):
                break
            src = src.child
        return src

    for img in sepia_images:
        renpy.image(img + ' sepia', im.Sepia(get_base_image(img)))

    for img, amount in blur_images:
        renpy.image(img + ' blurred{}'.format(int(amount)), im.Blur(get_base_image(img), amount))

init:
    # Images and effects.
    image white = Solid("#ffffff")
    image creme = Solid("#fffbf4")
    image shadow = Solid("#000")
    image cg title = "ui/main/bg.webp"

# Eileen Flashback Layered Image
layeredimage eileen_sepia:
    group bodies:
        attribute indoors_crossed default:
            im.Sepia("sprites/eileen/bodies/indoors_crossed.webp")
        attribute indoors_fists:
            im.Sepia("sprites/eileen/bodies/indoors_fists.webp")
        attribute indoors_onhip:
            im.Sepia("sprites/eileen/bodies/indoors_onhip.webp")
        attribute outdoors_crossed:
            im.Sepia("sprites/eileen/bodies/outdoors_crossed.webp")
        attribute outdoors_fists:
            im.Sepia("sprites/eileen/bodies/outdoors_fists.webp")
        attribute outdoors_onhip:
            im.Sepia("sprites/eileen/bodies/outdoors_onhip.webp")
        attribute outdoorsnoscarf_crossed:
            im.Sepia("sprites/eileen/bodies/outdoorsnoscarf_crossed.webp")
        attribute outdoorsnoscarf_fists:
            im.Sepia("sprites/eileen/bodies/outdoorsnoscarf_fists.webp")
        attribute outdoorsnoscarf_onhip:
            im.Sepia("sprites/eileen/bodies/outdoorsnoscarf_onhip.webp")
        attribute hiking_onhip:
            im.Sepia("sprites/eileen/bodies/hiking_onhip.webp")
        attribute naked_towel:
            im.Sepia("sprites/eileen/bodies/naked_towel.webp")
        attribute pjs_onhip:
            im.Sepia("sprites/eileen/bodies/pjs_onhip.webp")
        attribute pjs_crossed:
            im.Sepia("sprites/eileen/bodies/pjs_crossed.webp")

    group eyes:
        attribute normal default:
            im.Sepia("sprites/eileen/eyes/normal.webp")
        attribute annoyed:
            im.Sepia("sprites/eileen/eyes/annoyed.webp")
        attribute closed:
            im.Sepia("sprites/eileen/eyes/closed.webp")
        attribute disbelief:
            im.Sepia("sprites/eileen/eyes/disbelief.webp")
        attribute frowning:
            im.Sepia("sprites/eileen/eyes/frowning.webp")
        attribute lookaway:
            im.Sepia("sprites/eileen/eyes/lookaway.webp")
        attribute lookawaynarrow:
            im.Sepia("sprites/eileen/eyes/lookawaynarrow.webp")
        attribute narrow:
            im.Sepia("sprites/eileen/eyes/narrow.webp")
        attribute sad:
            im.Sepia("sprites/eileen/eyes/sad.webp")

    group faces:
        attribute neutral default:
            im.Sepia("sprites/eileen/faces/neutral.webp")
        attribute angry:
            im.Sepia("sprites/eileen/faces/angry.webp")
        attribute frown:
            im.Sepia("sprites/eileen/faces/frown.webp")
        attribute grumble:
            im.Sepia("sprites/eileen/faces/grumble.webp")
        attribute open:
            im.Sepia("sprites/eileen/faces/open.webp")
        attribute sadmouth:
            im.Sepia("sprites/eileen/faces/sadmouth.webp")
        attribute smile:
            im.Sepia("sprites/eileen/faces/smile.webp")
        
    group _misc:
        attribute none default:
            im.Sepia("sprites/eileen/_misc/none.webp")
        attribute blush:
            im.Sepia("sprites/eileen/_misc/blush.webp")
        attribute tears:
            im.Sepia("sprites/eileen/_misc/tears.webp")
