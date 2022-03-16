label scene_1S7_en:
######################
# Act 1, Scene 7

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg downtown pizzeria HD sketch
$camera_move(2000,-2000,0,0,0,'dissolve')
with inkfade
play ambiance "sfx/ambiance/crowd_cafe.ogg" fadein 5.0
scene bg downtown pizzeria HD
$camera_move(2000,-2000,0,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

play music "music/diner_2_m2.ogg" fadein 3.0
show caprice indoors_pumped raised closedhappy grin at center:
    xzoom -1
    zoom 0.68 yoffset -450
    xpos 0.485
    time 0.5
    easein .15 yoffset -468
    easeout .175 yoffset -450
    easein .15 yoffset -458
    easeout .175 yoffset -450
show eileen indoors_onhip normal neutral at rightish:
    xzoom 1
    zoom 0.68 yoffset -450
    xpos 0.72
show wallace indoors even open neutral at rightedge:
    zoom 0.68 yoffset -450
    xpos 0.95
with dissolve
voice "Caprice_Wallace1.ogg"
caprice "Wallace! It's nice to see you again. How's it going?"

show wallace heightened halfopen at rightedge
$ renpy.transition(dissolve, layer='master')
voice "Wallace_No2.ogg"
wallace "I'm not joining this club thing, if that's what you're thinking."

show eileen indoors_onhip closed neutral at rightish:
    xpos 0.72
show caprice indoors_chintap raised normal grumble at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Caprice_ComeOooon2.ogg"
caprice "But..."

show wallace closed mopen at rightedge
$ renpy.transition(dissolve, layer='master')
wallace "Word on the street was that pizza was involved."

show wallace neutral at rightedge
show eileen indoors_crossed narrow grumble at rightish:
    xpos 0.72
show caprice indoors_behindback even half puffed at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble2.ogg"
eileen "Besides, I don't think I can deal with the both of you without some backup."
voice "Allison_NervousLaugh.ogg"
allison "I'm not that much trouble, am I?"

show wallace open neutral at rightedge
show eileen indoors_crossed closed open at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
eileen "Remind me who persuaded me into agreeing to this, again?"

show caprice indoors_handonhip even wink grin at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
caprice "She's got a point."

show eileen lookaway neutral at rightish:
    xpos 0.72
$ renpy.transition(dissolve, layer='master')
"You're the last person who should be agreeing with her..."

scene bg downtown pizzeria
$camera_move(3800,-600,700,0,0,'dissolve')
with fadeInOut
play sound "sfx/chair_scrape_fast.ogg"
$camera_move(-3800,-600,700,0,15,'ease')
"Smiling and sitting back in the old wooden chair, I take a look about the noisy room."

"Everyone inside must be thankful for the heat being turned up, the weather outside having been freezing before we entered. There's a certain charm to the restaurant given its exposed aging brick walls and wooden furniture, however hard it may be."

"It takes a bit of speaking up for us to hear each other over the busily chatting couples and groups around us, but like dad said, the more people at a restaurant, the better the food will be."

stop sound fadeout 1.0
scene bg downtown pizzeria
$camera_move(-2750,-480,500,0,0,'dissolve')
show wallace indoors even forward neutral at leftside:
    zoom 0.9 yoffset -80
    xzoom -1 xpos 0.18
show eileen indoors_onhip lookawaynarrow frown at center:
    zoom 0.9 yoffset -80
    xpos 0.525
show caprice indoors_behindback even normal neutral at rightside:
    zoom 0.9 yoffset -80
    xpos 0.84
with fadeInOut
"I notice Eileen eyeing Wallace's beer in an unsubtle manner, the large glass perspiring away like in a commercial. I'd taken his apparent age as just his beard making him look older, but I guess he really does have a few years on us."

show eileen sad frown at center:
    xpos 0.525
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "Man, I miss beer. It'd go so well with this."

show wallace heightened halfforward smile at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
wallace "Here I was thinking you were far too uptight to do something like underage drinking."

show eileen indoors_crossed disbelief open at center:
    xpos 0.525
$ renpy.transition(dissolve, layer='master')
eileen "Remember the trip to Europe me and my family took last year? You think I just drank soda over there?"

show eileen indoors_crossed disbelief neutral at center:
    xpos 0.525
show wallace indoors even open frown at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
wallace "Well..."

show caprice indoors_behindback raised closedhappy neutral at rightside:
    xpos 0.84
show eileen narrow open at center:
    xpos 0.525
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Seriously1.ogg"
eileen "I was in Munich, Wallace. I mean, really."

$camera_move(0,0,0,0,4,'ease')
"Caprice and I can only smile at her little lecture."

show eileen narrow neutral at center:
    xpos 0.525
show caprice indoors_chintap even wink open at rightside:
    xpos 0.84 yoffset -30
    ease 1.0 rotate -5
    ease 1.0 rotate 0
voice "Caprice_Laugh2.ogg"
caprice "Don't be sad, Eileen; it's only a couple more years! Then you can drink all you want!"

show wallace heightened forward neutral at leftside:
    xpos 0.18
show caprice closedhappy neutral at rightside:
    xpos 0.84 rotate 0
show eileen indoors_onhip annoyed frown at center:
    xzoom 1 xpos 0.525
    linear 0.7 xzoom -1 xpos 0.485
"The look of pure and unrelenting disdain Eileen gives her at being reminded of the wait goes gleefully ignored, which is probably for the best."

show wallace even open neutral blur at leftside:
    xpos 0.18
show eileen normal neutral blur at center:
    xzoom -1 xpos 0.485
show caprice indoors_behindback raised normal open blur at rightside:
    xpos 0.84
show bg downtown pizzeria blurred2
$ renpy.transition(midDissolve, layer='master')
show misc cutins pizzas:
    xalign 0.5 yoffset -600
    ease 1.5 yoffset -50
"Our chatter is interrupted by the arrival of a waiter, a weedy young man clad in a plain red and black uniform. It's impressive how well he maneuvers all our pizzas and sides onto the table, all our mouths watering as they steam away."

"With a curt 'please enjoy', he leaves us to our feast."

show misc cutins pizzas:
    xalign 0.5 yoffset -50
    ease 1.5 yoffset -600
with None
show bg downtown pizzeria
$ renpy.transition(dissolve, layer='master')
pause 0.5
show wallace indoors even closed smile at leftside:
    xpos 0.18
show eileen indoors_onhip normal open at center:
    xzoom -1 xpos 0.485
show caprice indoors_behindback raised normal open at rightside:
    xpos 0.84
with midDissolve
eileen "Damn, they're fast here."

show eileen neutral at center:
   xpos 0.485
show caprice indoors_pumped closedhappy at rightside:
    xpos 0.84 yoffset -30
    easein .15 yoffset -48
    easeout .175 yoffset -30
    easein .15 yoffset -38
    easeout .175 yoffset -30
voice "Caprice_Exactly.ogg"
caprice "Best pizza place in the city!"

show wallace indoors even open smile at leftside:
    xpos 0.18
show eileen indoors_crossed lookawaynarrow smile at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh4.ogg"
eileen "How many have you actually tried?"

show eileen neutral lookaway at center:
   xpos 0.485
show caprice indoors_behindback raised closedhappy grin at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
caprice "Doesn't matter, since I've already tried this place."

show caprice indoors_behindback even opensmile at rightside:
    xpos 0.84
    ease 0.5 yoffset -25
    ease 0.5 yoffset -35
    ease 0.2 yoffset -30
"She says, busily shoving a slice of pizza into her mouth. Eileen starts on hers, but mine catches the eye of Wallace."

show eileen normal neutral at center:
   xpos 0.485
show caprice indoors_behindback neutral normal even at rightside:
    xpos 0.84
show wallace indoors frown halfopen even at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
voice "Wallace_Huh.ogg"
wallace "Vegetarian? You're not a leaf-eater, are you?"

"He says this with genuine concern in his voice."

allison "I just like the taste."

show wallace indoors neutral open even at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
"The answer satisfies him as he goes to work on his own. The fact it's a meat-lover's pizza is less than surprising."

show eileen indoors_onhip lookaway open at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
eileen "Think you can take the wallet hit for tonight?"

show eileen indoors_onhip lookaway neutral at center:
   xpos 0.485
show caprice indoors_wave even wink grin at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
voice "Caprice_Yeah2.ogg"
caprice "No problem."

show caprice grumble closedhappy raised at rightside:
    xpos 0.84
    ease 0.5 yoffset -25
    ease 0.5 yoffset -35
    ease 0.2 yoffset -30
voice "Caprice_Uuh1.ogg"
caprice "Yeah, no problem."

show wallace indoors neutral closed upturned at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
"It's a little sad how obviously she's trying to convince herself of the fact. The only reason I'm not having a quick check myself is because I budgeted the trip days in advance, and even Wallace looks like he's doubting himself a little."

show wallace upturned forward mopen at leftside:
    xpos 0.18
show caprice indoors_behindback even normal grumble at rightside:
    xpos 0.84
show eileen indoors_onhip normal neutral at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Wallace_Sigh7.ogg"
wallace "Such is life of a struggling college student."

show wallace upturned forward neutral at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
voice "Allison_Sigh2.ogg"
allison "Sure is. I really need to get a job."

show wallace heightened open neutral at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
wallace "You don't have one either?"

allison "I'm planning to get one."

show wallace indoors neutral open even at leftside:
    xpos 0.18
show eileen indoors_crossed narrow open at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "And when will you?"
voice "Allison_HuhAndUm.ogg"
allison "...Soon."

show eileen closed open at center:
   xpos 0.485
show caprice even normal neutral at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"Eileen just grimaces. She got me."

show eileen closed neutral at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
allison "How's working at the store, Wallace?"

show wallace indoors neutral closed even at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
wallace "Not exactly riveting, but it's a living."

show eileen indoors_onhip lookaway angry at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
"As I turn to Eileen, she just shrugs as she pulls out another slice."

show wallace indoors neutral forward even at leftside:
    xpos 0.18
show caprice raised half neutral at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
eileen "No job, and no excuse like studying. Guess I'm a slacker like Caprice."

"Given her apartment, it's a surprise that she could afford to live in that area and pay her tuition at the same time."

"I have to admit, I am envious of how she seems to have her life together. I've never met someone so independent, yet doing such a good job at it."

show wallace indoors neutral halfopen heightened at leftside:
    xpos 0.18
    easein 0.5 yoffset -75
    easeout 0.2 yoffset -85
    easeout 0.2 yoffset -80
"Wallace momentarily bringing his phone up to check the time spurs Caprice into action."

$camera_move(3050,200,600,0,4,'ease')
play sound "sfx/rustle-clothes.ogg"
show eileen indoors_onhip lookawaynarrow frown at center:
   xpos 0.485
show wallace indoors neutral forward heightened at leftside:
    xpos 0.18
show caprice indoors_chintap even normal pout at rightside:
    xpos 0.84
    nod2
    repeat 3
"Her twisting about in her seat and fussing around with her coat draped over the back takes everyone's attention."
voice "Allison_Caprice1.ogg"
allison "Caprice?"

"She finally rights herself after a few moments, her own phone proudly in hand."

stop sound fadeout 1.0
show caprice indoors_handonhip raised closedhappy grin at rightside:
    xpos 0.84
    easein .15 yoffset -48
    easeout .175 yoffset -30
    easein .15 yoffset -38
    easeout .175 yoffset -30
$camera_move(0,0,0,0,3,'ease')
caprice "Let's exchange phone numbers! As a club, we have to stay in contact."

show eileen indoors_onhip closed frown at center:
   xpos 0.485
show caprice indoors_behindback even closedhappy neutral at rightside:
    xpos 0.84
show wallace even halfsmall frown at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
"I quickly turn to grab my phone, while Caprice tries to talk a very reluctant Wallace into going along with her plan. His dreary look makes me feel a little sorry for him, especially as he cracks and gives up."

show wallace upturned closed mopen at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
"At least she and I are already sorted; it wasn't long after we met that Caprice asked to exchange contact details with me. I take my phone in hand and look to Eileen instead, who looks up from eating with little interest."

allison "Don't want to?"

$ renpy.music.set_volume(0.0, delay=12.0)
show wallace even forward neutral at leftside:
    xpos 0.18
show eileen indoors_crossed narrow frown at center:
   xpos 0.485
show caprice indoors_behindback raised normal frown at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"She just shrugs. I feel myself deflate a little from the excitement of earlier, having overestimated how close we'd managed to become."

show eileen indoors_crossed narrow open at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "I don't really use it much."

show eileen indoors_crossed lookaway grumble at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
"Reading the room as she glances about, she reluctantly pulls out an ancient-looking flip phone. I can't help but stare in stunned silence at such a relic."

show wallace heightened halfforward neutral at leftside:
    xpos 0.18
show eileen indoors_fists sad neutral at center:
   xpos 0.485
show caprice indoors_behindback raised normal flat at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh2.ogg"
eileen "It's not that weird, is it? I just never had a use for a fancy one."

show caprice indoors_chintap puffed half even at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
voice "Caprice_Hmm1.ogg"
caprice "It's definitely weird. I was gonna try to get everyone on this group messaging app, too!"

show eileen lookawaynarrow frown at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
eileen "What's wrong with calling? You know, that thing phones were made for?"

show shadow:
    alpha 0
    ease 1.0 alpha 0.4
show eileen indoors_onhip closed frown at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
"Thoughts I had of possibly messaging Eileen start to vanish. I can't imagine her actually wanting to text anyone with that thing, and even the idea of calling somebody fills me with anxiety."

"As for Eileen, I think I might have inadvertently disappointed her by not tempering Caprice's reaction."

"With a quiet falling over the table, we end up concentrating on our cooling pizza rather than our phones."

$ renpy.music.set_volume(1.0, delay=5.0)
show shadow:
    alpha 0.4
    ease 1.0 alpha 0
show caprice indoors_pumped raised closedhappy grin at rightside:
    xpos 0.84
    easein .15 yoffset -48
    easeout .175 yoffset -30
    easein .15 yoffset -38
    easeout .175 yoffset -30
caprice "So? I was right, right? Best pizza place?"

show wallace even closed smile at leftside:
    xpos 0.18
show caprice indoors_handonhip even normal neutral at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"At least Caprice's endless enthusiasm and bright nature come in useful sometimes, the mood instantly lifting."

show eileen indoors_crossed normal open at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble3.ogg"
eileen "You were right."

show eileen indoors_crossed normal neutral at center:
   xpos 0.485
show wallace even open smile at leftside:
    xpos 0.18
show caprice indoors_handonhip even wink neutral at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"Wallace gives a thumbs up as he tries to grab some cheese coming off the slice he's working on."

allison "They don't skimp on the toppings, do they?"

$camera_move(3050,-450,600,0,4,'ease')
show caprice indoors_wave raised closedhappy grin at rightside:
    xpos 0.84 yoffset -30
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "Alright! Listen up everybody! My first executive decision as club president: coming here is now a regular event!"

show wallace even forward neutral at leftside:
    xpos 0.18
show eileen narrow at center:
   xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_No1.ogg"
eileen "Don't try your luck. You've got my art room and a warm body for the numbers you needed. That's it."

show caprice indoors_behindback even half pout at rightside:
    xpos 0.84 rotate 0
$ renpy.transition(dissolve, layer='master')
voice "Caprice_Eileen4.ogg"
caprice "So cold."
voice "Allison_SoftLaugh.ogg"
allison "I'll come here with you, don't worry."

show caprice indoors_chintap angry normal open at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
caprice "See, Allison's a true friend!"

$camera_move(2750,-480,500,0,1,'ease')
play sound "sfx/chair_scrape_fast.ogg"
show caprice indoors_behindback even closedhappy neutral at rightside:
    subpixel True
    zoom 0.9 yoffset -30
    xpos 0.84
    ease 1.0 zoom 0.95
show eileen indoors_crossed lookaway neutral at center:
    zoom 0.9 yoffset -80
    xpos 0.485
    ease 1.0 xoffset -20
show wallace even closed neutral at leftside:
    zoom 0.9 yoffset -80
    xpos 0.18
    ease 1.0 xoffset -20
"She slips her arm around mine and pulls us together tightly. Not knowing how I should react, I end up nervously smiling while feeling myself flushing from the contact. I guess I'm just happy to hear her call me a friend."

show eileen indoors_onhip closed smile at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
eileen "Least you've got Caprice with you as company during the day. For better or worse."

stop sound fadeout 1.0
show caprice indoors_handonhip grin half raised at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
caprice "C'mon, Eileen, you're not jealous, are you? You and I can hang out at the club all the time now too!"

show eileen indoors_onhip narrow frown at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble5.ogg"
eileen "Are you trying to make me reconsider it?"

play sound "sfx/chair_scrape_fast.ogg"
show caprice indoors_behindback even normal grumble at rightside:
    subpixel True
    zoom 0.95 yoffset -30
    xpos 0.84
    ease 1.0 zoom 0.9
show eileen narrow frown at center:
    zoom 0.9 yoffset -80
    xpos 0.485 xoffset -20
    ease 1.0 xoffset 0
show wallace even forward neutral at leftside:
    zoom 0.9 yoffset -80
    xpos 0.18 xoffset -20
    ease 1.0 xoffset 0
"Caprice satisfies herself with pouting as she takes a big bite from her pizza. Eileen might've agreed to the club, but I do wonder if the two will ever really get along. It's probably for the best that I'll be around to mediate."

"I'm glad things turned out this way, in the end. Something about Eileen feels different from my high school friends, or Caprice; every time we become a little closer feels like a small victory."

stop sound fadeout 1.0
show caprice neutral at rightside:
    xpos 0.84
show eileen normal neutral at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
"As Caprice grins at me, I realize that I'm smiling widely. I guess things really did turn out well."

show caprice indoors_chintap even half neutral at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
caprice "Hey, Eileen?"

show eileen indoors_crossed disbelief open at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
eileen "Yes...?"

show eileen neutral at center:
    xpos 0.485
show caprice closedhappy at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
caprice "How do you say cheers in Germany?"

show eileen indoors_onhip lookaway open at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
eileen "Usually 'prost'. Why?"

show eileen lookawaynarrow frown at center:
    xpos 0.485
show caprice indoors_handonhip grin closedhappy raised at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"She looks suspicious until Caprice raises her glass of lemonade. The other side of the table groans loudly but I've already begun to lift my glass in preparation, now left awkwardly dangling it midair."

show wallace heightened halfforward frown at leftside:
    xpos 0.18
show eileen narrow frown at center:
    xpos 0.485
$ renpy.transition(dissolve, layer='master')
eileen "We're not doing this."

show caprice indoors_pumped normal opensmile at rightside:
    xpos 0.84
    easein .15 yoffset -48
    easeout .175 yoffset -30
    easein .15 yoffset -38
    easeout .175 yoffset -30
caprice "C'mon! This is a celebration, right?"

$camera_move(-2750,-480,500,0,3,'ease')
show caprice indoors_pumped closedhappy neutral at rightside:
    xpos 0.84
show eileen indoors_crossed disbelief open at center:
    xzoom -1 xpos 0.485
    linear 0.7 xzoom 1 xpos 0.525
eileen "Wallace, help me out here."

show eileen indoors_crossed disbelief frown at center:
    xzoom 1 xpos 0.525
show wallace heightened closed mopen at leftside:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
"Wallace pauses, a piece of pizza hovering before his mouth. His dreary stare-down makes it clear that he's here for pizza alone, and not having a bar of this."

$camera_move(0,0,0,0,3,'ease')
pause 3.0
show eileen indoors_onhip closed frown at center:
    xpos 0.525
show wallace heightened forward neutral at leftside:
    xpos 0.18
show caprice indoors_chintap half grin at rightside:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"A disappointed Eileen lets it drop, the neutral party going back to his meal."

caprice "You're still here celebrating, though! See, Allison's in for it!"

"Well that's one way to drag me into this. All I can do is awkwardly smile in apology as the others grimace."

scene cg act1 clubtoast
$camera_move(2850,400,850,0,0,'dissolve')
with fadeInOut
"While they might hesitate to follow our diminutive new leader, Wallace and Eileen begrudgingly lift their glasses in solidarity with me. Even if her enthusiasm might not be matched, there is some sense of camaraderie between us all."

"As I raise my glass, I realize that a familiar feeling is no longer weighing me down. For the first time in a long while, I don't feel the unease of loneliness."

"In the end, maybe that's enough for me to toast this new club, and the friends in it."

stop music fadeout 4.0
$camera_move(0,0,0,0,4,'ease')
pause 4.0
caprice "To our new art club! Prost!"

$ _dismiss_pause = False
everyone "Prost!"

stop ambiance fadeout 3.0
window hide dissolve
scene black with longDissolve
stop sound fadeout 1.0
return
