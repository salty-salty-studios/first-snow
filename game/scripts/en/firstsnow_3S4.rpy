label scene_3S4_en:
######################
# Act 3, Scene 4

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg colorado house livingroom sketch
$camera_move(-2000,-650,250,0,0,'dissolve')
with inkfade
scene bg colorado house livingroom
$camera_move(-2000,-650,250,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
$ _dismiss_pause = True

play music "music/whimsical_faster_m.ogg" fadein 4.0
show eve indoors normal shy at centerleft:
    zoom 0.82 yoffset -220
    xzoom -1 xpos 0.38
$ renpy.transition(dissolve, layer='master')
window show dissolve

"The sound of Saturday morning kid's shows fills the living room as I walk back in, each hand carefully balancing a bowl of cereal."

show eve indoors normal shy at centerleft:
    xzoom -1 xpos 0.38 yoffset -220
    ease 1.0 yoffset -190
"Eve sits quietly, wholly focused on watching television."

show eve indoors normal grin at centerleft:
    xzoom -1 xpos 0.38 yoffset -190
$ renpy.transition(dissolve, layer='master')
"While still something of a work in progress, she seems more content to let me hang around now, even if she doesn't engage much. Maybe simply being friendly company is enough for her."

"Despite being the weekend, Eve's parents are out once again. This time, they're with Eileen to check how her car is going."

show eve indoors normal neutral at centerleft:
    xzoom -1 xpos 0.38
$ renpy.transition(dissolve, layer='master')
"Of all the ways Eileen's home is different to my own, it's the sheer quiet that most gets me. With few cars around nor people nearby, there's only the odd boisterous bird outside to make noise. I could get used to small town life like this."

play sound "sfx/door_close.ogg"
$camera_move(2000,-650,250,0,4,'ease')
show eileen outdoors_onhip closed neutral at rightside:
    subpixel True
    zoom 1.15 yoffset 120
    xpos 1.2
    ease 4.0 xpos 0.85
"My spacing out is interrupted as the main door shuts with a loud thud, a familiar figure striding past."
voice "Allison_Hey2.ogg"
allison "Welcome back. How's the car?"

stop sound fadeout 1.0
show eileen narrow open at rightside
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "It's fine."

show eileen lookaway at rightside
$ renpy.transition(dissolve, layer='master')
eileen "We're heading out once dad's finished poking at it, by the way."

show eileen neutral at rightside
$ renpy.transition(dissolve, layer='master')
voice "Allison_Um2.ogg"
allison "Uh, sure. Where're we going?"

show eileen outdoors_crossed normal open at rightside
$ renpy.transition(dissolve, layer='master')
eileen "You'll see. Finish your breakfast for now, I'll get your clothes out and pack everything."

show eileen neutral at rightside
$ renpy.transition(dissolve, layer='master')
"Isn't this a bit of a rush? I still have sleep in my eyes from waking up, and she's usually a zombie at this time of morning."

"Still standing around with bowls in my hands, I hold them out and look down, checking that I'm not going crazy and did actually dress myself this morning."

allison "But I'm already dressed."

stop music fadeout 3.0
show eileen closed open at rightside
$ renpy.transition(dissolve, layer='master')
eileen "Not for where we're going."

scene black with midDissolve
$ renpy.sound.set_volume(0.5, channel='ambiance')
play ambiance "sfx/ambiance/forest-afternoon.ogg" fadein 4.0
scene bg colorado hiking1:
    xalign 0.0
$camera_move(650,-2200,800,0,0,'dissolve')
with longDissolve
play music "music/snow_4_m.ogg" fadein 8.0
$camera_move(0,0,0,0,20,'ease')
$ renpy.sound.set_volume(0.8, channel='loopsfx')
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 4.0
"The quiet morning is only punctuated by the crunch of snow underfoot, the occasional bird's chirping, and the jangle of items from our backpacks."

"Apart from the woman plodding ahead before me and the footprints she leaves behind, all that I can see are pine trees, as much snow on their branches as greenery."

"Oh, and the puffs of condensation from our breaths."

"The scenery is nice, at least. I'd hardly expected to be spending today hiking through the forest when she dragged me out of the house, but so far, it's been a pleasant way to spend the day."

"Tired as my legs may be, Eileen's pace doesn't falter. The hiking clothes she lent me hang off my frame, but I suppose that should have been expected given our height difference. They're comfortable, though, and most of all warm."

show eileen hiking_onhip closed open at center
$ renpy.transition(dissolve, layer='master')
eileen "Picked a good day for all this. Not exactly warm, but at least it's not bitterly cold."

show eileen hiking_onhip lookaway neutral at center
$ renpy.transition(dissolve, layer='master')
"She says this with all the care that one might give when looking out the window of a morning. Eileen really seems to be treating this as almost an everyday activity."

"The fact we need bear spray out here also weighs on my mind, apparently being black bear country. Eileen simply carries it in stride."

stop loopsfx fadeout 2.0
window hide dissolve

scene bg colorado hiking1:
    subpixel True
$camera_move(3200,-2500,600,0,0,'dissolve')
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.13
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.588
with fadeInOut
$camera_move(-3200,-2500,600,0,20,'ease')

letterbox "And so we keep plodding ahead."

letterbox "On the plus side, the air is nice and fresh up here. The odd huge bird squawking as it flies above us, its calls echoing around the mountains, makes for a nice atmosphere."

letterbox "When we're alone like this, her family feels like the elephant in the room. There's so much I want to talk to her about, but I'm not sure what I'm supposed to say, since she told me not to pry."

$ renpy.sound.set_volume(1.0, channel='loopsfx', delay=4.0)
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 4.0
scene black with midDissolve
$ camera_reset()
scene bg colorado colorado hiking loop:
    subpixel True
    xalign 1.0 yalign 0.2
    parallel:
        linear 60.0 xalign 0.0
    parallel:
        linear 1.0 yoffset -1
        linear 1.0 yoffset 1
        repeat 30
show bg colorado colorado hiking loop blurred2 as bg2:
    subpixel True
    xalign 1.0 yalign 0.2 alpha 0.85
    parallel:
        linear 60.0 xalign 0.0
    parallel:
        linear 1.0 yoffset -1
        linear 1.0 yoffset 1
        repeat 30
show black
$ renpy.transition(dissolve, layer='master')
hide black
show eileen hiking_onhip neutral lookaway at right2:
    zoom 1.2 yoffset 180
    xpos 0.755
with longDissolve
window show dissolve

"Wanting to fill the air with something, I end up settling for the mildest of smalltalk."

allison "So you're experienced at this, huh?"

show eileen hiking_onhip open normal at right2:
    xpos 0.755
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Sure1.ogg"
eileen "Yeah, been for a few hikes 'round here."

eileen "Played outside a lot as a kid, ended up adventuring more and more until I started hiking."

show eileen hiking_onhip neutral normal at right2:
    xpos 0.755
$ renpy.transition(dissolve, layer='master')
allison "With your father, or...?"

show eileen hiking_onhip narrow open at right2:
    xpos 0.755
$ renpy.transition(dissolve, layer='master')
voice "Eileen_No1.ogg"
eileen "No, alone. It's nice to have some time to myself."

show eileen hiking_onhip angry at right2:
    xpos 0.755
$ renpy.transition(dissolve, layer='master')
"Without a doubt, Eileen has to be the most solitary person I've ever met. Maybe this explains her abrasiveness towards her parents, but it feels little unfair for her to take it out on them."

show eileen hiking_onhip lookawaynarrow at right2:
    xpos 0.755
$ renpy.transition(dissolve, layer='master')
eileen "Coming out here's been a real help with my art, too."

show eileen hiking_onhip closed neutral at right2:
    subpixel True
    xpos 0.755
    ease 3.0 xpos -0.2
allison "But we're..."

stop loopsfx fadeout 2.0
show bg colorado colorado hiking loop:
    subpixel True
    parallel:
        linear 10000.0 xalign 0.0
    parallel:
        linear 2.0 yoffset 0 yalign 0.5
show bg colorado colorado hiking loop blurred2 as bg2:
    subpixel True
    parallel:
        linear 10000.0 xalign 0.0
    parallel:
        linear 2.0 yoffset 0 yalign 0.5
    parallel:
        alpha 0.85
        linear 2.0 alpha 0
show shadow:
    alpha 0
    ease 2.0 alpha 0.4
"Running out of breath, I have to stop and take a moment to collect myself. My natural pace is slower then Eileen's, making this hike all the more taxing."
voice "Allison_Sigh1.ogg"
allison "How is all this related to art?"

hide eileen
show cutin eileen hiking:
    zoom 0.99 xoffset 0 yoffset 0
with midDissolve
eileen "The more life experiences you have, the more inspiration you have; hard to create anything of worth while stuck in the four walls of my room."

eileen "You need input to be able to create output. That's how culture works."

$ renpy.sound.set_volume(0.3, channel='ambiance', delay=2.0)
scene bg colorado hiking1 HD
$camera_move(0,-3000,250,0,0,'dissolve')
with fadeInOut
"Thinking on her words as I turn and start moving once more, Eileen's voice calls out."

show eileen hiking_onhip open normal at centerleft:
    zoom 0.65 yoffset -510
    xzoom -1 xpos 0.37
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Allison2.ogg"
eileen "Watch out, there's a stone there."

show eileen hiking_onhip neutral normal at centerleft:
    xzoom -1 xpos 0.37
$ renpy.transition(dissolve, layer='master')
"I look at my feet, quickly stepping around the dangerous trip hazard. If it weren't so big, I'd move it out of the way for future people coming up here."

show eileen hiking_onhip closed open at centerleft:
    xpos 0.37
$ renpy.transition(dissolve, layer='master')
eileen "I took this route a lot as a kid. It's probably the easiest way to make it through this area, but you still have to keep an eye out."

show eileen hiking_onhip neutral normal at centerleft:
    xpos 0.37
$ renpy.transition(dissolve, layer='master')
"My breathing heavy, I come to the grim realization that Eileen must've been far more fit when she was young than I am now."
voice "Allison_Sorry1.ogg"
allison "Sorry. I'm a total city kid, I guess."

show eileen hiking_onhip narrow smile at centerleft:
    xzoom -1 xpos 0.37
    linear 0.7 xzoom 1 xpos 0.42
voice "Eileen_Heh3.ogg"
eileen "You're plenty smart, but you can't just pick up everything from books and internet, you know."

"I don't really know how to receive that half-compliment, half-criticism."

show eileen hiking_onhip closed at centerleft:
    xzoom 1 xpos 0.42 alpha 1
    ease 1.5 xpos 0.35 alpha 0
"Is this where Eileen picked up her independence, hiking in the woods alone? It's not like it's bad out here; the air and the sounds and everything are nice. I just can't imagine doing this alone."

"And not just because I'm barely being pulled along as it is."

play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 4.0
scene bg colorado hiking1:
    xalign 0.0
show eileen hiking_onhip disbelief frown at center
with fadeInOut
$ camera_reset()
allison "Do you think maybe we can rest soon?"

show eileen hiking_onhip narrow at center
$ renpy.transition(dissolve, layer='master')
"Going by the frown on her face, Eileen is clearly disappointed with my request."

$ renpy.sound.set_volume(0.1, channel='ambiance', delay=5.0)
show eileen hiking_onhip lookawaynarrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "We've barely started. There's a resting place I want to reach, but we can't stop every few minutes if we want to get back by sundown."

stop music fadeout 5.0
show eileen hiking_onhip frown at center
$ renpy.transition(dissolve, layer='master')
"Just how far does she plan to take us?"

$ renpy.sound.set_volume(1.0, channel='ambiance2')
scene black with circlewipe
play ambiance2 "sfx/ambiance/water-stream.ogg" fadein 0.5
scene bg colorado hiking2:
    xalign 0.0
with circlewipe
"The sound of the river getting louder and louder as we walk, before the two of us finally reach a clearing after a couple of hours or so of hiking."

"Despite barely being able to walk, I've kept myself from complaining any more, not wanting Eileen to be disappointed in me again. With the two of us slowing to a stop as she looks around, it seems we'll be finally making a pit stop here."

stop loopsfx fadeout 2.0
$ renpy.sound.set_volume(0.1, channel='ambiance')
play ambiance "sfx/ambiance/forest-afternoon.ogg" fadein 2.0
show eileen hiking_onhip lookaway neutral at offcenterleft as eileen2:
    zoom 0.68 yoffset -235
    xzoom -1 xpos 0.485
show eileen hiking_onhip lookaway neutral at center:
    alpha 0 xpos 0.5
$ renpy.transition(dissolve, layer='master')
eileen "Same as it always was, looks like nobody's messed with it."

show eileen hiking_onhip lookaway neutral at center as eileen2:
    xzoom -1 xpos 0.485
    nod2
"I'm about to ask what's so significant about this place before she bends down and sweeps some snow off a few large rocks, showing them to be purposefully set in a small circle."

show eileen hiking_onhip open normal at offcenterleft as eileen2:
    xzoom -1 xpos 0.485
$ renpy.transition(dissolve, layer='master')
eileen "Here, have a seat."

$ renpy.sound.set_volume(0.3, channel='sound')
$ renpy.sound.set_volume(0.6, channel='ambiance2', delay=5.0)
$camera_move(3000,200,600,0,5,'ease')
show eileen hiking_onhip normal neutral at offcenterleft as eileen2:
    xpos 0.485 yoffset -235
    ease 1.0 yoffset -220
show eileen hiking_onhip lookaway neutral at center:
    alpha 0 xpos 0.5
    ease 3.0 xpos 0.1
play sound "sfx/muffled-drop.ogg"
"Setting herself down on a particularly large rock, I quickly follow her lead and sit next to her. Looks like most of the rocks here were carefully set in the ground to make a little campsite, positioned next to the gently flowing river. My legs are happy I get to sit down."

allison "Looks like you've come here before."

show eileen hiking_onhip lookawaynarrow open at offcenterleft as eileen2:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "I ended up building this place up into a little base camp over the years. Bears kept taking out anything I brought in or set up, but at least they leave the rocks and ditches alone."

$ renpy.sound.set_volume(1.0, channel='sound')
play sound "sfx/water-pour.ogg"
show eileen hiking_onhip closed neutral at offcenterleft as eileen2:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
"Eileen makes herself comfortable as she pulls out a tin and thermos to pour herself some water, while I cup my hands and huff into them to warm up a little."

window hide dissolve
$ renpy.sound.set_volume(0.5, delay=3.0, channel='ambiance')
scene bg colorado hiking2
$camera_move(3200,-1800,600,0,0,'dissolve')
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.06
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.668
with fadeInOut
$camera_move(-3200,-1800,600,0,20,'ease')
stop sound fadeout 1.0

letterbox "With the two of us settling down to recover for a while, I listen to the sounds around us."

letterbox "It's so different to my own home, with the sounds of cars and crowds replaced by the river's slow trickling and various birds and other wildlife."

letterbox "Somehow, it isn't a surprise this is the kind of place Eileen would like. As she sits out here thinking to herself, she looks like part of the scenery, just as she did in her quiet art room. At least, until Caprice and I made it decidedly less quiet."

letterbox "Then there's me, in my oversized clothes and labored breaths."

$ renpy.music.set_volume(0.65)
play music "music/painter.ogg" fadein 8.0
$ renpy.sound.set_volume(0.08, delay=2.0, channel='ambiance')
$ renpy.sound.set_volume(0.25, delay=2.0, channel='ambiance2')
scene bg colorado hiking2:
    xalign 0.5 yalign 0.5
show eileen hiking_onhip closed neutral at center
with fadeInOut
$ camera_reset()
window show dissolve
voice "Allison_Hm2.ogg"
allison "It's peaceful."

show eileen hiking_onhip neutral normal at center
$ renpy.transition(dissolve, layer='master')
eileen "Yeah."

allison "I thought my apartment was quiet, but it's nothing like this."

show eileen hiking_onhip disbelief open at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "Your place wasn't quiet at all when I was there. Constant cars, construction, and people walking by."

show eileen hiking_onhip neutral at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hm2.ogg"
allison "I'm not like you; I've only ever lived in the big city."

allison "I was worried about being so far from home, but I think I like it here. Playing with Eve has been fun, too."

allison "Your family has been really nice to me, as well."

show eileen hiking_onhip narrow frown at center
$ renpy.transition(dissolve, layer='master')
"Eileen's face sours, making me immediately regret adding that last little addendum, or more to the point, that lecturing tone."

"I want to understand her, but she only gives me small pieces to work with; not enough to puzzle things together."

"I knew my sudden intrusion into her home would be at least a little awkward, but I've begun to realize Eileen's resistance to bringing me here was about more than that."

show eileen hiking_onhip lookawaynarrow at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Eileen3.ogg"
allison "Just..."

"I've started speaking before even gathering my thoughts. This isn't a great start."

allison "Just what is it that makes you want to be away from them so much? To move to a different state..."

allison "I mean, is it just about your choice of career, or--"

show eileen hiking_onhip annoyed open at center
$ renpy.transition(dissolve, layer='master')
stop music fadeout 4.0
stop ambiance fadeout 4.0
stop ambiance2 fadeout 4.0
voice "Eileen_Ugh3.ogg"
eileen "Can we not bring all that up? I came here exactly to get away from my parents being on my case."

$camera_move(-150,600,600,0,5,'ease')
show bg colorado hiking2 sepia as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0
    ease 5.0 alpha 0.2
show shadow behind eileen:
    alpha 0
    ease 5.0 alpha 0.35
show eileen hiking_onhip frown at center
with None
show bg colorado hiking2 blurred4 as bg3 behind eileen, bg2:
    xalign 0.5 yalign 0.5
$ renpy.transition(verylongDissolve, layer='master')
$ renpy.sound.set_volume(0.2, channel='ambiance')
play ambiance "sfx/ambiance/soft-tonal-wind.ogg" fadein 5.0
"And then there was silence."

"That explains her rush in the morning to organize our hiking trip out here, especially if she was stuck with her parents while they gave her car a spin around town."

"So what am I even here for?"

$camera_move(-150,-650,600,0,3,'ease')
show bg colorado hiking2 sepia as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0.2
    ease 5.0 alpha 0.0
show bg colorado hiking2 blurred4 as bg3 behind eileen, bg2:
    xalign 0.5 yalign 0.5 alpha 1
    ease 3.0 alpha 0.4
show shadow behind eileen:
    alpha 0.35
    ease 3.0 alpha 0.2
show eileen hiking_onhip normal open at center
eileen "Something up?"

show eileen hiking_onhip angry at center
$ renpy.transition(dissolve, layer='master')
allison "I thought you brought me out here because you wanted to share it with me. I was really excited to see the kinds of things you did growing up."

show eileen hiking_onhip lookaway frown at center
$ renpy.transition(dissolve, layer='master')
"Her face tells me that she hadn't even considered that reasoning. I feel a little stupid for attaching so much feeling to this, now."

show eileen hiking_onhip lookawaynarrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "Well, I mean... it wouldn't be a good look if I left you back at the house while I wasted time out here."

$ renpy.music.set_volume(0.8)
play music "music/more_sad_m.ogg" fadein 8.0
$camera_move(0,0,0,0,8,'ease')
show bg colorado hiking2 blurred4 as bg3:
    xalign 0.5 yalign 0.5 alpha 0.4
    ease 8.0 alpha 1.0
show bg colorado hiking2 sepia as bg2:
    xalign 0.5 yalign 0.5 alpha 0
    ease 5.0 alpha 0.2
show shadow:
    alpha 0.2
    ease 8.0 alpha 0.5
show eileen hiking onhip blurry as eileen2 at center:
    alpha 0
    ease 8.0 alpha 1
show eileen hiking_onhip lookawaynarrow angry at center:
    alpha 1
    ease 10.0 alpha 0
"So this was just stress relief for her. Even now she's not looking at me, probably more busy thinking things over with regards to her family. I open my mouth to try and ask her about it, but I can't work out what to say."

"I'm just here because she feels obligated to invite me. I guess I should have realized she doesn't want me here. She didn't want me here at her home at all."

"I'm the invader, I'm in her space. It's no wonder she treated me like a burden this entire walk. If I was going to get in her way, she should have just said so."

"In the end, the only reason I even know anything about her disagreement with her parents is because Eve told me. Eileen doesn't want me to know."

stop music fadeout 4.0
stop ambiance fadeout 4.0
"For now, I'll just have to be content as a spectator, looking into her life without getting too involved."

scene bg colorado hiking2
show eileen hiking_onhip sad open at center
with midDissolve
$ renpy.sound.set_volume(0.08, delay=8.0, channel='ambiance')
play ambiance "sfx/ambiance/forest-afternoon.ogg" fadein 2.0
$ renpy.sound.set_volume(0.25, delay=8.0, channel='ambiance2')
play ambiance2 "sfx/ambiance/water-stream.ogg" fadein 0.5
voice "Eileen_Huh2.ogg"
eileen "Um..."

show eileen hiking_onhip disbelief frown at center:
    nod2
"I quickly look to her, but rather than acting contrite, she's pointing to my left side with her gaze focused."

play music "music/anxiety_2_m.ogg" fadein 5.0
"An insect seems to be lazily crawling around on the top of my left hand, the thing about a fingernail in length and jet black. I don't recognize it, but it looks harmless enough."

"To be honest, I couldn't care less about the little beetle right now."

show eileen hiking_onhip normal open at center
$ renpy.transition(dissolve, layer='master')
eileen "You're not worried?"

show eileen hiking_onhip neutral at center
$ renpy.transition(dissolve, layer='master')
allison "Should I be?"

show eileen hiking_onhip narrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "Well, I mean... most people don't like bugs crawling on them much."

show eileen hiking_onhip neutral at center
$ renpy.transition(dissolve, layer='master')
"I just shrug, leaning down to press the side of my hand to the cold ground while gently persuading the bug to get off with my other hand."

"After a bit of effort, the little fellow gets off my glove and onto the soil, scampering off a little faster for the experience."

allison "It won't hurt me."

show eileen hiking_onhip narrow smile at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh2.ogg"
eileen "What, just another of your animal friends?"

"I'm not exactly in the mood for being teased."
voice "Allison_Hm4.ogg"
allison "It's the kind of thing you can learn in books or on the internet."

show eileen hiking_onhip sad smile at center
$ renpy.transition(dissolve, layer='master')
"Eileen laughs it off, but I'm sure she can tell I'm being snippy."

scene bg colorado hiking2:
    xalign 0.0
$camera_move(1500,200,600,0,0,'dissolve')
show eileen hiking_onhip closed neutral at offcenterleft as eileen2:
    zoom 0.68 yoffset -220
    xpos 0.48
    time 1
    ease 1.0 yoffset -235
    nod2
show eileen hiking_onhip lookaway neutral at center:
    alpha 0 xpos 0.1
with fadeInOut
"With that, she stands up, putting her thermos and cup back into her backpack before dusting herself off."

show eileen hiking_onhip normal open at offcenterleft as eileen2:
    xpos 0.48
$ renpy.transition(dissolve, layer='master')
eileen "Ready to keep going, then? We've still got the afternoon ahead of us."

show eileen hiking_onhip lookaway frown at offcenterleft as eileen2:
    xpos 0.48
    ease 2.0 xpos 0.1
voice "Allison_NervousSure.ogg"
allison "Yeah, sure."

"I try to put as much enthusiasm into it as I can muster, but I get the distinct feeling that I'm just along for the ride, now."

hide eileen
hide eileen2
$camera_move(0,0,0,0,5,'ease')
stop music fadeout 5.0
stop ambiance fadeout 5.0
stop ambiance2 fadeout 5.0
show shadow:
    alpha 0
    ease 5.0 alpha 0.5
"And so, she pushes forward without looking back at me."

$ _dismiss_pause = False
"This is always where I am, with her. Whether I'm watching Eileen paint or watching her hike, I'm always far behind her with eyes on her back."

window hide dissolve
scene black with longDissolve
$ renpy.music.set_volume(1.0)
$ renpy.sound.set_volume(1.0, channel='ambiance', delay=2.0)
$ renpy.sound.set_volume(1.0, channel='ambiance2', delay=2.0)
$ renpy.sound.set_volume(1.0, channel='loopsfx')
return
