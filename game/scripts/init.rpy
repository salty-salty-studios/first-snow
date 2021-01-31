# init.rpy
# Global script initialization.

label scene_init:
    python:
        all_languages = []

        scenes = []
        for act in range(1, 5):
            for scene in range(1, 30):
                name = '{}S{}'.format(act, scene)
                label = 'scene_{}_{}'.format(name, rabbl.current_language)
                if renpy.has_label(label):
                    scenes.append(name)
                else:
                    break

        tracks = [
            'music/snow.ogg',
            'music/art_club_a.ogg',
            'music/relaxing.ogg',
            'music/caprice_default_m.ogg',
            'music/anxiety_2_m.ogg',
            'music/energetic.ogg',
            'music/caprice_ringtone.ogg',
            'music/whimsical_faster_m.ogg',
            'music/conflict.ogg',
            'music/romance_2_m.ogg',
            'music/millie_2.ogg',
            'music/questioning.ogg',
            'music/zoo_4_m2.ogg',
            'music/touching.ogg',
            'music/snow_4_m.ogg',
            'music/night_2.ogg',
            'music/dozy_comfy.ogg',
            'music/more_sad_m.ogg',
            'music/eve_3_m.ogg',
            'music/eileen_5_m.ogg',
            'music/diner_2_m2.ogg',
            'music/painter.ogg',
            'music/ringtone.ogg',
            'music/credits.ogg',
            'music/snow-eileen.ogg',
        ]

        track_categories = {
            'music/ringtone.ogg': 'event',
            'music/caprice_ringtone.ogg': 'event',
            'music/diner_2_m2.ogg': 'event',
            'music/snow_4_m.ogg': 'event',
            'music/more_sad_m.ogg': 'event',
            'music/painter.ogg': 'event',
            'music/romance_2_m.ogg': 'event',
            'music/millie_2.ogg': 'event',
            'music/touching.ogg': 'event',
            'music/credits.ogg': 'event',
            'music/eve_3_m.ogg': 'event',
            'music/zoo_4_m2.ogg': 'event',
            'music/credits.ogg': 'event',
            'music/snow-eileen.ogg': 'event',
        }

        characters = {
            # Main.
            'allison':   {'color': '#eef0f1'},
            'eileen':    {'color': '#9a9065'},
            'eileenu':   {'color': '#9a9065'},
            # Side.
            'caprice':   {'color': '#6e9aa1'},
            'millie':    {'color': '#ba5a4d'},
            'wallace':   {'color': '#b2678a'},
            'wallaceu':  {'color': '#b2678a'},
            'rose':      {'color': '#c7633b'},
            'eve':       {'color': '#f5ecc1'},
            'dad':       {'color': '#eef0f1'},
            'andrew':    {'color': '#eef0f1'},
            'elizabeth': {'color': '#eef0f1'},
            'hayley':    {'color': '#9a9065'},
            # Misc.
            'everyone':  {'color': '#ffff00'},
            'letterbox': {'color': '#ffffff', 'what_color': '#ffffff', 'window_background': 'ui/textbar/empty.webp', 'ctc': DynamicDisplayable(ctc_letterbox)},
            'eileenlb':  {'color': '#9a9065', 'what_color': '#ffffff', 'window_background': 'ui/textbar/empty.webp', 'ctc': DynamicDisplayable(ctc_letterbox)},
        }


        cg_art = [
            {
                'title': 'Balcony',
                'file': ['cgs/act1_balcony_morning.webp'],
                'thumb': ['cgs/act1_balcony_morning_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('1S1'),
            },
            {
                'title': 'Art Matters',
                'file': ['vfx/title/act1.webp'],
                'thumb': ['vfx/title/act1_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('1S2')
            },
            {
                'title': 'The Painter',
                'file': ['cgs/act1_eileenpainting.webp'],
                'thumb': ['cgs/act1_eileenpainting_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('1S5')
            },
            {
                'title': 'Cooking',
                'file': ['cgs/act1_cooking.webp', 'cgs/act1_cooking_happy.webp'],
                'thumb': ['cgs/act1_cooking_thumb.webp', 'cgs/act1_cooking_happy_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('1S6')
            },
            {
                'title': 'Toast!',
                'file': ['cgs/act1_clubtoast.webp'],
                'thumb': ['cgs/act1_clubtoast_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('1S7')
            },
            {
                'title': 'Falling Snow',
                'file': ['vfx/title/act2.webp'],
                'thumb': ['vfx/title/act2_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('2S1')
            },
            {
                'title': 'Nude Painting',
                'file': (lambda:
                    ['dlc/h/cgs/act2_boobpainting.webp', 'dlc/h/cgs/act2_boobpainting_embarrassed.webp', 'dlc/h/cgs/act2_boobpainting_smile.webp']
                    if store.rabbl.allow_explicit else
                    ['cgs/act2_nudepainting.webp', 'cgs/act2_nudepainting_embarrassed.webp', 'cgs/act2_nudepainting_smile.webp']
                ),
                'thumb': (lambda:
                    ['dlc/h/cgs/act2_boobpainting_thumb.webp', 'dlc/h/cgs/act2_boobpainting_embarrassed_thumb.webp', 'dlc/h/cgs/act2_boobpainting_smile_thumb.webp']
                    if store.rabbl.allow_explicit else
                    ['cgs/act2_nudepainting_thumb.webp', 'cgs/act2_nudepainting_embarrassed_thumb.webp', 'cgs/act2_nudepainting_smile_thumb.webp']
                ),
                'locked': lambda: not store.rabbl.seen_scene('2S3')
            },
            {
                'title': 'Balcony Chat',
                'preview': 'cgs/act2_balconychat_talk_thumb.webp',
                'file': ['cgs/act2_balconychat_alone.webp', 'cgs/act2_balconychat_rose.webp', 'cgs/act2_balconychat_talk.webp', 'cgs/act2_balconychat_talk_2.webp', 'cgs/act2_balconychat_talk_3.webp', 'cgs/act2_balconychat_talk_4.webp', 'cgs/act2_balconychat_talk_5.webp'],
                'thumb': ['cgs/act2_balconychat_alone_thumb.webp', 'cgs/act2_balconychat_rose_thumb.webp', 'cgs/act2_balconychat_talk_thumb.webp', 'cgs/act2_balconychat_talk_2_thumb.webp', 'cgs/act2_balconychat_talk_3_thumb.webp', 'cgs/act2_balconychat_talk_4_thumb.webp', 'cgs/act2_balconychat_talk_5_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('2S4')
            },
            {
                'title': 'Kiss',
                'file': ['cgs/act2_kiss_surprise.webp', 'cgs/act2_kiss_after.webp'],
                'thumb': ['cgs/act2_kiss_surprise_thumb.webp', 'cgs/act2_kiss_after_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('2S6')
            },
            {
                'title': 'Zoo',
                'file': ['cgs/act2_zoo_smile.webp', 'cgs/act2_zoo_bird.webp'],
                'thumb': ['cgs/act2_zoo_smile_thumb.webp', 'cgs/act2_zoo_bird_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('2S8')
            },
            {
                'title': 'Fingering',
                'file': ['dlc/h/cgs/act2_finger_start.webp', 'dlc/h/cgs/act2_finger_mid.webp', 'dlc/h/cgs/act2_finger_end.webp'],
                'thumb': ['dlc/h/cgs/act2_finger_start_thumb.webp', 'dlc/h/cgs/act2_finger_mid_thumb.webp', 'dlc/h/cgs/act2_finger_end_thumb.webp'],
                'locked': (lambda: not store.rabbl.seen_scene('2S8_b')),
                'visible': lambda: store.rabbl.allow_explicit,
            },
            {
                'title': 'H',
                'file': ['dlc/h/cgs/act2_cunnilingus_start.webp', 'dlc/h/cgs/act2_cunnilingus_mid.webp', 'dlc/h/cgs/act2_cunnilingus_end.webp'],
                'thumb': ['dlc/h/cgs/act2_cunnilingus_start_thumb.webp', 'dlc/h/cgs/act2_cunnilingus_mid_thumb.webp', 'dlc/h/cgs/act2_cunnilingus_end_thumb.webp'],
                'locked': (lambda: not store.rabbl.seen_scene('2S8_b')),
                'visible': lambda: store.rabbl.allow_explicit,
            },
            {
                'title': 'Pillowtalk',
                'file': ['cgs/act2_pillowtalk_eyesclosed.webp', 'cgs/act2_pillowtalk_talk.webp'],
                'thumb': ['cgs/act2_pillowtalk_eyesclosed_thumb.webp', 'cgs/act2_pillowtalk_talk_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('2S8_c')
            },
            {
                'title': 'Photo',
                'file': ['cgs/act2_photo.webp'],
                'thumb': ['cgs/act2_photo_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('2S9')
            },
            {
                'title': 'A World Away',
                'file': ['vfx/title/act3.webp'],
                'thumb': ['vfx/title/act3_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('3S1')
            },
            {
                'title': 'Roadtrip',
                'file': ['cgs/act3_roadtrip_{}.webp'.format(i) for i in range(1, 7)],
                'thumb': ['cgs/act3_roadtrip_{}_thumb.webp'.format(i) for i in range(1, 7)],
                'locked': lambda: not store.rabbl.seen_scene('3S1')
            },
            {
                'title': 'Family Dinner',
                'file': ['cgs/act3_familydinner_{}.webp'.format(i) for i in range(1, 11)],
                'thumb': ['cgs/act3_familydinner_{}_thumb.webp'.format(i) for i in range(1, 11)],
                'locked': lambda: not store.rabbl.seen_scene('3S2')
            },
            {
                'title': 'Pinned!',
                'file': ['cgs/act3_pinned_allisontalk.webp', 'cgs/act3_pinned_eileentalk.webp', 'cgs/act3_pinned_shocked.webp', 'cgs/act3_pinned_kiss.webp'],
                'thumb': ['cgs/act3_pinned_allisontalk_thumb.webp', 'cgs/act3_pinned_eileentalk_thumb.webp', 'cgs/act3_pinned_shocked_thumb.webp', 'cgs/act3_pinned_kiss_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('3S2')
            },
            {
                'title': 'Kitchen',
                'file': ['cgs/act3_kitchen.webp'],
                'thumb': ['cgs/act3_kitchen_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('3S3_a')
            },
            {
                'title': 'Unison',
                'file': ['dlc/h/cgs/act3_mast{}.webp'.format(i) for i in range(1, 8)],
                'thumb': ['dlc/h/cgs/act3_mast{}_thumb.webp'.format(i) for i in range(1, 8)],
                'locked': (lambda: not store.rabbl.seen_scene('3S3_b')),
                'visible': lambda: store.rabbl.allow_explicit,
            },
            {
                'title': 'Snowmen',
                'file': ['cgs/act3_snowmen.webp'],
                'thumb': ['cgs/act3_snowmen_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('3S3_c')
            },
            {
                'title': 'Overlook',
                'file': ['cgs/act3_swings.webp'],
                'thumb': ['cgs/act3_swings_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('3S6')
            },
            {
                'title': 'Sleeping Sisters',
                'file': ['cgs/act3_sleepingsisters.webp'],
                'thumb': ['cgs/act3_sleepingsisters_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('3S7')
            },
            {
                'title': 'Together',
                'file': ['cgs/act3_hug_run.webp', 'cgs/act3_hug_end.webp'],
                'thumb': ['cgs/act3_hug_run_thumb.webp', 'cgs/act3_hug_end_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('3S8')
            },
            {
                'title': 'Voiced',
                'file': ['cgs/act4_vacg1.webp', 'cgs/act4_vacg2.webp', 'cgs/act4_vacg3.webp', 'cgs/act4_vacg4.webp'],
                'thumb': ['cgs/act4_vacg1_thumb.webp', 'cgs/act4_vacg2_thumb.webp', 'cgs/act4_vacg3_thumb.webp', 'cgs/act4_vacg4_thumb.webp'],
                'locked': lambda: not store.rabbl.seen_scene('4S2')
            },
        ]

        guests = [
            ('Szmitten',       'https://twitter.com/szmitten',    'webp'),
            ('Lilium',         'https://twitter.com/Lilaq__',     'webp'),
            ('adirosa',        'https://twitter.com/adirosette',  'webp'),
            ('Anon',           None,                              'webp'),
            ('VCR',            'https://twitter.com/Hachisame',   'webp'),
            ('rtil',           'https://twitter.com/rtil',        'webp'),
            ('umujacha',       'https://twitter.com/umujacha',    'jpg'),
            ('minute',         'https://twitter.com/minutekiwi',  'jpg'),
            ('TopHat',         'https://twitter.com/ToppeHatte',  'webp'),
            ('AcoTan',         'https://twitter.com/AcoTan2194',  'webp'),
            ('Skrats',         'https://twitter.com/Skratsu',     'webp'),
            ('tentakl',        None,                              'webp', {'file': [Animation('cgs/guest/tentakl-1.webp', 0.5, 'cgs/guest/tentakl-2.webp', 0.5)]}),
            ('Chiru',          'https://twitter.com/guy_kun',     'webp'),
            ('renessia',       'https://twitter.com/embrasseren', 'webp'),
            ('Anna',           'https://twitter.com/ripandtir',   'webp'),
            ('Cura & tentakl', 'https://twitter.com/cura_chan',   'webp'),
            ('All-Maker',      'https://twitter.com/AllMaker',    'webp'),
        ]
        guest_art = []
        for guest in guests:
            if len(guest) > 3:
                name, social, ext, data = guest
            else:
                name, social, ext = guest
                data = {}
            sname = name.lower().replace(' ', '_').replace('&', '')
            data = {
                'title':  None,
                'file':   data.get('file', ['cgs/guest/{}.{}'.format(sname, ext)]),
                'thumb':  ['cgs/guest/{}_thumb.{}'.format(sname, ext)],
                'info': {
                    'artist': name,
                    'url': social,
                }
            }
            native = data.get('native', ['cgs/guest/{}_native.{}'.format(sname, ext)])
            if renpy_exists(native[0]):
                data['native'] = native
            guest_art.append(data)

        ui_season = 'winter'

label scene_start:
    $ text_log = TextLog()
    return

label scene_end:
    scene black with dissolve
    return
