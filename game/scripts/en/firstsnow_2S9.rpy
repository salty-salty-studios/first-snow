label scene_2S9_en:
######################

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg buildingmisc generichall sketch with inkfade
scene bg buildingmisc generichall with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

play ambiance "sfx/ambiance/class_test.ogg" fadein 0.1
"The classroom lies silent, save for the scratching of pencil against paper."

"I've already finished my math test, the unwillingness to be the first to turn it in being the only thing keeping me glued to my desk."

"I'm thankful for the chance to rest, though; Eileen's pace as we scooted around the zoo took all my effort to keep up with, and then there was the other business we got up to."

"Someone finally brings his paper to the front, other students following suit soon after."

stop ambiance fadeout 4.0
"I quickly join them, eagerly placing my test on the teacher's desk and packing my things afterwards."

play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 1.0
scene bg buildingbusiness hallway1f with midDissolve
"The last final of the semester now over, I'm ready to go home... and to see Eileen one last time before she leaves for Colorado."

play music "music/caprice_default_m.ogg" fadein 5.0
$ renpy.transition(vpunch, layer='master')
caprice "{size=32}{b}Hey!{/b}{/size}"

"The loud voice from behind makes me jump in startlement."

show caprice outdoors_wave raised closedhappy opensmile at offcenterright:
    bounce
$ renpy.transition(dissolve, layer='master')
allison "Oh, Caprice. Hey."

show caprice outdoors_handonhip normal neutral at offcenterright
$ renpy.transition(dissolve, layer='master')
"My heart slowly moves out of my throat, with Caprice and I starting off together towards art club. I had considered asking Eileen if we could walk back to her apartment together instead, but I couldn't leave without saying my goodbyes to Caprice, and Wallace if I could find him."

allison "What brings you to my class, anyway?"

show caprice outdoors_chintap pout half sad at offcenterright
$ renpy.transition(dissolve, layer='master')
caprice "Millie wasn't around, so I got lonely."

"So I'm the second choice, huh? Well, at least I can be around for her."

show caprice outdoors_chintap neutral normal even at offcenterright
$ renpy.transition(dissolve, layer='master')
allison "You two really are close, aren't you?"

show caprice outdoors_pumped grin normal even at offcenterright:
    bounce
caprice "Yep! We grew up together, and now we even live together. Millie, and me, and Hayley! She's our other friend. We take good care of each other."

"There really are all kinds of relationships. It's so different from high school, where everyone was neatly organized into friends, classmates, or strangers, and we all just lived with our parents."

show caprice outdoors_behindback raised normal open at offcenterright
$ renpy.transition(dissolve, layer='master')
caprice "Do you have a roommate? What're they like?"

allison "I live with a family friend. She's nice, even if she looks a bit rough. I have the apartment to myself a lot, though."

show caprice outdoors_chintap frown half even at offcenterright
$ renpy.transition(dissolve, layer='master')
"The statement seems to give Caprice food for thought."

caprice "You shouldn't look so tired, school's finally over for the year."

show caprice outdoors_pumped opensmile normal angry at offcenterright:
    bounce
caprice "...And that's why we're having an extra special art club meeting!"

show caprice neutral at offcenterright
$ renpy.transition(dissolve, layer='master')
allison "'Extra special'?"

show caprice outdoors_behindback neutral closedhappy even at offcenterright
$ renpy.transition(dissolve, layer='master')
caprice "You'll see what I mean!"

stop ambiance fadeout 2.5
"I have a feeling she's working this out as she goes along. I still can't decide if I like that spontaneity of hers. It's endearing, but there's no sense of stability to her like Eileen has."

$ renpy.music.set_volume(0.1, delay=5.0)
play sound "sfx/door_close2.ogg"
scene black with dissolve
$ renpy.sound.set_volume(1.5, channel='ambiance')
play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
scene bg buildingunion outside snow blurred2:
    xalign 0.5 yalign 0.5 alpha 0.85
show eileen outdoors_fists lookaway angry at centerright:
    zoom 0.88 yoffset -100
    xzoom -1 xpos 0.62
with midDissolve
$camera_move(1800,-150,400,0,6,'ease')
"As we head towards the arts building, we spot Eileen just outside. Busy huffing into her hands and rubbing them together for a little warmth, it takes a moment for her to notice us."

