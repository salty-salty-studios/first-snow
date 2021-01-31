label scene_init_en:
    python:
        all_languages.append('en')

        character_names = {
            # Main characters.
            'allison':   'Allison',
            'eileen':    'Eileen',
            'eileenu':   'Mad girl{=eileen}',
            'eileenlb':  'Eileen',

            # Side characters.
            'caprice':   'Caprice',
            'millie':    'Millie',
            'wallace':   'Wallace',
            'wallaceu':  'Tall guy{=wallace}',
            'rose':      'Rose',
            'dad':       'Dad',
            'eve':       'Eve',
            'andrew':    'Andrew',
            'elizabeth': 'Elizabeth',
            'hayley':    'Hayley',

            # Anonymous characters.
            'everyone':  'Everyone',
            'letterbox': '',
            'allisoneve': 'Allison & Eve',
        }

        character_tags = {
            'Mad girl{=eileen}':   'eileen_madgirl',
            'Tall guy{=wallace}':  'wallace_tallguy',
        }

        store.rabbl.act_titles = {
            4: '?',
        }

        store.rabbl.scene_titles = {
            '1S1': 'First Snow',
            '1S2': 'The Daily Bread',
            '1S3': 'Cup of Joe',
            '1S4': 'Page Turner',
            '1S5': 'Art Matters',
            '1S6': 'Sticking in the Knife',
            '1S7': 'Prost!',

            '2S1': 'Drive',
            '2S2': 'The Club with No Rules',
            '2S3': 'The Painter',
            '2S4': 'La Vie en Rose',
            '2S5': 'Hand in Hand',
            '2S6': 'The Day After',
            '2S7': 'Hot Coffee',
            '2S8': 'Zoology',
            '2S9': 'Semester\'s End',

            '3S1': 'Interstate 80',
            '3S2': 'Meeting the Parents',
            '3S3': 'A Little Voice',
            '3S4': 'Into the Wild',
            '3S5': 'The New World',
            '3S6': 'Lakeside',
            '3S7': 'C\'est La Vie',
            '3S8': 'Home',

            '4S1': 'Credits',
            '4S2': 'A Hard Secret to Keep',
        }
        
        scene_descriptions = {
            '1S1': 'As Christmas approaches, two students meet.',
            '1S2': 'While helping Rose, Allison ponders her new life.',
            '1S3': 'Encouragement comes from an unexpected source.',
            '1S4': 'Allison learns not all have a head for math.',
            '1S5': 'Eileen explains difficulties in life and art.',
            '1S6': 'A hungry Allison finds help in another.',
            '1S7': 'The new art club celebrates their founding.',

            '2S1': 'The first club outing doesn\'t go to plan.',
            '2S2': 'The first of many club meetings.',
            '2S3': 'Eileen requests delicate assistance with art.',
            '2S4': 'Two very different people are introduced.',
            '2S5': 'In the falling snow, emotions spring forth.',
            '2S6': 'The implications of a relationship become clear.',
            '2S7': 'Three friends discuss the outdoors, indoors.',
            '2S8': 'Allison and Eileen share their first date.',
            '2S9': 'A final gathering of friends as the year ends.',

            '3S1': 'Rose and Allison enjoy a pitstop between states.',
            '3S2': 'An unsure Allison\'s first impressions.',
            '3S3': 'A day well spent with Eileen\'s sister, Eve.',
            '3S4': 'Eileen leads a surprise expedition.',
            '3S5': 'Far from home, doubts emerge in Allison.',
            '3S6': 'Two worlds come into sharp contrast.',
            '3S7': 'A farewell is given, as it comes time to leave.',
            '3S8': 'Christmas arrives, the two finding home.',

            '4S1': 'You have reached the end of the line.',
            '4S2': 'As the snow begins to thaw, another story unfolds.',
        }

        track_titles = {
            'music/snow.ogg': 'Snowy City',
            'music/snow-eileen.ogg': 'Our Snowy City',
            'music/art_club_a.ogg': 'Watercolors',
            'music/relaxing.ogg': 'Winding Down',
            'music/caprice_default_m.ogg': 'Cute Salute',
            'music/anxiety_2_m.ogg': 'So You Do Have a Name',
            'music/energetic.ogg': 'The Usual Excitement',
            'music/whimsical_faster_m.ogg': 'Comfortable Silence',
            'music/conflict.ogg': 'Bitter Medicine',
            'music/romance_2_m.ogg': 'Butterflies',
            'music/millie_2.ogg': 'Boundless Worlds',
            'music/questioning.ogg': 'Sketchy Skills',
            'music/ringtone.ogg': 'Ringtone',
            'music/caprice_ringtone.ogg': 'Ringtone (Caprice)',
            'music/zoo_4_m2.ogg': 'Unexpected Comfort',
            'music/touching.ogg': 'Wonderful Warmth',
            'music/snow_4_m.ogg': 'Snow Circles',
            'music/night_2.ogg': 'Warm-Hearted World',
            'music/night_2_r2.ogg': 'Warm-Hearted World',
            'music/more_sad_m.ogg': 'Left Behind',
            'music/eve_3_m.ogg': 'Sibling Scuffles',
            'music/eileen_5_m.ogg': 'Mixed Messages',
            'music/dozy_comfy.ogg': 'Pick-Me-Up',
            'music/diner_2_m2.ogg': 'Prost!',
            'music/painter.ogg': 'Did You Paint All These?',
            'music/credits.ogg': 'Snowmelt',
        }

label scene_start_en:
    return

label scene_end_en:
    return
