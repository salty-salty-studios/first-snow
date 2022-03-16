label scene_1S6_en:
######################
# Act 1, Scene 6

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg buildingunion cafeteria snow sketch:
    xalign 0.5 yalign 0.5
$camera_move(-850,-200,450,0,0,'dissolve')
with inkfade
scene bg buildingunion cafeteria snow:
    xalign 0.5 yalign 0.5
$camera_move(-850,-200,450,0,0,'dissolve')
with inkfade2
play ambiance "sfx/ambiance/crowd_cafetaria.ogg" fadein 0.1
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True
"The cafeteria hums away as students talk amongst themselves, the room having mostly filled up by now. The thought briefly passes my mind that winter must be great for business, given this being the closest place for cheap food during bad weather."

show bg buildingunion cafeteria snow moreblur as cafeteria_snow_moreblur:
    xalign 0.5 yalign 0.5
    alpha 0
    ease 0.5 alpha 1
window show
$ phone.show('unlock')
"Some smears on the edges of the plate are all that remains of the mostly-cooked pasta served today, what's left of my accompanying soda bubbling away while I pass some time browsing this site and that."

show eileen indoors_onhip normal neutral blur at rightish:
    xpos 1.0
    ease 1.0 xpos 0.7
"As I read, a shadow suddenly looms over the other side of the table. Looking up from my phone reveals a very familiar figure."

$ phone.hide()
show bg buildingunion cafeteria snow moreblur as cafeteria_snow_moreblur:
    xalign 0.5 yalign 0.5
    alpha 1
    ease 0.5 alpha 0
show eileen indoors_onhip normal neutral at rightish
$ renpy.transition(dissolve, layer='master')
window hide
"Eileen peers down as she stands at the opposite side of the table, a large plate of food steaming away in her hand. The fresh pasta sauce is strong enough to smell from here."

show eileen open at rightish
$ renpy.transition(dissolve, layer='master')
eileen "Okay to sit here?"

show eileen neutral at rightish
$ renpy.transition(dissolve, layer='master')
voice "Allison_NervousHi3.ogg"
allison "Ah, sure!"

$ renpy.music.set_volume(0.4, delay=3, channel='ambiance')
play music "music/anxiety_2_m.ogg" fadein 3.0
$camera_move(0,0,0,0,5,'ease')
play sound "sfx/chair_scrape.ogg"
show eileen indoors_fists closed at rightish:
    yoffset 0
    ease 3.0 yoffset 50
"I quickly set my phone down as she takes a seat and arranges her tray on the table, happy that she'd choose to sit with me."

"A glance around to see if anyone's with her makes me realize why she probably chose to sit here; the cafeteria's practically full, and this is simply the nearest table with space available."

show eileen indoors_fists normal at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
"About to take her first gulp of food, Eileen's fork halts midair before saying something."

stop sound fadeout 1.0
show eileen indoors_crossed lookaway open at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "Cold any better?"

allison "Yeah, clearing up now."

show eileen closed grumble at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
eileen "Good to hear."

show eileen indoors_onhip normal at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
window show
"With that, she starts on her pasta and salad."

show bg buildingunion cafeteria snow moreblur as cafeteria_snow_moreblur:
    xalign 0.5 yalign 0.5
    alpha 0
    ease 0.5 alpha 1
show eileen indoors_onhip normal grumble blur at rightish with dissolve:
    yoffset 50
$ phone.show('unlock')
"As I take my phone to browse some more, and Eileen calmly eats the average-at-best cafeteria food, it feels as though there's no need to chat just to fill the air. That silence between us is becoming more comfortable."

"That is, before I get a message."
$ phone.message('rose', '1:05 PM', 'Can\'t make dinner, work sucks')
$ phone.show('messages', who='rose')
"Flicking away the browser app, I take a quick look."

window hide
$ phone.message('rose', '1:05 PM', 'you were getting groceries yesterday right?', to=True)
$ phone.wait()
$ phone.message('rose', '1:06 PM', 'anything in the fridge? :s', to=True)
$ phone.wait()
"Seconds tick by as I wait for a response, a sense of concern starting to take over."

