label scene_1S1_en:
######################
# Act 1, Scene 1

window hide
play ambiance "sfx/ambiance/winter.ogg" fadein 2.0
scene cg title
show snow light
with longDissolve
window show dissolve
$ _dismiss_pause = True
"The first snow of the year should be a comforting sight, yet this carries a different feeling when so far from home."

scene cg act1 balcony morning
$camera_move(-3800,2000,880,0,0,'dissolve')
show snow light
with menuFade
pause 0.5
$camera_move(400,-400,600,0,7,'ease')
"Winter has always been my favorite time of the year, but the joy of warm fires and upcoming holidays is missing. There's only a month left to go until the season begins in earnest, but I can't feel any of the usual excitement."

"The coming winter will be the first I've spent away from my family, after all. It's just me now, standing alone on a concrete balcony and looking out onto a gray sky."

stop music fadeout 4.0
$ renpy.transition(vpunch, layer='master')
$camera_move(0,0,0,0,4,'ease')
rose "Hey, Allison! Aren't classes soon!?"

"A woman's barking from down below breaks me out of my thoughts. Her familiar figure clad in leather stares up, snow heaped on the rusted shovel in her hands."

window hide dissolve
scene black with dissolve
stop ambiance fadeout 1.5
scene bg aptallison livingroom with dissolve
window show dissolve

"Looks like the heating's died again, the inside of the apartment no warmer than out there. This new home might be a little shabby, but at least it's ours."

"A quick glance at my phone as I walk to get my coat and bag confirms her to be right, the morning's message from a friend still showing on the screen."

$ phone.message('caprice', '8:17 AM', "BIG NEWS allie!!! :):):)\o/\o/\o/")
$ phone.message('caprice', '8:17 AM', "tell you later in bio!!!!!! ;)\o/\o/<3<3")
$ phone.show('messages', who='caprice')
show bg aptallison livingroom blurred2:
    xalign 0.5 yalign 0.5
$ renpy.transition(dissolve, layer='master')
"The idea of big news at this of all times fills me with worry; I'm already too busy just trying to keep up with my new life."

$ phone.hide()
show bg aptallison livingroom
$ renpy.transition(dissolve, layer='master')
"With time marching on, I quickly slip the phone back into my coat and set off for the stairs. I shouldn't have a problem making it to class if I keep a good pace."

window hide dissolve
scene black with dissolve
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
play loopsfx "sfx/snow-removing.ogg" fadein 0.5
scene bg aptallison outside
show snow light
show rose outdoors_handonhip neutral normal at right2:
    xzoom -1 xpos 0.79
    nod2_repeat
with dissolve
window show dissolve
"The busily shoveling woman is still working away, her efforts obvious to see. The snowfall's been impressive for a single night, but a good amount's already been cleared, her heavy breathing easily visible in the cold air."

stop loopsfx fadeout 5.0
show rose outdoors_handonhip neutral normal at right2:
    xzoom -1 xpos 0.79
    time 3
    bounce
"Keeping a brisk pace, as much to get to my classes on time as it is to try and warm myself up, I try to wave a quick goodbye. It's obvious she won't let me go without giving her two cents, though, as she puts her shovel against the wall and takes a good stretch."

stop loopsfx fadeout 1.0
allison "'Morning, Rose. Working hard already?"

show rose concerned at right2:
    xzoom -1 xpos 0.79
    linear 0.7 xzoom 1 xpos 0.775
rose "Someone's gotta do it; not like those useless lumps will."

"Rose jerks her head towards the apartments. She's not really wrong, but her usual tactlessness is on full display."

show rose concerned at right2:
    xzoom 1 xpos 0.775
rose "You all bundled up? Looks like winter's coming early goin' by the paper."

allison "I'll be fine, don't worry."

rose "Just take it easy on the way there, alright?"

allison "I will!"

show rose weaksmile at right2
$ renpy.transition(dissolve, layer='master')
"A weak smile is her response as I start off down the road; she knows that I'm right."

play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 0.5
scene bg aptallison outside:
    xalign 0.5 yalign 0.5
    subpixel True
    parallel:
        ease 30 zoom 2.0 xalign 1.0 yalign 0.3
    parallel:
        ease 1 yoffset 1
        ease 1 yoffset -1
        repeat 20
show snow light
with midDissolve
"This is hardly the first exchange we've had like this. Every other morning Rose comes up with something or another to definitely not be concerned about. I don't mind, though; that kindness is one of her better traits."

"The weather's been getting steadily colder for a while now. The few workers braving the morning chill are slowly making their way down to the bus station for work, those staying behind grumbling as they shovel snow from the roofs of their cars and their driveways."

"There aren't many students down this way as I walk, however. Student accommodation filled up fast, and the nearby apartments were all rented out soon after that. Thank goodness for a family friend offering to let me live with them."

"Helpful as Rose may be, there's still some sense of being a foreigner. It's only been two months since I moved in and started classes at college, my circle of high school friends and boisterous family home turning overnight to a cramped apartment shared between Rose and I."

window hide dissolve
scene bg campus outskirts snow
show snow light
with midDissolve
window show dissolve

