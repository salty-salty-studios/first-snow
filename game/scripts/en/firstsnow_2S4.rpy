label scene_2S4_en:
######################

stop music fadeout 2.0
scene bg texture with menuFade
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg aptallison road sketch
$camera_move(3500,-1500,800,0,0,'dissolve')
with inkfade
scene bg aptallison road dusk
$camera_move(3500,-1500,800,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

$ renpy.sound.set_volume(1.5, channel="ambiance")
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 1.0
"The streetlights lead us along as we walk along the snow-dusted street, their pinpricks of light piercing the evening's darkness."

$ renpy.music.set_volume(0.5)
play music "music/night_2.ogg" fadein 4.0
scene bg aptallison road dusk
$camera_move(0,0,0,0,0,'dissolve')
show eileen outdoors onhip blurry at right2:
    zoom 1.3 yoffset 300
    xpos 0.8
with smoothDissolve
$camera_move(500,0,300,0,18,'ease')
"The two of us walk side by side without a word, the only sound being snow crunching underfoot. Far from the silence feeling oppressive, I'm rather glad that we don't need to fill the air with idle conversation."

"With our classes finished, I offered to repay her for the dinner she'd made for me. Hardly one to turn down a free meal, she readily accepted. It's not like that excuse to bring her over was a lie, as such. Or at least, that's what I tell myself."

show bg aptallison road dusk blurred4
$ renpy.transition(midDissolve, layer='master')
show eileen outdoors_onhip normal neutral at right2:
    zoom 1.3 yoffset 300
    xpos 0.8 alpha 0
    ease 1.0 alpha 1
"In truth, I want to be closer to Eileen. As I throw furtive glances to her, I muse about how the times we're together feel different to when I'm with others, her earnest yet clumsy attempts to help me feeling all the more rewarding."

"I'm not sure, but... I don't think these feelings are just friendship, any more."

scene bg aptallison road dusk
show eileen outdoors_onhip normal open at rightish
with fadeInOut
$ camera_reset()
voice "Eileen_Hmm2.ogg"
eileen "You're lucky to live so close to school."

show eileen neutral at rightish
$ renpy.transition(dissolve, layer='master')
voice "Allison_Sigh2.ogg"
allison "I still have no idea how you can hike all the way to your place every single day and not be exhausted."

show eileen outdoors_crossed narrow smile at rightish
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh2.ogg"
eileen "That's what happens when you don't wimp out of walking. Being fit has its advantages."

"While I stop myself from imagining how fit Eileen's body is, I'm reminded that she's seen my own body. I cringe in embarrassment as I remember modeling for her the other day, trying to shake off the feeling before she notices."

stop loopsfx fadeout 3.0
show eileen outdoors_crossed normal neutral at rightish:
    xpos 0.7
    ease 2.0 xpos 0.5
show bg aptallison outside dusk as aptallison_outside_dusk behind eileen with midDissolve
"Eventually we reach the now-familiar apartment building, the two of us stopping a moment."

"I'm a little surprised myself at how quickly I came to think of this place as home, the ill-maintained building feeling so foreboding at first."

"Everything here is so different to home, right down to the streetlights we stand under. Gone were the modern white lights of downtown and the suburbs, replaced by dull orange lamps which occasionally flickered."

show eileen outdoors_onhip lookaway neutral at center:
    xzoom 1 xpos 0.5
    linear 0.7 xzoom -1 xpos 0.45
voice "Allison_Um1.ogg"
allison "Well... here it is."

"I'm more than a little nervous about what she thinks of this new home after bringing her all the way here. Rather than judging me for it, she looks more to be carefully studying it. My nervous attempts to read her stoic gaze get me nowhere."

show eileen outdoors_onhip normal open at center:
    xzoom -1 xpos 0.45
    linear 0.7 xzoom 1 xpos 0.5
eileen "Looks nice."

show eileen outdoors_crossed narrow smile
$ renpy.transition(dissolve, layer='master')
eileen "So what's your roommate like, anyway?"

$ renpy.sound.set_volume(0.2)
play sound "sfx/body_prod.ogg"
stop music fadeout 3.0
show eileen outdoors_crossed frowning open at center:
    time 0.2
    ease 0.2 yoffset -50
    ease 0.2 yoffset 0
show rose outdoors_smoking normal smile behind eileen at centerright:
    xpos 0.65 alpha 0.0
    ease 0.3 alpha 1.0
"No sooner do the words leave her mouth, than she jumps from a hand latching tightly onto her shoulder."

show eileen outdoors_onhip disbelief angry at offcenterleft:
    xzoom 1 xpos 0.5 yoffset 0
    linear 0.5 xzoom -1 xpos 0.45
    xpos 0.45
    ease 1.0 xzoom -1 xpos 0.3
"I didn't even notice her in the darkness; she must've been having a smoke outside when she saw us."

stop ambiance fadeout 2.0
stop sound fadeout 1.0
show rose halfclosed smirk at centerright:
    alpha 1.0
$ renpy.transition(dissolve, layer='master')
voice "Rose_Hey1.ogg"
rose "Yo!"

scene black with midDissolve
$ renpy.sound.set_volume(1.0)
$ renpy.sound.set_volume(1.0, channel="ambiance")
$ renpy.music.set_volume(1.0)
play music "music/eileen_5_m.ogg" fadein 2.0
scene bg aptallison livingroom HD
$camera_move(-1050,-1000,-600,0,0,'dissolve')
show eileen indoors_crossed normal neutral at left2:
    alpha 0 xzoom -1 xpos 0.2
show eileen indoors_fists lookaway neutral at leftedge as eileen2:
    zoom 0.9 yoffset -220
    xzoom -1 xpos 0.065
with midDissolve
"As we sit at the dinner table, Eileen's gaze has trouble staying on us. I know those eyes well; they're those of a tourist, taking in everything around them while desperately trying to engrave it in memory. Or, perhaps, in order to judge my living conditions."

"I have to admit, this must look a bit shabby compared to her home. She's surely worked out that I'm not exactly well-off from the area already, though."

"Compared to Eileen's apartment, ours is full with the artifacts of life. A couple stuffed animals, some movie posters and DVDs around the place, an ageing console next to the television, and various bits and bobs accumulated through the years litter the room."

show eileen indoors_crossed closed neutral at leftedge as eileen2:
    xzoom -1 xpos 0.065
$ renpy.transition(dissolve, layer='master')
"Eileen's eyes pass over it all, but she stays unusually subdued. Perhaps the reason isn't the room itself, but the person sitting across from her."

show eileen open at leftedge as eileen2:
    xpos 0.065
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "So this is where you live, huh?"

allison "Sorry if it's a bit cold; the heating's having problems."

show eileen normal neutral at leftedge as eileen2:
    xpos 0.065
show rose indoors_handonhip normal neutral at right2:
    alpha 0 xpos 0.8
show rose indoors_handonhip halfclosed weaksmile at right2 as rose2:
    zoom 1.65 yoffset 400
$ renpy.transition(dissolve, layer='master')
voice "Rose_Heh1.ogg"
rose "You mean having problems as usual."

"There goes trying to put on a front."

show rose normal talking at right2 as rose2
$ renpy.transition(dissolve, layer='master')
rose "I know it doesn't look great from the outside, but we try to keep the place nice to live in. Fixing leaks, giving the place a lick of paint, patching holes, and all that. Gets Allison a crash-course in handywork, too."

show rose laugh at right2 as rose2
$ renpy.transition(dissolve, layer='master')
rose "It isn't much, but it's home. That's gotta count for something, right?"

show eileen indoors_onhip open at leftedge as eileen2:
    xpos 0.065
$ renpy.transition(dissolve, layer='master')
eileen "It does. You've done a good job on making this place homely."

show rose normal smile at right2 as rose2
show eileen indoors_onhip disbelief open at leftedge as eileen2:
    xzoom -1 xpos 0.065
    linear 0.7 xzoom 1 xpos 0.075
eileen "You never told me you were this good at science and math, Allison. No wonder it seems so easy for you."

show eileen neutral at leftedge as eileen2:
    xzoom 1 xpos 0.075
    nod2
show rose normal smile at rightedge as rose2:
    subpixel True
    xpos 0.775
    ease 4.0 xpos 0.95
$camera_move(-6550,-1000,-600,0,4,'ease')
"She gestures towards the trophy on the side-table and certificate on the wall above it, being awards from competitions I won in high school."
voice "Allison_HuhAndUm.ogg"
allison "You never asked."

show eileen indoors_crossed narrow at leftedge as eileen2:
    xpos 0.075
$ renpy.transition(dissolve, layer='master')
show rose halfclosed puzzled at centerright as rose2:
    subpixel True
    xpos 0.95
    ease 1.5 xpos 0.58
pause 1.0
voice "Rose_Allison2.ogg"
rose "What, seriously? Allison, c'mon."

show rose weaksmile at centerright as rose2:
    xpos 0.58 yoffset 400
    time 2.0
    ease 0.2 yoffset 410
    ease 0.2 yoffset 390
    ease 0.2 yoffset 400
show eileen lookaway smile at leftedge as eileen2:
    xzoom 1 xpos 0.075
    linear 0.7 xzoom -1 xpos 0.065
$camera_move(-3250,-1000,-600,0,3,'ease')
"I earn a playful clip over the head, Eileen snorting in amusement."

show rose normal smile at centerright as rose2:
    xpos 0.58
$ renpy.transition(dissolve, layer='master')
rose "She was good enough to get a science scholarship thanks to that brain of hers."

show eileen normal neutral at leftedge as eileen2:
    xzoom -1 xpos 0.065
$ renpy.transition(dissolve, layer='master')
"Never having been great at knowing how to respond to praise, I just hang my head. It feels a little embarrassing to be complimented in front of Eileen."

show rose neutral at centerright as rose2:
    xpos 0.58
show eileen indoors_onhip closed neutral at leftedge as eileen2:
    xzoom -1 xpos 0.065
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "Makes sense; she's got me out of a jam a few times now. She's a handy person to have around."

"I feel myself flower into a blush at the words, sinking lower into my chair as my face feels hot."

"I'm surprised how nice it feels, despite being so awkward. A smile spreads on my face as my legs sway beneath the table with unexpected energy. It feels different when it comes from Eileen."

scene bg aptallison livingroom
show eileen indoors_onhip normal open at left2:
    xzoom -1
show rose indoors_handonhip normal neutral at rightish
with fadeInOut
$ camera_reset()
voice "Eileen_Thanks1.ogg"
eileen "Thanks for the food, by the way."

show eileen neutral at left2
show rose normal smile at rightish
$ renpy.transition(dissolve, layer='master')
voice "Rose_YeahYeah.ogg"
rose "It's nothing. Nice to finally meet someone from Allison's side of the fence for a change, actually."

show rose smirk at rightish
$ renpy.transition(dissolve, layer='master')
rose "I was starting to get worried that she didn't have any friends."

show eileen disbelief at left2
$ renpy.transition(dissolve, layer='master')
"I can only bring my hand to my face as Eileen raises an eyebrow in pointed interest. I do wish Rose wouldn't make such a big deal out of my being shy."

show eileen indoors_crossed open at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "Really?"

show eileen neutral at left2
show rose normal laugh at rightish
$ renpy.transition(dissolve, layer='master')
rose "Not exactly the outgoing type, I guess."

show rose neutral at rightish
show eileen indoors_onhip lookawaynarrow angry at left2
$ renpy.transition(dissolve, layer='master')
eileen "I'm shocked."

play sound "sfx/mug-put-down.ogg"
show eileen closed angry at left2:
    nod
"She takes a large sip of the soda before her before continuing on."

show eileen normal open at left2
$ renpy.transition(dissolve, layer='master')
eileen "There's a few of us in her little circle now, no thanks to her dragging me into a club."

stop sound fadeout 1.0
show rose smile at rightish
show eileen neutral at left2
$ renpy.transition(dissolve, layer='master')
voice "Allison_Eileen6.ogg"
allison "You agreed to come! It's Caprice's club, anyway!"

show eileen indoors_crossed narrow smile at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh3.ogg"
eileen "Oh, so now you have nothing to do with it. This is a new story."

show eileen normal neutral at left2
$ renpy.transition(dissolve, layer='master')
"All I can do is grimace as Eileen lifts an eyebrow, getting the rise out of me that she wanted."

show rose halfclosed weaksmile at rightish
show eileen disbelief neutral at left2:
    nod2
"She softens the blow a little with a small nudge from her shoulder, earning a smile from Rose."

show rose normal neutral at rightish
show eileen indoors_onhip closed open at left2
$ renpy.transition(dissolve, layer='master')
"Eileen gives a mighty yawn, poorly hidden by a hand over her mouth. I don't think I've seen her bother trying to hide one before."

show eileen lookaway neutral at left2
$ renpy.transition(dissolve, layer='master')
eileen "Sorry."

allison "Tired?"

show eileen indoors_crossed narrow angry at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble2.ogg"
eileen "I'm always tired."

show rose talking at rightish
$ renpy.transition(dissolve, layer='master')
rose "What's with the bags under your eyes, anyway? Rough night?"

show eileen lookawaynarrow angry at left2
show rose neutral at rightish
$ renpy.transition(dissolve, layer='master')
eileen "Insomnia. It's fun stuff."

"Here I was trying to be tactful in not bringing that up, and Rose just kicks down the door as usual. That does give some context to Eileen's short fuse, though I shouldn't jump to conclusions."

show rose laugh at rightish
$ renpy.transition(dissolve, layer='master')
rose "Well, they say good, wholesome food can fix that. Hopefully this will pick you up a bit."

show eileen indoors_onhip narrow smile at left2
$ renpy.transition(dissolve, layer='master')
eileen "Nothing says homemade like burgers and fries, after all."

show eileen closed smile at left2
show rose smile at rightish
$ renpy.transition(dissolve, layer='master')
"As the two talk, I quietly begin on my food. I hadn't realized how empty I was, the fries disappearing into my mouth at a quick pace. Thank goodness for having a good metabolism."

show eileen normal neutral at left2
show rose halfclosed laugh at rightish
$ renpy.transition(dissolve, layer='master')
voice "Rose_Heh2.ogg"
rose "Someone's hungry."

"I look up quizzically at her, drawing a raised eyebrow. It's only now I realize my cheeks are as full as a chipmunk's."

show eileen indoors_crossed open at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "Good to see you two get along well."

show eileen neutral at left2
show rose normal smile at rightish:
    nod2
"Rose takes a hold of my shoulder and gives a playful shake, my head bobbing to and fro as I try to avoid choking on the fry on its way down."

show eileen lookaway at left2
show rose weaksmile at rightish
$ renpy.transition(dissolve, layer='master')
rose "Allison's fine. Quiet as a mouse, and manages to put up with my crap."
voice "Allison_NervousLaugh.ogg"
allison "Considering how much she takes care of chores and errands, I can't really complain."

stop music fadeout 5.0
show eileen normal at left2
show rose concerned at rightish
$ renpy.transition(dissolve, layer='master')
rose "You mean considering how nice of a person I am, right?"

allison "That too."

window hide dissolve
$ renpy.sound.set_volume(0.5, channel='loopsfx')
play ambiance "sfx/ambiance/tv.ogg" fadein 2.0
$ renpy.sound.set_volume(0.05)
play sound "sfx/dumptruck.mp3" fadein 1.0
scene bg aptallison livingroom HD
$camera_move(4400,-1050,-250,0,0,'dissolve')
show eileen indoors_onhip normal neutral at centerleft:
    zoom 0.84 yoffset -160
    xzoom -1 xpos 0.385
show rose indoors_handonhip normal neutral at rightedge:
    zoom 0.84 yoffset -165
    xpos 1.04
show bg aptallison livingroom table as livingroom_table2:
    xalign 0.5 yalign 0.5
show misc letterbox1 as lb1: 
    zoom 2.0 xcenter 0.5 ycenter -0.1
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.87
with fadeInOut

letterbox "The three of us munch away on our food, the quiet sound of cars outside and prattling from the television providing what little noise there is to be heard."

letterbox "It seems like Eileen is starting to settle, which is a relief. It took me a while myself when I first met Rose."

stop loopsfx fadeout 3.0
play music "music/whimsical_faster_m.ogg" fadein 5.0
scene bg aptallison livingroom blurred2:
    xalign 0.5 yalign 0.5
show eileen indoors_crossed lookawaynarrow open at left2:
    zoom 1.2 yoffset 200
    xzoom -1
show rose indoors_handonhip normal neutral at right2:
    zoom 1.2 yoffset 200
    xpos 0.74
with fadeInOut
window show dissolve
$ camera_reset()
$ renpy.sound.set_volume(1.0)

eileen "Surprised you two can keep your figures eating this kind of stuff. You don't have it often, do you?"

show eileen neutral at left2
show rose halfclosed at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
"Rose and I share a quick glance."

$ renpy.sound.set_volume(1.0, channel='loopsfx')
show rose talking at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
voice "Rose_No.ogg"
rose "No. Not at all."

show rose neutral at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
allison "Not often. Just special events."

show eileen narrow at left2
$ renpy.transition(dissolve, layer='master')
"There we go, falling afoul of Eileen's judgment."

show eileen indoors_onhip closed open at left2
$ renpy.transition(dissolve, layer='master')
eileen "Should just get a rice cooker. Buy rice in bulk, grab some vegetable packets, throw them together. Easy, cheap, healthier than take-out."

show eileen normal neutral at left2
show rose halfclosed puzzled at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
voice "Rose_Hm.ogg"
rose "I have to admit, it was nice when I dated a guy who could cook..."

show eileen indoors_onhip disbelief open at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "Having her around doesn't make things too awkward when you bring guys over?"

show eileen neutral at left2
show rose normal weaksmile at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
rose "You learn to be quiet."

show eileen indoors_crossed closed open at left2
$ renpy.transition(dissolve, layer='master')
eileen "I guess you would."

show eileen normal neutral at left2
show rose neutral at right2:
    xpos 0.74
show eileen neutral at left2
$ renpy.transition(dissolve, layer='master')
"I frown at the both of them."
voice "Allison_Hm4.ogg"
allison "I don't want to hear about this."

show eileen indoors_onhip frown at left2
show rose smirk at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
rose "If you didn't know already, that means I've been doing a good job."

"Rose's comment only causes my frown to deepen. I can feel myself blushing just from the topic of conversation, which just embarrasses me more."

show rose halfclosed at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
rose "Besides, if you ever get a boyfriend, you're going to have to learn too if you want to bring him around here."

allison "I won't be doing anything like that!"

show rose laugh at right2:
    xpos 0.74
show eileen lookaway smile at left2
$ renpy.transition(dissolve, layer='master')
voice "Rose_Laugh2.ogg"
"Rose laughs, and even Eileen looks amused. I sulk, hating that the attention has been centered on me now. I especially don't want this kind of conversation around Eileen. Thankfully, Rose seems content with her teasing."

show rose normal talking at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
rose "So, what's your story? You're a friend of Allison's, right?"

show rose neutral at right2:
    xpos 0.74
show eileen indoors_crossed normal open at left2
$ renpy.transition(dissolve, layer='master')
eileen "Turned out that way. Just another student at the community college, majoring in art."

show rose weaksmile at right2:
    xpos 0.74
show eileen neutral at left2
$ renpy.transition(dissolve, layer='master')
rose "The artsy type, huh? Going for the big bucks, then."

show eileen lookawaynarrow angry at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Ugh3.ogg"
eileen "Thanks."

show rose halfclosed at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
rose "I'm sure you'll find something. Hopefully not involving burgers and fries."

show eileen annoyed angry at left2
$ renpy.transition(dissolve, layer='master')
"Eileen's limits are clearly being tested, being less tolerant of being poked at than I. Hopefully Rose realizes it."

show eileen indoors_onhip disbelief open at left2
show rose normal neutral at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
eileen "You seem like the artsy type yourself. What's with all the ink?"

show eileen neutral at left2:
    nod2
"Eileen motions to Rose's left side while brandishing a french fry, the tattoo on her upper arm only made more noticeable by her tank top."

show rose smile at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
rose "Looks cool."

show eileen indoors_crossed narrow open at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Seriously3.ogg"
eileen "Uh huh."

show rose talking at right2:
    xpos 0.74
show eileen neutral at left2
$ renpy.transition(dissolve, layer='master')
rose "Expected it to be my life story or something?"

show eileen indoors_onhip disbelief open at left2
$ renpy.transition(dissolve, layer='master')
eileen "That was my first-"

stop music fadeout 8.0
show rose halfclosed smirk at right2:
    xpos 0.74 yoffset 200
    easein .15 yoffset 182
    easeout .175 yoffset 200
    easein .15 yoffset 192
    easeout .175 yoffset 200
voice "Rose_OhYeah3.ogg"
rose "Wait, no, forget what I said. I'm in the Yakuza, and they gave me these as my initiation."

show eileen indoors_crossed closed smile at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_AwkwardGiggle2.ogg"
eileen "Nothing says Yakuza like a biker in Middle America."

stop ambiance fadeout 4.0
show rose normal laugh at right2:
    xpos 0.74
$ renpy.transition(dissolve, layer='master')
"As Rose's chest heaves with lighthearted laughter, I find myself smiling as well. I'm glad the two get along, though a little part of me wishes I could be like Eileen. It took me months to warm up to Rose, yet Eileen gets on with others so smoothly."

scene black with longDissolve
play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
scene bg aptallison outside night
show eileen outdoors_onhip neutral normal at center
with dissolve
"Standing out in front of the apartment once more, we say our goodbyes for real this time. Even if she pointedly refused Rose's later offer of transport, at least she'll be going home on a full stomach."

"It's an odd atmosphere. It's time to say our goodbyes - especially given the night's chill having set in - but neither of us quite want to say the words."

show eileen lookaway open at center
$ renpy.transition(dissolve, layer='master')
eileen "When you said you had a roommate, that's the last kind of person I expected you to be shacked up with."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "Rose is nice. Once you get to know her."

allison "She's a family friend, so I guess you could say I got this apartment through connections."

show eileen normal neutral at center
$ renpy.transition(dissolve, layer='master')
"Eileen's not really wrong, though. Ever since starting at community college, I've gone from having a couple of very alike friends at high school, to an increasing menagerie of odd characters."

show eileen outdoors_crossed lookawaynarrow angry at center
$ renpy.transition(dissolve, layer='master')
"The way Eileen looks as she gazes at the building catches me off guard. It's hardly the comfortable existence she seems to have, Rose and I pretty much eking out a living with what scraps we get, yet she looks so wistful."

show eileen closed at center
$ renpy.transition(dissolve, layer='master')
eileen "You really have a nice thing going, don't you?"

allison "Yeah. I guess so."

show eileen lookaway neutral at center
$ renpy.transition(dissolve, layer='master')
allison "Um, if you ever want to visit again, you're definitely welcome!"

show eileen outdoors_onhip smile sad at center
$ renpy.transition(dissolve, layer='master')
"She gives an amused snort and a smile."

eileen "I'll have to take you up on that sometime."

show eileen closed at center
$ renpy.transition(dissolve, layer='master')
"Moments tick by as the two of us stand out on the sidewalk, neither quite knowing what to say next. I want her to stay around some more to talk to, but I know it's already getting late."

"Idly thinking over our dinner together for something to talk with her about, one particular part of the conversation keeps sticking out. Replaying it in my head, I can feel my face going red before I can cover it with my hands."

show eileen disbelief open at center
$ renpy.transition(dissolve, layer='master')
eileen "What's wrong?"

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "I can't believe Rose was talking about... that kind of stuff, even though you just met her. Sorry about that."

show eileen outdoors_crossed lookawaynarrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "It's alright. I'm the one who brought it up."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "That's right! You're just as bad!"

$ renpy.sound.set_volume(0.2)
play sound "sfx/body_prod.ogg"
show eileen disbelief at center
$ renpy.transition(vpunch, layer='master')
"I give her shoulder a firm tap. Immediately feeling conscious of the gesture, I pull away from her and look elsewhere, fuming away in my embarrassment."

play music "music/night_2.ogg" fadein 6.0
show eileen outdoors_fists lookawaynarrow frown at center:
    nod2
"Eileen rocks back and forth between her heels and the ball of her feet to pass the time while I recover, hands not quite knowing what to do."

$camera_move(500,0,300,0,6,'ease')
show eileen outdoors_onhip lookaway frown at center:
    subpixel True
    zoom 1.0 xpos 0.5
    ease 6.0 zoom 1.2 ypos 1.28 xpos 0.52
with None
show bg aptallison outside night blurred2
$ renpy.transition(verylongDissolve, layer='master')
"Eventually - thankfully - Eileen breaks the silence between us."

pause 1.0
show eileen outdoors_onhip lookaway open at center:
    zoom 1.2 ypos 1.28 xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "Thanks for inviting me here. I'm glad to have been over tonight."

show eileen neutral at center:
    zoom 1.2 ypos 1.28 xpos 0.52
$ renpy.transition(dissolve, layer='master')
allison "Why?"

show eileen outdoors_crossed lookawaynarrow open at center:
    zoom 1.2 ypos 1.28 xpos 0.52
$ renpy.transition(dissolve, layer='master')
voice "scene_2S4_en_1ea54d8d.ogg"
eileen "To be honest, I had you pegged as some spoiled little delicate flower when I first met you. You know, the kind who coasts along on their parent's attention, before the real world punches them in the face."

show eileen normal at center:
    zoom 1.2 ypos 1.28 xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "It looks like you have your life pretty sorted, though. You've got a good head on your shoulders, friends, and a cool roommate. You've managed to scratch together a pretty decent life for yourself."

show eileen closed neutral at center:
    zoom 1.2 ypos 1.28 xpos 0.52
    nod2
"She just gives a long breath, rocking back and forth on her feet as she tries to put some words together. I want to thank her for the kind words, but I'm left speechless after such a warmhearted appraisal of my current world."

show eileen lookaway open at center:
    zoom 1.2 ypos 1.28 xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "I don't really know what to say, now. I guess I feel a bit dumb for lecturing you so much."

show eileen normal neutral at center:
    zoom 1.2 ypos 1.28 xpos 0.52
$ renpy.transition(dissolve, layer='master')
allison "It's fine, really!"

show eileen smile at center:
    zoom 1.2 ypos 1.28 xpos 0.52
$ renpy.transition(dissolve, layer='master')
"My frantic brushing off of the idea puts the both of us on the back foot. Smiling, with that wonderful rare smile of hers, she seems to accept the situation."

show eileen outdoors_onhip closed smile at center:
    zoom 1.2 ypos 1.28
    xzoom 1 xpos 0.52
    linear 0.7 xzoom -1 xpos 0.45
"Before I can say anything more, the blonde girl turns to begin the long walk back home."

$camera_move(0,0,0,0,3,'ease')
show shadow:
    alpha 0
    time 3
    ease 3.0 alpha 0.4
show eileen outdoors_onhip closed at offcenterleft:
    subpixel True
    zoom 1.2 ypos 1.28
    xzoom -1 xpos 0.45
    parallel:
        ease 3.0 alpha 0.0 xpos 1.2
    parallel:
        easeout 1.0 yoffset -1
        easein 1.0 yoffset 1
with None
show bg aptallison outside night
$ renpy.transition(longDissolve, layer='master')

"Without looking back, Eileen simply raises her hand into the air as she strolls off down the road. She's as confident as ever."

"Things just happened around me, and I worked problems out as they occurred. Is that really worth respect? It feels strange to have someone I admired to turn that right back on me."

stop music fadeout 5.0
"I feel my heart sting as her figure gets smaller in the dark night sky, but there's nothing I can say or do. Just... watch her go."

scene black with midDissolve
scene cg act2 balconychat alone
$camera_move(0,0,0,0,0,'dissolve')
with midDissolve
$ renpy.sound.set_volume(0.05)
play sound "sfx/dumptruck.mp3" fadein 1.0
$camera_move(3000,200,750,0,30,'ease')
"The cold night's breeze wafts past the balcony, my thin jacket doing little to stop it. The only noise to be heard is the odd car rushing down the street through the darkness, or snippets of muffled music from neighboring apartments."

"Moments like this are nice, circumstances aside. Just being able to be alone with my thoughts, without the distraction of others."

"That said, I already have my answer to what had been on my mind. That was the real point of this dinner after all."

stop sound fadeout 1.0
"When I modelled for her, I wanted to be a part of something that was important to Eileen. Even before then, I wonder if the times I tried to get closer weren't out of friendship alone."

"What I felt as I watched Eileen walk away was all the confirmation of my feelings I needed."

"A dark figure suddenly appears, taking no heed of my surprise as it leans against the balcony beside me. As I compose myself once more, the familiar acrid smell passing my nose tips me off before my eyes do."

$ renpy.sound.set_volume(1.0)
play music "music/snow.ogg" fadein 8.0
scene cg act2 balconychat rose with vpunch
$ camera_reset()
allison "Don't scare me like that."

rose "Hey, I called out. Not my fault you were daydreaming."

$camera_move(-450,-400,450,0,5,'ease')
"Her mention of it brings all my worries flooding right back. Hardly wanting to look at Rose while thinking about all this, I turn back and try to ignore her as best I can."

"Rose mentioned how I should think about finding a partner sometime while in college. My parents too, and even my high school friends before I came."

"I was content to focus on school, and keep such complications out of mind until my life was all set up and ready. College has already set me right on that account; life doesn't go on hold until you're ready to face it."

$camera_move(0,0,0,0,5,'ease')
"Rose simply blows a puff of smoke, a thin stream passing her lips and disappearing into the night sky. I try to keep my mouth shut, but the smell proves too much for me as I bring my hand to my face."

allison "That's terrible."

rose "You're the one who banishes me here, remember?"

"I hate to admit it, but she does have a point. Rose stubbornly makes a point of taking a puff of her cigarette, but soon notices that something is amiss."

rose "C'mon, out with it. What's on your mind?"

scene cg act2 balconychat talk
$camera_move(-3900,650,900,0,0,'dissolve')
with fadeInOut
"It'd be easy enough to wave her off; one of the things I like about Rose is that she knows when to step back, and this is the kind of thing plenty of people keep private."

"But somehow... even if I haven't told Eileen how I felt, I kind of want someone else to know."

$camera_move(-3900,-1200,900,0,8,'ease')
allison "I think I like someone."

"I watch her reaction with the best attempt I can muster at casual interest. I'm surprised by how... unsurprised Rose is."

"After a tortuously long time, she finishes her puff of the cigarette and takes it from her mouth."

rose "You had the look of someone with that on the mind. It's that Eileen girl, right?"

$camera_move(-420,-350,450,0,8,'ease')
show cg act2 balconychat talk 2 with smoothDissolve
"My mind blanks. She picked that up herself? She isn't taken off guard by my liking a girl at all?"

"The knot of anxiety I hadn't even noticed forming inside of me suddenly twists and turns, the expected spluttering explanation suddenly not needed. I psyched myself up so much, only for it to go nowhere."

"The silence between us continues as Rose patiently waits for me to respond. It's just... What's supposed to come after saying that?"

show cg act2 balconychat talk 5 with smoothDissolve
allison "I didn't think you knew. About Eileen or, you know..."

rose "Well... I mean..."

rose "Kinda hard to ignore what's in front of your face, you know. Seeing you two together, it all clicked."

show cg act2 balconychat talk with midDissolve
allison "You don't think I'm weird?"

"Apparently feeling a little more sure of what to say, she gives a disarming smile."

rose "Believe me, I'm not in any position to call someone weird."

show cg act2 balconychat talk 2 with midDissolve
allison "Yeah."

voice "scene_2S4_en_62fc89aa.ogg"
rose "Hey, that's not what you're supposed to say!"

$ renpy.transition(hpunch, layer='master')
"She elbows me in response to my mostly unintentional bite back."

show shadow:
    alpha 0
    ease 3.0 alpha 0.35
show cg act2 balcony allison as act2_balcony_allison:
    alpha 0
    ease 3.0 alpha 1
with None
show cg act2 balconychat talk 4 blurred2
$ renpy.transition(longDissolve, layer='master')

"With the situation defused, I'm managed to calm down a little."

"Just saying I like her makes my thoughts feel all the more real, my heart skipping a beat as I repeat the words in my mind."

"Rose thinks to herself a little, before snuffing out her cigarette on the ashtray and looking at me squarely."

scene cg act2 balconychat talk 4
$camera_move(-420,-350,450,0,0,'dissolve')
with midDissolve

rose "Sorry, I shouldn't be so flippant when you're all worked up. I get that coming out can be hard."

rose "For what it's worth, I really appreciate that you trust me so much."

show cg act2 balconychat talk 3 with midDissolve
$camera_move(0,0,0,0,18,'ease')
"The warm smile on her face proves infectious, all tension from the air fading away. I hardly mind, now that I've managed to unwind a little; I get the feeling she's stumbling through this herself."

"Minutes go by with only the passing of cars beneath us for noise, both of us savoring the peacefulness of the winter's night. At loose ends, I lean against the balcony railing and finally break the silence."

show cg act2 balconychat talk 4 with midDissolve
allison "What should I do?"

rose "I don't think that's something I can decide for you. Just remember that you're still young."

show cg act2 balconychat talk 5 with midDissolve
allison "So you don't think it'll work out."

rose "I'm not saying that. Just... take it easy, alright? Relationships are a pain in the ass."

"This isn't what I'd hoped Rose would say at all, but that doesn't mean she's wrong."

show cg act2 balconychat talk 4 with midDissolve
allison "I thought love was supposed to feel all happy and warm, but I feel more nervous than anything else."

rose "Welcome to relationships. Falling for someone is easy, it's what comes next that's hard."

show cg act2 balconychat talk 3 with midDissolve
"Her disarming smile at least puts me a little more at ease."

"I'm glad I have Rose here for me. In many ways, I feel like we can't relate to each other, but we can still have this kind of conversation and understand each other. We're just two girls, talking about love."

voice "scene_2S4_en_f3f2d29e.ogg"
rose "You're a good girl, Allison. I promise that whatever happens, you can call on me. Okay?"

allison "Thanks."

stop music fadeout 2.5
rose "But, you know... if things do work out, you're still gonna have to learn how to be quiet for my sake if you bring her around."

stop ambiance fadeout 4.0
scene cg act2 balconychat talk 5 with hpunch
$ _dismiss_pause = False
allison "Rose!"

window hide dissolve
scene black with longDissolve
$ camera_reset()
return