$ phone.message('rose', '1:08 PM', 'rose', to=True)
$ phone.wait()
$ phone.message('rose', '1:12 PM', 'rose', to=True)
$ phone.wait()
$ phone.message('rose', '1:13 PM', 'Sorry')
$ phone.wait()
$ phone.message('rose', '1:13 PM', 'rose', to=True)
$ phone.wait()
$ phone.message('rose', '1:14 PM', 'Work needs me, see you later')
$ phone.wait()
window show
$ phone.hide()
show bg buildingunion cafeteria snow moreblur as cafeteria_snow_moreblur:
    xalign 0.5 yalign 0.5
    alpha 1
    ease 0.5 alpha 0
show eileen indoors_onhip disbelief frown at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
window hide
voice "Allison_Sigh2.ogg"
"All I can do is sigh and slump down in my seat as I lay my phone on the table."

"Eileen looks at me in puzzlement, her fork hovering near her mouth."

show eileen disbelief open at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "Bad news?"

show eileen neutral at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hm4.ogg"
allison "Roommate forgot to do groceries. We're out of food."

show eileen indoors_crossed narrow at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
eileen "Can't you just grab a burger on the way home?"

"That would be the plan... if I wasn't nearly through my allowance. I just look away and groan, not up to outright saying that I'm broke."

show eileen sad frown at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
eileen "It's that bad, huh?"

show eileen indoors_fists lookawaynarrow frown at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
"At first glance, she shrugs off as she goes back to eating, but she seems to actually be in thought after watching her a bit."

show eileen indoors_fists closed at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
"Eventually, after finishing her food, she speaks up."
voice "Eileen_Hmm1.ogg"
eileen "I guess I was cooking some extra anyway..."

show eileen indoors_onhip normal open at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
eileen "You can come over for dinner if you want. It's within walking distance."

show eileen neutral at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
"The suggestion's enough to make me bolt upright in an instant."

allison "What, to your place?"

show eileen normal open at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
eileen "Yeah. Should be fine, right? You okay with stir fry?"

show eileen neutral at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
voice "Allison_ThankYou.ogg"
allison "I... yes. Thank you. Thank you so much. I really, really appreciate this."

show eileen indoors_crossed disbelief open at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble2.ogg"
eileen "Sure, whatever. Just don't make it weird."

show eileen angry at rightish:
    yoffset 50
$ renpy.transition(dissolve, layer='master')
stop ambiance fadeout 3.0
stop music fadeout 3.0
"Considering the discussion over, Eileen goes back to finishing off her food without much concern for what she's just said. Maybe she does have a good side."

scene black with longDissolve
$ renpy.music.set_volume(1.0, channel='ambiance')
play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
scene bg apteileen outside with dissolve
"Stopping before the large black door, I repeat the address Eileen gave me to reassure myself I've come to the right place. Eileen's definition of 'walkable' is apparently rather different than mine, still catching my breath from the hike."

"I thought I was going to be fine, but my nerves are getting the better of me now that I'm here. I'm going into a near-stranger's home, after all, and it'll be just the two of us. In school we just happened to be around each other, but this is entirely different."

"Glancing down the hall to make sure nobody's watching me awkwardly loiter around, I take a moment to appreciate how nice her apartment building is. This is a nice area, and everything inside is immaculate. Even the hallway carries a slight scent of cleaning products."

$camera_move(1550,200,450,0,4,'ease')
pause 4.0
play sound "sfx/eileen_doorbell.ogg"
"Out of excuses to stall any longer, I take a breath and gingerly press the doorbell, its muffled chime ringing out from behind the door."

"I run my hands through my hair one more time to make sure I look presentable as footsteps come to the door."

play sound "sfx/door_open2.ogg"
"The plain wooden door swings open, answered by-"

show wallace indoors heightened open neutral at centerright:
    zoom 0.6 yoffset -250
    xpos 0.75 alpha 0
    ease 0.8 xpos 0.68 alpha 1