"As the school buildings come into view, I join the tired masses staggering through the gates and towards their classes. Much as I might worry, I know I'm not alone; I'm sure many of the students around me right now are going through exactly the same thing."

"It's only now that I realize I haven't had my usual morning coffee back at the apartment to wake myself up. With little time before biology class starts, I'll have to content myself with a quick can of soda from the vending machine."

stop loopsfx fadeout 1.0
scene bg buildingunion outside snow
with midDissolve
"Heading over to the union building on the way to class, the morning chill's driven away the usual gaggle of those sitting on the stairs and blocking the entrance."

play sound "sfx/door_open.ogg"
"Rubbing my hands together to summon some warmth, I head on in."

stop ambiance fadeout 2.0
play sound "sfx/door_close2.ogg"
scene bg buildingunion foyer
with midDissolve
"With the heating being cranked right up, you could almost forget it's winter outside. My relief doesn't last long, however."

play sound "sfx/vending_hit.ogg"
$ renpy.transition(hpunch, layer='master')
$camera_move(-3250,0,800,0,3,'ease')
"My heart nearly stops as a deafening clatter comes from ahead."

play sound "sfx/vending_hit.ogg"
play music "music/questioning.ogg" fadein 2.0
$camera_move(-3250,0,800,0,0,'dissolve')
show eileen indoors_crossed lookawayangry angry at left2:
    zoom 0.42 yoffset -470
    xpos 0.27
    nod2
with dissolve
"A couple walking arm-in-arm skirt around the edge of the room, doing their best to not draw the attention of a blonde woman nearby. She grumbles loudly before delivering another kick to the poor, abused vending machine in front of her."

"I hate situations like these. Either I do nothing and feel bad for not helping, or step in and deal with the stress that comes with confronting someone involved."

$camera_move(-800,0,800,0,4,'ease')
show eileen indoors_crossed angry annoyed at left2:
    zoom 0.42 yoffset -470
    xpos 0.27
    time 2
    linear 0.7 xzoom -1 xpos 0.24
stop sound fadeout 1.0
"As I try to work my way out of this, my heart freezes as the woman locks eyes with me. I must make for a pitiable sight with my hands raised defensively in front of me, her rage calming as she settles for staring daggers at the machine."

play ambiance "sfx/ambiance/heartbeat_light.ogg" fadein 0.1
$camera_move(-2800,0,800,0,3,'ease')
show eileen indoors_crossed angry annoyed at left2:
    zoom 0.42 yoffset -470
    xzoom -1 xpos 0.24
"Resigned to my fate, I reluctantly shuffle towards her as my heart beats wildly. As I do, her dour look is only made all the more intimidating from the bags under her eyes."

scene bg buildingunion foyer
show eileen indoors_crossed angry annoyed at center:
    xzoom -1 xpos 0.45
with midDissolve
$ camera_reset()
allison "Is... something wrong?"

show eileen indoors_onhip closed open at center:
    xzoom -1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
eileenu "Stupid thing ate my money; no can or change at all. Threw five bucks in there, too."

show eileen indoors_onhip frown at center:
    xzoom -1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
allison "Ah, the vending machine here messes up sometimes. It's usually better to go through to the cafeteria for drinks."

show eileen indoors_onhip narrow frown at center:
    xzoom -1 xpos 0.45
    linear 0.7 xzoom 1 xpos 0.52
eileenu "They should fix it, then."

play sound "sfx/vending_hit.ogg"
scene bg buildingunion foyer
$camera_move(-3250,0,800,0,0,'dissolve')
show eileen indoors_crossed angry lookawayangry at left2:
    zoom 0.42 yoffset -470
    xpos 0.27
    nod2
    repeat 2
with hpunch
"Recounting the event only serves to stir up her annoyance, another foot being jammed into the accused."
"The horrible noise makes me cringe again, and I'm starting to worry she'll hurt herself as much as the machine itself."

allison "Don't kick it again!"

stop music fadeout 10.0
stop sound fadeout 1.0
show eileen annoyed at left2:
    xzoom 1 xpos 0.27
    linear 0.7 xzoom -1 xpos 0.24
eileenu "Why not? Thing's already broken isn't it?"

show eileen annoyed at left2:
    xzoom -1 xpos 0.24
"I want to say that I'd rather not get in trouble with the staff, but I get the feeling that wouldn't faze her."

"Reviewing my options as quickly as I can, there's only one solution I can think of that might settle her down. I probably shouldn't, but if nobody's paying much attention..."

allison "Which drink did you want?"

play music "music/conflict.ogg" fadein 2.0
show eileen indoors_onhip disbelief frown at left2:
    xzoom -1 xpos 0.24
$ renpy.transition(dissolve, layer='master')
"She gives me a curious look after I manage to squeak the words out, but eventually points."

show eileen indoors_onhip open at left2:
    xpos 0.24
$ renpy.transition(dissolve, layer='master')
eileenu "Was just grabbing a lemonade on the way out."

show eileen indoors_onhip disbelief neutral at left2:
    xpos 0.24
