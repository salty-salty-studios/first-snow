label scene_3S8_en:
######################
# Act 3, Scene 8

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg downtown square night sketch:
    zoom 1.325 xalign 0.01 yalign 0.12
# $camera_move(-3800,-1200,450,0,0,'dissolve')
with inkfade
scene bg downtown square night:
    subpixel True
    zoom 1.325 xalign 0.01 yalign 0.12
    time 1.0
    ease 30.0 xalign 0.99 yalign 0.12
# $camera_move(-3800,-1200,450,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
$ _dismiss_pause = True

play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
play music "music/dozy_comfy.ogg" fadein 2.0
show snow light with dissolve
# $camera_move(3800,-1200,450,0,30,'ease')
window show dissolve

"The snowfall is thankfully light as I walk through the city, bags in hand from the day's last-minute shopping downtown."

"People calmly walk to and fro, the occasional passerby of Eileen's country home replaced by the crowds of downtown Utah."

"Briefly distracted by the huge Christmas tree - completed just in time for Christmas Eve - I think back to yesterday's events."

# scene bg colorado house ext HD
# $camera_move(-8000,-2500,400,0,0,'dissolve')
# show eileen indoors_crossed lookawaynarrow frown at leftedge:
    # zoom 0.7 yoffset -400
    # xzoom -1 xpos -0.2
# show eve indoors normal sad at leftside:
    # zoom 0.7 yoffset -400
    # xzoom 1 xpos 0.06
# with fadeInOut
show misc rendered eileen leaving colorado sepia with flash
"When all's said and done, leaving Eileen's family ended up being a calm affair. I gave her parents my thanks for taking care of me at such short notice, and both said they'd be more than happy to have me again. Eve had also reluctantly come to terms with my leaving by then."

"Then there was the matter of Eileen. Our sullen farewell was short and sweet, but maybe that was because there wasn't much left to say."

hide misc with flash
"Thanks to my time in Colorado, a surprising amount of things I needed to buy before heading back to my family slipped my mind. At least wandering around the city tonight's given me a chance to unwind and set my thoughts straight."

$ renpy.music.set_volume(0.2, delay=1.0)
$ renpy.sound.set_volume(0.3, channel='loopsfx')
play loopsfx "music/ringtone.ogg"
scene bg downtown square night
show snow light
with fadeInOut
$ camera_reset()
"...Of course my phone starts ringing as soon as I appreciate some time alone to think."

show bg downtown square night blurred2 as bg2:
    xalign 0.5 yalign 0.5 alpha 0
    ease 1.0 alpha 0.9
$ phone.show('call-in')
pause 1.0
window show dissolve
"Pulling it from my pocket with my free hand, I'm surprised to see it's dad."

play sound "sfx/phone-pickup.ogg"
$ renpy.music.set_volume(0.5, delay=2.0)
stop loopsfx
voice "Allison_NervousHi3.ogg"
allison "Dad! Hi."

stop sound fadeout 1.0
dad "Hi, Allison. Not catching you at a bad time?"

allison "No, no, it's fine!"

dad "Sounds like you're busy; I can barely hear you."
voice "Allison_Um1.ogg"
allison "Just wandering about downtown to fill some time and do some errands."

dad "Still good to be picked up tomorrow morning?"

allison "Yeah, I'll be ready at the apartment with all my stuff. Sorry again about changing everyone's plans."

dad "I told you before, it's fine. Plans already had to change because of your finals. We'll pick you up tomorrow, then."

allison "It'll be good to see everyone again. Is mom doing okay?"

dad "She's better, thankfully. You gave a bit of a shock when you said you weren't coming back for so long."

dad "We were all shocked. It seemed like you were having a rough time away from home, so I never expected you to go out of state like that."

"So they could tell. I feel a little sheepish, thinking back."

dad "So you had a good trip, then?"

show shadow:
    alpha 0
    ease 2.0 alpha 0.4
"I feel a chill as the last few days rush through my head."
voice "Allison_Hm1.ogg"
allison "Yeah. I did."

dad "Hmm."

"Once again, dad can tell just from my voice. It's impossible for me to hide how I'm feeling. Something in me compels me to try anyway."