stop sound fadeout 1.0
allison "Eileen, hi."

show eileen outdoors_onhip neutral normal at centerright:
    zoom 0.88 yoffset -100
    xzoom -1 xpos 0.62
    linear 0.7 xzoom 1 xpos 0.67
"As she looks up in my direction, I notice her shoulders relax a little. It wasn't long ago that I only ever saw Eileen tense and on guard, but now she reflexively relaxes when around me. It's nice."

$ renpy.sound.set_volume(1.0, channel='ambiance')
scene bg buildingunion outside snow
show eileen outdoors_onhip neutral normal at centerleft:
    xpos 0.3
with fadeInOut
$ camera_reset()
$ renpy.music.set_volume(1.0, delay=2.0)
show caprice outdoors_wave neutral normal even at right2:
    xpos 1.1 alpha 0
    ease 1.5 xpos 0.775 alpha 1
"For her part, Caprice just bowls on ahead without a care in the world."

show caprice outdoors_wave grin normal even at right2:
    xpos 0.775 alpha 1
    bounce
caprice "{b}Hey!{/b}"

show eileen outdoors_crossed disbelief at centerleft:
    xzoom 1 xpos 0.3
    linear 0.7 xzoom -1 xpos 0.25
show caprice outdoors_behindback grin half raised at right2 with dissolve
"Eileen tenses right back up as she sees my companion, the moment lost. Still, I'm left rather happy at the effect I have on Eileen, whether she notices it or not."

show eileen outdoors_crossed closed open at centerleft:
    xzoom -1 xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "'Afternoon, you two."

show eileen outdoors_crossed narrow frown at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "Caprice, why are you looking at me like that? It's creeping me out."

show caprice outdoors_behindback grin half raised at right2:
    nod2
"Caprice grabs onto both our shoulders, and to my surprise, directs us away from the arts building."

show caprice outdoors_chintap open wink even at right2
$ renpy.transition(dissolve, layer='master')
caprice "We've had a change of plans."

show eileen lookawaynarrow open at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "Do I get a say in this?"

stop ambiance fadeout 4.0
stop music fadeout 4.0
show eileen frown at left2:
    xpos 0.25
show caprice outdoors_behindback neutral closedhappy even at right2
$ renpy.transition(dissolve, layer='master')
"Once again, Caprice either doesn't hear, or chooses to ignore the question."

scene black with circlewipe
play music "music/whimsical_faster_m.ogg" fadein 4.0
$ renpy.sound.set_volume(0.2)
play sound "sfx/dumptruck.mp3" fadein 1.0
scene bg aptallison livingroom
show eileen indoors_onhip normal neutral at left2:
    xzoom -1
show caprice indoors_chintap raised normal pout at right2:
    xzoom -1 xpos 0.75
with circlewipe
"By the time we arrive at my apartment and shirk our coats, it's already dark enough to flick the lights on as we enter. Apart from the sound of passing cars, the only sounds are Caprice's exaggerated sounds of thoughtful inspection."

show eileen disbelief at left2:
    xzoom -1
$ renpy.transition(dissolve, layer='master')
"Eileen raises an eyebrow as Caprice whips out her phone to take a photo for posterity, the item disappearing into her pants pocket almost as quickly as it appeared."

show caprice indoors_chintap raised half pout at right2:
    xpos 0.75
show eileen indoors_crossed narrow open at left2:
    xzoom -1
$ renpy.transition(dissolve, layer='master')
eileen "Will you just leave that thing? You've been fiddling with your phone on the way here more than Allison does."

show eileen neutral at left2:
    xzoom -1
$ renpy.transition(dissolve, layer='master')
allison "Hey."

show eileen indoors_onhip lookaway angry at left2:
    xzoom -1 xpos 0.225
    linear 0.7 xzoom 1 xpos 0.28
eileen "Well, it's true."

show caprice indoors_handonhip grin closedhappy even at right2:
    xzoom -1 xpos 0.75
    bounce
    linear 0.7 xzoom 1 xpos 0.775
"Caprice gives a thumbs-up, but it has the opposite effect if anything. Her agreement is a little too quick, given how stubborn Caprice usually is."

show eileen indoors_crossed normal open at left2:
    xzoom 1 xpos 0.28
show caprice indoors_behindback neutral normal even at right2:
    xzoom 1 xpos 0.775