$ renpy.transition(dissolve, layer='master')
allison "Could you turn around for a moment?"

$camera_move(-4800,0,1000,-1,4,'ease')
show eileen indoors_onhip disbelief neutral at left2:
    xpos 0.24
    ease 2.5 xpos 0.48
"With great reluctance, she turns away as I ask. I doubt she could work out what I'm doing by looking, but it's better to be safe than sorry."

"Closing my eyes and silently mouthing the right sequence to make sure I don't mess it up, I go about my business. With any luck, the software inside hasn't been updated since I last tested this."

play sound "sfx/vending_drop.ogg"
$ renpy.transition(hpunch, layer='master')
"A long sigh of relief passes my lips as the vending machine rattles away, loudly dumping a can into the small opening."

$camera_move(-3250,0,800,0,4,'ease')
pause 4.0
show eileen indoors_onhip normal open at offcenterleft:
    xzoom -1 xpos 0.48
    linear 0.7 xzoom 1 xpos 0.51
"Holding the can before the blonde woman's face as she turns back around, my reward is a somewhat impressed expression as she takes the item."

show eileen indoors_onhip normal neutral at center:
    xpos 0.51 xzoom 1
    ease 1.5 xpos 0.35
"Now that she has her drink - and had a chance to get her frustration out of her system - she seems to be calming a little. Her height doesn't help her look any less intimidating, though."

scene black
$ camera_reset()
scene bg buildingunion foyer
show eileen indoors_crossed normal neutral at left2:
    xzoom 1 xpos 0.25
$ renpy.transition(dissolve, layer='master')
$camera_move(0,0,300,0,5,'ease')
"With that, I consider the matter settled as I nod and begin to walk away. Only as I leave, do I realise my heart's racing after having to deal with her."

$camera_move(500,0,300,0,3,'ease')
play sound "sfx/door_open.ogg"
show eileen normal open at left2:
    xzoom 1 xpos 0.25
    linear 0.7 xzoom -1 xpos 0.25
eileenu "Hey, wait up-"

stop music fadeout 5.0
stop ambiance fadeout 2.0
show eileen normal open at left2:
    xzoom -1 xpos 0.25
"Reaching for my instinctual response, I pretend not to hear her as I skitter away and disappear back through the entrance."
$camera_move(2500,0,300,0,3,'ease')
pause 1.5

play sound "sfx/door_close2.ogg"
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
scene black with dissolve
$ camera_reset()
scene bg buildingunion outside snow
$ renpy.transition(hpunch, layer='master')
"The cold hits me like a wall as I leave through the door. I hardly mind, heaving a sigh to steady myself as I head towards classes. I only remember now that I'd intended to grab a drink myself, but fiddling with the machine's probably made me too late."

"The empty campus grounds make me nervous, making me take my phone in hand to check the time. A quick glance is all that's needed to send me dashing toward the sciences building."

window hide dissolve
stop ambiance fadeout 5.0
stop sound fadeout 1.0
scene black with longDissolve
window show dissolve
"It's going to be one of those days..."
window hide dissolve

play sound "sfx/door_close.ogg"
scene bg buildingmisc generichall
show caprice indoors_chintap normal even neutral at right2:
    zoom 0.55 yoffset -280
    xzoom -1 xpos 0.085
show bg buildingmisc lecture table as lecture_table:
    xalign 0.5 yalign 0.5
with midDissolve
window show dissolve
"Panting from the run, I stagger into biology class with as much composure as I can muster. The sight seems to make a pitiable impression on the professor, who merely nods for me to take a seat."

$ renpy.sound.set_volume(0.8, channel='ambiance')
play ambiance "sfx/ambiance/class_chatter.ogg" fadein 1.0
$camera_move(-3400,1500,800,0,4,'ease')
"Setting my bag next to me, I quickly take the seat next to a now-familiar figure."
play sound "sfx/chair_scrape_fast.ogg"
show caprice indoors_wave grin at right2:
    zoom 0.55 yoffset -280
    xzoom -1 xpos 0.085
    easein .15 yoffset -298
    easeout .175 yoffset -280
    easein .15 yoffset -288
    easeout .175 yoffset -280
"The diminutive Caprice shoots a grin and a wave as I sit, earning a smile in return."

show caprice indoors_wave neutral at right2:
    zoom 0.55 yoffset -280
    xzoom -1 xpos 0.085
$ renpy.transition(dissolve, layer='master')
"It's nice to see a friendly face."

scene black
play music "music/relaxing.ogg" fadein 5.0
$ renpy.music.set_volume(0.1, delay=0)
scene bg buildingmisc generichall
$ camera_reset()
with midDissolve
play sound "sfx/paper_shuffling.mp3"
"As the professor gets back to lecturing, I grab my still-pristine textbook from my bag, flicking through to the bookmark I'd added for where we currently are."
"Movement from the corner of my eye takes my attention, a ripped piece of sketchpad sliding before me."
stop sound fadeout 1.0

show bg buildingmisc generichall blurred2:
    xalign 0.5 yalign 0.5