"-not Eileen."

stop sound fadeout 1.0
voice "Allison_Um1.ogg"
allison "Uh-"

show wallace even open smile at centerright:
    xpos 0.68 alpha 1
$ renpy.transition(dissolve, layer='master')
voice "Wallace_Hey2.ogg"
wallace "Oh, 'evening."

show wallace heightened forward neutral at centerright:
    zoom 0.6 yoffset -250
    xpos 0.68 alpha 1
    linear 0.7 xzoom -1 xpos 0.65
"Before I can ask if I got the right apartment, he turns around."

show wallace heightened forward mopen at centerright:
    xzoom -1 xpos 0.65
wallace "Allison's here!"

show wallace even closed neutral at centerright:
    xpos 0.65
$ renpy.transition(dissolve, layer='master')
"Wallace jerks his head around for me to follow. I obediently do so, still too confused to get a word out."

show wallace at centerright:
    zoom 0.6 yoffset -250
    xzoom -1 xpos 0.65 alpha 1
    ease 0.8 xpos 0.72 alpha 0
$camera_move(2550,450,850,0,4,'ease')
stop ambiance fadeout 4.0
"Eileen didn't mention he would be here. I don't know how I feel about it. Maybe I should be relieved it's not just the two of us."

play sound "sfx/door_close2.ogg"
play ambiance "sfx/ambiance/water_boiling.ogg" fadein 2.0
play music "music/eileen_5_m.ogg" fadein 5.0
scene bg apteileen livingroom:
    subpixel True
    xalign 0.0
    ease 5.0 xalign 1.0
show wallace indoors even open neutral at midright:
    subpixel True
    alpha 0.0
    xpos 0.9
    parallel:
        ease 3.0 alpha 1.0
    parallel:
        ease 5.0 xpos 0.7
with fadeInOut
$ camera_reset()
"Barely noticing the thud of the door closing behind me, I take a quick glance around her apartment as I place my coat on the counter. The first striking thing is how clean it is, with everything put neatly in its place."

stop sound fadeout 1.0
"Then again, aside from a few paintings on the walls that are possibly her own, there's not much clutter around to clean up."

"The television - quite a decent size for a student's - sits on a cable news channel. Riveting as the economic situation report is, it's barely audible over the clacking rice cooker coming from the kitchen."

show bg:
    subpixel True
    xalign 1.0
    ease 3.0 xalign 0.5
show wallace indoors even closed neutral at right2:
    subpixel True
    xpos 0.7 alpha 1.0
    ease 3.0 xpos 0.78
show eileen indoors_onhip closed open at leftside:
    xzoom -1
    xpos -0.2
    ease 3.0 xpos 0.15
"As Wallace and I stride in, Eileen comes to her feet after having been on the couch. She lazily covers a deep yawn with her hand as she does."

scene bg apteileen livingroom:
    xalign 0.5
show wallace indoors neutral closed even at right2:
    xpos 0.78
show eileen indoors_onhip normal neutral at leftside:
    xzoom -1
    xpos 0.15
$ renpy.transition(dissolve, layer='master')
voice "Allison_NervousHi2.ogg"
allison "Um, hi."

show wallace forward at right2:
    xpos 0.78
show eileen indoors_onhip lookaway open at leftside:
    xzoom -1
    xpos 0.15
$ renpy.transition(dissolve, layer='master')
eileen "So you managed to find the place. Welcome to my home, I guess."

show eileen narrow at leftside
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "I'd introduce you to this guy as well, but it seems you two already know each other."

show eileen neutral at leftside
show wallace open neutral at right2:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
"Wallace and I exchange a brief glance."

show wallace mopen at right2:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
wallace "Just had a coffee together once."

show eileen disbelief neutral at leftside
show wallace forward smile at right2:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
"While I did find his size intimidating at first, he seems a bit of a gentle giant figure now that I'm around him more. Looks like this isn't going to be dinner for just me and Eileen, then."

"Taking one last glance about, the inside of her place is as nice as the outside. From the meticulous cleanliness to the trendy furniture, her home looks more suited to a design magazine than a student's living area."