$ renpy.transition(dissolve, layer='master')
eileen "So Rose isn't here, then?"

show eileen neutral at left2:
    xzoom 1 xpos 0.28
$ renpy.transition(dissolve, layer='master')
allison "She drifts in and out. I've given up trying to work out any schedule to it."

show caprice indoors_chintap open normal even at right2
$ renpy.transition(dissolve, layer='master')
caprice "Cool posters."

show caprice neutral at right2
$ renpy.transition(dissolve, layer='master')
allison "They're my roommate's. She's been living here longer than me, so the decorations are all hers."

$ renpy.sound.set_volume(1.0)
play sound "sfx/door-knock.ogg"
stop music fadeout 8.0
show eileen disbelief at left2:
    xzoom 1 xpos 0.28
    linear 0.7 xzoom -1 xpos 0.225
"A knock on the door rings out, four light taps struck with a metronome's timing."

show caprice indoors_wave opensmile closedhappy raised at right2:
    bounce
caprice "Come in, door's unlocked!"

show caprice grin at right2
show eileen indoors_crossed angry narrow at left2:
    xzoom -1 xpos 0.225
$ renpy.transition(dissolve, layer='master')
allison "Huh? What's going on? This is my apartment, you know."

stop sound fadeout 1.0
"Caprice just grins, drawing a grimace from Eileen."

show caprice indoors_handonhip grin wink raised at right2
$ renpy.transition(dissolve, layer='master')
caprice "What did you think I was on my phone for? I called over some friends!"

play music "music/diner_2_m2.ogg" fadein 5.5
play sound "sfx/door_open2.ogg"
scene bg aptallison livingroom HD
$camera_move(-5000,-1650,-250,0,0,'dissolve')
show millie outdoors_neutral raised normal frown at leftedge:
    zoom 0.85 yoffset -250
    xzoom -1 xpos -0.4 alpha 0
    time 1
    ease 1.5 xpos -0.2 alpha 1
show bg aptallison livingroom wall as livingroom_wall:
    xalign 0.5 yalign 0.5
with fadeInOut
"The old door creaks open, with Millie's head peering into the living room."

play sound "sfx/door_close2.ogg"
show millie outdoors_neutral even closedhappy neutral at leftedge:
    xzoom -1 xpos -0.2 alpha 1
    ease 0.6 yoffset -245
    ease 0.6 yoffset -255
    ease 0.3 yoffset -250
show wallace outdoors neutral open even behind millie at leftside:
    zoom 0.85 yoffset -250
    xzoom -1 xpos -0.35 alpha 0
    ease 2.0 xpos 0.05 alpha 1
"Assured that she's come to the right place, she skips in with the unmistakable figure of Wallace following her like a giant shadow."

scene bg aptallison livingroom
show wallace outdoors neutral forward even at leftside:
    zoom 0.85 yoffset -120
    xzoom -1 xpos 0.14
show millie outdoors_neutral neutral normal even at centerleft:
    zoom 0.85 yoffset -120
    xzoom -1 xpos 0.39
show caprice indoors_wave open closedhappy raised at centerright:
    zoom 0.85 yoffset -120
    xpos 0.65
    time 1
    easein .15 yoffset -138
    easeout .175 yoffset -120
    easein .15 yoffset -128
    easeout .175 yoffset -120
show eileen indoors_crossed lookaway neutral at rightside:
    zoom 0.85 yoffset -120
    xpos 0.9
with fadeInOut
$ camera_reset()
stop sound fadeout 1.0
caprice "Millie! Have you heard from Hayley?"

show millie indoors_neutral neutral closedsad even at centerleft with dissolve:
    xzoom -1 xpos 0.39
    nod2
pause 0.5
show wallace indoors neutral closed even at leftside:
    xzoom -1 xpos 0.14
    nod2
show caprice indoors_handonhip neutral normal at centerright:
    xpos 0.65
$ renpy.transition(dissolve, layer='master')
"Millie answers as she takes off her coat, Wallace doing the same for his scarf."

show millie indoors_neutral speaking normal sad at centerleft:
    xzoom -1 xpos 0.39
$ renpy.transition(dissolve, layer='master')
millie "She's at home, sleeping. Seems like finals tired her out."

show millie neutral at centerleft:
    xpos 0.39
