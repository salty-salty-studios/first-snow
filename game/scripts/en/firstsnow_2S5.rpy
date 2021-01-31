label scene_2S5_en:
######################

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg downtown square sketch with inkfade
scene bg downtown square with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
$ renpy.sound.set_volume(0.8, channel="ambiance2")
play ambiance2 "sfx/ambiance/crowd_loud.mp3" fadein 2.0
"While I'd had my doubts, the city workers managed to get the Christmas tree in the city's main square finished, just on schedule for the first day of December. Its oversized tinsel and baubles gleam happily in the morning's light, proudly announcing the coming holiday."

play sound "sfx/sack_drop.ogg"
scene bg downtown square
$camera_move(1000,800,400,0,0,'dissolve')
with midDissolve
$camera_move(600,-1400,400,0,15,'ease')
$ renpy.sound.set_volume(0.5, channel="ambiance2", delay=10.0)
play music "music/whimsical_faster_m.ogg" fadein 10.0
"Rose takes my pause in the middle of the city square as an excuse for a break, setting down her bags down as I look up to the huge tree before us."

"It's not the tree that's most interesting, so much as the crowd around us. Everyone walks to and fro just a little faster than normal walking speed, hurrying from shop to shop while hardly even glancing at the Christmas tree looming over everything."

"I think I read something once about feeling alone, even in a crowd. So many faces pass by, from couples holding hands, to businessmen, to groups of friends, yet I feel more disconnected than when I'm actually alone."

scene bg downtown square:
    xalign 1.0 yalign 1.0
show rose outdoors_smokingmouth normal neutral2 at rightish:
    zoom 1.2 yoffset 180 xpos 1.0
    xpos 0.7 alpha 1
    time 1
    ease 0.5 yoffset 185
    ease 0.5 yoffset 175
    ease 0.2 yoffset 180
with fadeInOut
$ camera_reset()
play sound "sfx/zippo_open.ogg"
"The clicking of a lighter next to me reminds me of my companion, the cigarette now perched in the corner of her mouth glowing brightly."

play sound "sfx/zippo_click1.ogg"
show rose outdoors_smokingmouth normal neutral2 at rightish:
    xpos 0.7 alpha 1
    nod2
allison "Shame we couldn't park closer."

show rose laugh2 at rightish
$ renpy.transition(dissolve, layer='master')
rose "Downtown's pretty crazy these days, isn't it?"

allison "Maybe we should put up our own Christmas tree."

show rose outdoors_smoking normal talking at rightish
$ renpy.transition(dissolve, layer='master')
rose "Hey, I got a tree for us a few days ago."

allison "I was the one who bought that. It's also like a foot tall."

show rose halfclosed smirk at rightish
$ renpy.transition(dissolve, layer='master')
rose "Oh yeah."

show rose outdoors_smokingmouth concerned2 at rightish
$ renpy.transition(dissolve, layer='master')
"The cigarette perched in her mouth tilts downward as she looks at me, her smile turning just a little less cheerful."

show rose normal concerned2 at rightish
$ renpy.transition(dissolve, layer='master')
rose "Missing holidays at home, are ya?"

allison "A bit."

stop sound fadeout 1.0
show rose neutral2 at rightish:
    subpixel True
    xpos 0.7
    ease 1.0 xpos 0.5
    ease 0.2 yoffset 185
    ease 0.2 yoffset 175
    ease 0.1 yoffset 180
pause 1.0
with hpunch
"She clamps onto my shoulder and gives me a firm shake."

show rose weaksmile at center
$ renpy.transition(dissolve, layer='master')
rose "Hang in there. I might not be much company, but at least you've got someone around."

allison "Were you homesick when you first moved out from home?"

show rose outdoors_smoking halfclosed concerned at center:
    xpos 0.5
    ease 1.5 xpos 0.7
rose "Given the circumstances... no."

show rose normal at rightish
$ renpy.transition(dissolve, layer='master')
rose "I don't think you appreciate how lucky you are, sometimes."

"Wandered straight onto that landmine. Rose has never talked about her immediate family in the few months I've known her, so maybe I should have taken the hint."

$camera_move(-1400,-1500,250,0,4,'ease')
show snow light starting behind rose:
    subpixel True
    zoom 1.5 xcenter 0.5 ycenter 0.4 alpha 0
    ease 4.0 alpha 1