$ renpy.transition(dissolve, layer='master')
show note late1:
    xalign 0.5 yoffset -650
    ease 1.5 yoffset 120
pause 1.5
"Her writing is surrounded by various doodles and scribbles already on the page. I should pay attention to the class, but it isn't that easy to wave Caprice off."

"Then again, this is largely reviewing what we covered in high school right now. It probably wouldn't hurt to chat with her a bit."

show note late2:
    xalign 0.5 yoffset 120
with inkfade2
pause 2.0
show note:
    xalign 0.5 yoffset 120
    ease 1.5 yoffset -650
pause 2.5
"I write a brief reply and a little accompanying drawing before sliding it back over, a quick look to the professor making sure the coast is clear as he drones on."

show note late3:
    xalign 0.5 yoffset -650
    ease 1.5 yoffset 120
pause 1.5
"Caprice's reply as the page is passed back makes me grimace. I should have expected that."

"I almost reply before noticing the professor casting a knowing glance my way as he continues with his teaching. He knew what we were doing, didn't he?"

show bg buildingmisc generichall
hide note
$ renpy.transition(dissolve, layer='master')
"Thinking better of it, I tuck the page beneath my textbook and start listening properly. I don't need to look at Caprice to know her reaction."

"I hardly think worse of her for it, though; swapping doodles during these classes was how she broke the ice with me when I was just another lonely freshman student. A shy one, at that. Given we're still friends, I suppose it worked."

show bg buildingmisc generichall blurred2:
    xalign 0.5 yalign 0.5
show note late3:
    xalign 0.5 yoffset 120
$ renpy.transition(dissolve, layer='master')
stop music fadeout 3.0
stop ambiance fadeout 3.0
"Sneaking a glance back at the page beneath my book reminds me how well the mercurial girl can draw, at least compared to me. She mentioned one time that she's also taking art classes, which must be paying off."

hide note
show bg buildingmisc generichall
$ renpy.transition(dissolve, layer='master')
"Before I know it, the class starts winding up. The other students begin to get distracted as time goes on, the professor soon starting to wrap things up in response."

$ renpy.sound.set_volume(1.0, channel='ambiance')
play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.0
"No sooner do the words come from his mouth that the class is over, does the loud clatter of people packing books and pens into their bags and backpacks begin."

play music "music/caprice_default_m.ogg" fadein 2.0
$ renpy.music.set_volume(1.0, delay=0)
show caprice indoors_chintap normal even puffed at center with dissolve
"Caprice wastes no time in talking as the two of us do the same."

show caprice indoors_chintap even normal puffed at center:
    nod2
caprice "I was worried you were sick today, Allie!"

allison "It was only a couple of minutes..."

show caprice indoors_behindback raised open at center:
    bounce
caprice "For you, that's a lot!"

"She has a point. It's likely I was more concerned about this than the teacher. After near-perfect attendance through high school though, the last thing I want is to set a bad expectation from the staff here."

show caprice even neutral at center
allison "Setting that aside, I'm not sure the professor really likes us passing notes to each other in class."

show caprice wink grin at center:
    subpixel True
    xpos 0.5 yoffset 55
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "Oh, don't worry about him! He's cool. We've talked."

allison "Well, if you're sure. I do like seeing your drawings."

show caprice indoors_handonhip normal grin at center:
    xpos 0.5 yoffset 55 rotate 0
$ renpy.transition(dissolve, layer='master')
caprice "Aw, and I like seeing yours! I'm glad you're here today, actually. I've been thinking, and I need your help with something."

show bg buildingmisc generichall blurred2 behind caprice:
    xalign 0.5 yalign 0.5
show caprice closedhappy at center:
    zoom 1.5 yoffset 500
    xpos 0.48
    easein .15 yoffset 482
    easeout .175 yoffset 500
    easein .15 yoffset 492
    easeout .175 yoffset 500
with hpunch
caprice "We're making an art club!"

allison "But there's already an art-"

allison "Wait, why is there a 'we' there? How am I part of this?"

show caprice wink at center:
    subpixel True
    zoom 1.5 yoffset 500
    xpos 0.48
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "You're a founding member, of course!"

$ achievement.grant('story_artclub')

show shadow:
    alpha 0.0
    ease 1.0 alpha 0.35
show caprice closedhappy at center:
    zoom 1.5 yoffset 500
    xpos 0.48 rotate 0
"Why do I get the feeling Caprice has been mulling this over in her head for ages? Plans seem to already be in motion for her, and I'm not sure what choice I have left in this."

show caprice outdoors_handonhip closedhappy at center:
    zoom 1.5 yoffset 500
    xpos 0.48
    time 0.2
    nod2
with dissolve
"I'm left to mull things over as I take my coat from the back of my seat and slip it on, the two of us taking our bags and joining the others in heading out into the hallway."

"I hadn't even considered joining a club, let alone starting one up with all the work that'd entail."

scene black with dissolve
scene bg buildingbusiness hallway1f
show caprice outdoors_handonhip even normal grin at center
with dissolve
allison "I can help, but... I have my schoolwork to concentrate on, you know. Getting a scholarship wasn't easy, and I'd rather not waste it."