show caprice indoors_behindback puffed half even at centerright
$ renpy.transition(dissolve, layer='master')
caprice "She never wants to go anywhere!"

show wallace indoors neutral forward even at leftside:
    xzoom -1 xpos 0.14
show eileen lookawaynarrow at rightside:
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
"I don't know this Hayley, but I feel like I can relate. It's not just about finals, or going particular places. Being around people is exhausting in itself."

show caprice indoors_behindback grumble closedsad even at centerright
$ renpy.transition(dissolve, layer='master')
"Lately I've been looking forward to it, though. Even if it takes a lot out of me."

show eileen indoors_onhip normal at rightside with dissolve:
    xpos 0.9
play sound "sfx/bottle-clank.ogg"
show millie even smile at centerleft:
    xpos 0.39
    nod2
"The clinking of bottles draws my attention, looking downward showing a six-pack of bottled beer being carried in one hand, and a plastic bag with a couple of brightly colored nacho packets visible inside."

show wallace indoors smile open even at leftside:
    xpos 0.14
show caprice indoors_chintap pout normal raised at centerright
$ renpy.transition(dissolve, layer='master')
"Caprice looks up to the two, surprised just as I am by the present they've brought along."

stop sound fadeout 1.0
show millie indoors_tented smile closedhappy even at centerleft:
    xpos 0.39
$ renpy.transition(dissolve, layer='master')
millie "Just a little something for the special event."

show caprice indoors_behindback neutral normal even at centerright with dissolve
show millie indoors_tented pout half even at centerleft:
    xzoom -1 xpos 0.39
    linear 0.7 xzoom 1 xpos 0.42
millie "I can't believe you didn't take the santa hat they were offering, though..."

show wallace indoors frown halfopen even at leftside:
    xpos 0.14
$ renpy.transition(dissolve, layer='master')
wallace "I'm not wearing a santa hat, Christmas or not."

show millie indoors_neutral neutral closedhappy even at centerleft:
    xzoom 1 xpos 0.42
show eileen indoors_crossed smile lookawaynarrow at rightside:
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
eileen "Why not? Would've suited you."

show caprice indoors_behindback grin closedhappy raised at centerright
show wallace indoors frown halfsmall even at leftside:
    xpos 0.14
$ renpy.transition(dissolve, layer='master')
wallace "Don't you start."

show wallace indoors mopen closed even at leftside:
    xpos 0.14
show millie indoors_neutral smile half angry at offcenterleft:
    xzoom 1 xpos 0.42
$ renpy.transition(dissolve, layer='master')
"So this was Caprice's plan; a party to celebrate the end of college for the year. I really would have preferred her to just tell me, but there's also a begrudging respect that she apparently managed to organize all this during the short trip from college to my apartment."

show eileen narrow neutral at rightside:
    xpos 0.9
show bg aptallison livingroom blurred2 as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0
    time 2
    ease 2.0 alpha 1
$camera_move(3800,-850,880,0,5,'ease')
"I'm about to warn Wallace about Millie casting covetous eyes on his beer, when Eileen leans over and murmurs in my ear."

show eileen indoors_fists sad open at rightside:
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
eileen "Is a party here going to be a problem for you?"

show wallace indoors neutral open even at leftside:
    xpos 0.14
show millie indoors_neutral neutral normal even at offcenterleft:
    xzoom 1 xpos 0.42
show eileen neutral at rightside:
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
allison "It'll be fine. I think."

show bg aptallison livingroom blurred2 as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 1
    ease 2.0 alpha 0
$camera_move(0,0,0,0,5,'ease')
pause 2.0
show eileen indoors_crossed closed open at rightside:
    xzoom 1 xpos 0.9 alpha 1
    linear 0.7 xzoom -1 xpos 0.85
    ease 1.5 xpos 1.2
"Satisfied with my answer, she steps over to the couch and takes a seat with a sigh. Despite my waving off of the concern, I appreciate Eileen's sense of responsibility."

show bg aptallison livingroom:
    subpixel True
    zoom 1.0 xalign 0.5 yalign 0.5
    ease 3.0 zoom 1.2 xalign 0.5 yalign 0.5
show wallace indoors neutral open even at left2:
    subpixel True
    zoom 0.85 yoffset -120 xpos 0.14 xzoom -1 
    ease 3.0 zoom 1.0 yoffset 0 xpos 0.2
