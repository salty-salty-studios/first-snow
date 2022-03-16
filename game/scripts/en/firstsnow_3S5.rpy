label scene_3S5_en:
######################
# Act 3, Scene 5

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg colorado town sketch:
    xalign 0.0 yalign 0.0
$camera_move(3500,-800,400,0,0,'dissolve')
with inkfade
scene bg colorado town:
    xalign 0.0 yalign 0.0
$camera_move(3500,-800,400,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
$ _dismiss_pause = True

play sound "sfx/car-pulling-away.ogg" fadein 1.0
show eve outdoors neutral normal at center:
    zoom 1.0 yoffset -85
    xzoom -1 xpos 0.5
with dissolve
$ renpy.pause(2.0, hard=True)
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
show eve outdoors normal happy at center:
    zoom 1.0 yoffset -85
    xzoom -1 xpos 0.5
    easein .15 yoffset -102
    easeout .175 yoffset -85
    easein .15 yoffset -92
    easeout .175 yoffset -85
$ renpy.music.set_volume(0.65)
play music "music/whimsical_faster_m.ogg" fadein 8.0
window show dissolve

"With a wave to her father as his car disappears down the road, Eve takes my hand in hers as we start off down the street."

window hide dissolve
scene bg colorado town
$camera_move(3200,-2500,600,0,0,'dissolve')
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.13
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.588
with fadeInOut
$camera_move(-3200,-2500,600,0,20,'ease')
stop sound fadeout 1.0

letterbox "With the weather particularly nice today, and Eve needing to burn off some energy, we decided to take a grand tour of the local town. Her pace is thankfully slower than her sister's, with my sore legs needing a rest after the excursion yesterday."

letterbox "I had wanted to do this with Eileen, but she couldn't be dissuaded from painting in her room. There wasn't much fight in me to argue with her, so that was that."

letterbox "Maybe some time away from her is for the best. Even people who like each other sometimes need a break, I think."

letterbox "The old wooden storefronts hardly loom over us, being mostly just a couple of stories tall, themselves dwarfed by the forested hills behind. Strolling around is a much nicer way to take it in than clutching to Rose on the back of her bike."

scene bg colorado town HD
$camera_move(2000,-600,-850,0,0,'dissolve')
show eve outdoors neutral normal at left2:
    zoom 1.4 yoffset 150
    xzoom -1 xpos 0.18
with fadeInOut
window show dissolve
voice "Allison_SoftLaugh.ogg"
allison "It's nice here."

show eve outdoors half unsure at left2:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
voice "Eve_Grumble3.ogg"
eve "Kinda boring sometimes, though."

"Thinking about it, I could see that being the case for a child. The few people out and about today are basically all graying older folk hobbling along as I look around us. Such a pleasant atmosphere has its downsides."

play sound "sfx/cell_phone_vibrate.ogg"
show eve outdoors normal surprised at left2:
    xpos 0.18
    shaking2
"My thinking's interrupted by a ping from my pocket."

$ renpy.music.set_volume(0.5, delay=1.0)
show bg colorado town HD blurred4
show eve outdoors blurry at left2 as eve2:
    zoom 1.4 yoffset 150
    xzoom -1 xpos 0.18
$ renpy.transition(dissolve, layer='master')
window show
$ phone.show('unlock')
"As we stop for a moment, I pluck my phone from my pocket and unlock it."

stop sound fadeout 1.0
window hide
$ phone.message('dad', '11:02 AM', 'Hi Allison')
$ phone.message('dad', '11:02 AM', 'How are things going')
$ phone.show(mode='messages', who='dad')
window show
eve "Who is it?"

allison "Just my dad asking how I'm doing."

$ phone.hide()
window hide
$ renpy.music.set_volume(0.65, delay=1.0)
show eve outdoors normal surprised2 at left2:
    xpos 0.18
    time 0.8
    ease 0.5 yoffset 155
    ease 0.5 yoffset 145
    ease 0.2 yoffset 150
show eve outdoors blurry at left2 as eve2:
    xpos 0.18 alpha 1.0
    ease 1.0 alpha 0
with None
show bg colorado town HD
$ renpy.transition(dissolve, layer='master')
"As she stands on tiptoes, trying to look over the phone in curiosity, I get an idea."

$camera_move(-2500,650,-450,0,3,'ease')
$ renpy.pause(3.0, hard=True)
"Crouching a little and bringing the phone level with her as she sets herself back down, I try to hold it steady."

show white:
    zoom 2.0 xcenter 0.3 ycenter 0.4 alpha 0.5
show cg act2 photo camera as act2_photo_camera:
    subpixel True
    zoom 1.2 xcenter 0.345 ycenter 0.56
with midDissolve
play sound "sfx/camera_focus.ogg"
allison "I'll send him a photo, stay still."

show eve outdoors normal grin at left2:
    xpos 0.18
    nod2
"In response, Eve fixes her posture to stand up prim and proper, dusting herself off to look as good as possible. It's charming how seriously she takes this."

play sound "sfx/camera_shutter.ogg"
hide act2_photo_camera
hide white
with flash
"With a tap and click, the photo's saved and quickly sent on to dad as a message."

$ renpy.music.set_volume(0.5, delay=3.0)
$camera_move(2000,-600,-850,0,3,'ease')
show eve outdoors blurry at left2 as eve2:
    xpos 0.18 alpha 0.0
    ease 4.0 alpha 1.0
with None
show bg colorado town HD blurred4
$ renpy.transition(longDissolve, layer='master')
stop sound fadeout 1.0
$ renpy.pause(3.0, hard=True)

$ phone.show(mode='messages', who='dad')
$ phone.message('dad', '11:05 AM', 'friend\'s sister is showing me around', to=True)
$ phone.wait()

$ phone.message('dad', '11:07 AM', 'Sounds like you\'re having fun')
$ phone.wait()

$ phone.message('dad', '11:07 AM', 'yup \o/', to=True)
$ phone.wait()
$ phone.message('dad', '11:08 AM', 'how are things there?', to=True)
$ phone.wait()

$ phone.message('dad', '11:10 AM', 'Back home safe and sound')
$ phone.wait()
$ phone.message('dad', '11:10 AM', 'Your brothers are driving us nuts')
$ phone.wait()
$ phone.message('dad', '11:11 AM', 'We\'ll be glad to have you back')
$ phone.wait()

"Sounds like things are the same as ever, then."

$ phone.message('dad', '11:11 AM', 'see you in a few days!', to=True)
$ phone.wait()
$ phone.message('dad', '11:11 AM', 'miss you <3', to=True)
$ phone.wait()

$ phone.message('dad', '11:14 AM', 'Take care, enjoy the last of your trip')
$ phone.wait()
window show
$ phone.hide()

$ renpy.music.set_volume(0.65, delay=1.0)
show eve outdoors normal neutral at left2:
    xpos 0.18
show eve outdoors blurry at left2 as eve2:
    xpos 0.18 alpha 1.0
    ease 1.0 alpha 0
with None
show bg colorado town HD
$ renpy.transition(dissolve, layer='master')
"I smile and lock the phone once more, slipping it back where it belongs."

window hide
"I have to stop myself from counting down the days left here. I don't want to start regretting this trip, and once again wishing I was home."

scene bg colorado town:
    xalign 0.0
$camera_move(250,400,350,0,0,'dissolve')
show eve outdoors normal shy at center:
    zoom 1.0 yoffset 0
    xzoom -1
with fadeInOut
eve "Hey, what's your family like?"
voice "Allison_Hm3.ogg"
allison "Totally different, I'll say that much."

show eve outdoors normal neutral at center
$ renpy.transition(dissolve, layer='master')
allison "I have mom, dad, three brothers, and a cat. We all live in the city, and it's really busy and noisy every day."

allison "They're nice, though. It'll be good to be back home."

stop music fadeout 8.0
show eve outdoors grin normal at center
$ renpy.transition(dissolve, layer='master')
"Satisfied with my answer, Eve pulls me forward as we begin our tour in earnest."

show eve outdoors grin normal at center:
    xpos 0.5
    ease 1.5 xpos 1.2
$camera_move(0,0,0,0,20,'ease')
show bg colorado town HD sepia as bg2:
    zoom 0.5 xalign 0.0 yalign 0.5 alpha 0
    ease 8.0 alpha 0.3
show shadow:
    zoom 2.0 alpha 0
    ease 8.0 alpha 0.5
with None
show bg colorado town HD blurred4:
    zoom 0.5
$ renpy.transition(thelongestDissolve, layer='master')
$ renpy.sound.set_volume(0.25, channel='ambiance2')
play ambiance2 "sfx/ambiance/soft-tonal-wind.ogg" fadein 15.0
"As she points out this and that, though, my thoughts aren't about Eve or my family, but stuck on wanting to be doing this with Eileen."

show misc rendered eileen painting flashback:
    alpha 0.6
with longDissolve
"Just as it was whenever I watched her paint, I feel like I'm watching her life from outside, rather than sharing our time together."

show misc rendered eileen physical flashback:
    alpha 0.6
with midDissolve
"I don't doubt that she likes me... she certainly likes me in a physical sense. I like those times too, but I feel like I'm the only one who wants us to become closer in more than just a physical sense."

"I'm the one who planned our first date. I'm the one who asked to come here. Now I'm wondering if Eileen even wanted any of this."

show misc rendered eileen hiking flashback:
    alpha 0.5
with midDissolve
"The one time I thought Eileen wanted to share something with me, she was just using me to distract herself from her problems. Problems that she wouldn't talk to me about."

stop ambiance2 fadeout 4.0
scene bg colorado town:
    xalign 0.0
show bg colorado town HD blurred4 as bg2:
    zoom 0.5 xalign 0.0 yalign 0.5 alpha 1
show eve outdoors normal neutral at center:
    zoom 1.4 yoffset 150
    xzoom -1
$ renpy.transition(midDissolve, layer='master')
voice "Allison_Sigh1.ogg"
"All I can do is sigh."

$ renpy.music.set_volume(0.65)
play music "music/eileen_5_m.ogg" fadein 10.0
show eve outdoors unsure normal at center
$ renpy.transition(dissolve, layer='master')
voice "Eve_Grumble1.ogg"
eve "What's wrong?"

allison "Just a shame your sister was busy, that's all."

show eve outdoors normal sadopen at center
$ renpy.transition(dissolve, layer='master')
voice "Eve_Allison4.ogg"
eve "Is Eileen having a good time in college?"

show eve outdoors normal sad at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Huh1.ogg"
allison "Why do you ask?"

eve "Mom said she was worried about Eileen since she moved out, but when Eileen's around they always argue."

show eve outdoors half sadopen at center
$ renpy.transition(dissolve, layer='master')
voice "Eve_SadOh1.ogg"
eve "Is she really alright?"

show eve outdoors half sad at center
$ renpy.transition(dissolve, layer='master')
"Eve says this with genuine worry in her voice. Eileen's parents really do care about her, even if she doesn't think so sometimes."

allison "Eileen's fine. Every day she's making pretty paintings and having fun with friends, and she's helped me a lot since I met her."

show eve outdoors normal shy at center
$ renpy.transition(dissolve, layer='master')
"Eileen's always been fine, now that I think about it. Ever since we met, I've merely watched her as she lived her life."

"Since getting together, has anything really changed? For all our intimacy, she still treats me the same way she always has, all while relentlessly pursuing her ambition."

"No, I can't think like that. I'm getting myself wound up."

allison "Your parents are nice, aren't they?"

show eve outdoors normal happy at center:
    yoffset 150
    ease 0.5 yoffset 155
    ease 0.5 yoffset 145
    ease 0.2 yoffset 150
"She gives an enthusiastic nod."

eve "They think you're nice too, since you hang out with me."
voice "Eve_Giggle.ogg"

show eve outdoors normal neutral at center
$ renpy.transition(dissolve, layer='master')
"At least they think I'm useful, I suppose."

"I never realized it before, but having a little sister is really fun. Not that I mind my own siblings, but three older brothers aren't quite the same company."
voice "Allison_SoftLaugh.ogg"
allison "Let's see some more of town before we have to go back then, okay?"

show eve outdoors normal grin at center:
    yoffset 150
    easein .15 yoffset 132
    easeout .175 yoffset 150
    easein .15 yoffset 142
    easeout .175 yoffset 150
stop music fadeout 3.0
stop ambiance fadeout 3.0
voice "Eve_Gotcha.ogg"
eve "Yeah!"

scene black with circlewipe
$ camera_reset()
play music "music/anxiety_2_m.ogg" fadein 3.0
play sound "sfx/door_close.ogg"
scene bg colorado house livingroom
$camera_move(-800,-650,250,0,0,'dissolve')
show eve outdoors grin normal at leftedge:
    zoom 0.82 yoffset -220
    xzoom -1 xpos -0.2
    ease 2.0 xpos 0.15
show eileen indoors_onhip neutral normal at rightside as eileen2:
    zoom 1.15 yoffset 120
    xpos 0.87
show eileen indoors_onhip neutral normal at rightside:
    alpha 0 xpos 0.7
with circlewipe
"Finally back from our trip after a bus ride back, Eve bounds through the door as I drag myself in and close it behind us. I don't know how kids can have so much energy."

$camera_move(2000,-650,250,0,4,'ease')
show eve outdoors grin normal at leftedge:
    xzoom -1 xpos 0.15 yoffset -220
    ease 2.5 xpos 0.38
    ease 1.5 yoffset -190
show eileen indoors_crossed narrow angry at rightside as eileen2 with dissolve:
    xzoom 1 xpos 0.87
stop sound fadeout 1.0
"Eileen stands with a glass of water, looking nonplussed at our entrance before noticing the new book held tightly under Eve's arm as she skips over to the living room sofa."

show eileen indoors_fists narrow angry at rightside  as eileen2:
    xzoom 1 xpos 0.87
    linear 0.7 xzoom -1 xpos 0.8
voice "Eileen_Allison5.ogg"
eileen "You didn't."

show eve outdoors normal neutral at centerleft:
    xzoom -1 xpos 0.38 yoffset -190
$ renpy.transition(dissolve, layer='master')
allison "I can spare that much money. It can be her Christmas present from me."

show eileen indoors_fists disbelief smile at rightside as eileen2:
    xzoom -1 xpos 0.8
$ renpy.transition(dissolve, layer='master')
eileen "You're enjoying having a little sis, aren't you?"

"She got me."
voice "Allison_Hmwithquestionmark.ogg"
allison "How's the painting going?"

show eileen indoors_onhip lookaway open at rightside as eileen2:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "Need to go down to the city soon for supplies and stuff; no art supply stores around here. Want to come?"

show eileen indoors_onhip lookaway neutral at rightside as eileen2:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
"So I'm along for the ride as usual."

"I feel bad for thinking bad thoughts about her, but I can't muster any real want to come along. I'd just be baggage while she did her thing."
voice "Allison_Sorry1.ogg"
allison "Sorry, still tired from yesterday."

show eileen indoors_crossed lookawaynarrow open at rightside as eileen2:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Sure1.ogg"
eileen "Suit yourself, I'll be straight back afterwards. We're having pizza for dinner tonight, by the way."

show eileen indoors_crossed neutral at rightside as eileen2:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
allison "Ah, good."

show eileen indoors_crossed narrow angry at rightside as eileen2:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
"The two of us briefly wonder how to continue conversation, but I can't think of anything to add."

show eileen indoors_crossed closed at rightside as eileen2:
    xpos 0.8 alpha 1
    ease 1.2 xpos 1.1 alpha 0
"With that, she wanders back to her room to keep painting. I feel like I should follow, at least to see how her painting's coming along, but my feet feel stuck."

show eve indoors normal neutral at centerleft with dissolve:
    xzoom -1 xpos 0.38 yoffset -190
    nod2
$camera_move(-1500,-650,250,0,4,'ease')
pause 2.0
play sound "sfx/door_open.ogg"
"Left to mill about alone as Eve can be heard happily humming to herself from the sofa, I decide to turn around and head back out the door for some air."

play sound "sfx/door_close.ogg"
scene bg colorado house ext
$camera_move(-2000,1000,600,0,0,'dissolve')
with smoothDissolve
$camera_move(-2000,-1800,600,0,15,'ease')
play ambiance "sfx/ambiance/outside.ogg" fadein 0.5
"The warm afternoon air is starting to fade by now, causing me to push my hands into my pockets to try and save whatever warmth I can. At the rate the weather's going, it's sure going to be a cold Christmas."

"At least the snowmen are liking it, still standing tall as they guard Eileen's house from the front yard."

"It's easy to lose sight of when inside, but her house sure is big. Even the yard's pretty spacious, but I suppose living so far from town would help that."

window hide dissolve
stop sound fadeout 1.0
$ renpy.sound.set_volume(0.3, channel='ambiance2')
play ambiance2 "sfx/ambiance/soft-tonal-wind.ogg" fadein 12.0
stop music fadeout 12.0
scene bg colorado house ext
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter 0.05
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.95
with fadeInOut
$ camera_reset()
show bg colorado house ext blurred4 as bg2:
    xalign 0.5 yalign 0.5 alpha 0
    ease 18.0 alpha 1
show bg colorado house ext sepia as bg3:
    xalign 0.5 yalign 0.5 alpha 0
    ease 18.0 alpha 0.4
show shadow:
    alpha 0
    ease 18.0 alpha 0.55
window hide

letterbox "A nice house, enough money to live alone on her parent's dime, trips all the way to Germany... Eileen really did get a good start in life compared to me. It annoys me a little that she doesn't seem to see that especially when it's her parents paying for her apartment."

letterbox "Painting alone in a room, hiking alone in the woods. Living alone in an apartment too big for one person. Is that really independence? Moving out, away from her parents, but still relying on them for everything?"

letterbox "Try as I might to get closer to Eileen, I can't help but feel like I'm just hanging around her."

letterbox "When I'm looking at her back, is it just because she's always ahead of me? Why shouldn't she turn around to look at me?"

letterbox "I wonder what I really am to Eileen? The fact that I can't work out an answer makes me restless."

stop ambiance fadeout 4.0
stop ambiance2 fadeout 4.0
$ _dismiss_pause = False
letterbox "As a lump starts to form in my throat, I quickly decide to wander back inside; all I'm doing is making myself feel worse by dwelling on all this. I should make the most of my time here, given I only have a few days left."

window hide
scene black with longDissolve
$ renpy.music.set_volume(1.0)
$ renpy.sound.set_volume(1.0, channel='ambiance2')
return