show caprice outdoors_behindback raised normal open
$ renpy.transition(dissolve, layer='master')
caprice "Ahh, right. You were majoring in chemistry, weren't you?"

"I give a nod, albeit a slightly guilty one. Not that I'd dare have told my family, but I only picked chemistry because I happened to be good at it. Like most things in life, I just went with the default option before me."

show caprice even neutral
$ renpy.transition(dissolve, layer='master')
"At least Caprice seems to have moved on from me being a part of this. I have enough going on in my life between moving to a new home and studying for college. To think about spending time in clubs and things..."

allison "I'm surprised you're taking biology classes, to be honest. Aren't you more into art?"

show caprice outdoors_chintap raised normal open
$ renpy.transition(dissolve, layer='master')
caprice "Umm... it's hard to pick a favorite. But right now, bio is just the entry level stuff... It's so boring, right?"

show caprice even closedhappy grin at center:
    bounce
caprice "I talked to the professor, though, and we're getting into some marine life chapters soon!"

allison "That seems very specific."

show caprice outdoors_pumped at center:
    subpixel True
    xpos 0.5 yoffset 55
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "It's the most interesting part! I gotta focus hard when we get there. I plan on making it my major."

stop music fadeout 2.0
stop ambiance fadeout 2.0
"So even a free spirit like Caprice has something she's working towards. It seems I can't get away from how much of a mess my life is, with no idea what I want to do for a career."

play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
play music "music/energetic.ogg" fadein 2.0
scene bg campus reverse snow
with fadeInOut
"The two of us head outside, with our next classes in other buildings. As we do, I look about warily as students from other classes pass by. I'd rather not bump into that angry woman again."

show caprice outdoors_behindback even wink neutral at center
$ renpy.transition(dissolve, layer='master')
caprice "Who were you held up with, anyway? Bump into a friend?"

show caprice normal at center
$ renpy.transition(dissolve, layer='master')
"That would require there to be another beyond her in the first place."

show caprice raised at center
$ renpy.transition(dissolve, layer='master')
allison "She's about the last person I'd call a friend. Kind of scary, actually."

"She might've been asking out of smalltalk before, but now I have her full interest. With reluctance, I think back to the event."

allison "Not sure if you'd know her. Tall, blonde, green eyes. Very sharp look, with high boots. Kinda pretty?"

show caprice closedhappy at center
$ renpy.transition(dissolve, layer='master')
"Now that I have time to think it through, she was quite beautiful. In more than her body, too; I liked her sense of fashion."

show caprice outdoors_chintap normal grin at center:
    bounce
caprice "Hmm. I think I know who you're talking about, actually."

allison "You do?"

show caprice wink at center
$ renpy.transition(dissolve, layer='master')
caprice "Yep. Our other founding member."

"She hasn't dropped the idea of me joining at all, and now wants her of all people to be part of this. My reaction to the news apparently shows on my face."

caprice "If we're thinking of the same person... I've seen her around, and I've heard some things. She floats around the art department a lot, so the other art club tried to grab her. She didn't even pretend to consider it, just told them to get lost."

show caprice closedhappy at center
$ renpy.transition(dissolve, layer='master')
caprice "Which means she's still free."

allison "If she already rejected one club, why would she join another?"

show caprice outdoors_pumped normal at center:
    bounce
caprice "Because it's led by me, of course!"

"I just sigh."

allison "I need to get to my next class. Being late for one today is already too much."

"Resigned to my fate, I wave goodbye and start to head off. Not more than a couple of seconds later, I hear her calling out behind me."

show caprice outdoors_handonhip normal open at center:
    bounce
caprice "Ah, before you go!"

caprice "Meet me on the second floor of the arts building after classes, okay? We need to get started on finding a club room and stuff!"

stop music fadeout 3.0
stop ambiance fadeout 2.0
show caprice neutral at center
$ renpy.transition(dissolve, layer='master')
"Looks like I'm going to be a part of this scheme whether I like it or not. Dealing with that woman again makes me shudder, but she'll surely just reject Caprice and that'll be that."

scene black with fadeInOut
play music "music/dozy_comfy.ogg" fadein 2.0
scene bg buildingart hallway1f
with longDissolve
"Walking through the halls at these hours is a wholly different experience to the normal hustle and bustle."

"Where students gossiped in the hallways, organized dates, and hurried between classes with arms full of overpriced textbooks, there's now a sweet silence. All to be seen at this hour is the odd straggler thinking more about dinner than schoolwork."

"Well, them and the Christmas decorations. I get the feeling that the arts and humanities staff take some enjoyment out of getting ready for the occasion. Much like the school itself, the decorations look a bit ragged, probably hauled out every year for decades."

"With little to do until Caprice shows up, exploring the arts building and peering into this classroom or that winds up passing the time."

scene bg buildingart hallway2f dusk with dissolve
"Heading up the stairs, I take my time strolling through the hallways. Everything is bathed in the orange of the sunset, the quiet of the halls giving the building a serene atmosphere. It's calming after the day's events."

