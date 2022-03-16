label scene_2S3_en:
######################

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg buildingart hallway2f sketch with inkfade
scene bg buildingart hallway2f dusk with inkfade2
stop sound fadeout 0.1
play ambiance "sfx/ambiance/crowd_inner.ogg" fadein 4.0
$camera_move(2500,-950,800,0,6,'ease')
pause 2.0
window show dissolve
$ _dismiss_pause = True

play music "music/relaxing.ogg" fadein 4.0
scene bg buildingart hallway2f dusk HD
show bg buildingart hallway2f dusk HD blurred2 as bg2:
    xalign 0.5 yalign 0.5 alpha 0.5
$camera_move(2500,-3000,800,0,0,'dissolve')
with fadeInOut
show eileen outdoors_onhip narrow neutral at centerright:
    subpixel True
    zoom 0.42 ypos 0.05 xpos 0.8 alpha 0
    parallel:
        ease 3.0 zoom 0.5 ypos 0.15 xpos 0.65 alpha 1
    parallel:
        easeout 0.5 yoffset -1
        easein 0.5 yoffset 1
        repeat 3
"With the sun beginning to set, Eileen and I say our goodbyes to Caprice before heading out into the hallway."

"Calming Caprice down after she gets a bright idea feels like trying to stifle a shaken soda can after opening it. She might still be brimming with energy, but the two of us leave the art club's room utterly deflated."

show eileen outdoors_crossed closed open at centerright:
    zoom 0.5 ypos 0.15
    xpos 0.65 alpha 1
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Ugh2.ogg"
eileen "We should have just joined the normal art club. You know, the one which isn't led by a maniac."

show eileen angry at centerright:
    ypos 0.15
$ renpy.transition(dissolve, layer='master')
"I wish I could get the two of them to see eye to eye more often. Caprice did say she's doing all this for Eileen's sake as much as her own, and she's far too straightforward to be lying about that."

"It's difficult to push back on Eileen though, given how prideful a person she is. I seem to attract strong-willed friends."

show eileen normal at centerright:
    ypos 0.15
$ renpy.transition(dissolve, layer='master')
voice "Allison_Um2.ogg"
allison "She is... a lot. She means well, though."

show eileen outdoors_onhip narrow open at centerright:
    ypos 0.15
$ renpy.transition(dissolve, layer='master')
eileen "Well, maybe it's not so bad if you're around to keep her occupied."

show eileen neutral at centerright:
    ypos 0.15
$ renpy.transition(dissolve, layer='master')
allison "For what it's worth, I was actually thinking this might be a fun little adventure. I wanted to thank you for making all of this work out."

show eileen disbelief frown at centerright:
    ypos 0.15
$ renpy.transition(dissolve, layer='master')
"She makes an exquisitely awkward face, caught between my thanking her and the idea of having to share her room with us - and anyone else Caprice manages to rope in - from now on."

show eileen outdoors_crossed lookaway at centerright:
    ypos 0.15
$ renpy.transition(dissolve, layer='master')
"I just smile as we start down the quiet hallway, Eileen taking a look out the window."
$camera_move(0,-3000,800,0,6,'ease')
window hide dissolve
pause 2.0

scene bg campus outskirts snow
show snow light
$camera_move(3200,-1900,600,0,0,'dissolve')
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.07
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.655
with fadeInOut
$camera_move(-3200,-1900,600,0,15,'ease')
letterbox "Her gaze lingers for just that little longer than usual, the snow once again having started falling outside. I can't blame her, given how pretty it looks."

eileenlb "Damn, going to be shoveling snow again. What a pain."

letterbox "She really isn't the sentimental type."

scene bg buildingart hallway2f dusk
show eileen outdoors_onhip normal open at center
with fadeInOut
window show dissolve
$ camera_reset()
voice "Eileen_Huh1.ogg"
eileen "Did I say something wrong?"

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "I was just thinking... you don't seem to have a very romantic view of the world, being an artist."

show eileen outdoors_crossed disbelief open at center
$ renpy.transition(dissolve, layer='master')
eileen "Is there much good about winter?"

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hm1.ogg"
allison "Being back with family, all the pretty snow around, people in cute jackets and coats, holidays..."

