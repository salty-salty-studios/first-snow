label scene_1S5_en:
######################
# Act 1, Scene 5

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg buildingbusiness hallway1f sketch with inkfade
scene bg buildingbusiness hallway1f with inkfade2
stop sound fadeout 0.1
play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.0
window show dissolve
$ _dismiss_pause = True
"With time on my hands thanks to the last class of the week finally being over, some quiet sketching would be a nice way to unwind. With that in mind, I make my way up to the art room."

"Studying would be the proper thing to do, but I'm just too burned out. Not that this stubborn cold helps, either."

stop ambiance fadeout 0.1
play sound "sfx/door_close2.ogg"
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 2.0
scene bg campus reverse snow:
    xalign 1.0
show snow light
with midDissolve
show bg:
    subpixel True
    parallel:
        ease 15.0 xalign 0.0
    parallel:
        ease 1.0 yoffset 1
        ease 1.0 yoffset -1
        repeat 5
"While most classes are winding down, their professors aware that the looming holidays are a big distraction, others have tried ramping up the workload to try and cover everything in their semester plans. I might be keeping up, but plenty aren't."

"With my bag tucked under my arm, I give a sigh as I stagger along the snowy path to the arts building. It would be nice to feel like I'm doing more than treading water, in class and socially."

stop loopsfx fadeout 0.1
stop ambiance fadeout 0.1
play sound "sfx/door_open.ogg"
$ renpy.sound.set_volume(0.5, channel="loopsfx", delay=0.5)
play loopsfx "sfx/ambiance/crowd_loud.mp3" fadein 2.0
scene bg buildingart hallway1f with midDissolve
play sound "sfx/door_close2.ogg"
"Stepping into the arts building with its strung-up decorations reminds me to look on the bright side: It's already the middle of November, so not long until Christmas and being back with my family. I'll be thankful to be back with them, even if the rest of the holiday period is a wash."

"I manage to angle around a chatting group of friends blocking the hallway, and start up the stairs without bothering them. Another small success."

scene bg buildingart hallway2f dusk with midDissolve
"I briefly wonder if Eileen's in the art room as I proceed along the second floor hallway. Her paintings are always nice to see, but whether she thinks of me as just another pain like she views Caprice weighs on my mind."

play sound "sfx/door_open2.ogg"
$ renpy.sound.set_volume(0.2, channel="loopsfx", delay=0.5)
scene bg buildingart art dusk womanwip
$camera_move(-200,-250,650,0,0,'dissolve')
show eileen indoors_onhip lookaway neutral at center:
    zoom 0.65 yoffset -300
    xpos 0.52
with fadeInOut
"Opening the door to the quiet room, I can't say I'm surprised at the sight before me. Of course she was going to be here."

play sound "sfx/door_close.ogg"
python:
    # work around ren'py bug where audio emphasis "lowers" the volume absolutely,
    # resulting in possible *higher* volumes
    if _preferences.emphasize_audio:
        renpy.sound.stop(channel="loopsfx", fadeout=0.5)
    else:
        renpy.sound.set_volume(0.02, channel="loopsfx", delay=0.5)
    renpy.music.set_volume(0.8)

show eileen indoors_onhip normal at center:
    zoom 0.65 yoffset -300
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
play music "music/eileen_5_m.ogg" fadein 5.0
"Eileen's eyes glance over as I gingerly shut the door behind me, ending up being the only acknowledgement of my presence at all before she goes right back to her work."

show eileen indoors_onhip lookaway at center:
    zoom 0.65 yoffset -300
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Curiosity about what she's painting gets the better of me."
voice "Allison_Hey2.ogg"
allison "Is it okay if I watch?"

show eileen indoors_onhip closed at center:
    zoom 0.65 yoffset -300
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Sure1.ogg"
eileen "Go ahead."

stop sound fadeout 1.0
play ambiance "sfx/ambiance/painting.ogg" fadein 2.0
scene cg act1 eileenpainting
$camera_move(200,1550,650,0,0,'dissolve')
with fadeInOut
show eileen indoors_onhip neutral normal at center:
    xpos 0.5 alpha 0
$camera_move(200,-250,650,0,10,'ease')
"She doesn't bother to look at me as she says it, but doesn't sound reluctant either, so I scoot over and sit myself on a table as quietly as I can. Eileen's brush continues to flick to and fro as she works on the background."
voice "Eileen_Hmm1.ogg"
eileen "So Caprice is a no-show?"

allison "She said she had to go do something with her roommates."

"Her shoulders slump as she sighs, relieved."