allison "What? I had fun!"

dad "Well... when you're home, you'll tell us all about it, right?"

allison "Of course. I'm looking forward to it."

dad "I am too. You know that you can tell me anything."
voice "Allison_TakeCare2.ogg"
allison "I know. Bye, dad."

dad "See you soon, love you."

play sound "sfx/phone-hangup.ogg"
$ phone.show('unlock')
pause 1.0

"With that, the call ends. I stare blankly at the screen of my phone. I'll be happy to see my family again, not to mention the warmth and liveliness of home. I have to take a deep breath, a lump in my throat forming from homesickness."

stop sound fadeout 1.0
"I guess that feeling never goes away completely..."

scene black
hide screen phone
with dissolve
play sound "sfx/phone-taps.ogg"
"With the phone already out, I take a moment to glance through the photos I've taken on it."

"A few from Colorado are most recent, which'll be nice to show my parents. As I keep going back though, I stop at a photo taken just before I left for there."

scene cg act2 photo
show white:
    alpha 0.5
show cg act2 photo camera as act2_photo_camera
with midDissolve
stop music fadeout 10.0
stop sound fadeout 1.0
"The screen shines brightly in the darkness of the night, the photo of everyone gathered in my apartment celebrating the end of semester making me mull over everything that's happened since I arrived here."

"It's only been a few months, but my time since starting college has been an adventure already. I've learned so much, found so many friends, and discovered so many kinds of relationships. It's such a different way of life I lead now."

"The smiling faces all gathered for that one moment in time... it's all thanks to those around me, like them."

scene bg downtown square night
show snow light
show shadow:
    alpha 0.4
with fadeInOut
"The phone goes dark once more as I lock it, the precious memory slipped into my pocket once more. The only light to be seen now is that cast by the Christmas tree, occasionally broken by the passing crowds."

"A strange sense of calm falls over me as I stand in the falling snow, hands slipping into my pockets for warmth."

"I was alone and afraid. Eileen was the answer to that, I thought. She seemed so cool and collected, managing life by herself. That strength of will was what drew me to her, in hindsight."

"It was thanks to Eileen, Caprice, and our little club that I was able to cope with being alone. The reason that I'm so at peace with myself isn't that I've finally learned to live without others. It's because I know I have others to help."

"Maybe I was too clingy, as Eileen  said. I just wanted to know her more, even if she was brusque at the best of times. If she wants to retain her solitude so dearly though, perhaps it's for the best that things go like this."

show shadow:
    alpha 0.4
    ease 2.0 alpha 0
"Swallowing the lump in my throat as I push the thoughts aside, I begin to walk once more."

play loopsfx "music/ringtone.ogg" fadein 2.0
"It's then, that my phone begins to buzz in my pocket. Did dad forget to say something?"

show bg downtown square night blurred2 as bg2:
    xalign 0.5 yalign 0.5 alpha 0
    ease 1.0 alpha 0.9
$ phone.show('call-in')
pause 1.2
with vpunch
"Eileen!? Why is she calling me, now of all times? Should I answer? My phone is shaking in my hand."

play sound "sfx/phone-pickup.ogg"
stop loopsfx
"I pick up the call, but I have no idea what to say."

stop sound fadeout 1.0
eileen "Hello? Allison?"

eileen "Allison, where are you right now?"

"She doesn't allow me to so much as get a word out, her voice breathless."

allison "I'm back home in Utah."

eileen "No, I mean... I know, so am I. Can we meet somewhere? Where are you, exactly?"

allison "I'm... by the Christmas tree, in the city square."

eileen "Okay. Stay where you are."

$ phone.hide()
play sound "sfx/phone-hangup.ogg"
show bg downtown square night blurred2 as bg2:
    xalign 0.5 yalign 0.5 alpha 0.9
    ease 2.0 alpha 0.0
"As the line goes dead, I'm left dumbfounded. Eileen is coming here...?"

play sound "sfx/car-door-slam.ogg"
"Within moments, I hear a car door slam loudly. Surely she wasn't looking around for... me..."