show eileen lookawaynarrow angry at center
$ renpy.transition(dissolve, layer='master')
"I end up trailing off, Eileen hardly looking swayed as I count my favorite things about the season on my fingers."

show eileen open at center
$ renpy.transition(dissolve, layer='master')
eileen "'Holidays' are the problem; everywhere's starting to close up or shut down for the new year already."

show eileen outdoors_onhip closed neutral at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble3.ogg"
eileen "I want to keep practicing instead of loafing around, but the life drawing classes are over and all the student modelling offers have dried up."

show eileen normal neutral at center
$ renpy.transition(dissolve, layer='master')
"I have seen notices for those on the noticeboards around campus, with students and others making a little cash on the side by modelling for artists. Those same noticeboards have become much more bare over the last month."

show shadow:
    alpha 0
    ease 1.0 alpha 0.4
"I feel sorry for her, given she takes her painting so seriously. I was so caught up in wanting to be back with my family that I didn't think about how it'd be for her, especially when she doesn't get along with hers."

"As we walk along the hallway, I realize this might present an opportunity; a chance for me to help Eileen and be a part of her painting, instead of simply watching her from afar."

show eileen narrow angry at center
$ renpy.transition(dissolve, layer='master')
"I'm not completely sure about this, but my obvious scheming has already caught Eileen's eye."

$ renpy.music.set_volume(0.2, delay=1.0)
$ renpy.sound.set_volume(1.5, channel="ambiance", delay=1.0)
show shadow:
    alpha 0.4
    ease 1.0 alpha 0
voice "Allison_Um2.ogg"
allison "If it'd be helpful, I mean... maybe I could do it?"

show eileen outdoors_crossed disbelief neutral at center:
    xzoom 1 xpos 0.5
    linear 0.7 xzoom -1 xpos 0.45
"At this, Eileen stops and turns to me. Should I not have suggested this?"

allison "You just need me to stand around and be a model, right?"

show eileen outdoors_onhip open at offcenterleft:
    xzoom -1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
eileen "There's not a lot to it. This would be live modelling you know? I don't want to give you the wrong idea."

show eileen normal neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"The reminder does make me hesitate. I know there's nothing sexual about it, but I'd be standing without clothes on as she alone looked at me, analyzing my whole body."

"Eileen herself doesn't look fussed, though she rarely does. She seems content to let me come to a conclusion myself as she stands about, but my body language soon gives away what I'm thinking."

show eileen outdoors_crossed lookaway grumble at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Sorry if I made you uncomfortable. I can just work on other studies instead."

allison "No, I mean..."

show eileen normal at offcenterleft
$ renpy.transition(dissolve, layer='master')
"She did mention herself that she's done this before. It'd simply be another method of practicing painting, for her."

allison "Would it be in your apartment, or something?"

show eileen outdoors_onhip normal open at offcenterleft
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Yeah1.ogg"
eileen "Yeah."

show eileen disbelief neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"She looks mildly surprised I'm still considering this. If it was anyone else, I don't think I could do this. For Eileen, though..."

stop ambiance fadeout 3.0
stop music fadeout 3.0
voice "Allison_Okay.ogg"
allison "It's fine. I'll do it."

scene black with circlewipe
$ renpy.sound.set_volume(1.0, channel="ambiance")
$ renpy.music.set_volume(0.8)
play music "music/painter.ogg" fadein 4.0
scene bg apteileen livingroom messy
show eileen outdoors_onhip closed neutral at offcenterleft:
    xzoom -1 xpos 0.2 alpha 0
    time 1.8
    ease 2.0 xpos 0.45 alpha 1
with circlewipe
play sound "sfx/door_close.ogg"
"We set down our coats as we enter her apartment, the bright light giving such a different look to her living room compared to mine. As for Eileen herself, I don't get how she isn't exhausted at all after a walk like that from school."

show eileen indoors_onhip closed neutral at offcenterleft:
    xpos 0.45 alpha 1
    nod2
