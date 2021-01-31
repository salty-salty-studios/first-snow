label scene_2S6_en:
######################

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg aptallison livingroom sketch
$camera_move(1550,-200,650,0,0,'dissolve')
with inkfade
scene bg aptallison livingroom
$camera_move(1550,-200,650,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
$ _dismiss_pause = True

play ambiance "sfx/ambiance/tv.ogg" fadein 1.0
$camera_move(-650,-200,650,0,8,'ease')
$ renpy.sound.set_volume(0.05)
play sound "sfx/dumptruck.mp3" fadein 1.0
window show dissolve

"A loud yawn fills the living room, the droning of the television briefly overshadowed."

"The scene couldn't be more normal; Rose lounging about on the couch watching the morning news, the sounds of traffic outside heading off to work, and me, stumbling around pulling on the last of my clothes as the morning's lessons loom."

"One thing is different now, though."

stop sound fadeout 0.1
$ renpy.sound.set_volume(0.1, channel="ambiance", delay=0.5)
$ renpy.music.set_volume(0.2)
play ambiance2 "sfx/ambiance/outside.ogg" fadein 2.0
play music "music/touching.ogg" fadein 1.5
scene bg downtown park sepia:
    xalign 1.0
show snow sepia
show eileen_sepia outdoors_fists lookawaynarrow sadmouth blush at center:
    ypos 1.525
with flash
"Just thinking about what happened last night makes my heart race, but I have no idea what's supposed to happen after something like that."

"What happens when I see Eileen again? How close am I meant to be with her, now that we're going out?"

$ renpy.sound.set_volume(1.0)
scene cg act2 kiss after sepia with flash
"Then there's the kiss itself, playing over and over in my mind. The feeling of her soft lips on mine, the way she looked so flustered afterwards..."

stop music fadeout 0.1
stop ambiance2 fadeout 0.1
$ renpy.sound.set_volume(1.0, channel="ambiance", delay=0.5)
play sound "sfx/sack_drop.ogg"
scene bg aptallison livingroom
$camera_move(0,0,0,0,0,'dissolve')
with hpunch
allison "Ow!"

$ renpy.music.set_volume(1.0)
"A sharp pain from my shin brings me back into the real world, bending down to rub my poor leg revealing the cause to be walking into a chair. The feeling of embarrassment isn't helped by Rose looking over in concern."

show rose indoors_handonhip concerned normal at center
$ renpy.transition(dissolve, layer='master')
rose "You okay?"

stop sound fadeout 1.0
allison "It's nothing, just bumped my leg."

show rose indoors_handonhip puzzled at center
$ renpy.transition(dissolve, layer='master')
rose "Not sick or something are you? You're even more clumsy than usual today."

allison "I'm fine, just didn't sleep much last night."

show rose halfclosed at center
$ renpy.transition(dissolve, layer='master')
"It's times like this that normally being a morning person doesn't pay off. I shrug off her concern as best I can, distracting myself by throwing on my clothes to prepare for the chill outside."

show rose normal talking at center
$ renpy.transition(dissolve, layer='master')
rose "Just take it easy, alright? The ice is bad enough out there already."

stop ambiance fadeout 2.0
play sound "sfx/door_open2.ogg"
show rose weaksmile at center
$ renpy.transition(dissolve, layer='master')
allison "I will."

# Timeskip
play sound "sfx/door_close3.ogg"
window hide dissolve
scene black with midDissolve
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 1.0
scene bg aptallison road
show snow light
$camera_move(-3200,-1900,600,0,0,'dissolve')
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.07
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.655
with midDissolve
$camera_move(3200,-1900,600,0,30,'ease')

letterbox "The walk down the road towards campus does me good, giving time for my mind to settle and get back to the daily routine. Not everything is quite the same, though; my footsteps feel light, and what's typically an arduous walk feels unusually easy."

stop sound fadeout 1.0
letterbox "I'm not quite dancing in the streets, but the day feels just a little brighter than usual. It's nice."

letterbox "The snowfall's been getting heavier, now that it's December. I pass a few people standing outside buildings while looking mournfully at their roofs, plotting how to dislodge the snow piled on top. The traffic's also slowed to a crawl, rolling by carefully."

letterbox "Ads for Christmas sales on television are into full swing by now, which reminds me that I should get my shopping done when I have some free time. I think I can scrape together enough money to buy a little something for everyone in my family."

letterbox "Then there's Christmas cards for my new friends here, not to mention organizing a trip home for the break. Christmas is meant to be relaxing, but it feels like there's so much to organize for it."

play music "music/dozy_comfy.ogg" fadein 8.0
scene bg campus outskirts snow:
    xalign 0.0
show snow light
with fadeInOut
$ camera_reset()
window show dissolve

"Coming up to the campus, I try to focus my thoughts back onto school for the time being. Thankfully the paths here are better cleared, if nothing else."

show eileen outdoors_onhip lookaway grumble at left2:
    zoom 0.75 yoffset -200
    xzoom -1 xpos -0.05 alpha 0
    ease 2.0 xpos 0.25 alpha 1
"As students file in past the gate, my heart skips a beat as I recognize a particular blonde girl."

$camera_move(-2850,-450,680,0,5,'ease')
show eileen neutral normal at left2:
    xzoom -1 xpos 0.25 alpha 1
"She looks back and notices me as I skip up to meet her, her usual tired expression unwavering. I've never met someone so far from a morning person."

stop loopsfx fadeout 2.0
allison "'Morning!"

show eileen outdoors_crossed smile at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "Hey, Allison."

"With that, the both of us begin the walk in side by side."

show bg campus outskirts snow blurred2 as bg2 behind eileen:
    xalign 0.0 yalign 0.5 alpha 0
    ease 3.0 alpha 0.85
show shadow behind eileen:
    alpha 0.0
    ease 3.0 alpha 0.3
show eileen outdoors_fists lookawaynarrow angry at left2:
    xpos 0.25
$ renpy.transition(dissolve, layer='master')
"All thoughts of schoolwork leave my mind as I try to stop myself glancing at Eileen, furtively trying to work out exactly how I'm expected to act around her."

"The part where we admit we're interested in each other is also where most of the romance movies I've seen end, and I've never gone out with anyone before. Then there's the fact that neither of us has said a word to the other beyond a quick greeting."

"I try to comfort myself with the thought that it's probably the same for Eileen, too. It's always so hard to read her poker face."

scene bg campus outskirts snow
show snow light
show eileen outdoors_crossed closed open at offcenterleft:
    zoom 1.3 yoffset 300
    xzoom -1 xpos 0.45
with fadeInOut
$ camera_reset()
eileen "Good grief it's cold today."

show eileen narrow neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"She's not thinking at all about yesterday, is she?"

"With a long breath, it feels like all my restlessness leaves me. Eileen's relaxed attitude makes me feel embarrassed for getting so worked up after seeing her again."

show eileen normal at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "How are you so confident about this? You know, with us going out and everything?"

show eileen outdoors_onhip smile sad at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "I'm just really good at faking it."

"Hanging my head, I give up on ever trying to read her."

"The grin Eileen gives makes me feel better about today in an instant. Her normally cold demeanor - if just for a moment - is pierced by that sincere smile that peeks through."

show eileen outdoors_crossed lookaway angry at offcenterleft
$ renpy.transition(midDissolve, layer='master')
"A smile which soon evaporates collapsing into something else entirely."

allison "Is something wrong?"

show eileen outdoors_onhip narrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "I just remembered something troublesome."

show eileen lookawaynarrow at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Caprice..."

show eileen frown at offcenterleft
$ renpy.transition(dissolve, layer='master')
"I almost ask why before the obvious hits me. With my thoughts finally moving beyond the girl at my side, the implications of all this become clearer."

allison "Should we just tell her?"

show eileen outdoors_crossed closed neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "I'd rather not. You know Caprice as well as I do; I don't want her to make a fuss about us getting together."

show eileen outdoors_crossed frown narrow at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Then again, she'll probably work it out herself. She's not stupid."

allison "She knows to pay attention if I'm serious. Besides, is there really that much harm in letting her be happy for us?"

show eileen outdoors_fists disbelief neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"My serious tone in defense of Caprice seems to catch Eileen off guard. It catches me a little off guard, too."

show eileen narrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Fine. If you're going to tell her, then I want to be there too."

show eileen lookaway neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"The discussion comes to an end, yet I find myself not wanting to leave despite having nothing further to say in particular."

show eileen outdoors_onhip at offcenterleft
$ renpy.transition(dissolve, layer='master')
"It seems Eileen has the same problem as she awkwardly mills about, the chatting students passing around us only making the silence between us more pointed."

show eileen normal at offcenterleft
$ renpy.transition(dissolve, layer='master')
"Would it be okay to kiss her, here and now? Yesterday in the park, we did it without thinking. Eileen's always so awkward about physical affection that I'm not sure she'd like it, especially in public."

show bg campus outskirts snow blurred2 as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0
    ease 2.0 alpha 0.85
show white behind eileen:
    alpha 0.0
    ease 2.0 alpha 0.1
show eileen normal smile at offcenterleft:
    zoom 1.3 yoffset 300
    time 0.5
    ease 0.5 yoffset 305
    ease 0.5 yoffset 295
    ease 0.2 yoffset 300
    nod2
"What I'm thinking must've been plain to see as Eileen reaches down, placing her hand on top of my head and scruffing it around in response. It might be an odd way for her to show her feelings, but I can't say I hate the gesture."

"I feel my cheeks blushing as her hand rubs my head, enjoying every moment until she stops. Eileen's awkwardness around all this makes me feel a little better about my own uncertainty."

show bg campus outskirts snow blurred2 as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0.85
    ease 2.0 alpha 0
show white behind eileen:
    alpha 0.1
    ease 2.0 alpha 0.0
allison "Everything will work out fine, I'm sure of it."

show eileen closed open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Ever the optimist."

show eileen lookawaynarrow at offcenterleft:
    xzoom -1 xpos 0.45
    linear 0.7 xzoom 1 xpos 0.5
eileen "We'd better get to classes. See you at the club, I suppose."

stop music fadeout 4.0
stop ambiance fadeout 3.0
show eileen closed neutral at offcenterleft:
    xzoom 1 xpos 0.5 alpha 1
    ease 1.0 xpos 0.4 alpha 0
"She sure doesn't seem to share my optimism as she waves and walks off, nor my like of our new club. I'm sure she'll come around, though."

scene black with longDissolve
play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 2.0
scene bg buildingart hallway2f with midDissolve
"With the afternoon wearing on, I trudge up the familiar route to the second floor of the arts building. The sounds of raised voices come from up ahead, easily audible in the otherwise dead silent hallways."

"If I'm not mistaken, they're coming from the art room itself. Steeling myself for what's to come, I sigh and head on up to the door inside."

play sound "sfx/door_open2.ogg"
$ renpy.sound.set_volume(0.8, channel="ambiance", delay=0.5)
scene bg buildingart art dusk:
    xalign 1.0
show caprice indoors_behindback grumble normal angry at rightside:
    zoom 0.9 yoffset -80
    xpos 0.8
show eileen indoors_fists angry lookawaynarrow at leftside:
    alpha 0
show eileen indoors_fists angry closed at leftish as eileen2:
    zoom 0.9 yoffset -80
    xzoom -1 xpos 0.28
with smoothDissolve
"Eileen and Caprice have already arrived as usual, each standing on the opposite side of a table as they fume at each other."

play sound "sfx/door_close.ogg"
$ renpy.sound.set_volume(0.5, channel="ambiance", delay=0.5)
play music "music/questioning.ogg" fadein 1.0
$camera_move(500,250,350,0,1,'ease')
show caprice indoors_handonhip frown normal angry at rightside:
    xpos 0.8
show eileen indoors_crossed angry annoyed at leftish as eileen2:
    xzoom -1 xpos 0.28
"Their heads snap towards me in unison the moment the door rattles open, making my heart skip a beat."

allison "Yes...?"

show eileen indoors_onhip narrow open at left2 as eileen2:
    xzoom -1 xpos 0.28
    linear 0.7 xzoom 1 xpos 0.32
eileen "Help me talk some sense into this woman, please!?"

show eileen neutral at centerleft as eileen2:
    xzoom 1 xpos 0.32
show caprice indoors_pumped angry normal open at rightside:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
caprice "Just relax! As art club president, I have everything under control."

show eileen indoors_onhip narrow open at left2 as eileen2:
    xzoom 1 xpos 0.32
    linear 0.7 xzoom -1 xpos 0.28
eileen "Everything except the 'club' part."

show caprice indoors_handonhip angry half puffed at rightside:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
eileen "I mean, I would have thought a club needed things like official paperwork, an advisor, funding for supplies that haven't been pilfered from the real art classes..."

show eileen indoors_crossed annoyed angry at left2 as eileen2:
    xpos 0.28 yoffset -80
    ease 0.2 yoffset -85
    ease 0.2 yoffset -75
    ease 0.1 yoffset -80
eileen "Basically, more than an excited proclamation of a club existing!"

show caprice indoors_chintap angry normal opensmile at rightside:
    subpixel True
    xpos 0.8 yoffset -30
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "That's why I'm working on the posters!"

# Cutin of art club poster
show bg buildingart art dusk blurred2
show eileen indoors_crossed annoyed angry blur at left2 as eileen3:
    zoom 0.9 yoffset -80
    xzoom -1 xpos 0.28 yoffset -80
show eileen indoors_crossed frown narrow at left2 as eileen2:
    xzoom -1 alpha 0 xpos 0.28
show caprice indoors_chintap even normal neutral blur at rightside as caprice2:
    zoom 0.9 yoffset -80
    xpos 0.8 yoffset -30 rotate 0
show caprice indoors_chintap even normal neutral at rightside:
    alpha 0 xpos 0.8 rotate 0
$ renpy.transition(dissolve, layer='master')
show misc cutins postermulti:
    subpixel True
    zoom 0.8 xcenter 0.54 ycenter -0.2
    ease 1.5 ycenter 0.43
"Feeling sorry for the heavily sighing Eileen, my eyes drift to said posters lying on the table between them."

"I walk over and tentatively take a look at the one sitting on top, its sharp graphics and color scheme catching the eye."

show misc cutins postermulti:
    subpixel True
    zoom 0.8 xcenter 0.54 ycenter 0.43
    ease 1.5 ycenter -0.2
pause 1.0
show bg buildingart art dusk
show eileen indoors_crossed frown narrow at left2 as eileen2:
    alpha 1 xpos 0.28
show caprice indoors_chintap even normal neutral at rightside:
    alpha 1 xpos 0.8 rotate 0
hide eileen3
hide caprice2
$ renpy.transition(dissolve, layer='master')
allison "They do look nice."

show caprice indoors_pumped grin closedhappy raised at rightside:
    xpos 0.8 yoffset -30
    easein .15 yoffset -48
    easeout .175 yoffset -30
    easein .15 yoffset -38
    easeout .175 yoffset -30
caprice "See? People will love 'em!"

"I may say that, but it's a little obvious this is out of her comfort zone when it comes to art. Her sketching is always nice, but her work with paints comes off as a little crude. Still, trying new things is to be praised."

hide misc cutins postermulti
show eileen indoors_onhip closed open at left2 as eileen2:
    xpos 0.28
$ renpy.transition(dissolve, layer='master')
eileen "Think about this logically. It's nearly Christmas; all the students are going to be on break soon. Even if they weren't, nobody would be looking for a club to join around now anyway."

show eileen disbelief neutral at left2 as eileen2:
    xpos 0.28
show caprice indoors_chintap raised normal pout at rightside:
    xpos 0.8 yoffset -30
$ renpy.transition(dissolve, layer='master')
caprice "I wouldn't exactly say that."

show caprice indoors_wave grin half raised at rightside:
    xpos 0.8 yoffset -30
    nod2
$ renpy.transition(vpunch, layer='master')
"Caprice is quick on the draw as she leans over and latches onto my shoulder, beaming a smug look of victory at her opponent. I feel like I've been reduced to a useful prop in an argument... but Caprice isn't wrong."

show caprice indoors_behindback neutral even at rightside:
    xpos 0.8 yoffset -30
show eileen indoors_crossed frown narrow at left2 as eileen2:
    xpos 0.28
$ renpy.transition(dissolve, layer='master')
"Eileen looks physically pained as she groans in frustration. She did walk right into that one."

stop music fadeout 4.0
$camera_move(0,0,0,0,3,'ease')
show caprice indoors_behindback normal at rightside:
    xpos 0.8 yoffset -30
show eileen closed at left2 as eileen2:
    xzoom -1 xpos 0.28 alpha 1
    linear 0.7 xzoom 1 xpos 0.32
    ease 2.0 xpos 0.1 alpha 0
"In what could only be interpreted as the universal sign of giving up, she shakes her head and starts to walk away, retreating to the cabinet to grab her things."

"It looks like posters will be the accomplishment of today as far as the club goes."

play music "music/whimsical_faster_m.ogg" fadein 4.0
scene bg buildingart art dusk blurred2:
    xalign 1.0
show eileen indoors_crossed frown narrow blur at centerleft:
    zoom 0.6 yoffset -350
    xpos 0.38
show caprice indoors_behindback neutral normal even at right2:
    zoom 1.4 yoffset 315
    xpos 0.75
$camera_move(600,-400,250,0,0,'dissolve')
with fadeInOut
allison "I suppose it doesn't hurt to try and draw in some more members."

show caprice indoors_pumped raised open at right2:
    xpos 0.75
$ renpy.transition(dissolve, layer='master')
caprice "Hopefully we can get 'em soon, too! I wanted to have another club outing, and the more the merrier."

show caprice indoors_chintap opensmile closedhappy raised at right2:
    xpos 0.75
    easein .15 yoffset 298
    easeout .175 yoffset 315
    easein .15 yoffset 308
    easeout .175 yoffset 315
caprice "And like I declared, we're going to make the pizza place a regular thing for the club!"

allison "I'm up for it."

scene bg buildingart art dusk:
    xalign 1.0
show eileen indoors_crossed narrow grumble at centerleft:
    zoom 0.6 yoffset -350
    xpos 0.38
show caprice indoors_chintap opensmile closedhappy raised blur at right2:
    zoom 1.4 yoffset 315
    xpos 0.75
$camera_move(600,-400,250,0,0,'dissolve')
with midDissolve
"Eileen looks drearily at the traitor to her cause, but knows her goose is cooked as she hangs her head. I swear she looks more tired than usual."

scene bg buildingart art dusk blurred2:
    xalign 1.0 yalign 0.5
show eileen indoors_crossed frown narrow blur at centerleft:
    zoom 0.6 yoffset -350
    xpos 0.38
show caprice indoors_pumped grin normal raised at right2:
    zoom 1.4 yoffset 315
    xpos 0.75
    time 1
    easein .15 yoffset 298
    easeout .175 yoffset 315
    easein .15 yoffset 308
    easeout .175 yoffset 315
$camera_move(600,-400,250,0,0,'dissolve')
with midDissolve
caprice "Then it's settled!"

show caprice indoors_behindback pout closedhappy raised at right2:
    xzoom 1 xpos 0.75 alpha 1
    linear 0.7 xzoom -1 xpos 0.7
    nod2
    # ease 1.2 xpos 1.2 alpha 0
"Caprice goes back to fussing over her posters, brushing off some specks of dust that've settled on the paint."

scene bg buildingart art dusk:
    xalign 1.0
show eileen indoors_crossed closed neutral at centerleft:
    zoom 0.6 yoffset -350
    xpos 0.38
show caprice indoors_behindback pout closedhappy raised blur at right2:
    zoom 1.4 yoffset 315
    xzoom -1 xpos 0.7
$camera_move(600,-400,250,0,0,'dissolve')
with smoothDissolve
$camera_move(-1500,-250,650,0,5,'ease')
"Taking advantage of the distraction, I look to Eileen."

show eileen indoors_crossed disbelief sadmouth at centerleft:
    xpos 0.38
$ renpy.transition(dissolve, layer='master')
"She grimaces as I pointedly flick my eyes back to our companion, plainly hoping to leave this for another day by her reaction."

show eileen indoors_fists lookawaynarrow sadmouth at centerleft:
    xzoom 1 xpos 0.38
    linear 0.7 xzoom -1 xpos 0.35
"Reluctantly, Eileen sets her paints down and plods back over like a child accepting their bitter medicine. In hindsight, perhaps she was trying to use her painting as an excuse to not deal with this."

"Caprice is one of my few friends, however; I'd feel bad hiding this from her. Even if we tried to, she'd just poke and poke until one of us eventually spilled the beans."

stop music fadeout 10.0
scene bg buildingart art dusk
show caprice indoors_chintap frown normal raised at right2
show eileen indoors_onhip lookaway grumble at left2:
    xzoom -1
with fadeInOut
$ camera_reset()
caprice "What's up with you two?"

allison "Caprice, there's something we need to tell you."

show eileen indoors_crossed lookawaynarrow open at left2
$ renpy.transition(dissolve, layer='master')
eileen "To make this absolutely clear, this does not leave the room. Do you understand?"

show eileen neutral at left2
show caprice indoors_pumped open wink raised at right2:
    bounce
caprice "Yes ma'am!"

show eileen narrow at left2
$ renpy.transition(dissolve, layer='master')
eileen "I'll bet..."

show caprice indoors_handonhip raised at right2
$ renpy.transition(dissolve, layer='master')
allison "Eileen and I have started- I mean, it just happened recently, but-"

show eileen indoors_onhip closed open at left2
$ renpy.transition(dissolve, layer='master')
eileen "We're going out."

show eileen neutral at left2:
    nod2
"I feel Eileen take my hand in hers. I worry for a second about the sweatiness of my palm, but feeling her hand closing around mine settles my nerves. I never realized how warm someone else's hand could feel."

show eileen indoors_onhip normal neutral at left2
$ renpy.transition(dissolve, layer='master')
"As her fingers tighten, I realize something else. Eileen's settling herself just as much as me."

show caprice pout normal raised at right2
$ renpy.transition(dissolve, layer='master')
caprice "Eh? Like, dating? So you guys are both...?"

show eileen indoors_crossed narrow at left2
$ renpy.transition(dissolve, layer='master')
eileen "Yeah."

$ renpy.music.set_volume(0.8)
play music "music/art_club_a.ogg" fadein 3.0
show caprice indoors_chintap open normal even at right2
$ renpy.transition(dissolve, layer='master')
caprice "Ooooooh."

"My guess that Caprice wouldn't go too wild turns out to be true, with even her surprise feeling a little exaggerated for effect."

show caprice indoors_behindback grin half raised at right2
$ renpy.transition(dissolve, layer='master')
caprice "Well then, aren't you glad you can do art together all the time now?"

show eileen indoors_onhip lookawaynarrow open at left2
$ renpy.transition(dissolve, layer='master')
eileen "Look, we don't need any help. Much less, help from you."

show eileen neutral at left2
show caprice indoors_pumped puffed normal sad at right2
$ renpy.transition(dissolve, layer='master')
caprice "But-"

show eileen narrow at left2
$ renpy.transition(dissolve, layer='master')
allison "It's alright, I appreciate what you've done. Just don't go too crazy helping things along, promise?"

show caprice indoors_pumped grin normal angry at right2:
    nod
play sound "sfx/door_open2.ogg"
caprice "Promise!"

$ renpy.sound.set_volume(0.8, channel="ambiance", delay=0.5)
wallace "Sounds like things are lively in here."

scene bg buildingart art dusk:
    xalign 1.0
$camera_move(2200,-250,680,0,0,'dissolve')
with dissolve
show wallace outdoors heightened halfopen neutral at rightedge:
    zoom 0.62 yoffset -300
    xpos 1.1
    ease 3.0 xpos 0.955
$camera_move(2800,-250,680,0,3,'ease')
stop sound fadeout 1.0
"Our gazes snap towards the doorway, Wallace strolling in with an expression more bored than in the least bit surprised. Eileen's hand lets go of mine, but the warmth remains as I reflexively feel my hand with the other to recount the sensation."

"I'm glad Eileen is a more collected person than I am, calmly playing off the interruption."

show millie outdoors_neutral even closedhappy neutral behind wallace at right2:
    zoom 0.62 yoffset -300
    xpos 1.08
    ease 1.5 xpos 0.775
"Just as she's about to greet him though, Millie slides around his large figure and into the room."

scene bg buildingart art dusk
show caprice indoors_wave opensmile normal raised at centerleft:
    zoom 0.85 yoffset -120
    xzoom -1 xpos 0.35
    time 1.5
    easein .15 yoffset -138
    easeout .175 yoffset -120
    easein .15 yoffset -128
    easeout .175 yoffset -120
show eileen indoors_onhip neutral normal at leftside:
    zoom 0.85 yoffset -120
    xzoom -1 xpos 0.14
show wallace outdoors neutral forward even at rightside:
    zoom 0.85 yoffset -120
    xpos 0.86
show millie outdoors_neutral even closedhappy neutral at centerright:
    zoom 0.85 yoffset -120
    xpos 0.62
with fadeInOut
$ camera_reset()
caprice "Millie, you're here!"

show millie outdoors_tented even normal speaking at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
millie "You're looking cheerful today. We just finished our own club work, so thought we'd pop by."

show wallace outdoors heightened open neutral at rightside:
    xpos 0.86
show millie neutral at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
allison "So you're in the writing club too, Wallace?"

show caprice indoors_chintap grin half raised at centerleft
show millie sad normal pout at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
caprice "Only for now."

show wallace outdoors frown halfsmall at rightside:
    xpos 0.86
show millie outdoors_neutral even closedhappy smile at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
wallace "Only until I graduate from this place. I'm not joining this club no matter how many times you ask."

show eileen indoors_crossed narrow angry at leftside:
    xpos 0.14
show caprice indoors_behindback grumble half angry at centerleft
$ renpy.transition(dissolve, layer='master')
eileen "You make it sound like being here is some horrible fate."

show wallace outdoors even closed neutral at rightside:
    xpos 0.86
show eileen indoors_onhip lookaway neutral at leftside:
    xpos 0.14
$ renpy.transition(dissolve, layer='master')
"I smile a little at Eileen suddenly finding some pride in the art club, now that someone's spoken against it."

show millie outdoors_tented raised normal speaking at centerright:
    xpos 0.62
$ renpy.transition(dissolve, layer='master')
millie "As for what I actually came here for: Hayley was wanting us to join her for take-out."

show millie outdoors_tented neutral at centerright:
    xpos 0.62
show caprice indoors_pumped opensmile normal raised at centerleft:
    xpos 0.35
    easein .15 yoffset -138
    easeout .175 yoffset -120
    easein .15 yoffset -128
    easeout .175 yoffset -120
caprice "Alright, take-out! Lead the way!"

show millie outdoors_neutral even closedsad smile at centerright:
    xpos 0.62
    time 0.5
    ease 0.5 yoffset -115
    ease 0.5 yoffset -125
    ease 0.2 yoffset -120
show caprice outdoors_handonhip neutral closedhappy raised at centerleft:
    xpos 0.35
    nod2
show wallace outdoors even forward neutral at rightside:
    xpos 0.86
$ renpy.transition(dissolve, layer='master')
"Millie gives us a polite wave goodbye as Caprice skips over to pick up her hoodie on the way out."

show millie outdoors_neutral even normal neutral behind wallace at centerright:
    xzoom 1 xpos 0.62
    linear 0.7 xzoom -1 xpos 0.58
    ease 1.55 xpos 1.2
show caprice outdoors_handonhip neutral closedhappy raised at centerleft:
    xpos 0.35
    time 1
    ease 0.8 xpos 0.58
"Unfortunately for Caprice, Eileen doesn't let her go so easily."

show eileen indoors_crossed disbelief open at leftside:
    xpos 0.14
$ renpy.transition(dissolve, layer='master')
eileen "And your club?"

show eileen neutral at leftside:
    xpos 0.14
show caprice outdoors_chintap frown normal raised at offcenterright:
    xzoom -1 xpos 0.58
    linear 0.7 xzoom 1 xpos 0.6
caprice "Uh..."

show caprice outdoors_pumped closedhappy grin at centerright:
    xzoom 1 xpos 0.6
    easein .15 yoffset -138
    easeout .175 yoffset -120
    easein .15 yoffset -128
    easeout .175 yoffset -120
caprice "Today's art club meeting is over! Good work everyone!"

stop music fadeout 5.0
show wallace outdoors heightened halfforward neutral at rightside:
    xpos 0.86
show eileen indoors_crossed closed angry at leftside:
    xpos 0.14
show caprice outdoors_wave grin closedhappy raised at centerright:
    xzoom 1 xpos 0.6
    linear 0.7 xzoom -1 xpos 0.58
    ease 1.2 xpos 1.2
"With a thumbs up from Caprice, the two disappear out the door and head off down the hallway. The three of us are left to our own devices after they leave."

scene bg buildingart art dusk
show wallace outdoors neutral open heightened at rightish
show eileen indoors_onhip neutral normal at left2:
    xzoom -1
with fadeInOut
"While I think Wallace to be a perfectly nice person, I'm still not really sure how to act around him. With Caprice no longer being the center of attention, that familiar self-consciousness I have around strangers flares up once again."

"It seems I'm not alone in not quite knowing what to say, Wallace and Eileen doing little more than awkwardly mill around. Given that they're good friends, it makes me think something is going on."

allison "Um-"

$ renpy.music.set_volume(1.0)
play music "music/relaxing.ogg" fadein 3.0
show eileen indoors_crossed lookaway open at left2
$ renpy.transition(dissolve, layer='master')
eileen "I've told her, Wallace. You don't need to keep your mouth shut any more."

show wallace outdoors mopen closed upturned at rightish
show eileen neutral at left2
$ renpy.transition(dissolve, layer='master')
"As he lets out a sigh of relief, it finally clicks."

show wallace outdoors neutral at rightish
$ renpy.transition(dissolve, layer='master')
allison "Wait, you knew about Eileen and I?"

show wallace outdoors even open frown at rightish
$ renpy.transition(dissolve, layer='master')
wallace "Eileen, yes. Not you, though."

show wallace outdoors heightened halfopen mopen at rightish
$ renpy.transition(dissolve, layer='master')
wallace "Going by the fact this didn't just become intensely awkward, I'm going to say things worked out?"

show wallace neutral at rightish
show eileen indoors_onhip normal at left2:
    nod2
"Eileen takes my opposite shoulder and shakes me lightly."

show eileen indoors_onhip narrow smile at left2
$ renpy.transition(dissolve, layer='master')
eileen "Seems so."

show wallace outdoors smile open upturned at rightish
$ renpy.transition(dissolve, layer='master')
wallace "Well, I'm happy for you two. Hope it works out."

allison "Thanks!"

show eileen indoors_crossed closed open at left2
$ renpy.transition(dissolve, layer='master')
eileen "Told you I'd find someone who could put up with me."

show wallace outdoors mopen halfopen even at rightish
show eileen lookaway angry at left2
$ renpy.transition(dissolve, layer='master')
wallace "That's not the kind of thing you should say about yourself."

show wallace outdoors frown open even at rightish
$ renpy.transition(dissolve, layer='master')
wallace "Guess I'll get out of your way, then. Just take things easy, okay?"

show eileen closed at left2
show wallace outdoors smile at rightish:
    xzoom 1 xpos 0.7
$ renpy.transition(dissolve, layer='master')
allison "We will."

show wallace outdoors closed at rightish:
    xzoom 1 xpos 0.7
    linear 0.7 xzoom -1 xpos 0.65
    ease 1.5 xpos 1.2
pause 1.5
$ renpy.sound.set_volume(0.5, channel="ambiance", delay=0.5)
play sound "sfx/door_close.ogg"
"We give each other our goodbyes before he leaves, his unmistakably large figure slowly disappearing down the orange-lit hallway."

show eileen indoors_onhip neutral normal at left2:
    xpos 0.225
    ease 1.2 xpos 0.45
"And then there were two."

allison "I thought you didn't want to tell anyone."

hide wallace
show eileen indoors_crossed lookawaynarrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Wallace is different. He's known I like girls since we were in high school."

show eileen closed at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "He's known I like you for a while now, too."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"I feel myself blush. The thought that Eileen talked to Wallace about me like that makes me smile."

show eileen indoors_onhip normal open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Suppose we'd better head home too, given the club meet's over."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "Guess so."

"It's an obvious invitation for us to leave together, but I find my feet stuck. I know I'll see her again tomorrow, but..."

show eileen indoors_crossed disbelief frown at offcenterleft:
    xzoom -1 xpos 0.45
    linear 0.7 xzoom 1 xpos 0.5
eileen "Something on your mind?"

allison "I don't really know how to phrase this, but... what happens now?"

show eileen indoors_onhip narrow at center:
    xzoom 1 xpos 0.5
$ renpy.transition(dissolve, layer='master')
"The expression she gives is one of genuine thought rather than judging me for being so lost. It's only now that I wonder if this is actually her first relationship or not; if it is, that makes my confusion a lot more embarrassing."

show eileen indoors_onhip lookaway open at center
$ renpy.transition(dissolve, layer='master')
eileen "That's up to you as much as it is me, you know."

show eileen indoors_crossed normal open at center
$ renpy.transition(dissolve, layer='master')
eileen "I guess school has got us for the week, but how about we go for a date on Saturday? Be good to get some use out of the car for once."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "Yes! That would be good!"

allison "I mean, uh... yes. Let's do that."

show eileen narrow at center
$ renpy.transition(dissolve, layer='master')
eileen "I can drive us, so just give a heads-up once you've worked something out."

"As I consider the prospect, I can see a little excitement from Eileen at the idea of going on our first date, though I doubt she's realised it herself."

stop music fadeout 6.0
stop ambiance fadeout 6.0
$camera_move(-500,0,300,0,6,'ease')
show bg buildingart art dusk blurred2 as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0
    ease 5.5 alpha 0.9
show eileen indoors_onhip disbelief open at center:
    subpixel True
    zoom 1.0 xpos 0.5
    ease 6.0 zoom 1.2 ypos 1.3 xpos 0.48
"As silence settles in the room, I see my chance."

eileen "Allison?"

# Handhold insert CG
$ renpy.music.set_volume(0.4)
play music "music/touching.ogg" fadein 1.5
scene black with vpunch
scene bg buildingart art dusk blur
show misc cutins hands:
    zoom 0.95 xalign 0.5 yoffset 2
with longDissolve
$ camera_reset()
"Taking Eileen's hands in mine and raising myself to my toes, I close my eyes and let my chin push forward. My heart feels to stop for a fleeting moment, my lips gently pressing to Eileen's as our hands intertwine."

"As our lips part and I come back down, my heart makes up for lost time. Come to think of it, I guess that's the first time I've ever kissed somebody myself. I have to admit, the physical side of us being together is nice, even if it is awkward."

"I can't help but feel the sensation lingering despite the moment having passed, filling me with warmth. Even Eileen, so normally placid and stoic, looks flushed. The two of us end up standing around like complete dorks, the only sound being the trees rustling outside."

# End insert
$ renpy.sound.set_volume(1.0, channel="ambiance")
scene bg buildingart art dusk
show eileen indoors_onhip lookawaynarrow  sadmouth blush at center
with dissolve
allison "I've been wanting to do that since this morning."

show eileen narrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "I swear you're getting bolder by the day."

show eileen smile at center:
    nod2
"With a gentle smile, Eileen reaches over and rubs my hair."

stop music fadeout 5.0
$ _dismiss_pause = False
"Even if I still don't quite know how to react when she does so, I can feel my head leaning into it and a dumb grin spreading on my face."

$ renpy.music.set_volume(1.0, delay=4.0)
window hide dissolve
scene black with longDissolve
return