allison "Your apartment's really nice."

show eileen indoors_crossed closed neutral at leftside
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Thanks1.ogg"
eileen "Thanks. I like to try and keep things organized."

show wallace even halfopen smile at right2:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
voice "Wallace_Yeah1.ogg"
wallace "Especially when visitors are over."

show eileen indoors_crossed annoyed angry at leftside
show wallace even closed at right2:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
"Eileen glares daggers at Wallace, but he doesn't pay any heed. The two seem to have a good handle on each other."

show eileen lookawaynarrow open at leftside
$ renpy.transition(dissolve, layer='master')
eileen "Moving on... Wallace, just watch TV or something while we get dinner sorted."

show wallace open mopen at right2:
    xpos 0.78
$ renpy.transition(dissolve, layer='master')
wallace "Can do."

show wallace open neutral at right2:
    linear 0.7 xzoom -1 xpos 0.72
    ease 1.5 xpos 1.2
pause 0.8
$camera_move(-2500,-200,400,0,4,'ease')
show eileen indoors_onhip normal neutral at leftside:
    xpos 0.15
    ease 2.0 xpos 0.3
allison "Thanks again for letting me have dinner with you."

show eileen indoors_onhip closed open at leftside:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
eileen "Don't get too comfortable; I'm going to make you work for your food."

show eileen indoors_onhip closed open at leftside:
    xpos 0.3
    nod2
"Eileen motions for me to come over with her, but the gesture was unnecessary given her commanding tone. Wallace gives a dreary glance as he follows his orders, and I quickly do the same."

scene bg apteileen livingroom HD
$camera_move(-8500,-2000,0,0,0,'dissolve')
with fadeInOut
show bg apteileen livingroom HD blurred5
with midDissolve
show cutin cutboard:
    xcenter -0.01 ycenter -0.5
    ease 1.0 ycenter 0.2
"I end up standing before a well-used wooden cutting board, taking the large knife Eileen offers before sizing up the variety of vegetables awaiting its blade."

"I don't think she notices my hesitation as she opens the rice cooker and gives the contents a stir."

play sound "sfx/knifechops.ogg" loop
"The two of us waste little time in getting to work, the sound of food being prepared filling the room."

"Unfortunately, it isn't long before I've earned Eileen's ire."

$ renpy.music.set_volume(0.0, delay=1.0)
stop sound fadeout 1.0
with vpunch
voice "Eileen_No4.ogg"
eileen "Stop!"

stop sound fadeout 1.0
show cutin cutboard:
    xcenter -0.01 ycenter 0.2
    ease 1.0 xcenter -0.15
with None
show bg apteileen livingroom HD blurred2:
    xalign 0.5 yalign 0.5
$ renpy.transition(dissolve, layer='master')
show eileen indoors_crossed annoyed open at right2:
    alpha 0 xpos 0.8
show eileen indoors_crossed annoyed angry at centerleft as eileen2 with dissolve:
    zoom 1.2 yoffset 0
    xpos 0.32
"My heart practically leaps out of my chest as I immediately freeze, hands retreating from the cutting board."

show eileen indoors_crossed annoyed open at centerleft as eileen2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
eileen "Did I hand you a hatchet?"
voice "Allison_Hm2.ogg"
allison "No..."

show eileen indoors_crossed narrow at centerleft as eileen2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
eileen "Then why are you using that as one? It looks like you're trying to lop off some fingers."

play sound "sfx/knifechops.ogg" loop
$ renpy.music.set_volume(1.0, delay=5.0)
show eileen indoors_crossed narrow at centerleft as eileen2:
    xpos 0.32
    nod2
    repeat 2
"In response to my puzzled look, she takes the knife off me and starts demonstrating the correct technique herself."

show eileen indoors_fists disbelief frown at centerleft as eileen2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
eileen "Thought you'd be more help than him in fixing this up... Look, curl your hand in next to where you want to cut like this."