$ renpy.transition(dissolve, layer='master')
stop sound fadeout 1.0
"But try as I might to distract myself, something feels off no matter how I try to ignore it. Painting live models is probably totally normal for an artist like Eileen, so I don't bother saying anything as she sets down her coat."

show eileen indoors_onhip narrow open at offcenterleft:
    xzoom -1 xpos 0.45 alpha 1
$ renpy.transition(dissolve, layer='master')
eileen "Want a drink or something?"

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "I'm fine, thanks."

show eileen normal open at offcenterleft
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Sure2.ogg"
eileen "Suit yourself. I'll grab my stuff, just make yourself comfortable."

show eileen indoors_onhip normal neutral at offcenterleft:
    xpos 0.45 alpha 1
    ease 2.0 xpos 1.2 alpha 0
"She walks off to get her easel and paints as I nod."

scene bg apteileen livingroom messy
$camera_move(-4000,400,750,0,0,'dissolve')
with dissolve
$camera_move(2500,400,750,0,15,'ease')
"Without much else to do as she disappears into another room, I idly look around while taking off my own coat and gloves."

"Her apartment hasn't been cleaned up this time, which is an interesting change. Beyond the easel with a finished painting still sitting on it, a few colorful fashion magazines lie on the coffee table, near a mug left sitting around."

"On the couch, a couple of crumpled t-shirts and an old pair of jeans lie strewn over the back and arm. What catches my eye most, however, is the resident who looks very comfortable on the other end of it."

$camera_move(2500,400,750,0,0,'dissolve')
show bg apteileen livingroom messy norabbit
$ renpy.transition(midDissolve, layer='master')
"Without thinking, I walk over and pick him up."

show bg apteileen livingroom messy norabbit blurred2:
    xalign 0.5 yalign 0.5
$ renpy.transition(midDissolve, layer='master')
show misc cutins bunny:
    subpixel True
    zoom 0.6
    xalign 0.68 yoffset -250
    ease 1.5 yoffset 155
"A particularly large stuffed rabbit, big enough to need two hands to hold comfortably. Though well-made and adorably designed, it's obviously a little well-loved by now."

"I'm sure I'd have noticed such a thing if it were around when Wallace and I came for dinner, so it must've been stuffed into her bedroom or something."

# scene bg apteileen livingroom messy:
    # subpixel True
    # ease 1.5 xalign 1.0
# show misc cutins bunny:
    # subpixel True
    # xalign 0.5 yoffset 35
    # ease 1.5 xalign 0.4
# show eileen indoors_crossed frown narrow:
    # subpixel True
    # xpos 0.8 yalign 1.0
    # alpha 0.0
    # ease 1.5 xpos 0.7 alpha 1.0
show eileen indoors_crossed frown narrow at rightish:
    zoom 0.6 yoffset -310
    xpos 0.85 alpha 0
show eileen indoors_crossed frown narrow blur at rightside as eileen2:
    zoom 0.6 yoffset -310
    xpos 1.1
    ease 1.5 xpos 0.85
"Noticing movement out of the corner of my eye, I turn and look up."

$camera_move(2200,250,600,0,3,'ease')
show misc cutins bunny:
    subpixel True
    zoom 0.6
    xalign 0.68 yoffset 155
    ease 1.5 yoffset -250
show eileen indoors_crossed frown narrow at rightish:
    zoom 0.6 yoffset -310
    xpos 0.85 alpha 0
    ease 1.0 alpha 1
show eileen indoors_crossed frown narrow blur at rightside as eileen2:
    zoom 0.6 yoffset -310
    xpos 0.85 alpha 1
    ease 1.5 alpha 0
with None
show bg apteileen livingroom messy norabbit
$ renpy.transition(midDissolve, layer='master')

"Eileen simply stares at me, face flat as she holds a bag of supplies in her hand. I really shouldn't have just gone and started fiddling with her stuff."
voice "Allison_Sorry1.ogg"
allison "Sorry."
voice "Allison_Um1.ogg"
allison "Um, it's really cute."

hide eileen2
hide misc cutins bunny
# show eileen normal open:
    # yalign 1.0
    # easeout 0.5 yoffset 20
    # easein 0.5 yoffset 0