show millie indoors_neutral neutral normal even at offcenterright:
    subpixel True
    zoom 0.85 yoffset -120 xpos 0.42
    ease 3.0 zoom 1.0 yoffset 0 xpos 0.55
show caprice indoors_handonhip open normal even at right2:
    subpixel True
    zoom 0.85 yoffset -120 xpos 0.65
    ease 3.0 zoom 1.0 yoffset 0 xpos 0.82
"As we talk, Wallace sets down the beer and chips on the table."

"Caprice wastes no time in scooting over and ripping open the bag, Millie soon following and taking a seat across from her."

show millie indoors_neutral angry half smile at offcenterright:
    zoom 1.0 yoffset 0
    xzoom 1 xpos 0.55
    nod2
"The fact she steals one of the beer bottles doesn't go unnoticed."

show caprice indoors_behindback closedhappy neutral at right2:
    zoom 1.0 yoffset 0
    xpos 0.82
show wallace indoors frown halfsmall even at left2:
    zoom 1.0 yoffset 0
    xzoom -1 xpos 0.2
$ renpy.transition(dissolve, layer='master')
wallace "Millie..."

show millie indoors_tented pout half sad at offcenterright:
    xpos 0.55
$ renpy.transition(dissolve, layer='master')
millie "Just the one. It won't hurt, right?"

show caprice indoors_pumped puffed normal angry behind millie at right2:
    xpos 0.82
    bounce
caprice "Hey, stop hogging the chips!"

show millie indoors_neutral frown normal angry at offcenterright:
    xzoom 1 xpos 0.55
    linear 0.7 xzoom -1 xpos 0.53
millie "But I'm hungry!"

show millie indoors_neutral half at offcenterright:
    xzoom -1 xpos 0.53
show caprice half grumble at right2:
    xpos 0.82
show wallace indoors mopen closed upturned at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
"Wallace just sighs, defeated as the two bicker over the food. I feel a little sorry for him, but given he did bring them..."

allison "Make yourselves at home..."

scene bg aptallison livingroom HD
$camera_move(4500,-1000,-650,0,0,'dissolve')
show wallace indoors neutral open even at leftedge:
    zoom 1.05 yoffset -80
    xzoom -1 xpos -0.08
show eileen indoors_crossed neutral normal at centerleft:
    zoom 1.05 yoffset -80
    xzoom -1 xpos 0.33
    time 1
    nod2
with fadeInOut
"Eileen gestures for me to join her, jerking her head. Giving up any thought that I could control them, I skip over and take a seat on the cushion next to her."

$camera_move(-3000,-1000,-650,0,5,'ease')
show wallace indoors neutral open even at leftedge:
    zoom 1.05 yoffset -80
    xzoom -1 xpos -0.08
    ease 2.0 xpos -0.04
pause 1.0
show eileen indoors_crossed disbelief open at centerleft:
    xzoom -1 xpos 0.33
    linear 0.7 xzoom 1 xpos 0.39
    shaking2
"As Eileen turns towards the television, she finds a beer bottle held in front of her face. Looking up to the smiling Wallace offering it, she takes it in her hand."

show wallace indoors smile open even at leftedge:
    xpos -0.04
$ renpy.transition(dissolve, layer='master')
wallace "Merry Christmas, Eileen."

show eileen indoors_onhip smile normal at centerleft:
    xzoom 1 xpos 0.39
$ renpy.transition(dissolve, layer='master')
eileen "Cheers. Same to you."

play sound "sfx/bottle-clink.ogg"
show wallace indoors smile open even at leftedge:
    xpos -0.04
    ease 0.5 xoffset 5
    ease 0.2 xoffset 0
    ease 0.5 xoffset -5
    ease 0.2 xoffset 0
show eileen indoors_onhip smile normal at centerleft:
    xzoom 1 xpos 0.39
    ease 0.5 xoffset -5
    ease 0.2 xoffset 0
    ease 0.5 xoffset 5
    ease 0.2 xoffset 0
"The two clink their bottles together, popping the lids with a bottle opener on Wallace's keychain before Eileen slouches back into the couch."

show wallace indoors smile closed even at leftedge:
    xpos -0.04
show eileen closed at centerleft:
    xzoom 1 xpos 0.39