play sound "sfx/footsteps-on-tiles.ogg"
$ renpy.music.set_volume(0.5)
play music "music/anxiety_2_m.ogg" fadein 8.0
show eileen outdoors_onhip normal angry at rightside:
    zoom 0.68 yoffset -280
    xpos 1.2
    ease 1.2 xpos 0.88
"A familiar figure jogs up as quickly as she can in her high boots, her long strides clinking loudly on concrete."

scene bg downtown square night blurred2:
    zoom 1.05 xalign 0.5 yalign 0.5
show snow light
$camera_move(2200,1200,400,0,0,'dissolve')
show eileen outdoors_fists sad angry at rightside:
    zoom 1.1 yoffset 85
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
$camera_move(2200,-950,400,0,10,'ease')
stop sound fadeout 2.0
"As she slowly pulls up to a stop, our eyes finally meet. And so, we stand in the city square next to that large tree."

"Between us, only the falling snow."

allison "Eileen, why are you...?"

scene bg downtown square night
show snow light
show eileen outdoors_crossed narrow frown at center:
    zoom 1.3 yoffset 300
    xpos 0.52
with fadeInOut
eileen "What, you didn't want to see me?"

"I almost respond, but sheer surprise stops me from finding the right words. I end up just hanging my head, not knowing how to respond to her snark in such a situation. With my bags weighing down my arms, I set them down."

show eileen outdoors_crossed lookawaysad sadmouth at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"As I look back up, I see Eileen's quip for what it was; a diversion to hide her feelings. She soon realizes I've caught on, her voice turning soft."

show eileen outdoors_onhip open at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "I... found your voice message."

eileen "I didn't want to leave things as they were."

show eileen sadmouth at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"My face flowers into a blush as I grimace from embarrassment. I knew she'd eventually hear it, but it's still embarrassing to think about."

allison "Um, I..."

show eileen sad sadmouth at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"As I think back to everything that happened, I feel a pang of regret. Once again, I feel myself shrinking away from her."

allison "But... haven't I been a pain? Ever since we met, I've only caused you trouble."

show eileen outdoors_crossed narrow frown at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "Yeah, you sure have."

"There's that sardonic humour again. I can't remember if I ever found it endearing."

allison "Why do you do that?"

allison "Your first response to everything is to try and brush things off with a quip against someone."

show eileen outdoors_fists lookawaynarrow open at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "Only because everyone sticks their nose into my business."

show eileen outdoors_fists lookawaynarrow frown at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
allison "Including me, I guess."

"I follow that up with a dry laugh, yet Eileen's expression doesn't change. I should have expected that, but I feel my chest tighten in response nevertheless."

show eileen outdoors_crossed closed open at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "I just... I already had things figured out for myself."

show eileen outdoors_crossed lookaway neutral at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"As silence reigns, it feels as though we're just repeating the steps we took until now."

"Nothing's changed. I'm still me, and Eileen is still Eileen. For all I might want to get closer to her, she still keeps pushing me away. She came all the way back here to work things out, yet we're still stuck awkwardly trading barbs..."

show eileen outdoors_onhip normal at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
allison "Everything we did together... was it only ever a pain to you?"

allison "I didn't want to say it, but..."

"I steel my heart to try and force out the words, tightly holding my arm to try and steady myself."

allison "I suppose this is all over, then?"

stop music fadeout 2.0
show eileen outdoors_fists annoyed open at center:
    xpos 0.52
    nod2
with vpunch
eileen "No!"

show eileen outdoors_fists frown sad at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Her shout startles me, the point where she recoils a little from my reaction. I guess we're both getting flustered."

show eileen outdoors_onhip lookawaysad open at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "I mean, that's not what I meant."

show eileen outdoors_onhip lookawaysad frown at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Reminding us that we're not alone, a small child goes running by us as her mother runs after her. The distraction gives Eileen time to reason through all this, while I try my best to ignore the stinging of my heart. Everything is so confusing right now."

show eileen outdoors_crossed closedsad sadmouth at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
$ renpy.music.set_volume(0.5)
play music "music/touching.ogg" fadein 12.0
eileen "Every day was the same, living alone in my apartment and working away in that art room. I thought I was fine being alone, until you came into my life and messed everything up."