show eileen normal neutral at centerleft as eileen2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
eileen "Now use the knife like a lever, instead of wildly hacking away. We're making nice, slow slices, not some slasher B-movie scene."

stop sound fadeout 1.0
voice "Allison_Okay.ogg"
allison "Right, I think I have it."

show eileen indoors_onhip at centerleft as eileen2:
    xpos 0.32
$ renpy.transition(dissolve, layer='master')
"Eileen hands the knife back, and after a breath to steady myself, I have another try."

play sound "sfx/knifechops.ogg" loop
scene cg act1 cooking
$camera_move(-3200,1550,850,0,0,'dissolve')
with midDissolve
$camera_move(-3200,-250,850,0,6,'ease')
"She soon starts frowning as I slice away, but at least she's not yelling at me again."

show cg act1 cooking2 with dissolve
eileen "I'm guessing you don't cook for yourself?"

"Her eyes rest on the collection of lopsided shapes sitting before me."

stop sound fadeout 1.0
show cg act1 cooking
$camera_move(1200,0,450,0,6,'ease')
allison "I'm lucky if I don't mess up instant noodles."

show cg act1 cooking2 with dissolve
voice "Eileen_Huh1.ogg"
eileen "I thought those were impossible to get wrong. I'm genuinely impressed."

show cg act1 cooking happy2 with dissolve
voice "Allison_Hmwithquestionmark.ogg"
allison "You do all your own cooking?"

$camera_move(0,0,0,0,10,'ease')
show cg act1 cooking happy
eileen "Not like I have anyone else to cook for me. Healthier than living off pizza and burgers, too."

show cg act1 cooking happy2 with dissolve
allison "What about Wallace? Aren't you roommates?"

show cg act1 cooking happy with dissolve
eileen "No, he just loafs around here sometimes. I've tried to get him to help, but he's no better than you are. I'm always feeding him, and letting him crash on my couch. He even bugs me for free pictures for his writing."

show cg act1 cooking happy2
"She sets down her knife in genuine, if depressing, thought."

scene black with midDissolve
scene bg apteileen livingroom HD
$camera_move(-8500,-2000,0,0,0,'dissolve')
show eileen indoors_crossed frown narrow as eileen2 at leftedge:
    zoom 0.7 yoffset -450
    xpos 0.02
show eileen indoors_crossed frown narrow at centerright:
    alpha 0
with midDissolve
voice "Eileen_Hmm1.ogg"
eileen "Maybe we should just become roommates..."

"I think I'm starting to get a handle on their relationship, now. As strange a pair as they might seem, the stern and uncompromising Eileen and gentle giant Wallace seem like they're a compatible couple."

allison "I'm surprised you're not; I thought you might be together."

show eileen indoors_onhip closed neutral as eileen2 at leftedge:
    xpos 0.02
$ renpy.transition(dissolve, layer='master')
eileen "Nope, just friends."

show wallace indoors even open neutral at rightoffscreen:
    alpha 0
show wallace indoors even forward neutral as wallace2 at rightish:
    xzoom -1
    zoom 0.85 yoffset -100
    xpos 0.68 rotate -5
"So much for that. She waves away the idea so easily that it must've come up before. In fact, back at the café Wallace seemed quick to clarify that too."

$camera_move(-2000,-2000,0,0,4,'ease')
show eileen indoors_onhip normal neutral as eileen2 at leftedge:
    xpos 0.02
"Wallace's voice pipes up from behind us."

show wallace indoors even halfopen smile as wallace2 at rightish:
    xpos 0.68 rotate -5
$ renpy.transition(dissolve, layer='master')
wallace "You know, it's not often Eileen invites someone else over for dinner."

show wallace indoors even open smile as wallace2 at rightish:
    xpos 0.68 rotate -5
show eileen indoors_onhip normal open as eileen2 at leftedge:
    xzoom 1 xpos 0.02
    linear 0.7 xzoom -1 xpos -0.01
show eileen indoors_crossed frown narrow at leftedge:
    alpha 0
eileen "I don't invite anyone over for dinner; you just show up, most of the time."