show rose normal neutral at rightish:
    subpixel True
    xpos 0.7
    ease 4.0 xpos 0.72
"Noticing the gazes of a few around us have turned upward, I look up curiously. Looks like the weather's turned, the morning chill turning to snow."

show rose halfclosed talking at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
rose "Piss off, winter."

stop music fadeout 8.0
$camera_move(0,0,0,0,3.5,'ease')
pause 3.0
show rose outdoors_handonhip normal puzzled at rightish:
    xzoom 1 xpos 0.72
    linear 0.7 xzoom -1 xpos 0.75
    nod2
"With a dissatisfied puff, she puts out her cigarette on a nearby bin lid before flicking it in with a practiced motion."

stop ambiance2 fadeout 4.0
show rose outdoors_handonhip at right2:
    xzoom -1 xpos 0.75
    easein .15 yoffset 162
    easeout .175 yoffset 180
    easein .15 yoffset 172
    easeout .175 yoffset 180
"Taking her bags up once more, we continue the slog back to the bike."

scene black with circlewipe
$ renpy.sound.set_volume(1.0, channel="ambiance2")
play ambiance2 "sfx/ambiance/crowd_inner.ogg" fadein 5.0
scene bg downtown city:
    xalign 1.0
show snow light
show rose outdoors_handonhip normal weaksmile at right2
with circlewipe
rose "Chin up, eh? I was gonna say this later, but I bought your favorite while you weren't looking."

allison "Strawberry trifle?"

show rose laugh at right2
$ renpy.transition(dissolve, layer='master')
rose "You know it."

rose "Just a thanks for pulling your weight a bit more. It's nice to see you getting yourself together."

show rose halfclosed puzzled at right2
$ renpy.transition(dissolve, layer='master')
play sound "sfx/cell_phone_vibrate.ogg"
"Just as I'm about to thank her, a loud ping comes from my pocket."

show bg downtown city blurred3 behind rose, allison as bg2:
    xalign 1.0 yalign 0.5 alpha 0
    ease 1.0 alpha 0.9
show rose outdoors_handonhip halfclosed puzzled blur at right2 as rose2
$ renpy.transition(dissolve, layer='master')
$ phone.show('unlock')
"A little sheepish, I take my phone from my pocket to check what the message is."

$ phone.clear('eileen')
$ phone.message('eileen', '2:26 PM', 'Behind you.')
pause 0.5
$ phone.show('messages', who='eileen')
$ renpy.transition(smoothDissolve, layer='master')
$ renpy.pause()

window show
$ phone.hide()
window hide
stop sound fadeout 1.0
hide bg2
hide rose2
$ renpy.transition(dissolve, layer='master')
"Confused, I stop walking and turn about."
play music "music/anxiety_2_m.ogg" fadein 5.0
$camera_move(-4050,-1500,750,0,5,'ease')
pause 2.0

play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 1.0
scene bg downtown city HD
show snow light:
    zoom 1.5 xcenter 0.05 ycenter 0.12
$camera_move(-8500,-3000,-250,0,0,'dissolve')
show eileen outdoors_onhip narrow smile at leftedge:
    subpixel True
    xzoom -1 zoom 0.68 ypos 0.31 xpos -0.31
    parallel:
        ease 8.0 zoom 1.0 ypos 0.66 xpos -0.32
    parallel:
        easeout 0.5 yoffset -1
        easein 0.5 yoffset 1
        repeat 7
with fadeInOut
"Eileen holds her hand high as she slowly walks up the street, slipping her phone into her pocket as she arrives. I'm happy to see her, but something makes me hesitate. Something Rose picks up on, going by her churlish grin."

"I know full well I've fallen for Eileen. My stomach tying itself into knots at the sight of her, makes me realize that asking her out will have to come sooner rather than later. If she's even interested in girls, that is..."

"Trying to put my worries out of mind as best I can, I do my best to act normal."

scene bg downtown city
show snow light
show rose outdoors_handonhip normal smile at right2:
    zoom 1.05 yoffset 50
    xpos 0.75
show eileen outdoors_onhip narrow smile at left2:
    zoom 1.05 yoffset 50
    xzoom -1 xpos -0.2
    time 1
    ease 1.7 xpos 0.2