show eileen outdoors_crossed lookawaysad at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "When I thought you might really be gone, I realized how lonely I was."

show eileen outdoors_crossed sad at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "I meant what I said earlier; I can forget all my worries around you. I don't have to work hard and worry about being my best, I don't have to prove anything."

show eileen outdoors_crossed sad open at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "And I thought... I thought you'd understand."

eileen "I didn't ever expect you to take my parents' side. I didn't think you'd try to tell me I'm making the wrong choices."

show eileen outdoors_fists closedsad sadmouth at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"My heart sinks. Is that how it looked to her? Like I betrayed her?"

"How could I? I've always seen what her parents can't. She's serious about painting. If there's one thing I know about her, it's that. Why would I want to ruin that world of hers, that I found so fascinating?"

show eileen outdoors_fists frowning open at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "But when I thought I might lose you..."

show eileen outdoors_fists sad open at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "I realised you were right. For all I talked big about how you should try new things in college, I was the one pushing everyone away and trying to stay the same."

show eileen outdoors_fists sad sadmouth tears at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"As I try to think of how to explain myself, I realize Eileen's eyes have become moist. It's such a strange sight that I completely lose track of what I was going to say."

allison "Eileen?"

show eileen outdoors_onhip closedsad frown none at center:
    xpos 0.52
    nod2
eileen "I don't want to lose you, Allison. I... want to try again."

show eileen outdoors_onhip lookawaysad frown tears at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Moments pass as I think over her words, trying to sift through my emotions. She looks so different now, her proud stature somehow smaller and more fragile. She's scared."

"Seeing her in this state puts me on the brink of tears as well. I know my answer already, given how seeing her like this affects me."

show eileen outdoors_onhip sad frown tears at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
allison "I only ever wanted to be the person closest to you. Why would I want to ruin that world of yours, when it's what brought us together?"

allison "Let's..."

$ renpy.music.set_volume(1.0, delay=2.0)
stop music fadeout 2.0
show eileen outdoors_onhip sad sadmouth tears at center:
    xpos 0.52
    shaking2
allison "Let's try again, Eileen."

$ renpy.sound.set_volume(1.0, channel='loopsfx')
scene black with hpunch
scene cg act3 hug run
$camera_move(-200,-800,750,0,0,'dissolve')
with midDissolve
$camera_move(-200,-200,750,0,2,'ease')
play music "music/credits.ogg" fadein 8.0
pause 2.0
window show dissolve
"Without warning, she pulls me into an embrace, arms wrapped tightly around me."

"My brain short-circuits as she begins to weep, completely unable to handle the situation. I have no idea what to say as she clutches me tightly to her shuddering body, my own composure barely holding as my arms slowly raise and come around her back."

"Oh, I see now. Eileen's finally cracked under the pressure, that wall she carefully built up over so many years finally crumbling down at once."

window hide
show cg act3 hug end
with midDissolve
window show dissolve
"I hold her tightly to me as she cries, trying my best to comfort her. She's here, and in my arms. This vulnerable and honest girl is for only me to see, my own eyes only barely staying dry."

"This Eileen is one I've never seen, but she's the Eileen I've fallen for all over again. "

eileen "Thank you, Allison!"

"I feel a lump in my throat as I stroke her hair, trying my best to soothe her."

eileen "I love you, Allison! I love you!"

$camera_move(0,0,0,0,20,'ease')
show cg act3 hug foreground as cgf
with None
show cg act3 hug end blurred5
$ renpy.transition(thefinalDissolve, layer='master')
"Holding her close as her words are muffled into my shoulder, I close my eyes and savor the feeling of her against me. Eileen loves me. This feeling, this warmth throughout my entire body, as I hear those words..."

"I guess I really am in love with this hopeless girl."

allison "And I love you. Let's do this together."

"We're such different people, with wildly different backgrounds and worlds of our own. As long as the two of us can let each other in, though... we can build a life together. Side by side, we can start here."

stop ambiance fadeout 4.0
allison "It's okay, Eileen. Welcome home."

window hide midDissolve
# note: please don't do anything further here because of the credits transition!
return