$ renpy.transition(dissolve, layer='master')
"While the thought passes my mind that the last thing I'd want is an alcohol-fueled mess at my place, those fears are put to rest as the two gently sip away. They're just friends sharing a drink, not party-goers looking to get as drunk as they can."

stop sound fadeout 1.0
scene bg aptallison livingroom:
    xalign 1.0 yalign 1.0
show millie indoors_neutral neutral closedsad even at centerright:
    zoom 0.6 yoffset -350
    xpos 0.62
with fadeInOut
$ camera_reset()
"Looking around the room, this sure is low-key for a college party. We're just friends drinking and gossiping. It's nice, far from the wild craziness I expected when I heard tales about college when growing up. Guess I fell in with the right crowd."

$camera_move(200,-400,650,0,4,'ease')
pause 2.0
show eileen indoors_crossed normal open at offcenterleft:
    zoom 0.6 yoffset -350
    xzoom -1 xpos 0.2 alpha 0
    ease 2.0 xpos 0.4 alpha 1
pause 2.0
eileen "What're you doing hanging out with us losers anyway, Millie? Writing club not doing anything special?"

show eileen neutral at offcenterleft:
    xpos 0.4 alpha 1
show millie indoors_neutral speaking normal even at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
millie "They're doing this and that, but most of them seem to have plans. The leader and his friends are graduating, so it's going to be up to me to keep the ship sailing."

show millie neutral at centerright:
    xpos 0.62
show eileen indoors_onhip closed open at offcenterleft:
    xpos 0.4 alpha 1
$ renpy.transition(dissolve, layer='master')
eileen "Sounds like you're going to have your hands full next semester, then."

show eileen lookaway neutral at offcenterleft:
    xpos 0.4 alpha 1
show millie indoors_tented smile closedhappy raised at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
millie "Always up for a challenge."

show bg aptallison livingroom blurred2:
    xalign 1.0 yalign 1.0
show eileen indoors_onhip neutral lookaway blur at offcenterleft:
    zoom 0.6 yoffset -350
    xzoom -1 xpos 0.4
show millie indoors_tented smile closedhappy raised blur at centerright:
    zoom 0.6 yoffset -350
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
pause 1.0
$camera_move(0,0,0,0,4,'ease')
show wallace indoors neutral open even at left2:
    zoom 1.35 yoffset 300
    xzoom -1 xpos -0.12
    ease 2.0 xpos 0.12
show caprice indoors_chintap open half raised at right2:
    zoom 1.35 yoffset 300
    xpos 1.1
    ease 2.0 xpos 0.85
pause 3.0
caprice "Hey, Wallace?"

"Caprice's excited tone as she wolfs down her mouthful of nachos fails to enthuse him."

show wallace indoors neutral open heightened at left2:
    xzoom -1 xpos 0.12
show caprice indoors_chintap closedhappy at right2:
    xpos 0.85
$ renpy.transition(dissolve, layer='master')
caprice "Remember what we talked about at the pizza place? I mean, about your club 'n all..."

show wallace indoors frown closed even at left2:
    xpos 0.12
$ renpy.transition(dissolve, layer='master')
wallace "No."

show caprice indoors_pumped frown normal sad at right2:
    xpos 0.85
$ renpy.transition(dissolve, layer='master')
caprice "But-"

show wallace indoors frown halfopen even at left2:
    xpos 0.12
$ renpy.transition(dissolve, layer='master')
wallace "No."

show bg aptallison livingroom
show eileen indoors_onhip normal angry behind wallace at offcenterleft as eileen2:
    zoom 0.6 yoffset -350
    xzoom -1 xpos 0.4
show millie indoors_tented smile half even at centerright as millie2:
    zoom 0.6 yoffset -350
    xpos 0.62
show caprice indoors_behindback puffed half sad at right2:
    xpos 0.85
$ renpy.transition(dissolve, layer='master')
$ renpy.music.set_volume(0.1, delay=5.0)
"Millie grins triumphantly, at her friend's expense. I feel a little sorry for Wallace, being caught in their rivalry."

scene bg aptallison livingroom
show caprice indoors_wave grin closedhappy even at centerright:
    zoom 0.85 yoffset -120
    xzoom -1 xpos 0.6
show millie indoors_tented smile normal even at rightside:
    zoom 0.85 yoffset -120
    xpos 0.88