with fadeInOut
$ camera_reset()
stop loopsfx fadeout 0.5
allison "You've sure been getting some use out of that phone."

show eileen outdoors_crossed closed open at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
eileen "Starting to see the appeal of these things, yeah. 'Morning, Rose."

show eileen normal neutral at left2:
    xpos 0.2
show rose laugh at right2:
    xpos 0.75
$ renpy.transition(dissolve, layer='master')
rose "'Sup?"

show rose smile at right2:
    xpos 0.75
show eileen outdoors_onhip lookaway open at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
eileen "Just out for a walk; the apartment gets stifling after a while. Not interrupting anything, am I?"

play loopsfx "sfx/ambiance/heartbeat_light.ogg" fadein 4.0
show shadow:
    alpha 0
    ease 4.0 alpha 0.6
show eileen neutral at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
"When she puts it like that, she sounds far older than she should. In fact... Given she didn't own a smartphone, likes simple walks alone, and spends her days painting, I'm starting to doubt the girl I fell for is really my own age."

show rose talking at right2:
    xpos 0.75
show eileen outdoors_onhip closed neutral at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
"As the two strike up a casual chat, I remember how Eileen and I came to meet; being pushed into the club, taking chance after chance to come closer to her in hopes of spending more time together. It's only that persistence which gained me her friendship."

show rose neutral at right2:
    xpos 0.75
show eileen outdoors_crossed lookaway open at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
"My heart begins to beat as I talk myself into the plan forming in my head. Pushing myself got me this far; perhaps, if I could take one more step..."

show shadow:
    alpha 0.6
    ease 1.0 alpha 0
pause 1.0
stop loopsfx fadeout 1.0
show eileen normal neutral at left2:
    xpos 0.2
show rose normal neutral at right2:
    xpos 0.75
$ renpy.transition(dissolve, layer='master')
allison "Hey, Rose? Can I leave these with you?"

show rose smirk at right2:
    xpos 0.75
$ renpy.transition(dissolve, layer='master')
"She hesitates at the change of plans, the words blurted out before I can stop myself."

show rose weaksmile at right2:
    xpos 0.75
$ renpy.transition(dissolve, layer='master')
rose "Sure, I'll see you later. If you need a pickup, just call."

show rose halfclosed weaksmile at right2:
    xzoom 1 xpos 0.75
    linear 0.7 xzoom -1 xpos 0.78
    nod2
"Before I can so much as thank her, Rose quickly starts the work of strapping the shopping bags to her bike. It'll probably be easier to get everything home without me on the back, anyway."

show eileen outdoors_onhip normal frown at left2:
    xpos 0.2
show rose halfclosed laugh at right2:
    xzoom -1 xpos 0.78 alpha 1
    ease 1.5 xpos 1.2 alpha 0
"Eileen and I give her our goodbyes to her as we walk on, Rose waving us off. As we go, I think I see a small grin on her face. I guess she worked it out."

stop music fadeout 4.0
stop ambiance2 fadeout 2.0
"Once again, we're alone with each other. My stomach twists and turns as I desperately try to find some small talk to fill the air with, not that Eileen looks fussed about it all."

scene black with midDissolve
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 1.0
scene bg downtown park:
    subpixel True
    xalign 0.0
    parallel:
        ease 1.0 yoffset -1
        ease 1.0 yoffset 1
        repeat 10
    parallel:
        ease 20 xalign 1.0
show snow light
show eileen outdoors_onhip lookaway neutral at offcenterleft:
    subpixel True
    xzoom -1 xpos 0.4
    ease 1.0 yoffset 1
    ease 1.0 yoffset -1
    repeat 10
with midDissolve
"Buried in thought, I barely register us moving through the old wrought iron gates and into the city park."

"The water in the pond lies nearly still, the ducks lazily bobbing about with the odd flap of their wings to shake off the snow. The normally rustling branches of the trees stay silent as they gather falling snow, green slowly turning to white."

"With everybody in town busy shopping, all that's to be heard as we walk along the wide paths are our footsteps on freshly-fallen snow."

allison "Do you come here much?"

show eileen outdoors_crossed open at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "Yeah, every so often. Nice to just think to myself a bit without being cooped up."

show eileen normal at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "You?"

show eileen neutral at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
allison "Only when I was younger. I liked to feed bread to the ducks."

show eileen closed smile at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "I feel like I should have guessed that answer from you."