allison "Do you really hate her that much?"
voice "Eileen_Heh3.ogg"
eileen "Believe me, if I hated her, you'd know. I'm just glad to have some quiet."

"It's hard not to take that as a thinly-veiled implication that I should be quiet as well."

"Wallace might not be wrong that Eileen means well, but that doesn't make her any easier to talk to."

eileen "Something on your mind?"

$camera_move(0,0,0,0,5,'ease')
allison "You're really good at this."

"It'd feel weird to say I've been talking about Eileen behind her back. What I said is true though; I'm impressed she can carry on a conversation while working, and I like how her painting's turning out."
voice "Eileen_Thanks1.ogg"
eileen "Thanks. Been doing it for a while."
voice "Allison_Hmwithquestionmark.ogg"
allison "As a hobby?"

eileen "If everything works out, hopefully as a career. Artist or teacher, aiming for the latter."

"That does explain her persistence at working away to get better. Wanting to be a teacher, though... she gives the feeling of a drill sergeant more than an art tutor."

stop ambiance fadeout 1.0
scene bg buildingart art dusk womanwip
$camera_move(-200,-250,650,0,0,'dissolve')
show eileen indoors_crossed disbelief open at center:
    zoom 0.65 yoffset -300
    xpos 0.52
    time 2
    linear 0.7 xzoom -1 xpos 0.47
with fadeInOut
voice "Eileen_Hmm1.ogg"
eileen "Hmm, tube's out."

show eileen indoors_onhip normal grumble at center:
    zoom 0.65 yoffset -300
    xzoom -1 xpos 0.47
    ease 1.8 xpos 0.99
pause 1.5
play sound "sfx/rifling-through-drawer.ogg" fadein 0.1
"Eileen gets up and places her supplies on the sill beside her, opening the cupboard and fiddling around a bit."

scene bg buildingart art dusk womanwip
show bg buildingart art dusk womanwip blurred1 as bg2:
    xalign 0.5 yalign 0.5 alpha 0.85
show eileen indoors_fists normal grumble at center:
    zoom 1.5 yoffset 500
    xpos 0.99
    ease 1.5 xpos 0.5
with dissolve
$ camera_reset()
stop sound fadeout 1.0
"Before long, she emerges with a new tube of crimson paint in hand. Rather than get back to painting after closing the door though, she instead turns to me."

show eileen indoors_onhip narrow open at center:
    alpha 1.0
$ renpy.transition(dissolve, layer='master')
eileen "So what about you?"

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Huh1.ogg"
allison "Sorry?"

show eileen normal frown at center
$ renpy.transition(dissolve, layer='master')
eileen "What're you doing once you escape this place?"
voice "Allison_Um2.ogg"
allison "Oh, uh... I don't really know. Still trying to figure that out."

"I feel like I failed a test as I trail off, but Eileen doesn't seem worried."

show eileen indoors_crossed closed neutral at center
$ renpy.transition(dissolve, layer='master')
eileen "You're still young, and there's a good few courses to look into here. Just try your hand at whatever comes up until something grabs you."

show eileen open at center
$ renpy.transition(dissolve, layer='master')
eileen "There are plenty of worse ways to spend your time in college. You're smart too, so you have that going for you."

show eileen normal neutral at center
$ renpy.transition(dissolve, layer='master')
"I awkwardly smile at the praise. I've never been good at knowing how to handle compliments."

"She may say that, but the fact Eileen's so set on a career, yet only seems to be around my age rubs in my lack of direction. I'm still patting myself on the back for managing groceries."

allison "My parents always told me I could do whatever I set my mind to, but it was so easy to tread water for me that I never bothered trying to swim."

show eileen lookaway grumble at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "Sounds like you have a nice family."

stop music fadeout 8.0
"I move to respond, the memory of them gives me the familiar pang of homesickness all over again. I might've found time to call mom yesterday, but it just isn't the same."

show eileen indoors_onhip sad open at center
$ renpy.transition(dissolve, layer='master')
eileen "You okay?"

show eileen indoors_onhip sad frown at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Sigh1.ogg"
allison "Yeah, just... I miss them."

show eileen closed frown at center
$ renpy.transition(dissolve, layer='master')
eileen "Well, everyone here's going through the same thing."

allison "You as well?"

show eileen sad angry at center
$ renpy.transition(dissolve, layer='master')
eileen "I miss my sister, yeah. She's probably fine, but that doesn't make it easier."

allison "Mom and dad too?"

show eileen indoors_crossed lookawaynarrow at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble2.ogg"
eileen "To be honest, things've been easier between me and my folks since I moved out."
voice "Allison_Hm2.ogg"
allison "Huh..."