show eileen indoors_crossed narrow as eileen2 at leftedge:
    xzoom -1 xpos -0.01
$ renpy.transition(dissolve, layer='master')
eileen "Including now, actually."

show eileen closed angry as eileen2 at leftedge:
    xzoom -1 xpos -0.01
$ renpy.transition(dissolve, layer='master')
eileen "I've had to put up with him like this since high school. I guess no one else would."

show wallace indoors even halfopen mopen as wallace2 at rightish:
    xpos 0.68 rotate -5
$ renpy.transition(dissolve, layer='master')
wallace "Objection! I'm the one who puts up with you."

show wallace indoors even halfopen neutral as wallace2 at rightish:
    xpos 0.68 rotate -5
show eileen narrow frown as eileen2 at leftedge:
    xzoom -1 xpos -0.01
$ renpy.transition(dissolve, layer='master')
eileen "I'm the one currently holding a knife."

show wallace indoors heightened halfforward frown as wallace2 at rightish:
    xpos 0.68 rotate -5
$ renpy.transition(dissolve, layer='master')
wallace "...Objection withdrawn."

show wallace indoors heightened closed frown as wallace2 at rightish:
    xpos 0.68 rotate -5
show eileen indoors_onhip narrow frown as eileen2 at leftedge:
    xzoom -1 xpos -0.01
    linear 0.7 xzoom 1 xpos 0.02
$camera_move(-8500,-2000,0,0,4,'ease')
"With that, he goes back to quietly watching television."

stop ambiance fadeout 3.0
scene bg apteileen livingroom
show bg apteileen livingroom blurred2:
    xalign 0.5 yalign 0.5 alpha 0.95
show eileen indoors_onhip normal neutral at center:
    zoom 1.2 yoffset 180
    xpos 0.5
with midDissolve
$ camera_reset()
show shadow:
    alpha 0
    ease 2.0 alpha 0.4
"I'm starting to get how Eileen deals with others in general, now; she simply has no filter when it comes to stating what she believes to be true."

"That can be a problem just as much as shyness, though. Thinking back to when we met, the only reason I didn't write the episode with her off is Caprice and Wallace nudging me afterwards."

"But here she is, looking after her friend and providing me with a meal. It took a while, but I'm glad I met her in the end. Perhaps that's why it's a little worrisome that she lives alone like this."

show shadow:
    alpha 0.4
    ease 1.0 alpha 0
voice "Allison_Um1.ogg"
allison "You normally do all this without anyone to help?"

show eileen indoors_crossed lookaway open at center
$ renpy.transition(dissolve, layer='master')
eileen "You don't need to say that like it's a bad thing. There's all sorts in the world, some are better with people than others. Living alone suits me, and I can afford it."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "You know Caprice though, don't you? So you're not completely alone besides Wallace."

show eileen indoors_onhip narrow at center
$ renpy.transition(dissolve, layer='master')
"Maybe I shouldn't have said that."

show eileen open at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble3.ogg"
eileen "Tell me, how did you and Caprice meet?"

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hm3.ogg"
allison "We were sitting at the same table for a biology lecture, and she started passing me notes during class out of the blue. Once we started talking afterwards, she didn't really stop."

allison "...Ah."

show eileen closed frown at center
$ renpy.transition(dissolve, layer='master')
eileen "That's the way it goes with her. Once you get caught in her orbit, she doesn't let you go."
voice "Allison_NervousLaugh.ogg"
allison "Caprice isn't that bad. She's a sweet person, just... high energy."

show eileen lookaway neutral at center
$ renpy.transition(dissolve, layer='master')
"She gives a noncommittal grunt before getting on with her cooking. I do wish she'd give her a chance; Caprice does only mean the best for her."

show eileen normal neutral at center:
    xpos 0.5
    ease 1.0 xpos 0.25
eileen "Moving away from that, could you grab the plates and glasses? These shouldn't take long to fry."

stop music fadeout 10.0
show wallace indoors even open smile at rightedge:
    xpos 1.15 yoffset 55 rotate 0
    ease 1.0 xpos 1.0 rotate -15