play sound "sfx/muffled-drop.ogg"
show eileen normal at rightish:
    zoom 0.6 yoffset -310
    xpos 0.85 alpha 1
    ease 0.5 yoffset -305
    ease 0.5 yoffset -315
    ease 0.2 yoffset -310
"She puts her bag down and sighs, giving me a bit of relief that she isn't angry."

# show eileen neutral:
    # yalign 1.0
    # parallel:
        # ease 2.5 xpos 0.50
    # parallel:
        # easeout 1.0 yoffset -2
        # easein 1.0 yoffset 1
        # ease 0.5 yoffset 0
# show misc:
    # time 1.5
    # ease 2.0 ypos 1.5
stop sound fadeout 1.0
show eileen normal at rightish:
    zoom 0.6 yoffset -310
    xpos 0.85
    ease 1.5 xpos 0.65
    nod2
"Silently, she strides over and takes the toy from me as I offer it to her."

show eileen indoors_onhip lookawaynarrow open at centerright:
    zoom 0.6 yoffset -310
    xpos 0.65
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "My sister gave it to me to keep me company when I moved out."

scene black with dissolve
$ camera_reset()
scene bg apteileen livingroom messy HD:
    subpixel True
    xalign 0.0 yalign 0.5
    size (1600, 900) crop (1080, 500, 1280, 720)
    linear 12.0 crop (1080, 450, 1280, 720)
show bg apteileen livingroom messy HD blurred4:
    subpixel True
    xalign 0.0 yalign 0.5 alpha 0.95
    size (1600, 900) crop (1080, 500, 1280, 720)
    linear 12.0 crop (1080, 450, 1280, 720)
show white:
    zoom 2.0 xcenter 0.5 ycenter 0.5 alpha 0.05
show eileen indoors_onhip lookawaynarrow neutral:
    subpixel True
    size (1600, 900) crop (-420, 150, 1280, 720)
    linear 12.0 crop (-420, 50, 1280, 720)
with dissolve
"I'm disappointed by how little emotion's in Eileen's voice when she says so, but those thoughts quickly disappear as she gently sets down the rabbit where it had been."

"She takes care to set it down gently, with a quick brush of its fur."

show bg apteileen livingroom messy HD:
    xalign 0.0 yalign 0.5
    size (1600, 900) crop (1080, 450, 1280, 720)
show bg apteileen livingroom messy HD blurred4:
    xalign 0.0 yalign 0.5 alpha 0.95
    size (1600, 900) crop (1080, 450, 1280, 720)
show white:
    zoom 2.0 xcenter 0.5 ycenter 0.5 alpha 0.05
show eileen indoors_crossed closed smile:
    size (1600, 900) crop (-420, 50, 1280, 720)
$ renpy.transition(dissolve, layer='master')
"That momentary smile as she steps back and looks at it warms my heart."

"It only lasts for a second, but her face is unmistakably that of a child, one taking care of their favorite companion."

show eileen lookawaynarrow neutral:
    size (1600, 900) crop (-420, 50, 1280, 720)
$ renpy.transition(dissolve, layer='master')
"So Eileen does have a cute side to her."

"I somehow feel a bit less wound up about everything, now. She's not that different to me, in the end."

stop music fadeout 5.0
scene bg apteileen livingroom messy
show eileen indoors_onhip normal neutral at offcenterleft:
    xzoom 1 xpos 0.5
    time 1
    linear 0.7 xzoom -1 xpos 0.45
with fadeInOut
"As she turns away, I remember the task at hand."

allison "So...?"

show eileen normal open at offcenterleft:
    xzoom -1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
eileen "I'll just set up the easel and canvas, then I'll have everything ready."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
allison "Should... should I take my clothes off, then?"

show eileen indoors_crossed lookawaynarrow at offcenterleft
$ renpy.transition(dissolve, layer='master')
"She's about to answer, before pausing for a moment. Much as I might try to stifle my awkwardness, undressing in front of someone else is still weird."

show eileen closed open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "If it's a problem, you can grab a towel. I can make-do."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"Feeling more than a little sheepish, I glance around to be more sure of my surroundings. The blinds are shut as they were before, and the door's still locked, so I'm not sure what I expected."

