label scene_3S7_en:
######################
# Act 3, Scene 7

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg colorado town HD sketch
$camera_move(9000,-2200,0,0,0,'dissolve')
with inkfade
scene bg colorado town HD
$camera_move(9000,-2200,0,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1

play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
$ renpy.sound.set_volume(0.5, channel='sound')
play sound "sfx/door_close_bell.ogg"
show eve outdoors neutral normal at rightside as eve2:
    zoom 0.75 yoffset -400
    xzoom -1 xpos 0.9
show eve outdoors neutral normal at centerleft:
    alpha 0 xpos 0.35
show eileen outdoors_onhip lookaway neutral at centerright:
    alpha 0 xpos 0.65
$ renpy.transition(dissolve, layer='master')
$ _dismiss_pause = True

show eileen outdoors_onhip lookaway neutral at rightedge as eileen2:
    zoom 0.75 yoffset -400
    xzoom 1 xpos 1.3 alpha 0
    ease 2.0 xpos 1.15 alpha 1
$ renpy.music.set_volume(0.65)
play music "music/eileen_5_m.ogg" fadein 5.0
window show dissolve

"The jingle of the old bell above the grocery store door rings out as we step through into the street. There's a slight chill to the air, but that hasn't stopped a good few elderly people from hobbling along the town's streets."

stop sound fadeout 1.0
"Aside from needing to tell Eve she couldn't have this sugary snack or that as we walked around, shopping ended up being a quiet affair. Eileen went through the shelves with her usual military efficiency as she ticked off her mental checklist."

"Yesterday's argument between us hasn't helped, but that's not the only reason for Eileen's quietness. She might not even realize it herself, but it's small things like that which remind me of her solitary nature. That ability to tune others out so easily isn't something that comes naturally, at least to me."

show eileen normal neutral at rightedge as eileen2:
    xpos 1.15 alpha 1
show eve outdoors normal unsure at rightside as eve2:
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
"For want of helping at least a little, I took one of the overstuffed bags we ended up with to carry myself."

show eileen outdoors_fists normal open at rightedge as eileen2:
    xpos 1.15
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Thanks1.ogg"
eileen "Thanks for coming and helping carry all this."

show eileen normal neutral at rightedge as eileen2:
    xpos 1.15
$ renpy.transition(dissolve, layer='master')
voice "Allison_NervousSure.ogg"
allison "It's fine. I wanted to see a bit of the town, anyway."

show eve outdoors half sadopen at rightside as eve2:
    xpos 0.9
    nod2
voice "Eve_Eileen4.ogg"
eve "Can we sit down? I'm tired."

show eve outdoors half sad at rightside as eve2:
    xpos 0.9
show eileen outdoors_crossed lookawaynarrow angry at rightedge as eileen2:
    xpos 1.15
$ renpy.transition(dissolve, layer='master')
eileen "It's not that far to the car."

show eve outdoors normal shy at rightside as eve2:
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hey1.ogg"
allison "Wouldn't hurt to rest a bit, would it? There's a bench right up there."

show eileen narrow angry at rightedge as eileen2:
    xpos 1.15
$ renpy.transition(dissolve, layer='master')
"Taking Eve's side doesn't win me any favors, but Eileen knows she's been overruled."

scene bg colorado town HD blurred4:
    xzoom -1 xalign 0.0 yalign 0.0
show bg colorado town bench as town_bench
show eve outdoors normal neutral at right2:
    xzoom 1 xpos 1.2 yoffset -25
    ease 2.5 xpos 0.77
    linear 0.7 xzoom -1 xpos 0.75 yoffset 25
with fadeInOut
$ camera_reset()
$ renpy.pause(0.8, hard=True)
"As Eve jumps back onto the seat without any further prompting needed, Eileen and I carefully set our grocery bags on the ground and join her."

play sound "sfx/muffled-drop.ogg"
show eileen outdoors_onhip lookaway frown at left2:
    xpos 0.285 yoffset -25 alpha 0
    ease 1.2 yoffset 25 alpha 1
show eve outdoors normal neutral at right2:
    xzoom -1 xpos 0.75 yoffset 25 alpha 1
"Her parents sure chose a nice place to live. More a town than a city, the wooden buildings and stone retaining walls give a distinctly old fashioned, natural look. Even the Christmas decorations are understated, amounting to the occasional sign behind a shop window."

"The odd person walks to and fro as we sit back, paying us little heed as they slowly go about their day."

show eileen outdoors_onhip lookawaynarrow frown at left2:
    xpos 0.285 yoffset 25 alpha 1
$ renpy.transition(dissolve, layer='master')
"This should be the easiest occasion possible to make idle chatter with Eileen. As time lingers on, though, the silence between us does also."

show eileen outdoors_onhip closed frown at left2:
    xpos 0.285 yoffset 25 alpha 1
$ renpy.transition(dissolve, layer='master')
"Eve doesn't notice, of course. Her little legs swing up and down as she lazily watches the odd car go past."

stop music fadeout 4.0
stop sound fadeout 1.0
scene bg colorado town:
    xalign 0.0
show eve outdoors happy normal at centerright:
    xzoom -1 xpos 0.6
show eileen outdoors_crossed disbelief neutral at left2:
    xzoom -1 xpos 0.25
with fadeInOut
"As she suddenly brightens up and points ahead, Eileen and I follow her gaze."

play music "music/eve_3_m.ogg" fadein 4.0
"Inside the small ice cream parlor over the road, an old man in a pinstripe uniform turns the sign behind the glass door from closed to open."

show eileen outdoors_crossed narrow open at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
voice "Eileen_No2.ogg"
eileen "Don't even think about it."

show eileen outdoors_crossed neutral at left2:
    xpos 0.25
show eve outdoors normal annoyedopen at centerright:
    xzoom -1 xpos 0.6
    linear 0.7 xzoom 1 xpos 0.62
voice "Eve_Grumble4.ogg"
eve "Come on, I've been good!"

show eileen outdoors_onhip closed open at left2:
    xpos 0.25
show eve outdoors normal annoyed at centerright:
    xzoom 1 xpos 0.62
$ renpy.transition(dissolve, layer='master')
eileen "You know what mom said; you can't just have ice cream whenever you want."

show eileen outdoors_onhip normal open at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "Besides, why would you even want ice cream when it's already cold?"

show eileen outdoors_onhip neutral at left2:
    xpos 0.25
show eve outdoors half unsure at centerright:
    xzoom 1 xpos 0.62
$ renpy.transition(dissolve, layer='master')
"Eileen's answer doesn't exactly satisfy the young girl."

show eve outdoors normal unsure at centerright:
    xzoom 1 xpos 0.62
$ renpy.transition(dissolve, layer='master')
"After a moment's consideration, I take to my feet and start heading over."

show eileen outdoors_crossed narrow frown at left2:
    xzoom -1 xpos 0.25
    linear 0.7 xzoom 1 xpos 0.31
voice "Eileen_Allison5.ogg"
eileen "Allison..."

allison "I was just feeling like getting some ice cream for myself. Might as well get her one while I'm already there, right?"

show eve outdoors happy normal at centerright:
    xzoom 1 xpos 0.62
    bounce
eve "Strawberry!"

show eileen outdoors_crossed closed frown at centerleft:
    xzoom 1 xpos 0.31
$ renpy.transition(dissolve, layer='master')
voice "Allison_SureThing.ogg"
allison "Two strawberry ice creams, coming right up."

stop music fadeout 4.0
scene black with circlewipe
$ camera_reset()
scene bg colorado town:
    xalign 0.0
show eileen outdoors_fists normal neutral at left2:
    zoom 0.9 yoffset -80
    xzoom -1 xpos 0.255
show eve outdoors normal grin at center:
    zoom 0.9 yoffset -80
    xpos 0.525
    time 1.5
    ease 0.5 yoffset -75
    ease 0.5 yoffset -85
    ease 0.2 yoffset -80
with circlewipe
"With our sweets quickly devoured, we finish off the last of our cones. They sure serve them large here, but Eve managed to finish off hers even quicker than I did. Maybe eating ice cream is one of those skills kids are just better at."

$camera_move(-1250,250,450,0,5,'ease')
show eileen outdoors_fists closed neutral at left2:
    xzoom -1 xpos 0.255
    ease 2.0 xpos 0.355
    nod2
    ease 2.0 xpos 0.255
show eve outdoors normal annoyed at center with dissolve:
    xpos 0.525
"Without needing to be asked, Eileen pulls a tissue from a box in the bag and curtly wipes Eve's mouth."

"I get the feeling she'd enjoy being a mother, given how she fusses about her little sister."

show shadow:
    alpha 0.4
show bg colorado town HD blurred4 as bg2:
    xzoom -1 yanchor -0.55
    size (1280, 270) crop (300, 200, 1280, 270)
show eileen outdoors_onhip normal sadmouth as eileen2:
    yanchor 0.882
    size (1920, 325) crop (-400, 10, 1920, 325)
with midDissolve
"As Eileen looks to me, I notice that I'm smiling at her."

show eileen outdoors_onhip disbelief open as eileen2:
    yanchor 0.882
    size (1920, 325) crop (-400, 10, 1920, 325)
$ renpy.transition(dissolve, layer='master')
"My face collapses as she opens her mouth to speak, but visibly thinks better of it."

show eileen outdoors_onhip lookawaynarrow sadmouth as eileen2:
    yanchor 0.882
    size (1920, 325) crop (-400, 10, 1920, 325)
$ renpy.transition(dissolve, layer='master')
"As much as I want to make amends, I don't want to apologize if I'm not wrong."

"With neither of us willing to back down - nor wanting to fight with each other again - yesterday's argument looms over us as the elephant in the room."

scene bg colorado town:
    xalign 0.0
$camera_move(-1250,250,450,0,0,'dissolve')
show eileen outdoors_fists lookawaynarrow sadmouth at left2:
    zoom 0.9 yoffset -80
    xzoom -1 xpos 0.255
show eve outdoors half shy at center:
    zoom 0.9 yoffset -80
    xpos 0.525
with midDissolve
$camera_move(650,450,450,-0.5,4,'ease')
show eve outdoors normal neutral at center with midDissolve:
    xpos 0.525
"Focusing my attention on a less stressful topic, my gaze falls to Eve, the two of us sharing a brief smile."

show eileen outdoors_crossed closed open at left2:
    xzoom -1 xpos 0.255
$ renpy.transition(dissolve, layer='master')
eileen "I guess it isn't long now, huh?"

play music "music/anxiety_2_m.ogg" fadein 8.0
show eileen outdoors_crossed normal neutral at left2:
    xzoom -1 xpos 0.255
show eve outdoors half unsure at center:
    xpos 0.525
with dissolve
$camera_move(0,0,0,0,5,'ease')
"Eve and I just look to each other, but it becomes quickly apparent that the topic's reminded Eileen of something I'd been avoiding."

show eileen outdoors_crossed narrow open at left2:
    xpos 0.255
$ renpy.transition(dissolve, layer='master')
eileen "You're being extra nice because you're going back, aren't you?"

show eileen outdoors_crossed narrow neutral at left2:
    xpos 0.255
show eve outdoors normal surprised2 at center:
    xpos 0.525
$ renpy.transition(dissolve, layer='master')
"As Eve looks to and fro between Eileen and I, I try my best to hide my disappointment in being found out. I was trying to think of a better way to break it, before Eileen handled it so bluntly."

"It couldn't last forever, but I wanted to keep enjoying these carefree days just a little while longer. Maybe it was selfish of me to not make myself clearer, but..."

show eve outdoors normal surprised at center:
    xpos 0.525
    ease 1.2 xpos 0.62
eve "Wait, you're going?"

show eileen outdoors_onhip frowning angry at left2:
    xpos 0.255
show eve outdoors normal unsure at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
allison "Well, I do have my own family I want to spend time with."

show eve outdoors normal sad at centerright:
    xpos 0.62
    shaking
with dissolve
"Despite my best efforts to try and deliver the news as gently as possible, her bottom lip starts to quiver. Both of us panic a little as it becomes clear Eve's about to crack."

allison "Uh, Eve?"

scene bg colorado town blurred2:
    xalign 0.0 yalign 0.5 alpha 1
show eileen outdoors_onhip sad sadmouth at left2:
    zoom 0.85 yoffset -100
    xzoom -1 xpos 0.255
show eileen outdoors onhip blurry2 at left2:
    zoom 0.85 yoffset -100
    xzoom -1 xpos 0.255
show eve outdoors normal crying at centerright:
    zoom 1.5 yoffset 250
    xpos 0.655
    shaking
with vpunch
$ camera_reset()
"Her composure collapses as she reaches over, her face weeping as she stuffs it into my stomach and grabs at my skirt."

show eve outdoors normal cryingopen at centerright:
    xpos 0.655
    easein .15 yoffset 232
    easeout .175 yoffset 250
    easein .15 yoffset 242
    easeout .175 yoffset 250
eve "I don't want you to go, Allison! Stay here! I want you to stay!"

$camera_move(-450,-250,450,-0.5,4,'ease')
show eve outdoors blurry2 as eve2 at left2:
    zoom 1.5 yoffset 250
    xpos 0.655 alpha 0.0
    ease 4.0 alpha 1.0
show eileen outdoors onhip blurry2 as eileen2 at left2:
    xzoom -1 xpos 0.255 alpha 1.0
    ease 4.0 alpha 0.0
show eileen outdoors_onhip sad sadmouth at left2:
    xzoom -1 xpos 0.255
$ renpy.pause(4.0, hard=True)
"This has gone about as awfully as it could've done."

hide eileen2
show eileen outdoors_onhip lookawaysad sadmouth at left2:
    xzoom -1 xpos 0.255 alpha 1
$ renpy.transition(dissolve, layer='master')
"Glaring at Eileen in frustration, I seem to have made my feelings clear to her as she turns rather sheepish."

show eve outdoors blurry2 as eve2 at left2:
    xpos 0.655 alpha 1.0
    ease 2.0 alpha 0.0
show eve outdoors normal crying at centerright:
    xpos 0.655
"As Eve cries into my stomach, I stroke her shuddering head reassuringly, speaking as calmly as I can."

show eileen outdoors_onhip sad sadmouth at left2:
    xzoom -1 xpos 0.255
$ renpy.transition(dissolve, layer='master')
allison "Come on now, do you want me to remember you crying, or with a big smile?"

hide eve2
show eve outdoors sad normal at centerright:
    xpos 0.655
    nod2
with dissolve
"My gentle suggestion seems to work as Eve pulls back and sniffs hard, her little cheeks still stained red. She doesn't manage a smile, but I'll take what I can."

show eileen outdoors_crossed sad smile at left2:
    xzoom -1 xpos 0.255
$ renpy.transition(dissolve, layer='master')
allison "There we go, that's more like the Eve I know."

allison "It's been so much fun playing with you, so I wanted to thank you with a little something for being such a good girl."

show eve outdoors half sadopen at centerright:
    xpos 0.655
$ renpy.transition(dissolve, layer='master')
eve "You're gonna come back, right?"

show eve outdoors half sad at centerright:
    xpos 0.655
show eileen outdoors_crossed lookaway angry at left2:
    xpos 0.255
$ renpy.transition(dissolve, layer='master')
allison "Don't worry, I'll come back. Maybe you could even come to Utah and see my home for yourself!"

$camera_move(0,0,0,0,4,'ease')
show eve outdoors normal surprised2 at centerright:
    xpos 0.655
    nod2
"As she clumsily wipes her eyes, I give a big smile."

show eve outdoors normal surprised at centerright:
    xpos 0.655
show eileen outdoors_fists normal neutral at left2:
    zoom 1.4 yoffset 315
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
eve "Really?"

show eve outdoors normal shy at centerright:
    xpos 0.655
show eileen outdoors_fists closed neutral at left2:
    xpos 0.25
    ease 1.0 xpos 0.38
    nod2
    ease 1.0 xpos 0.25
"Eileen just scratches the back of her head, trying not to make things worse."

"We might have our disagreements, but I think we can at least hold things together for Eve's sake."

show eileen outdoors_onhip lookaway smile at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "I guess we can try to work something out."

show eileen outdoors_onhip grumble at left2 with dissolve:
    xpos 0.25
show eve outdoors half unsure at rightish:
    xpos 0.655
    ease 1.5 xpos 0.78
$ renpy.pause(1.5, hard=True)
"Eve looks from Eileen back to me, taking my hand in both of hers with as much strength as her little hands can muster."

show eve outdoors surprised normal at rightish:
    xpos 0.78
    easein .15 yoffset 232
    easeout .175 yoffset 250
    easein .15 yoffset 242
    easeout .175 yoffset 250
eve "Promise me! We're gonna play again, right?"

show eileen outdoors_onhip disbelief neutral at left2:
    xpos 0.25
show eve outdoors normal shy at rightish:
    xpos 0.78 yoffset 250
$ renpy.transition(dissolve, layer='master')
"I just smile as I bring my free hand over both of hers."

allison "I promise."

show eve outdoors grin normal at rightish:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
"At that, she gives that toothy grin that I so like to see. She really is a charming little girl."

show eileen outdoors_crossed smile sad at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "I guess that settles things, then."

stop music fadeout 4.0
show eileen outdoors_crossed closed at left2:
    xpos 0.25
show eve outdoors normal neutral at rightish:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
eileen "Now come on you two, lets get all this back to the car."
stop ambiance fadeout 4.0
show eileen outdoors_crossed lookawaysad sadmouth at left2 with midDissolve:
    xpos 0.25

scene black with midDissolve
$ renpy.sound.set_volume(0.4, channel='ambiance')
play ambiance "sfx/ambiance/fire.ogg" fadein 2.0
scene bg colorado house livingroom night
$camera_move(-800,-650,250,0,0,'dissolve')
with longDissolve
$ renpy.music.set_volume(0.4)
play music "music/night_2_r2.ogg" fadein 4.0
"A quiet yawn fills the living room as I tiredly wander through, the others in the house being quiet as mice."

"I really should have just gone to bed early like the others, in hindsight. Restless from the thought of the trip back, I ended up sitting around and watching television long after Eileen left for bed."

"Try as I might to find her to say good night before going to sleep though, she's nowhere to be seen."

$camera_move(2000,-650,250,0,4,'ease')
"Running through the possibilities, I wander up to Eve's room, opening the door as gently as I possibly can. The sight inside makes me feel warm just by looking at them."

$ renpy.sound.set_volume(0.25, channel='sound')
play sound "sfx/door_creak.ogg"
stop ambiance fadeout 2.0
scene cg act3 sleepingsisters
$camera_move(3400,1400,850,0,0,'dissolve')
with fadeInOut
"Eileen sleeps on her side, wrapped around the slumbering Eve, curled up in a ball on top of her bed. Eve must've wanted one last cuddle before tucking in for the night."

$camera_move(-3400,-2000,850,0,8,'ease')
stop sound fadeout 1.0
$ renpy.pause(8.0, hard=True)
window show dissolve
"I just smile as I silently look over them, slumbering peacefully together."

window hide
$camera_move(0,0,0,0,12,'ease')
"Even as I look at them, I wonder if I belong in their world."

"We have briefly pushed it from our minds, but I think both of us know that the closer we've become, the further apart we've felt."

"With Eileen's peaceful sleeping face lingering in my mind, I gently close the bedroom door and head slowly back down the stairs."

play sound "sfx/door_close.ogg"
scene black with midDissolve
$ camera_reset()
show eve indoors neutral normal at center:
    zoom 1.4 yoffset 150
with midDissolve
stop sound fadeout 1.0
"It's going to be hard saying goodbye to Eve. It's been nice to have a little sister, and I think she's enjoying having two older sisters doting over her just as much."

hide eve with dissolve
show eileen indoors_onhip closed angry at center:
    zoom 1.15 yoffset 135
    xpos 0.52
with midDissolve
"Then, there's Eileen."

scene bg colorado house livingroom night with fadeInOut
play ambiance "sfx/ambiance/fire.ogg" fadein 0.5
"As I try to settle myself before going to bed, I idly notice my phone left on the couch. Taking it in hand to bring it with me, I pause. Eileen's left hers on the table some distance away, the moonlight glinting off its screen."

"My heart stings as I turn on my own and unlock the display. Only the oppressive quiet is here to keep me company as I look down, a heavy weight weighing on me as I ponder."

"Eileen always did enjoy playing with her new phone. In time... she'll hear what I was too cowardly to say."

stop music fadeout 8.0
show bg colorado house livingroom night blurred4
show cg act1 eileenpainting sepia:
    #zoom 2.0 xcenter 0.4 ycenter 0.65 alpha 0.5
    alpha 0.75
with flash
$ renpy.sound.set_volume(0.0, channel='ambiance', delay=10.0)
"Thinking of the girl I admired so much, I make the call."

hide cg with flash
$ renpy.sound.set_volume(1.0, channel='sound')
play sound "sfx/phone-call.ogg"
$ phone.show('call-in')
pause 6.0
window show dissolve
"It doesn't go answered."

window hide
"She never changed the default voicemail message. As the uncharacteristically cheerful tone asks me to leave a message, my voice is barely a whisper for fear of waking them."

stop sound fadeout 1.0
allison "When I said that we had a family with our little art club at college, I really did mean it. It might not be much, but it's ours."

allison "You were an important part of that."

show shadow:
    alpha 0
    ease 8.0 alpha 0.55
"I pause for a moment, my heart stinging as I think of her. Even if it hurts, I know it needs to be said."

allison "Maybe it was naive of me to think that way. Maybe I've been having the wrong idea all this time."

allison "I think..."

$ renpy.sound.set_volume(0.2, channel='ambiance2')
play ambiance2 "sfx/ambiance/soft-tonal-wind.ogg" fadein 10.0
"My throat tightens. I wipe my eyes on my sleeve."

allison "I must have looked pretty stupid. I was so excited to be in love and to have a girlfriend that I pushed and pushed to get into your space, but you didn't let me. You didn't want me to. And even now I can't even muster the courage to tell you this when you're awake."

allison "I don't know where things will go from here. I want you to be happy, but I don't know if I can be the person who does that for you."

"In the end, the anger and frustration I felt at everything is nowhere to be found. There's just an emptiness. I can at least yell and vent to let go of the former, but nothing can fill that hollow feeling."

window show
allison "Good night, Eileen."

show shadow:
    alpha 0.55
    ease 1.0 alpha 0.2
with None
show bg colorado house livingroom night
$ renpy.transition(dissolve, layer='master')
$ phone.hide()
window hide
"With that, I end the call."

stop ambiance fadeout 2.0
scene black with midDissolve
stop ambiance2 fadeout 2.0
$ _dismiss_pause = False
"Silence returns to the dark room once more."

window hide dissolve
scene black with midDissolve
$ renpy.music.set_volume(1.0)
$ renpy.sound.set_volume(1.0, channel='ambiance')
$ renpy.sound.set_volume(1.0, channel='sound')
$ renpy.sound.set_volume(1.0, channel='ambiance2', delay=3.0)
return