wallace "Root beer, please!"

show eileen indoors_crossed narrow open at center:
    xzoom 1 xpos 0.25
    linear 0.7 xzoom -1 xpos 0.2
voice "Eileen_No2.ogg"
eileen "Water is healthier."

show wallace indoors heightened halfopen frown at rightedge:
    yoffset 55 xpos 1.0 rotate -15
show eileen neutral at left2:
    xzoom -1 xpos 0.2
$ renpy.transition(dissolve, layer='master')
voice "Wallace_Allison5.ogg"
wallace "Allison, please save me from this woman."

"All I can do is give a weak smile. Much as I'd like to give him what he asks for, following Eileen's orders would probably be for the best."

scene black with circlewipe
$ camera_reset()
play music "music/dozy_comfy.ogg" fadein 3.0
scene bg apteileen livingroom with circlewipe
"With all of us well and truly full, we sit around the table and savor the meal we've had. It was the best food I've had in a while, since it was neither take-out nor cooked by Rose."

"Having sent a text message to her for a pickup, all that's left is to run down the clock as the evening wears on."

scene bg apteileen livingroom
$camera_move(2200,1200,600,0,0,'dissolve')
$ renpy.transition(dissolve, layer='master')
$camera_move(2200,-1200,600,0,7,'ease')
"Looking around the apartment, I point to one of the paintings on the wall."

allison "Did you paint all these?"

show eileen indoors_onhip lookawaynarrow angry as eileen2 at offcenterleft:
    xzoom -1
    zoom 0.65 yoffset -335
    xpos 0.45
$ renpy.transition(dissolve, layer='master')
show eileen indoors_onhip neutral normal at left:
    alpha 0
eileen "Yeah. Really need to find something else to put up there, though."
voice "Allison_Huh2.ogg"
allison "But why? They're really good!"

show eileen indoors_crossed neutral disbelief  as eileen2 at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "I appreciate the thought. All of them have dumb little mistakes, though. Just needed something to make the walls less bare when I moved in, and never got around to replacing them."

allison "You like painting people in particular, don't you?"

show eileen normal open as eileen2 at offcenterleft
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "Just into portraits and figures. Modern art's all well and good, but I started with figure drawing and ended up attached to it."

show eileen closed open as eileen2 at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Bodies are pretty fascinating when you think about them. Really think about them, that is. I've spent days just sitting there sketching, trying to work out how the muscles fit together, how lighting interacts with skin, and all that."

"The way she rattles off her thoughts with such feeling gives away how much she cares about the subject. I can't say I take it quite as seriously as she does, but I can see where she's coming from."

scene bg apteileen livingroom
show eileen indoors_onhip normal neutral at left2:
    xzoom -1
show wallace indoors heightened open smile at right2
with fadeInOut
voice "Wallace_Hmm.ogg"
wallace "Interested in this stuff, Allison?"

allison "Me? I just drew a little in high school. Passing the time, that kind of thing."

show wallace even closed at right2
$ renpy.transition(dissolve, layer='master')
wallace "Nothing wrong with that. I sketch on my tablet, and Eileen gives pointers sometimes."

show eileen annoyed smile at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh1.ogg"
eileen "Maybe I should throw you to the wolves and tell Caprice you like doing art as well."

show wallace heightened halfsmall frown at right2
$ renpy.transition(dissolve, layer='master')
voice "Wallace_Sigh6.ogg"
wallace "You wouldn't."

show eileen indoors_crossed smile narrow at left2
$ renpy.transition(dissolve, layer='master')
eileen "I'm thinking about it."

show wallace upturned closed mopen at right2
$ renpy.transition(dissolve, layer='master')
"I can't help but giggle a bit at the two of them."

"Yet even as they do, there's a small pang of envy there. I can empathize with Eileen keeping her group of friends small, but I do wish I were closer to her. In more ways than one, she's who I wish I could be."