$camera_move(2500,-950,800,0,4,'ease')
"It isn't until a good few minutes pass that I find the first thing of much interest; a single room with the door left open."

"With curiosity getting the better of me, I stroll up the hallway and gingerly step inside. At least I can close the door for them."

scene bg buildingart art dusk siren
$camera_move(3800,0,800,0,0,'dissolve')
with midDissolve
$camera_move(-3200,0,800,0,20,'ease')
"With only a handful of chairs actually set against tables, I'd think the room unused if not for the paints, papers, and sketchbooks strewn across the tops of the cupboards. If Caprice wanted a club room, this would be as good as any."

"As I peer about, the sight of one particular canvas amongst it all catches my attention. The painting of a woman standing in water sits drying on the easel, the painter's utensils still lying about."

scene black with dissolve
scene bg buildingart art dusk siren
show bg buildingart art dusk siren blurred1:
    xalign 0.5 yalign 0.5
$camera_move(-200,820,650,0,0,'dissolve')
with dissolve
show misc cutins siren:
    subpixel True
    zoom 0.75
    xalign 0.5 yoffset -250
    ease 1.5 yoffset 175
"Stepping up to look at it, I'm surprised by how old-fashioned it is; like the kind of oil painting that would be drawn a century or so ago. Every brushstroke and line has depth to it, the painter's every movement clearly visible."

"I find myself struck by its beauty, time slipping by me as I stare. Her soft-looking skin and flowing locks of hair are enough to make me wistfully sigh, her face telling of her free spirit."

"It's beautiful..."

# End cutin
stop music fadeout 1.0
scene black
play sound "sfx/door_creak.ogg"
scene bg buildingart art dusk siren
$camera_move(-200,820,650,0,0,'dissolve')
with hpunch
"My thoughts are suddenly interrupted by the creaking of the door opening further, causing me to whip around in fright."
play ambiance "sfx/ambiance/heartbeat_light.ogg" fadein 0.1
play music "music/conflict.ogg" fadein 3.0
$ renpy.music.set_volume(0.4, delay=0)
stop sound fadeout 1.0

show eileen indoors_crossed normal neutral at center:
    zoom 0.65 yoffset -300
    xpos 0.52
with dissolve
$camera_move(-200,-250,650,0,3,'ease')
"The particular person standing in the doorway looking straight at me does nothing to settle my racing heart, much less the fact that I'm not even supposed to be in here."

show shadow:
    alpha 0.4
show bg buildingart art dusk siren blurred1 as bg2:
    yanchor -0.55
    size (1280, 270) crop (500, 300, 1280, 270)
show eileen indoors_crossed normal neutral as eileen2:
    yanchor 0.882
    size (1920, 325) crop (-400, 10, 1920, 325)
with midDissolve
allison "Sorry... I mean..."

"I quickly try to stammer out something, but the words keep catching in my throat."

show eileen open as eileen2:
    yanchor 0.882
    size (1920, 325) crop (-400, 10, 1920, 325)
$ renpy.transition(dissolve, layer='master')
eileenu "Oh, it's vending machine girl."

show eileen indoors_crossed normal neutral as eileen2:
    yanchor 0.882
    size (1920, 325) crop (-400, 10, 1920, 325)
$ renpy.transition(dissolve, layer='master')
allison "Allison!"

allison "Allison... Merlo."

show bg buildingart art dusk siren
hide shadow
hide eileen2
hide bg2
$ renpy.transition(dissolve, layer='master')
show eileen indoors_onhip lookaway open
$ renpy.transition(dissolve, layer='master')
eileen "So you do have a name. I'm Eileen Turner, for what it's worth."

show eileen indoors_onhip normal neutral
$ renpy.transition(dissolve, layer='master')
"I quickly nod. For all my nervousness about maybe being somewhere I shouldn't, Eileen doesn't actually seem to care that much. In fact, she almost looks bored. If this room's used by a bunch of people, there's a good chance she might not know I'm an intruder."

show eileen indoors_onhip closed
$ renpy.transition(dissolve, layer='master')
eileen "Well, I'm going to close the place up. If you want anything, you should grab it."

show eileen indoors_onhip lookawayangry
$ renpy.transition(dissolve, layer='master')
eileen "Not that I think you have anything here."

"The cold edge to her voice freezes my entire body."

allison "I mean, I can explain...!"

stop music fadeout 3.0
stop ambiance fadeout 3.0
show eileen indoors_crossed narrow
$ renpy.transition(dissolve, layer='master')
"Eileen narrows her eyes and crosses her arms, waiting for my response. A response which is interrupted by a familiar voice booming from the entrance."

scene black with dissolve
play music "music/art_club_a.ogg" fadein 2.0
$ renpy.music.set_volume(1.0, delay=0)
scene bg buildingart art dusk siren
show eileen indoors_crossed normal neutral at right2:
    xpos 0.82
show caprice indoors_wave even closedhappy grin at leftish:
    xpos 0.255
    bounce
with dissolve
$ camera_reset()
caprice "Hey, Allie!"

show caprice neutral normal at leftish:
    xpos 0.255