"Maybe the silence is putting me off, the apartment being set so far back the road, unlike mine."

$ renpy.music.set_volume(1.0)
play sound "sfx/rustle-clothes.ogg"
scene black with midDissolve
$ camera_reset()
if not store.rabbl.allow_explicit:
    "I want to say that I'm fine, but I can't quite get over the stumbling block of being bared in front of someone. Meeting halfway will have to do, for now."

    "As Eileen sets her previous painting on the kitchen counter, I pop into the bathroom."

else:
    "As Eileen sets her previous painting on the kitchen counter, I start taking my clothes off, my heart practically in my mouth by now."

play music "music/romance_2_m.ogg" fadein 2.0
if not store.rabbl.allow_explicit:
    scene cg act2 nudepainting embarrassed
    $camera_move(-2800,1500,750,2,0,'dissolve')
    with midDissolve
    "My heart's practically in my mouth as I reappear in the room with a towel wrapped around me, precious little being covered as I take my place before her."

else:
    scene cg act2 boobpainting embarrassed
    $camera_move(-2800,1500,750,2,0,'dissolve')
    with midDissolve
    "The last of my underwear falls to the ground beside me. Eileen's eyes flick between fixing her fresh canvas to the easel, and glancing at my fidgeting body as I take my place a few feet before her."
    
stop sound fadeout 1.0
allison "Should I stand like this, or...?"

$camera_move(3000,1550,750,0,8,'ease')
"She looks at me for a few moment in serious thought. It's a little interesting how quickly her demeanor changes to that of a painter carefully considering how best to use my body as an artistic prop."

eileen "Try turning around, so your back's towards me."

"My thoughts are in a haze, unable to let go of how exposed I am. All I can do is nod and dutifully do as she says."

eileen "Hmm... yeah, that's good. Keep your head like that, and maybe let your arms hang down."

allison "Like... like this?"

eileen "Yeah, just stay like that."

play loopsfx "sfx/ambiance/painting.ogg" fadein 1.5
if not store.rabbl.allow_explicit:
    show cg act2 nudepainting
else:
    show cg act2 boobpainting
$camera_move(0,0,0,0,12,'ease')
"I give a nod, trying to relax as much as I can. That isn't saying much, though."

"There's no other sound in the room as she starts sketching me out, the pencil's sharp scratching filling the air."

"It's certainly an odd experience to think somebody's looking at my body so analytically, taking in every detail, considering it, and copying it to canvas. For Eileen's sake, I try to keep as still as possible despite the butterflies in my stomach."

"Her pencil-work apparently finished, the gentle sound of brushstrokes starts as her painting begins in earnest. She's fast at her sketching, I suppose she'd have a good bit of practice at this."

"I can't see much at all with my head slightly down like this, but at least this position is easy to keep. Without anything in particular to focus my eyes on, I can't help but turn my thoughts inward."

if not store.rabbl.allow_explicit:
    show cg act2 nudepainting blurred4
else:
    show cg act2 boobpainting blurred4
$ renpy.transition(midlongDissolve, layer='master')
show shadow:
    alpha 0
    ease 2.0 alpha 0.45
if not store.rabbl.allow_explicit:
    show cg act2 nudepainting allison2 as cg2:
        alpha 0
        ease 2.0 alpha 1
else:
    show cg act2 boobpainting allison2 as cg2:
        alpha 0
        ease 2.0 alpha 1
"How do people do this without getting self-conscious?"

"Nobody's ever looked at my naked body like this, carefully analyzing every curve and muscle."

"I wonder how I look to her right now. Am I gross? Compared to Eileen, I probably look plain at best."

stop loopsfx
if not store.rabbl.allow_explicit:
    scene cg act2 nudepainting embarrassed with vpunch
else:
    scene cg act2 boobpainting embarrassed with vpunch
eileen "Hey, I know it's not easy, but can you try not to tense up so much?"

if not store.rabbl.allow_explicit:
    scene cg act2 nudepainting with midDissolve
else:
    scene cg act2 boobpainting with midDissolve