$ renpy.sound.set_volume(0.5, delay=0)
play sound "sfx/bike_horn.ogg"
show eileen indoors_onhip disbelief neutral at left2
show wallace indoors neutral open even at right2
$ renpy.transition(dissolve, layer='master')
"The familiar sound of a motorbike's horn can be faintly heard from outside, bringing an end to both my thoughts and this little outing."

$ renpy.sound.set_volume(1.0, delay=0)
show eileen open at left2
$ renpy.transition(dissolve, layer='master')
eileen "That for you?"

show wallace indoors even open smile at right2
show eileen indoors_onhip neutral normal at left2
$ renpy.transition(dissolve, layer='master')
stop sound fadeout 1.0
"Giving a nod, I get up from my chair and collect my coat from Eileen's helpful hand, quickly throwing it over myself."
voice "Allison_ThankYou.ogg"
allison "Thanks for tonight, it was nice."

stop music fadeout 5.0
show wallace indoors even closed smile at right2:
    nod
"Not wanting to keep Rose waiting, I wave Wallace goodbye as I take my leave, with Eileen coming along to see me out at the door."

play sound "sfx/door_open2.ogg"
play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
scene bg apteileen outside
$camera_move(2550,450,850,0,0,'dissolve')
show eileen indoors_crossed normal frown at centerright:
    zoom 0.6 yoffset -250
    xpos 0.68
with fadeInOut
eileen "Got everything with you?"

"I quickly pat around my pockets to make sure. Phone, purse, keys, they all seem to be there."

allison "All good."

show eileen indoors_crossed closed open at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
eileen "I'll see you, then. If you want to come around again, feel free."

show eileen normal neutral at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
allison "If I'm not too much trouble, that'd be nice."

"I do a poor job of hiding my happiness at the offer, my reply just a little too quick to sound natural."

show eileen indoors_onhip lookawaynarrow open at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
eileen "Believe me, you're no trouble. It honestly does me good to see you a bit more upbeat."

"I tilt my head a little at the odd idea."

show eileen normal smile at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
eileen "You just seemed kind of skittish before, but now you're all sunshine and rainbows. It suits you."

allison "Ah, sorry. I'm a bit shy."

"Not to mention a bit homesick. Being able to talk with friends outside of school was a nice change, not to mention having a homemade meal. Even if I didn't help that much, it did take my mind off things."

$camera_move(1550,200,450,0,4,'ease')
"Eventually, as my mind slowly manages to get back into gear, I muster the words to say what I want to tell her as I get past being so flustered."

allison "If you don't mind me being around for dinner, maybe being together in a club wouldn't be so bad?"

show eileen indoors_crossed narrow neutral at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
"She hesitates for a good few moments, making me doubt myself as I offer the suggestion as carefully as possible. She knows I like her as a person, so hopefully she can look past her previous experiences."

show eileen indoors_crossed closed open at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
"Just as I begin to think I've overstepped the mark, she gives an almost comically long sigh."

play sound "sfx/bike_horn.ogg"
"The horn sounds again in the distance as silence reigns, but my feet stay plastered as she comes to an answer."

show eileen indoors_crossed lookawaynarrow frown at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
eileen "Fine. Tell Caprice she can have her dumb club."

stop sound fadeout 1.0
allison "Thank you!"

show eileen indoors_onhip open at centerright:
    xzoom 1 xpos 0.68
    linear 0.7 xzoom -1 xpos 0.65
pause 0.8
eileen "Just don't make me regret it."

show eileen closed frown at centerright:
    xzoom -1 xpos 0.65 alpha 1
    ease 0.8 xpos 0.72 alpha 0
play sound "sfx/door_close2.ogg"
"With an enthusiastic nod and a wave, I start off down the hallway once more, Eileen disappearing into her apartment as I look back."

$camera_move(-1500,250,850,0,4,'ease')
stop ambiance fadeout 4.0
stop sound fadeout 1.0
$ _dismiss_pause = False
"Even as I walk down the hallway, my steps somehow feel lighter than they did as I entered. Being around others usually makes me exhausted, but right now, I feel more comfortable than ever."

window hide dissolve
scene black with longDissolve
$ camera_reset()
return