with fadeInOut
$ camera_reset()
play sound "sfx/door_open2.ogg"
"I'm the only one who notices the creak of the door, my attention wholly focused on it as I wonder who's arrived. Part of me worries that Caprice organized for more people to come, the girl now bickering with Millie."

show caprice indoors_behindback frown normal raised at centerright:
    xzoom -1 xpos 0.6
    linear 0.7 xzoom 1 xpos 0.62
show millie indoors_neutral raised normal speaking at rightside with dissolve:
    xpos 0.88
$camera_move(-4000,-480,780,0,3,'ease')
show rose outdoors_handonhip normal puzzled at left2:
    xzoom -1 xpos -0.2
    ease 3.0 xpos 0.25
"As the leather-clad woman steps in, everyone in the room suddenly drops into a dead silence as they stare back at her, the woman being just as dumbstruck."

stop sound fadeout 1.0
hide caprice
hide millie
show rose outdoors_handonhip halfclosed smirk at left2:
    xzoom -1 xpos 0.25 alpha 1
$ renpy.transition(dissolve, layer='master')
rose "...'Sup?"

"I struggle to stifle a chuckle, never having seen Rose act so awkwardly before."

$ renpy.music.set_volume(1.0, delay=5.0)
allison "Everyone, this is my roommate, Rose. Rose, these are my friends from college."

$camera_move(0,0,0,0,5,'ease')
"The clarification has the intended effect, everyone relaxing as soon as the words are said."

show rose outdoors_handonhip laugh at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
rose "Sure is some wild party you got goin' on here."

show rose outdoors_handonhip normal talking at left2:
    xpos 0.25
    bounce
rose "Oh, actually..."

show rose outdoors_handonhip neutral normal at left2:
    xpos 0.25
    ease 1.0 xpos 0.5
    nod2
play sound "sfx/rustle-clothes.ogg"
"I'm left wondering what she's doing as she clicks her fingers and dives back for my coat."

"After a few minutes fishing about, she manages to pluck out my phone."

stop sound fadeout 1.0
"After handing it to me to enter the unlock code, Rose stands back in the corner of the room and holds it up in both hands."

show rose outdoors_handonhip smile normal at center
$ renpy.transition(dissolve, layer='master')
rose "Just gonna take a quick photo for the folks. Smile, guys!"

scene black with dissolve
scene cg act2 photo
show white:
    zoom 2.0 alpha 0.5
show cg act2 photo camera as act2_photo_camera:
    zoom 0.53 xcenter 0.728 ycenter 0.522
$camera_move(3650,200,850,0,0,'dissolve')
play sound "sfx/camera_focus.ogg"
with midDissolve
pause 0.5
"Caprice and Millie need no further prompting, leaning towards each other as Caprice flashes a V and gives a toothy grin."

scene black with dissolve
scene cg act2 photo
show white:
    zoom 2.0 alpha 0.5
show cg act2 photo camera as act2_photo_camera:
    subpixel True
    zoom 0.41 xcenter 0.35 ycenter 0.38
$camera_move(-2400,-1080,1080,0,0,'dissolve')
play sound "sfx/camera_focus.ogg"
with midDissolve
pause 0.5
"I simply lean towards Eileen, as she does the same. As we do, I idly note that this will be our first photo together."

show cg act2 photo camera as act2_photo_camera:
    subpixel True
    zoom 0.41 xcenter 0.35 ycenter 0.38
    ease 10.0 zoom 1.0 xcenter 0.5 ycenter 0.5
$camera_move(0,0,0,0,10,'ease')
pause 8.0
"As Rose brings the camera steady, I can't stop myself from smiling. I spent so long stressing about being away from my family, but before I knew it, I found myself surrounded by a new one."

"We might all be a bit odd, but we get along. I found someone to hold dear, and who cares for me. We're all in this together, celebrating life in my little slice of the city."

"I've finally made a life that I can call my own. Thank you, everyone. Rose, Caprice, Wallace, even Millie."

stop music fadeout 4.0
play sound "sfx/camera_shutter.ogg"
hide act2_photo_camera
hide white
show cg act2 photo blurred2 as cg2:
    alpha 0.5
with flash
$ camera_reset()
"And especially, Eileen."

window hide dissolve
scene black with longDissolve
stop sound fadeout 1.0
return