"I don't think I've ever been so glad to see Caprice. Given this art club business was her idea, it's for the best if she explains it all."

show eileen indoors_crossed narrow at right2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
"Eileen doesn't look impressed as Caprice skips into the room, looking this way and that like some tourist."

show caprice indoors_handonhip closedhappy neutral at leftish:
    xpos 0.255
$ renpy.transition(dissolve, layer='master')
caprice "Good work, you already found us a room. This'll work perfectly."

show eileen frown at right2:
    xpos 0.82
show caprice normal at leftish:
    xpos 0.255
$ renpy.transition(dissolve, layer='master')
eileen "So, Caprice got herself a new goon. I wish I was surprised."

show caprice grin at leftish:
    xzoom 1 xpos 0.255
    linear 0.5 xzoom -1 xpos 0.225
caprice "Yep!"

show caprice grin at leftish:
    xzoom -1 xpos 0.225
$ renpy.transition(dissolve, layer='master')
"You're not supposed to agree with that."

show eileen open at right2:
    xpos 0.82
eileen "And what do you want this room for, pray tell?"

show eileen frown at right2:
    xpos 0.82
show caprice indoors_chintap raised closedhappy opensmile at left2:
    subpixel True
    xpos 0.225 yoffset 55
    ease 1.0 rotate 5
    ease 1.0 rotate 0
caprice "Weeeellll..."

show caprice normal at left2:
    xpos 0.225 yoffset 55 rotate 0
caprice "The current art club is awful, I'm sure you know."
show caprice indoors_pumped normal at left2:
    xpos 0.225 yoffset 55 rotate 0
    easein .15 yoffset 38
    easeout .175 yoffset 55
    easein .15 yoffset 48
    easeout .175 yoffset 55
caprice "So instead of dealing with them, we're going to form our own! And it looks like you and Allie have found us our club room!"

show caprice indoors_behindback closedhappy neutral at left2
"I see what's happened here now. Caprice engineered the situation so we'd all be here together. This isn't a very subtle scheme, but that's all the more reason for her to have come up with it. I try my best to backpedal, in a way that don't upset either."

allison "I just thought we'd... draw a bit. Didn't mean to intrude."

show eileen disbelief grumble at right2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
eileen "I got permission to use this room to practice my painting, not for some dumb club."

show caprice indoors_chintap wink at left2
$ renpy.transition(dissolve, layer='master')
caprice "Sorry, but it's two against one. Majority rule!"

allison "I didn't say anything about a club!"

show eileen annoyed at right2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
eileen "Well too bad, this is a dictatorship."

show caprice indoors_behindback closedhappy at left2
$ renpy.transition(dissolve, layer='master')
"Eileen stands her ground, staring down her opponent as I try my best to stay well out of their argument."

show eileen indoors_onhip closed open at right2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
"Her resolve doesn't last long, though. Realizing the futility of it, she eventually heaves a sigh at Caprice's antics. I can't say I wholly blame her."

show caprice normal at left2
show eileen normal angry at right2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
eileen "I just want to work in peace. That isn't much to ask."

show caprice raised open at left2
caprice "But-"

$ renpy.music.set_volume(0.0, delay=2.0)
show eileen annoyed at right2:
    xzoom 1 xpos 0.82
    linear 0.5 xzoom -1 xpos 0.8
show caprice flat at left2
eileen "I'm going. Not going to get anything more done today, anyway."

scene black with dissolve
scene bg buildingart art dusk siren blurred1:
    xalign 0.5 yalign 0.5
show caprice indoors_behindback raised normal flat at left2:
    zoom 0.8 yoffset -200
    xzoom -1 xpos 0.225
show eileen outdoors_onhip narrow grumble at right2:
    zoom 1.2 yoffset 150
    xzoom -1 xpos 0.725
    time 0.2
    nod2
with dissolve
"Eileen turns to me after picking up her coat from a desk and pulling her scarf around her, rather pointedly being finished with Caprice."

show eileen outdoors_onhip normal open at right2:
    zoom 1.2 yoffset 150
    xzoom -1 xpos 0.725
$ renpy.transition(dissolve, layer='master')
eileen "See you around, I guess."

show eileen outdoors_onhip normal angry at right2:
    xzoom -1 xpos 0.725
$ renpy.transition(dissolve, layer='master')
allison "Yeah..."

show eileen outdoors_onhip lookaway angry at right2:
    xzoom -1 zoom 1.2 yoffset 150
    xpos 0.725
    ease 1.5 xpos 1.5
pause 1.0
play sound "sfx/door_close.ogg"
"At a loss for how I'm supposed to respond to such an unenthusiastic tone, I'm left standing silently by as a frustrated Eileen throws her backpack over a shoulder and strides out."

$ renpy.music.set_volume(1.0, delay=2.0)
show bg buildingart art dusk siren
show caprice indoors_handonhip even closedhappy neutral at left2:
hide eileen
$ renpy.transition(dissolve, layer='master')
stop sound fadeout 1.0
"Caprice just smiles and shrugs as she looks back to me, the argument they had just moments ago flowing off her like water on a duck's back."