show eileen outdoors_onhip narrow smile at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
"All I can do is pout as she gives a smug smile at my expense."

stop loopsfx fadeout 0.5
$ renpy.music.set_volume(0.5)
play music "music/romance_2_m.ogg" fadein 5.0
scene bg downtown park blurred3:
    zoom 1.05
show snow light
$camera_move(-2200,1850,480,0,0,'dissolve')
show eileen outdoors_onhip lookaway neutral at left2:
    zoom 1.3 yoffset 300
    xzoom -1 xpos 0.25
with midDissolve
$camera_move(-2200,-850,480,0,12,'ease')
"Even as we walk on through the otherwise empty park, I can feel my eyes lingering on her."

"That difference between us is probably what drew me to her, now that I think about it. I've never felt like this towards anyone else before, but I know my feelings are genuine as I gaze at her."

"If she spends Christmas with her family, I won't get to see Eileen again until classes start in the new year. Telling her what I feel might ruin everything, but I don't want this to linger like a hanging thread. If she can push herself towards her goals, then so can I."

scene bg downtown park:
    xalign 1.0
show snow light
show eileen outdoors_crossed normal neutral at offcenterleft:
    xzoom -1 xpos 0.4
    time 1.5
    linear 0.7 xzoom 1 xpos 0.45
with fadeInOut
$ camera_reset()
"As I come to a stop, the ceasing of my footsteps on the crushed snow makes Eileen turn towards me."

"As her eyes fall to mine, my heart begins to race. I'm instantly filled with doubts, but now it's too late; I've psyched myself up so much that it's surely showing. All my life, others have helped push me forwards. Now I have to do something for myself."

"Eileen taught me how I have to do that."

play ambiance2 "sfx/ambiance/heartbeat.ogg" fadein 5.0
show shadow behind eileen:
    alpha 0.0
    ease 5.0 alpha 0.3
show eileen outdoors_onhip normal angry at offcenterleft:
    xzoom 1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
allison "Eileen... I wanted to tell you something."

"With my voice shaking and a hand clutching my other arm tightly out of nervousness, I take a long breath to clear my mind and sort out the words in my head. I ball my fists as I feel my hands shaking."

allison "After spending my whole life with such a big family, this was the first time I've ever tried to live by myself. I was really lonely at first, and didn't really know what was going on."

allison "But recently, I realized that loneliness hasn't been around. I've met so many wonderful people, and had so many nice experiences. Now I'm looking forward to every day, and what fun things might happen."

allison "A lot of that is thanks to you, so I wanted to thank you for helping me."

show eileen disbelief at offcenterleft
$ renpy.transition(dissolve, layer='master')
"This isn't exactly poetry so far, but I think I'm getting my feelings across right. Eileen simply looks at me, accepting the praise with only a touch of confusion."

show eileen outdoors_crossed lookawaynarrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Well... thanks. It's nice to be appreciated like that."

show eileen normal neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "It's more than that, though."

allison "I mean, I first thought it was just friendship, but..."

"Why can't I be more confident than this? My throat feels like it's closing as my nerves get the better of me, and it only gets worse the more I try to speak."

show eileen closed at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "It's... I..."

"I'm so busy reading Eileen's expression that I lose track of what I'm saying. I try desperately to force something out, but no words come to me."

show shadow behind eileen:
    alpha 0.3
    ease 3.0 alpha 0.0
show eileen outdoors_fists smile blush at offcenterleft
$ renpy.transition(smoothDissolve, layer='master')
"Looking at her face, though... I don't think the rest needs to be said."

$camera_move(-500,0,300,0,6,'ease')
show bg downtown park blurred3 behind eileen as bg2:
    xalign 1.0 yalign 0.5 alpha 0
    ease 5.5 alpha 0.9
show eileen outdoors_fists sad smile blush at center:
    subpixel True
    zoom 1.0 xpos 0.45
    ease 6.0 zoom 1.2 ypos 1.3 xpos 0.48
"We just look at each other silently, the winter's snow falling between us. She looks gentle, somehow."

"Stepping forward, she looks down at my blushing face. From here, I can see the faint red in her cheeks clearly. I can't think of anything else, just that gentle, calm face that I've never seen her wear before."

stop music fadeout 4.0
"After a moment's hesitation, Eileen brings her hands forward, grasping my shoulders delicately."

