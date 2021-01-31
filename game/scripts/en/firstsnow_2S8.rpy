label scene_2S8_en:
######################
    perform "2S8_a"
    perform "2S8_b" explicit
    perform "2S8_c"
    return


label scene_2S8_a_en:

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg misc zoo HD sketch
$camera_move(6500,-3000,500,0,0,'dissolve')
with inkfade
scene bg misc zoo HD
$camera_move(6500,-3000,500,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

$ renpy.sound.set_volume(0.2, channel='ambiance')
play ambiance "sfx/ambiance/crowd_loud.mp3" fadein 2.5
play music "music/zoo_4_m2.ogg" fadein 5.0
play sound "sfx/elephant.ogg"

"The elephant's mighty trumpeting sends a couple of children scurrying away with giggles of laughter, the animal as excited about the small crowd watching on as they are of him."

$camera_move(4500,-3000,500,0,4,'ease')
"Stepping back from the enclosure and joining Eileen once more, the two of us walk on."

stop sound fadeout 1.0
scene bg misc zoo with midDissolve
$ camera_reset()
"Even as we bought our tickets, I'd wondered if coming here during winter was such a good idea. It turned out to be better than I could've hoped."

allison "I've never been here with so few people around, usually this is a complete madhouse. It's nice."

scene bg misc zoo blur
show misc cutins hands:
    zoom 0.95 xalign 0.5 yoffset 2
with midDissolve
"As we stroll on, Eileen takes my hand in hers as we walk. It's weird how such a simple gesture can make me feel so warm, my cheeks hurting as I smile."

"I've seen it done in so many romantic movies, but actually feeling someone take my hand in theirs feels so unexpectedly comforting."

eileen "You're easy to please."

"Without any real idea of how to respond, all I can do is keep walking."

"Maybe I should find it off-putting that Eileen's so calm about this sort of thing compared to me, but I think I might even prefer it. She feels reliable, I think. Levelheaded."

scene bg misc zoo
show eileen outdoors_crossed normal open at rightish:
    zoom 1.25 yoffset 218
    xpos 0.72
with dissolve
eileen "Crowded or not, it's a nice zoo."

show eileen neutral at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
allison "You've never been here before?"

show eileen lookaway open at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
eileen "Considering I've only been in this city since college started? Not really."

show eileen neutral at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
allison "Wait, where do you come from, then?"

show eileen outdoors_fists closed frown at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
eileen "Russia. My family immigrated a few years ago, so still getting used to how things work around here."

"The question of whether she was a native has genuinely never occurred to me. She doesn't have any kind of accent, so I would never have thought of it."

show eileen disbelief frown at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
"If she's Russian, I couldn't tell at all."

show eileen outdoors_onhip narrow open at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
eileen "That was a lie."

show eileen sad neutral at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
allison "Oh."

"I can't tell if she meant for it to be a joke. Her expression makes it obvious she didn't expect me to actually fall for it. It's too late to laugh now, and I just feel stupid for not questioning her."

show eileen outdoors_crossed lookawaynarrow open at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
eileen "I'm actually from around here, but moved to Colorado when I was a kid. I never had much interest in zoos."

show eileen neutral at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
allison "Colorado, huh. But why would you come back here?"

show eileen closed open at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
eileen "Moved out from my folk's place to make my own path. Have my own home, partner, life, and all that."

show eileen neutral at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
"To choose to move so far away from her family, especially to live in her apartment alone... it's hard to imagine, considering how hard it's been for me. Having problems with her family is one thing, but jumping states to get away from them?"

show eileen outdoors_fists normal at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
"Left wondering if I should delve into the topic any further, Eileen speaks up as we leave the Savannah area."

$camera_move(-450,-1200,600,0,4,'ease')
show eileen outdoors_fists normal at rightish:
    subpixel True
    xpos 0.72
    ease 4.0 xpos 0.7
"The few people around the zoo seem to be congregating around the eating area ahead, which is a good sign we should grab some lunch too."

show eileen open at rightish
$ renpy.transition(dissolve, layer='master')
eileen "Hungry?"

show eileen neutral at rightish
$ renpy.transition(dissolve, layer='master')
allison "Just a bit."

"To be honest, I just need a rest. Eileen's pace is unrelenting, yet she looks fine despite how ragged I am. I don't understand it."

$camera_move(0,0,0,0,4,'ease')
show eileen outdoors_onhip closed neutral at rightish:
    subpixel True
    xpos 0.7
    ease 4.0 xpos 0.72
eileen "I'll go grab something, then. Go grab a seat for us before they're all taken, would you?"

allison "Roger!"

show eileen narrow angry at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
eileen "Caprice's speech patterns are rubbing off on you..."


scene bg misc zoo HD
$camera_move(-2800,-3000,500,0,0,'dissolve')
show eileen outdoors_onhip lookawaynarrow angry at offcenterright:
    zoom 0.45 yoffset -655
    xpos 0.65 alpha 0
    ease 1.5 xpos 0.55 alpha 1
with fadeInOut
"We both share a grimace at the idea before we part, Eileen heading for the hot food stall ahead as I skip down to one of two unused tables on the outside of the seating area."

play sound "sfx/body_prod.ogg"
with vpunch
"I practically fall into the hard metal seat, watching the condensation from my breathing rise into the air as I recover myself. If nothing else, at least going out with Eileen will do wonders for my fitness."

scene bg misc zoo HD blurred2:
    xalign 0.5 yalign 0.2
$camera_move(-1200,1850,200,0,0,'dissolve')
show eileen outdoors_crossed lookaway angry at centerright:
    zoom 1.3 yoffset 300
    xzoom 1 xpos 0.68
with midDissolve
$camera_move(-1200,-400,200,0,10,'ease')
"With several couples in line ahead of her, Eileen crosses her arms and patiently waits."

"I can't help but let my eyes settle on her as she does; ever since we met, I've noticed how beautiful she is."

scene bg misc zoo HD:
    xalign 0.48 yalign 0.2
$camera_move(-2500,-250,0,0,0,'dissolve')
show eileen outdoors_onhip normal neutral at offcenterleft:
    zoom 1.25 yoffset 218
    xpos 0.7 alpha 0
    time 1
    ease 1.8 xpos 0.45 alpha 1
with fadeInOut
"Her order made, I'm a little impressed at her managing to bring the sodas and hotdogs over in one trip with some very careful use of her fingers."

play sound "sfx/chair_scrape_fast.ogg"
show eileen outdoors_onhip normal neutral at offcenterleft:
    zoom 1.25 yoffset 218
    xpos 0.45 alpha 1
    ease 0.5 yoffset 222
    ease 0.5 yoffset 212
    ease 0.2 yoffset 218
"Hungry from all the walking, I quickly slide mine towards me as she sets them down and takes a seat."

allison "How much was my share?"

show eileen outdoors_crossed lookawaynarrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "It's fine, don't worry."

show eileen angry at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "You already bought my ticket..."

show eileen narrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "I said it's fine. Besides, it's nice to dote on someone."

show eileen angry at offcenterleft
$ renpy.transition(dissolve, layer='master')
"When she puts it like that, it's hard to argue with her. Letting Eileen have her way, I start on my food."

show eileen outdoors_fists normal neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
play sound "sfx/eagle.ogg"
"A loud bird squawks in the distance, its calls reaching right across the entire zoo. I've always liked the strange and unfamiliar sounds you get in a place like this, compared to the relative quiet of the apartments and the routine sounds of school."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"As comfortable as Eileen looks, packing up her quickly finished hotdog and soda and pitching them into a nearby bin, I can't quite seem to settle down. Thankfully she's willing to take charge, given that I have no idea what I'm doing or how to act."

$ renpy.music.set_volume(0.6, delay=4.0)
show eileen outdoors_onhip normal open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Enjoying yourself?"

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "Ah, yes!"

"I really need to settle down. At least she doesn't seem to be too harsh on me for my nervousness, but it's plainly obvious that this is my first date."

show eileen closed open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "That's good. I'm not sure what to make of you when you clam up."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "I'm just not as used to this as you are."

show eileen outdoors_crossed disbelief at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "What makes you think that?"

allison "You've never gone out with someone before?"

show eileen narrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Do I look like I have?"

show eileen angry at offcenterleft
$ renpy.transition(dissolve, layer='master')
"I almost blurt out a rather blunt answer. 'Uncompromising' is definitely the word for her, but that doesn't mean she couldn't have had a girlfriend before me."

"Especially at our age, come to think of it. At least I had the excuse of being a bit shy, and focusing myself on schoolwork. Eileen said herself she's known since at least high school."

scene cg act2 zoo smile with midDissolve
$ camera_reset()
"Eileen brings her head down, resting her chin on her arms as they lay on the table. I'm dumbstruck as she looks up at me with those tired eyes of hers."

eileen "For what it's worth, I'm glad you're my first. You're a sweet girl."

$ renpy.music.set_volume(1.0, delay=4.0)
"That look she gives me singlehandedly explains why people do all this dating business. For one brief moment, it feels like the two of us are really in sync as we look into each other's eyes."

play sound "sfx/bird-flap1.ogg"
scene cg act2 zoo bird
$camera_move(950,1200,600,0,0,'dissolve')
with hpunch
"Only for a moment though, before a small bird suddenly lands onto the table between us. Its head darts this way and that, but it doesn't seem in the least bit shy about parking itself in front of Eileen's startled face."

eileen "Well now, hello there."

stop sound fadeout 1.0
allison "Aaah, a little Fox Sparrow! It's so cute!"

"Even my excited whispers don't seem to bother the little thing, leading to me gingerly breaking off a little of my hotdog bun and trying to feed it."

"While a little too timid to outright take food from my fingers, it seems quite happy to pick at a few sprinkles of bun I leave before it on the table. Eileen seems content to simply watch our little companion."

$camera_move(0,0,0,0,5,'ease')
eileen "You know what it's actually called?"

allison "It's orange and white, after all."

eileen "That would make it easy to remember."

"As the slightly chubby bird busies itself becoming a little chubbier, I feel my cheeks hurting from my smiling."

eileen "You really like animals, don't you?"

"I pause a little, but quickly start feeding again as the bird looks at me expectantly. If our little friend lives around the zoo, it's obvious how it could become so tame."

allison "We've always had pets back home, so I grew up around them."

eileen "Your family keeps getting bigger and bigger. Must've been a hard change when you moved out."

play sound "sfx/bird-flap2.ogg"
scene cg act2 zoo nobird with hpunch
"Having apparently had its fill, the bird spreads its wings and flies off at a surprising speed for its weight. I wave as it goes, my hotdog the worse for wear thanks to my picking at the bun."

scene cg act2 zoo smile with midDissolve
allison "Bye bye!"

stop sound fadeout 1.0
eileen "You're a dork."

"I laugh off her jab, before returning to our conversation."

scene bg misc zoo HD:
    xalign 0.48 yalign 0.2
$camera_move(-2500,-250,0,0,0,'dissolve')
show eileen outdoors_fists lookaway neutral at offcenterleft:
    zoom 1.0 yoffset 0
    xpos 0.4
with midDissolve
allison "It was hard when I left, yeah."

allison "I have a new family now, though. You, Caprice, Rose, and everyone else I've met at college."

show eileen outdoors_onhip lookawaynarrow at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "Yeah, a real family..."

"Disappointingly, Eileen looks rather skeptical at the idea. Then again, she doesn't seem to get on that well with anyone besides Wallace and I."

allison "I was always an optimist, I guess."

show eileen outdoors_crossed narrow smile at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "Nothing wrong with that. Maybe some of it'll rub off on me."

show eileen closed frown at offcenterleft:
    xpos 0.4
    stretch
"Eileen picks herself up from the table, giving a big stretch as she does. For a moment we just look at each other, simply appreciative of the fact that we're here, together."

show eileen outdoors_onhip lookaway open at offcenterleft:
    xzoom 1 xpos 0.4
    linear 0.7 xzoom -1 xpos 0.35
eileen "Hey, Allison?"

show eileen outdoors_onhip sadmouth at offcenterleft:
    xzoom -1 xpos 0.35
$ renpy.transition(dissolve, layer='master')
allison "Yeah?"

$ renpy.music.set_volume(0.4, delay=6.0)
$camera_move(-2000,0,300,0,6,'ease')
show eileen normal at centerleft:
    subpixel True
    xzoom -1 xpos 0.35
    ease 6.0 zoom 1.3 yoffset 300 xpos 0.35
with None
show bg misc zoo HD blurred2
$ renpy.transition(verylongDissolve, layer='master')
"As she picks herself up a little off her chair in order to lean across the table, it becomes obvious what she's doing."

scene black with eye_shut
"Relaxed enough to let her get away with a quick peck, I close my eyes and lean forwards a little in anticipation, my heart beating just that little bit faster."

$ renpy.transition(hpunch, layer='master')
"As the feeling of her tongue hits my cheek, my body suddenly freezes up as a shiver runs down my spine."

$ renpy.music.set_volume(1.0, delay=4.0)
scene bg misc zoo HD:
    xalign 0.48 yalign 0.2
$camera_move(-2500,-250,0,0,0,'dissolve')
show eileen outdoors_onhip narrow smile at centerleft:
    zoom 1.0 yoffset 0
    xzoom -1 xpos 0.35
with eye_open
show eileen outdoors_onhip closed neutral at centerleft:
    xzoom -1 xpos 0.35
$ renpy.transition(dissolve, layer='master')
"I hear myself give a weird startled gasp before I reflexively fall back into my chair."

"Eileen looks rather nonplussed as she settles back into her own chair, her eyes studying me as she does."

allison "What was that!?"

show eileen outdoors_crossed open at centerleft
$ renpy.transition(dissolve, layer='master')
eileen "You just had mustard on your cheek."

show eileen narrow smile at centerleft
$ renpy.transition(dissolve, layer='master')
eileen "...And I was maybe bullying you a little."

"I feel my face flower into a wild blush as I grimace at her, partly for her betrayal after my expectation of an affectionate gesture, and partly for startling me so badly."

"I don't know quite how to read Eileen's interested expression, but I don't care to ask as I sulk. I am genuinely a little mad at her, but I don't think it's getting through. I'm still not used to the physical side of all this."

play sound "sfx/chair_scrape_fast.ogg"
show eileen outdoors_onhip normal at centerleft:
    xzoom -1 xpos 0.35
    linear 0.7 xzoom 1 xpos 0.4
"Letting out an amused snort and picking herself up from her seat, Eileen dusts herself off and gets ready to go."

stop ambiance fadeout 4.0
stop music fadeout 4.0
show eileen outdoors_onhip closed at offcenterleft:
    xzoom 1 xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "Come on miss pouty-lips. Let's get moving before the weather goes bad."

scene black with circlewipe
play sound "sfx/door_close3.ogg"
scene bg apteileen livingroom messy
show eileen outdoorsnoscarf_fists normal neutral at offcenterleft:
    xzoom -1 xpos 0.2 alpha 0
    time 1.5
    ease 2.0 xpos 0.45 alpha 1
with circlewipe
$ camera_reset()
play music "music/dozy_comfy.ogg" fadein 1.5
$ renpy.sound.set_volume(1.0, channel='ambiance', delay=4.0)
"As Eileen closes the door to the apartment, I let my coat drop to the floor as I collapse over the back of her couch in exhaustion."

show eileen indoors_fists normal neutral at offcenterleft:
    xzoom -1 xpos 0.45 alpha 1
    nod2
$ renpy.transition(dissolve, layer='master')
"How this girl can keep such a pace up for a whole day is totally beyond me. Even now she doesn't seem too bothered, the only sign she's tired at all being some stretching after she takes off her scarf and coat."

show eileen indoors_fists disbelief open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Haven't collapsed on me, have you?"

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "I'm dead. You can have my stuff."

show eileen indoors_onhip narrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Better check before digging the grave. Remember how they used to do that? Sticking a big pin into a toe to see if they woke up from the pain."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "Look at that, I'm suddenly alive!"

show eileen lookawaynarrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "It's a Christmas miracle."

show eileen closed neutral at offcenterleft:
    xzoom -1 xpos 0.45 alpha 1
    ease 2.0 xpos 1.2 alpha 0
$camera_move(2500,400,750,0,5,'ease')
"As she busies herself behind me, my eye is drawn to her entertainment cabinet that the television's sitting in."

"With curiosity getting the better of me, and perhaps to distract my wandering mind, I walk around the couch and press at the right door to pop it open."

"I'm hardly surprised that the movies inside are all perfectly organized, but the genres she's collected are strange."

show eileen indoors_crossed frown narrow at rightish:
    xpos 0.7 alpha 0
show eileen indoors_crossed narrow angry at rightside as eileen2:
    zoom 0.6 yoffset -310
    xzoom 1 xpos 1.1 alpha 1
    ease 2.0 xpos 0.82
pause 1.0
eileen "You want a coffee or something while you rummage through my stuff?"

allison "I'm not rummaging, I'm just..."

"I try to think of another word to describe what I'm doing, but it doesn't take long to realize Eileen's right. Looking like a kid caught with their hand in the cookie jar as she walks back over, I try to change topics."

allison "Do you really like Westerns or something? They're all either those or documentaries."

show eileen indoors_onhip closed open at rightside as eileen2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
eileen "Sorry to disappoint. I just like Westerns. Can't beat a nice, simple plot with a good guy drifting into a town, getting one over on the bad guy, and walking into the sunset. Nice landscapes, too."

show eileen normal neutral at rightside as eileen2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
allison "Right. That makes sense."

$ renpy.music.set_volume(0.5, delay=5.0)
show eileen disbelief at rightside as eileen2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
$camera_move(2800,600,480,0,5,'ease')
show shadow:
    zoom 2.0 xalign 0.5 alpha 0
    ease 5.0 alpha 0.4
"Something feels off as we stand around in her apartment and chat, but it's hard to put my finger on it. The silences are just a little too long, the chatter nothing more than the smalltalk we've usually never needed."

"Here we are, the evening after a date and filling in time milling about in her quiet apartment. Even the usual background noise of passing cars and busy tenants I hear around my home are nowhere to be heard, just the two of us shuffling about alone."

"The thought of sharing a night with Eileen has passed my mind more than once, even if I've tried to distract myself from it. Is it too early? Would she think I'm weird? I don't even know how you even bring that up."

"Without any real reason to, I idly fiddle with Eileen's movie collection and read off the covers to seem occupied."

stop music fadeout 8.0
show eileen indoors_crossed lookaway open at rightside as eileen2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
$camera_move(3800,0,750,0,4,'ease')
show shadow:
    zoom 2.0 xalign 0.5 alpha 0.4
    ease 3.0 alpha 0
eileen "You know, our date doesn't have to end now."

show eileen neutral at rightside as eileen2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
"As her words trail off, my heart freezes. Her stoic face only makes this worse, my brain freezing between bashfulness and shock at her being so blunt. We've only started dating, but the thought of sleeping together had passed my mind..."

"Left spluttering about, I awkwardly turn away to hide my expression."

allison "Do you... want to watch one of them together?"

show eileen lookawaynarrow at rightside as eileen2:
    xzoom 1 xpos 0.82
    linear 0.7 xzoom -1 xpos 0.785
eileen "Do what you want. I'm going to take a shower."

show eileen closed at rightside as eileen2:
    xzoom -1 xpos 0.785 alpha 1
    ease 2.0 xpos 1.2 alpha 0
pause 1.0
play sound "sfx/door_close2.ogg"
allison "Right. I'll just get a drink."
$camera_move(-600,0,750,0,7,'ease')
pause 2.0

window hide dissolve
$ renpy.music.set_volume(1.0)
play music "music/anxiety_2_m.ogg" fadein 4.0
scene bg apteileen livingroom HD
$camera_move(-8500,-4000,0,0,0,'dissolve')
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.4 ycenter -0.39
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.4 ycenter 0.508
with fadeInOut

letterbox "As she leaves, I wander over to the kitchen and grab a glass, pouring some orange juice for myself to try and refocus. My heart's still racing, the thought of what Eileen suggested still playing on my mind."

letterbox "I wonder if I should really be letting Eileen take care of so much. She doesn't seem to mind at all, but that's not really the problem. Even now she suggested we do what I did want to try, and I couldn't even bring myself to just accept."

letterbox "I want to get closer to her, but it feels like everything's happening at her pace. Then again, Eileen's not the only person in my life I've let dote on me while I go with the flow of others..."

scene black with dissolve
$ camera_reset()
play sound "sfx/door_open2.ogg"
scene bg apteileen livingroom messy with smoothDissolve
window show dissolve

"The door from the bathroom opens as I set down the now empty glass, but the words are stolen from my mouth as I walk over to talk with her."

stop music fadeout 5.0
show eileen naked_towel normal sadmouth at center:
    xpos 0.5 alpha 0
show eileen naked_towel normal sadmouth at center as eileen2:
    xpos 0.8 alpha 0
    ease 1.8 xpos 0.52 alpha 1
pause 1.0
eileen "Allison."

stop sound fadeout 1.0
play ambiance "sfx/ambiance/heartbeat_light.ogg" fadein 2.0
with vpunch
allison "Ah- Were you getting clothes? Um, sorry-"

$camera_move(-500,0,300,0,6,'ease')
show eileen naked_towel narrow at center as eileen2:
    subpixel True
    zoom 1.0 xpos 0.52 alpha 1
    ease 6.0 zoom 1.2 yoffset 200 xpos 0.5
with None
show bg apteileen livingroom messy blurred2
$ renpy.transition(verylongDissolve, layer='master')

"My face burns hot as I stammer out the words, but she only steps closer."

"She takes my hands to stop me from moving away, holding them softly. Her face is so, so close to mine. I can feel her breathing."

"Her eyes look into mine, questioning. Suddenly the thought of even a kiss makes my head light."

scene black with eye_shut
"All I can do is nod a tiny nod, which is enough for her to close the distance, kissing me more deeply than she ever has before. My heart races as her tongue touches mine, teasing it just a little before pulling back."

scene bg apteileen livingroom messy
$camera_move(-500,0,300,0,0,'dissolve')
show bg apteileen livingroom messy blurred2 as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0.9
show eileen naked_towel lookaway sadmouth at center:
    zoom 1.2 yoffset 200
    xpos 0.52
with eye_open
"I can hardly breathe by the time we separate, left clutching my chest and taking a deep breath to try and regain myself."

show eileen naked_towel lookawaynarrow at center:
    zoom 1.2 yoffset 200
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "It looked like you didn't get it, so I decided to be more blunt."

return

label scene_2S8_b_clean_en:
    # zip
    scene black with longDissolve
    return

label scene_2S8_b_en:

stop ambiance fadeout 8.0
play music "music/romance_2_m.ogg" fadein 8.0
allison "'Blunt' is one word for it..."

"What is it with me and suddenly being surrounded by such headstrong people? I should be thankful, given how I had no idea what to do."

play sound "sfx/rustle-clothes.ogg"
show eileen naked_fists lookawaynarrow sadmouth blush at center:
    zoom 1.2 yoffset 200
    xpos 0.52
    nod2
$ renpy.transition(dissolve, layer='master')
"She lets her towel fall to the floor. Only my clothes separate us, now. While she's seen my body before, the atmosphere couldn't be more different. All I can do is gulp at the sight before me."

show eileen naked_onhip narrow angry blush at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "Is this clear?"

stop sound fadeout 1.0
show eileen sad angry blush at center:
    xpos 0.52
$ renpy.transition(smoothDissolve, layer='master')
"She looks at me expectantly, her face flushed and breathing just a little uneven. Eileen's breasts, her thighs, everything about her... I'm caught between my reflex not to stare, and letting my lust taking over."

show eileen sad open blush at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "At least look, if you don't want to go further. This is something I can give only you."

scene black with midDissolve
scene bg apteileen livingroom messy blurred2:
    zoom 1.05 xalign 0.5 yalign 0.5
$camera_move(-2200,1200,480,0,0,'dissolve')
show eileen naked_fists frowning sadmouth blush at offcenterleft:
    zoom 1.15 yoffset 120
    xzoom 1 xpos 0.4
with midDissolve
$camera_move(-2200,-850,480,0,10,'ease')
"Made a little more confident by her words, I bring my fingertips to her collar, my heart racing. If I had any doubts about whether I truly leaned this way, they've been erased completely as I stare at her body's curves."

"My fingers slowly drag downward to the center of her chest, taking in the feeling of her soft skin as she moves with every breath. She's beautiful. I can't think of anything else."

allison "I don't..."

play sound "sfx/rustle-clothes.ogg"
scene black with midDissolve
allison "I don't... want to go."

scene cg act2 finger start
$camera_move(-2000,-1650,850,-5,0,'dissolve')
with midDissolve
stop sound fadeout 1.0
"As Eileen backs onto the soft bed, neatly set as always, I climb on after her. The quiet here is a stark contrast to my apartment, leaving the two of us to the total silence of her bedroom."

$camera_move(-1500,250,600,0,8,'ease')
"I'm so busy staring at Eileen's beautiful body that I almost forget my own embarrassment at being naked. It's a strange feeling to be resting my own skin against her own soft body, but her warmth feels so nice."

"I pass my hand over her stomach, but find myself hesitating as Eileen looks to me."

eileen "Allison?"

allison "I don't... I don't know what to do."

eileen "It's not like I really do, either."

$camera_move(-50,450,200,0,10,'ease')
"Of course, if this is the first time for both of us, that makes sense. Her slight embarrassment over the fact helps make me relax a bit."

"Never having had the chance to see or feel a woman's body like this, my hand begins to explore her. Her soft, warm skin under my hand makes my heart race, Eileen's muscles occasionally tensing out of reflex. This such an odd situation, for both of us."

"My hand passes lower and lower, her breath hitching as the tips of my fingers brush against the bushy hair between her legs. Heart racing and eyes carefully watching her face to gauge her reaction, my fingers slip down."

show cg act2 finger mid with smoothDissolve
"I briefly halt as her whole body tenses, face looking pained. Her sharp breaths settle down quickly, much to my relief; the sensation must've just startled her."

"This is a lot harder to do with another person than myself, especially from this angle. Thankfully just moving my fingers around, their tips becoming just a little moistened, seems to be exciting her. Eventually Eileen's legs begin to move, thighs tensing then loosening."

"Eileen runs her hand up and down my side, enjoying the sensation of my own body. From so close, I can see her chest moving as she breathes, the details of her skin, lines of her collarbone... all of her body in every detail."

"A moan escapes her lips, long and deep. It's strange how happy it makes me feel, seeing Eileen so wrapped in the joy I'm giving her."

scene cg act2 finger end 
$camera_move(-2800,2250,980,0,0,'dissolve')
with midDissolve
"Sounds I've never imagined her making begin to flow, Eileen's hands searching around gripping me and the sheets, her thighs beginning to quiver."

scene black with dissolve
scene cg act2 finger mid
$camera_move(-50,-450,200,0,0,'dissolve')
with midDissolve
show cg act2 finger end as cg2:
    alpha 0
    ease 0.8 alpha 1
$camera_move(-50,450,200,0,0.8,'ease')
"Having been lulled into the rhythm of things, I'm taken off guard when Eileen's pleasure finally overwhelms her. Her body tenses as her loud moan is cut off, hands clutching at the sheets and toes digging at the bed as she savors the feeling flowing throughout her."

$ renpy.music.set_volume(0.7, delay=8.0)
$camera_move(-2500,-1800,850,0,8,'ease')
"And then... it's over. Her body goes limp, legs falling flat and mouth gaping for air. She looks dreamy as she lazily looks up into my eyes, a hand reaching over to stroke my cheek."

eileen "Allison..."

"All I can do is give a shy smile as we look at each other. As we do, she seems to recover herself a little as the glow slowly wears off. Her exhausted smile is all I needed to see."

scene black with midDissolve
"I pick myself off of her to let Eileen clean herself up. I don't quite know where I should look as Eileen sits up and tries to collect herself, left sheepish about being naked with her now that I have less to distract me."

scene cg act2 cunnilingus start
$camera_move(3900,850,900,0,0,'dissolve')
with midDissolve
$ renpy.music.set_volume(1.0, delay=8.0)
$camera_move(100,850,700,0,8,'ease')
"Rather than cleaning herself though, the bedraggled Eileen rolls over onto my side of the bed. I slide back a little reflexively out of surprise, the girl lowering herself down between my legs."

allison "What are you doing!?"

eileen "I want to do this for you as well."

allison "But..."

eileen "If you don't want me to, I won't."

"That puts me in a rather awkward place..."

show cg act2 cunnilingus mid with midDissolve
"Still a bit unsure of myself, I stay silent as she lowers her head. Her breath against my crotch makes me shiver, and as she plants a kiss between my legs, I can't help but let out a satisfied sigh."

allison "Eileen..."

"Eileen seems satisfied I'm enjoying it as she begins to lap away, my eyes slowly closing as I try to let myself be swept away by the feeling."

"Whimpers fill the night air. It feels weird to make all these noises without thinking about it, but I don't care enough to try and stifle them. It feels so much better than doing it myself, her tongue moving this way and that."

"I can't get her out of my mind as pleasure starts to overwhelm me, everything starting to tense more and more. and then..."

scene black with dissolve
scene cg act2 cunnilingus mid
$camera_move(200,450,400,0,0,'dissolve')
with midDissolve
show cg act2 cunnilingus end as cg2:
    alpha 0
    ease 0.8 alpha 1
$camera_move(200,950,400,0,0.8,'ease')
"My entire body is completely overcome. Everything drops away in an instant, my mind blanked of everything but bliss. I can't say or do anything, I just want this to last longer and longer..."

"Soon, all too soon, it ends. With a long, drawn-out sigh, the last gasp of my excitement is released into the silent apartment."

stop music fadeout 8.0
scene cg act2 cunnilingus end
scene cg act2 cunnilingus start
$camera_move(-3900,-850,900,2,0,'dissolve')
with midDissolve
"All I can do is wearily look down at Eileen, her face with those emerald eyes silently staring up at mine."

return


label scene_2S8_c_en:

stop ambiance fadeout 4.0
scene black with midDissolve
$ camera_reset()
"With our excitement over, the two of us had a shower to clean up before settling in for the night."

play music "music/touching.ogg" fadein 8.0
scene cg act2 pillowtalk eyesclosed
$camera_move(200,950,450,0,0,'dissolve')
with longDissolve
$camera_move(200,-250,450,0,8,'ease')
"Enveloped in a soft, loving warmth as Eileen cuddles me, I almost want to nod off already as she gently strokes the back of my head."

"Given how cold she can be towards others, it's a real surprise she's so physically intimate. I have to admit that I like this side of Eileen, snuggling into her body as I think so."

allison "I love you, Eileen."

eileen "I know."

show cg act2 pillowtalk eileenclosed with dissolve
allison "That's not what you're supposed to say."

show cg act2 pillowtalk talk with dissolve
eileen "Alright, alright. I love you, too."

allison "Even a few weeks ago, I never imagined I'd be sleeping with someone..."

show cg act2 pillowtalk eileenclosed with midDissolve
eileen "We won't see each other for a while, so we have to make the most of our time before holidays."

$camera_move(-200,1550,900,-2,8,'ease')
"Oh yeah, I'd forgotten about that in all the excitement."

"It'll be nice to see everyone again, but there's a pang of disappointment that I can't be with Eileen more."

allison "You'll be going to stay with your family, right?"

eileen "Yeah. Colorado's not bad, so at least it'll be a nice change of scenery. It'll be nice to see my sister again, too."

show cg act2 pillowtalk allisonclosed with midDissolve
"As Eileen thinks about her faraway family, I'm reminded of my own. I've been excited to go back home for the holidays for weeks now, but with her gone..."

eileen "You okay?"

allison "I'll be fine. I just wish I could go with you."

eileen "Sorry?"

"As a plan forms in my head, I try to summon the same strong will she and Caprice have."

show cg act2 pillowtalk eileenclosed with vpunch
allison "I'd like to be with you over the break. Could I come?"

scene cg act2 pillowtalk talk
$camera_move(200,-1550,900,5,0,'dissolve')
with midDissolve
"Eileen looks unsure of what to say. I wonder if she's trying to decipher if I'm making a serious suggestion or not. Even I don't know."

eileen "And you talk about me going fast. Didn't you want to see your own family really badly?"

$camera_move(200,-250,450,0,7,'ease')
allison "I do, but they won't be back home right away. I'll go back before Christmas! I just..."

allison "I don't want to be alone until then."

"She looks taken aback. I suddenly find I'm actually arguing for this, instead of merely voicing a whim."

eileen "I'm not really sure about this..."

eileen "You've never been outside the city, let alone the state. Then there's the fact you'll be in a house full of strangers."

allison "I coped with moving into Rose's apartment, and I'll be with you! After how much you've helped me until now, I'm sure I'll be fine."

$camera_move(0,0,0,0,6,'ease')
"She tries to stare me down, but I've managed to find an internal willpower in some corner of myself I didn't know existed."

show cg act2 pillowtalk eileenclosed with midDissolve
"Eventually, thankfully, Eileen lets out a long, tired breath."

eileen "Fine. You win, you can come."

show cg act2 pillowtalk eyesclosed with dissolve
allison "Thank you!"

show cg act2 pillowtalk allisonclosed with dissolve
eileen "Just don't try to 'fix' things, okay?"

stop music fadeout 4.0
$ _dismiss_pause = False
"As I snuggle into her warmth with a grin of victory, Eileen silently smiles as she pats my head once more."

window hide dissolve
scene black with longDissolve
return