$camera_move(-650,50,400,0,3,'ease')
show caprice indoors_handonhip even closedhappy neutral at left2:
    xpos 0.225
    ease 1.0 xpos 0.32
caprice "Well, that's how it is."

show caprice normal at left2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
allison "I feel like I got dragged into something..."

show caprice indoors_behindback wink at left2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
caprice "I didn't really think that'd work, but it was worth a try."

show caprice closedhappy at left2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
"She's not listening to me at all. Am I really just an instrument to try and win this argument between them?"

show shadow:
    alpha 0
    ease 1.0 alpha 0.4
"No, I can't think that. Caprice is... forceful, but she means well. If this did end up being a club, I'd probably enjoy it."

"Caprice certainly wouldn't make it dull, and I think if Eileen got to know me she'd be nicer to me, but I don't want to risk Eileen getting even more annoyed with me."

"It feels like I've been left to hunker down in a foxhole in no-man's-land, and all I can do right now is hold my helmet on tight."

show shadow:
    alpha 0.4
    ease 1.0 alpha 0
show caprice normal at left2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
"As the orange of the sunset starts to wane outside, it becomes obvious that nothing more's going to get done today, just as Eileen said."

allison "I'd better head home, it's getting late. See you tomorrow."

hide shadow
show caprice indoors_handonhip wink at left2:
    zoom 0.8 yoffset -200
    xpos 0.32
    easein .15 yoffset -218
    easeout .175 yoffset -200
    easein .15 yoffset -208
    easeout .175 yoffset -200
caprice "See ya! If you ever wanna draw, feel free to drop by the new club room!"

stop music fadeout 5.0
"Precisely none of what Eileen said penetrated, did it?"

scene bg buildingart hallway2f dusk with midDissolve
$ camera_reset()
"I just give a weak smile as I wave and take my bag, idly wondering if Rose will be cooking something for dinner or bringing home take-out. It's something more heartening to think about than today's efforts, anyway."

window hide dissolve
scene black with longDissolve
play sound "sfx/door_close3.ogg"
scene bg aptallison livingroom
$camera_move(1550,-200,650,0,0,'dissolve')
with midDissolve
play sound "sfx/sitting-down-on-couch.ogg"
with vpunch
window show dissolve

"As I collapse onto the couch and settle in, the deafening sound of silence rushes in. The odd passing car from the street below the apartment only highlights the quiet of the room."

show bg aptallison livingroom blurred2:
    xalign 0.5 yalign 0.5
$ renpy.transition(dissolve, layer='master')
$ phone.show('unlock')
"Plucking my phone from my pocket after dropping my bag on the cushion beside me, I take quick note of the time. I guess Rose got stuck in traffic."
stop sound fadeout 1.0

show bg aptallison livingroom
$ renpy.transition(dissolve, layer='master')
$ phone.hide()
"An annoying train of thought starts up once again as I put it away. One that's crept up on me occasionally ever since moving out, just waiting for when nothing's around to distract me."

"I can cope with the schoolwork easily enough; it's mostly just review right now. People like Caprice might be a handful, but they do liven up the day's routine. It's a fair distance to campus from here, but the walk helps keep me fit."

"The silence. That, I can't deal with."

play ambiance "sfx/ambiance/tv.ogg" fadein 2.0
$camera_move(0,0,0,0,5,'ease')
"Grabbing the remote and flicking on the television at least provides some background noise, but it's no replacement for the sounds of home."

"There's no mother busying herself over the cooking pot to welcome me home and ask how my day was. No excitable older brothers fighting about this silly thing or that. No father for me to happily see come home from work..."

"It's just me, now."

show bg aptallison livingroom blurred2:
    xalign 0.5 yalign 0.5
$ renpy.transition(dissolve, layer='master')
$ phone.show('unlock')
"My fingers roll over the screen in thought as it brings up the lock screen, mindlessly tracing out the cracks in the bottom corner. I could easily call them right now; my mom and dad both made it clear I could ring any time at all."

"But as I stare at the screen, a deep apathy strikes me. Before college, I'd thought that with my family and old friends just a phone call away, nothing would feel all that different."

"Maybe I just couldn't admit to myself how big of a change this would really be."

show bg aptallison livingroom:
    xalign 0.5 yalign 0.5
$ renpy.transition(dissolve, layer='master')
$ phone.hide()
$ camera_move(1550,-200,650,0,4,'ease')

"Admitting defeat, the phone ends up on the couch beside me as I watch television. The news is interesting today, so at least it's some distraction from all this."

"Just when I thought I'd finally found a friend or two in college, it ends up being a mess. Why do people have to be so complicated?"

$camera_move(3550,-200,650,0,3,'ease')
play sound "sfx/door_open2.ogg"
stop ambiance fadeout 2.0
$ _dismiss_pause = False
"As the door behind me opens, I close my thoughts on the subject. There's no point in mulling things over any further."


stop sound fadeout 1.0
window hide dissolve
scene black with longDissolve
$ camera_reset()

$ achievement.grant('story_act1')
scene title act1 with menuFade
$ renpy.pause(5.0, hard=True)

return