"I glance back at Eileen. Our eyes meet and I force myself to face forward again, resuming my pose."

allison "Sorry."

eileen "It's okay. Not too much longer."

play loopsfx "sfx/ambiance/painting.ogg"
if not store.rabbl.allow_explicit:
    show cg act2 nudepainting blurred4
else:
    show cg act2 boobpainting blurred4
$ renpy.transition(verylongDissolve, layer='master')
show bg texture:
    alpha 0
    ease 5.0 alpha 0.05
if not store.rabbl.allow_explicit:
    show cg act2 nudepainting allison1 as cg2:
        alpha 0
        ease 5.0 alpha 1
else:
    show cg act2 boobpainting allison1 as cg2:
        alpha 0
        ease 5.0 alpha 1
"Her expression was so focused and analytical. I sometimes forget that serious artwork can take so much knowledge and logic as well as creativity. I really am just an art prop for her."

if not store.rabbl.allow_explicit:
    show cg act2 nudepainting allison3 as cg3:
        alpha 0
        ease 2.0 alpha 1
else:
    show cg act2 boobpainting allison3 as cg3:
        alpha 0
        ease 2.0 alpha 1
"That's good. If I remember that, this isn't so bad. Eileen's done this plenty of times, and I can trust her. I was the one who offered, anyway."

"The reason I did this was to help her, and now I can finally be a part of her true passion of painting. I feel the corners of my mouth tug a little at the idea."

stop loopsfx fadeout 4.0
"It makes me feel a little special that she's looking at me this way. While she's no doubt done life drawing before, this is something different."

if not store.rabbl.allow_explicit:
    scene cg act2 nudepainting smile with midDissolve
else:
    scene cg act2 boobpainting smile with midDissolve
"Only now do I realize that Eileen's brushstrokes have ceased."

"Just as I work up the will to question her, Eileen speaks up."

eileen "Alright, you can move now."

if not store.rabbl.allow_explicit:
    scene cg act2 nudepainting smile
    $camera_move(-2800,1500,750,2,0,'dissolve')
    with midDissolve
else:
    scene cg act2 boobpainting smile
    $camera_move(-2800,1500,750,2,0,'dissolve')
    with midDissolve
"A weight comes off me as my entire body slumps, a long breath escaping my lips. It feels like my entire body deflates."

scene black with dissolve
$ camera_reset()
scene bg apteileen livingroom messy with dissolve
if not store.rabbl.allow_explicit:
    "Thankful that my duty has been fulfilled, I adjust the towel a little to ensure it doesn't slip off. My first thought is to go to where I've carefully placed my clothes, but on the way I'm distracted by the sight of it."
else:
    "Thankful that my duty has been fulfilled, I immediately move my hands to cover myself. My first thought is to go to where I've carefully placed my clothes, but on the way I'm distracted by the sight of it."

show bg apteileen livingroom messy blurred2
$ renpy.transition(midDissolve, layer='master')
show misc paintings allison:
    zoom 0.9 xalign 0.5
    yoffset -200 alpha 0
    ease 1.5 yoffset 25 alpha 1
"I'm left speechless."

"I have to resist the urge to reach out and touch it. This is how Eileen sees me. Not gross, nor plain. I feel my heart sting a little as my eyes move across the canvas, seeing through Eileen's eyes how she sees me."

"As I stand gazing at the painting, I feel a coat come over me, Eileen draping it over my shoulders. I'm about to thank her, before the words are stolen from my mouth by her different demeanor."

show misc paintings allison:
    zoom 0.9 xalign 0.5
    yoffset 25 alpha 1
    ease 1.2 xalign 0.75
show eileen indoors_fists lookawaynarrow sadmouth blush at leftish:
    zoom 1.3 yoffset 300
    xpos 0.28 alpha 0
    ease 1.5 alpha 1
"Compared to her intense focus while painting, her gaze awkwardly avoids my appreciative expression. All I can do is smile as I clasp the coat tight, the bashful Eileen standing in silence beside me."

stop music fadeout 3.0
$ _dismiss_pause = False
allison "It's beautiful."

window hide dissolve
scene black with longDissolve
return