"It's hard to imagine being on such bad terms with my family that moving away was better. The best thing about Christmas will be the chance to see them again, but Eileen doesn't seem particularly fussed about it at all."

play music "music/dozy_comfy.ogg" fadein 5.0
scene bg buildingart art dusk womanwip
$camera_move(-1800,-250,650,0,0,'dissolve')
show eileen indoors_crossed lookawaynarrow neutral at center:
    zoom 0.65 yoffset -300 xpos 0.52
with dissolve
$camera_move(-200,-250,650,0,4,'ease')
"Leaving me to ponder, Eileen goes back to her painting."

show eileen indoors_onhip lookaway at center:
    zoom 0.65 yoffset -300 xpos 0.52
$ renpy.transition(dissolve, layer='master')
"I get the feeling she wouldn't be this gracious to Caprice, so she seems to think a little better of me at least. She's lent me an ear."

play ambiance "sfx/ambiance/painting.ogg" fadein 2.0
scene cg act1 eileenpainting with fadeInOut
show eileen indoors_onhip neutral normal at center:
    xpos 0.5 alpha 0
$ camera_reset()
eileen "Not boring you, am I?"

allison "No, not at all. I like watching you paint."

$ renpy.sound.set_volume(0.0, channel='ambiance')
"She pauses a moment before continuing."
$ renpy.sound.set_volume(0.8, channel='ambiance')
"It's only for a second, but I sense a hesitation there. Did I say something wrong?"

stop loopsfx fadeout 2.0
show cg act1 eileenpainting blurred4
show cg act1 eileenpainting eileen as act1_eileenpainting_eileen:
    subpixel True
    xalign 0.5 yalign 0.5 zoom 1.0
    ease 1.5 zoom 1.02 xoffset 5 yoffset 5
$ renpy.transition(dissolve, layer='master')

"The moment passes as soon as it arrived, Eileen's brush returning to the canvas. The other students appear to have left by now, the orange-stained room silent save for her work. The building's just a little cold, but that's fine."

"As the minutes roll by, I end up watching her for a while as I swing my legs. I almost forgot I came here to actually draw, but that doesn't matter. Watching her painting slowly progress is more than enough."

"Every so often, she mixes up a dab of this paint and that on the wooden palette beside her. The side of a hip is traced out, the light bouncing off a waist shaded, or a flowing strand of hair detailed with the fine tip."

"I can't help but admire her ability to set a goal and stay true to it, knowing exactly what she's working toward at this stage of her life."

"If only I had an ounce of the ambition Eileen has."

show cg act1 eileenpainting eileen as act1_eileenpainting_eileen2 behind act1_eileenpainting_eileen:
    xalign 0.5 yalign 0.5 alpha 1
    ease 1.2 zoom 1.0
show cg act1 eileenpainting eileen as act1_eileenpainting_eileen:
    subpixel True
    xalign 0.5 yalign 0.5 alpha 1
    zoom 1.02 xoffset 5 yoffset 5
    ease 1.2 zoom 1.0 xoffset 0 yoffset 0 alpha 0
with None
show cg act1 eileenpainting
$ renpy.transition(dissolve, layer='master')
allison "I might go to a café nearby to grab a coffee. I'll be back in a bit."

eileen "Tired?"

allison "Yeah. Sorry to distract you from your work."

eileen "Glad for the company. Have fun."

stop ambiance fadeout 1.0
scene bg buildingart art dusk woman
show eileen indoors_fists lookaway neutral at center:
    zoom 0.65 yoffset -300
    xpos 0.52
with fadeInOut
"With that, I hop off the table and start toward the door."

stop music fadeout 5.0
show eileen indoors_onhip normal open at center:
    zoom 0.65 yoffset -300 xpos 0.52
    linear 0.7 xzoom -1 xpos 0.47
eileen "Oh, wait."

"Her voice stops me in my tracks just as I'm about to go; it'd be great if she decided to come as well."

show eileen closed open at center:
    xzoom -1 xpos 0.47
$ renpy.transition(dissolve, layer='master')
eileen "Could you grab me a coffee too? Espresso, straight. I'll give you some cash when you come back."

show eileen normal neutral at center:
    xzoom -1 xpos 0.47
$ renpy.transition(dissolve, layer='master')
$ _dismiss_pause = False
"So much for that."

window hide dissolve
scene black with longDissolve
$ renpy.music.set_volume(1.0, delay=0)
$ renpy.sound.set_volume(1.0, channel="loopsfx")
$ renpy.sound.set_volume(1.0, channel="ambiance")
return