stop ambiance2 fadeout 3.0
scene black with dissolve
scene cg act2 kiss surprise
$camera_move(0,-800,450,0,0,'dissolve')
with midDissolve
$ renpy.music.set_volume(0.8)
play music "music/touching.ogg" fadein 6.0
$camera_move(0,800,450,0,3,'ease')
pause 3.0
window show dissolve
"And then, as she leans down... everything stops."

"I reflexively gasp in surprise as her soft lips press gently to mine, but it ends up stifled. With my body utterly frozen, I find myself completely in the grasp of the girl holding me, her breath tingling against my face."

window hide
$camera_move(0,0,0,0,3,'ease')
pause 3.0
show cg act2 kiss after with smoothDissolve
window show dissolve
"The sounds, the smells, everything beyond Eileen and I falls from my consciousness. All that's left is this wonderful warm feeling flowing through my entire body."

"Minutes, seconds, I have no idea how much time passes. I just know that I don't want it to stop."

"Eventually, sadly, Eileen's lips part from mine."

window hide
scene bg downtown park:
    xalign 1.0
show snow light
show eileen outdoors_onhip lookawaynarrow sadmouth blush at center:
    time 1
    bounce
with fadeInOut
"Straightening herself as she steps back, Eileen takes a long, shuddering breath as I stare dumbstruck at her wildly blushing face. The feeling of Eileen's lips pressed to mine replays endlessly in my confused mind, clouding everything else."

allison "Eileen, you..."

$ renpy.music.set_volume(0.5, delay=6.0)
scene bg downtown park blurred3:
    zoom 1.05
show snow light
$camera_move(-2200,1850,480,0,0,'dissolve')
show eileen outdoors_fists lookaway angry blush at center:
    zoom 1.3 yoffset 300
    xzoom 1 xpos 0.5
with midDissolve
$camera_move(-2200,-850,480,0,12,'ease')
"The air between us falls quiet, Eileen left waiting for a reply as I stand in a silent daze. Simple shock is one part of it, but far from all. Eileen is not only interested in women, but also in me. I feel like my heart could burst from the relief."

show eileen outdoors_fists lookaway angry blush at center:
    xzoom 1 xpos 0.5
    nod2
    repeat 2
"It's only now that I see her fidgeting, playing with her hair and unable to quite stand still. I wonder how long that's been going on, unnoticed."

"It makes me realize she's as unfamiliar at the situation as I am. Neither of us knows what we're supposed to do or say right now. Here I was trying to explain my feelings, when Eileen rushes ahead and does something brash like that..."

"Overcome with my own flood of emotions and confusion, it's Eileen who ends up having to reluctantly move things forward."

$ renpy.music.set_volume(0.8, delay=3.0)
scene bg downtown park:
    xalign 1.0
show snow light
show eileen outdoors_crossed lookaway open blush at center
with fadeInOut
$ camera_reset()
eileen "Sure hope I didn't misinterpret that."

show eileen sadmouth at center
$ renpy.transition(dissolve, layer='master')
"Her attempt to play off her nervousness is betrayed by her blushing. I finally realize just why she's so uncomfortable right now - she's left herself vulnerable. It's the first time I've seen her exposed like this, her feelings plain to see."

allison "I didn't know you felt that way."

show eileen outdoors_fists normal open blush at center
$ renpy.transition(dissolve, layer='master')
eileen "I... entertained the idea, I guess. Didn't ever think you'd be the one to make the first move."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "So you'll go out with me?"

show eileen outdoors_onhip neutral disbelief blush at center
$ renpy.transition(dissolve, layer='master')
eileen "No, I just kissed you for the sake of it."

show eileen outdoors_crossed narrow smile blush at center
$ renpy.transition(dissolve, layer='master')
eileen "Of course I will, you dolt."

show eileen lookawaynarrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "Guess we're in this thing together now, huh?"

stop ambiance fadeout 2.5
stop music fadeout 2.5
show eileen sadmouth at center
$ renpy.transition(dissolve, layer='master')
$ _dismiss_pause = False
"For all she tries to play things cool, it's obvious Eileen's as awkward about this as I am. The only reply I can muster, and perhaps the only one needed, is to smile."

$ renpy.music.set_volume(1.0)
window hide dissolve
scene black with longDissolve
return
