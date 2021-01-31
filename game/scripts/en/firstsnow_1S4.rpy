label scene_1S4_en:
######################

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg buildingmisc library sketch:
    xalign 1.0
with inkfade
scene bg buildingmisc library:
    xalign 1.0
with inkfade2
stop sound fadeout 0.1
play ambiance "sfx/ambiance/crowd_silent.ogg" fadein 1.0
window show dissolve
$ _dismiss_pause = True
"With the weather turning worse and worse as the week went on, the library seemed as good a place as any to spend some time before having lunch. Unfortunately, it looks like I wasn't the only one who had that idea."

"While the library here is bigger than my previous school's, that doesn't matter much when a large portion of the students are dumped inside. While my first choice would've been using one of the computers, that's obviously out of the question."

play music "music/anxiety_2_m.ogg" fadein 3.5
scene bg buildingmisc library:
    xzoom -1 xalign 1.0
$camera_move(3400,-1200,800,0,0,'dissolve')
with dissolve
$camera_move(-3400,-1200,800,0,20,'ease')
"Worried about looking like a dork as I loiter about, I start walking slowly through the library. Thankfully, nobody pays me much attention while I glance from side to side for an empty table or desk."

"The students who're actually studying seem to be outnumbered by those gossiping with friends or catching up on sleep."

"It's only in a far corner of the room that I catch a familiar face, albeit not necessarily a welcome one."
window hide dissolve

scene bg buildingmisc library HD
show bg buildingmisc library HD blurred2 as bg2:
    xalign 0.5 yalign 0.5 alpha 0.65
$camera_move(-1500,-2750,850,0,0,'dissolve')
show eileen indoors_fists narrow angry at left2:
    xzoom -1
    zoom 0.35 yoffset -655
    xpos 0.3
show bg buildingmisc library table as library_table:
    xalign 0.5 yalign 0.5
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.13
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.525
with fadeInOut
letterbox "Eileen sits hunched over a thick textbook, occasionally scribbling into a small notebook beside it as her finger stops every so often on one important part or another. It's hard to tell if she's annoyed or just studying hard."

show eileen indoors_crossed closed open at left2:
    xzoom -1
    zoom 0.35 yoffset -655
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
letterbox "I consider leaving Eileen to her studying and braving the weather outside, before she rubs her temple and looks down mournfully at her notebook. That pose is all too familiar for any student."

letterbox "I feel a little bad for her. Given the vending machine problems and how she wound up with Caprice stuck to her, she doesn't seem to have very good luck. She might not be the friendliest person, but if I could help her a bit..."

stop music fadeout 4.0
scene bg buildingmisc library:
    xalign 0.0 zoom 1.0
show bg buildingmisc library:
    subpixel True
    xalign 0.0 zoom 1.0
    parallel:
        ease 4.0 zoom 1.1
    parallel:
        ease 1.0 yoffset 1
        ease 1.0 yoffset -1
        repeat 2
show eileen indoors_onhip normal neutral at centerleft:
    subpixel True
    zoom 0.7 xpos 0.48 ypos 0.68 yoffset 50
    parallel:
        ease 4.0 zoom 1.0 xpos 0.5 ypos 1.0
    parallel:
        ease 1.0 yoffset 51
        ease 1.0 yoffset 49
        ease 1.0 yoffset 51
        ease 1.0 yoffset 50
with fadeInOut
$ camera_reset()
window show dissolve

"With Wallace's words weighing on my mind, I grimace and accept my fate as I begin walking to the otherwise empty table. She looks up and catches my eye as I come near, so I guess I'm committed to this now."

play music "music/eileen_5_m.ogg" fadein 3.0
show eileen indoors_onhip normal open at center:
    zoom 1.0 xpos 0.5 ypos 1.0 yoffset 50
$ renpy.transition(dissolve, layer='master')
eileen "'Afternoon."

"My existence has been noted. I don't think that could sound any more perfunctory, but at least she isn't shooing me away."

play sound "sfx/chair_scrape.ogg"
show bg:
    subpixel True
    zoom 1.1 xalign 0.0 yoffset 0
    ease 2.0 yoffset -50
show eileen normal neutral at center:
    subpixel True
    ypos 1.0 yoffset 50
    ease 2.0 yoffset 0
"Setting my bag beside my chair as I take a seat, I pull out my phone to check for any missed messages and switch it to silent before placing it on the table before me."

allison "Hi. Surprised you're not in the art room."

stop sound fadeout 1.0
show eileen indoors_onhip narrow neutral at center
$ renpy.transition(dissolve, layer='master')
eileen "I don't live there, you know."

allison "Wouldn't it be more private than here, though?"

show eileen indoors_crossed closed frown at center
$ renpy.transition(dissolve, layer='master')
"She lets out a long, miserable groan as her head sinks. Hardly difficult to work out what that means."

show eileen narrow frown at center
$ renpy.transition(dissolve, layer='master')
eileen "Caprice wouldn't stop bugging me to join her drawing for some stupid theme."

allison "What was it?"

show eileen lookawaynarrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "I wasn't really listening. Christmas scenes or something."

show eileen lookawaynarrow angry at center
$ renpy.transition(dissolve, layer='master')
"She's barely even listening to me as she tries to wave me off. Caprice is probably scurrying around campus as we speak, hoping for me to join her as a drawing partner."

allison "What're you studying?"

show eileen sad open at center
$ renpy.transition(dissolve, layer='master')
eileen "Math. It's been kicking my ass, so I need to get my head around it for these stupid gen-ed classes."

show eileen sad neutral at center
$ renpy.transition(dissolve, layer='master')
"Eileen barely lifts her head up from the notebook as she speaks. Looking over the table at her work, various practice equations cover the notebook's page."

"I have to admit, I do admire Eileen's drive. I was just going to pass some time in the library reading, but seeing her working away has made me feel a little guilty."

show eileen indoors_onhip normal neutral at center
$ renpy.transition(dissolve, layer='master')
eileen "You any good at this stuff?"

allison "Math? Well, I ended up skipping the gen-ed class thanks to my placement exam results."

show eileen indoors_crossed lookaway open at center
$ renpy.transition(dissolve, layer='master')
eileen "Someone spent their time studying like a good little teacher's pet."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "Nothing like that. Math and science are easy enough, so I ended up coasting along. I need to learn how to study now that I'm here."

show eileen narrow at center
$ renpy.transition(dissolve, layer='master')
"Eileen's eyes narrow. Maybe she wasn't exaggerating about her skills; after having such an easy time in high school, it's easy to forget I'm the odd one out here. Of course I'd put my foot in my mouth just as I was starting to break the ice with her."

allison "I mean, uh... If you want, I could have a look at your work?"

show eileen indoors_onhip closed neutral at center:
    xzoom 1 xpos 0.5
    ease 1.2 xpos 0.3 zoom 1.05 yoffset 50
"She's hardly enthusiastic, but shrugs and moves herself a little out of the way. My curiosity's gotten the better of me. Coming around the table and looking at the notebook from behind her, I take a gander at her notes so far."

show bg buildingmisc library blurred2 as bg2 behind eileen:
    zoom 1.1 xalign 0.0 yalign 0.5 yoffset -50
    alpha 0
    ease 1.5 alpha 0.85
show shadow:
    alpha 0
    ease 1.5 alpha 0.4
show note homework:
    subpixel True
    xalign 0.85 xoffset 850 alpha 0
    ease 1.5 xoffset 0 alpha 1
pause 1.5
"At least this is easy to read, given her immaculate handwriting. The more I check over her notes though, the more the corners of my mouth drag down."

show eileen indoors_onhip normal neutral at centerleft:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
"She's done a good job of showing her process, and the first couple of questions covering expressions look right at a glance. When it comes to polynomials, however, the next two have odd leaps of logic, while the last meanders off into the wilderness."

show eileen indoors_onhip frown disbelief at centerleft:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
"I realize I should say something to express how she's done so far, but the window of time to say something even mildly positive to soften the blow has long since passed."

show shadow:
    alpha 0.4
    ease 1.0 alpha 0
show eileen indoors_crossed at centerleft:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
eileen "So it's like that, huh?"

allison "You got some of it right."

show eileen frown narrow at centerleft:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
"That didn't help."

"Polynomials do seem to trip a lot of people up, so she isn't catastrophically bad at this. Still, considering this first semester of gen-ed subjects is mostly reviewing what we did in high school, this isn't a promising start."

allison "Mind if I scribble on this a bit?"

show eileen indoors_onhip lookaway open at centerleft:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
eileen "Knock yourself out."

show shadow:
    alpha 0
    ease 1.5 alpha 0.4
show note homework allisonnotes:
    xalign 0.85 xoffset 0 alpha 0
    ease 2.0 alpha 1
show eileen indoors_onhip lookaway neutral at centerleft:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
"I reach over to grab my pen from the other side of the table, before hunching over her book and jotting down a couple of notes."

"First up are a few pointers to where the first two polynomials went awry, before taking a parallel crack at the worst of them."

show eileen indoors_onhip normal neutral at offcenterleft:
    xpos 0.3
$ renpy.transition(dissolve, layer='master')
"Pausing for a moment halfway to check the logic of what I'm doing, I'm satisfied I'm on the right track as I finish it off. The result looks about right."

show note homework allisonnotes as note2:
    subpixel True
    xalign 0.85 xoffset 0 alpha 1
    ease 1.5 xoffset 850 alpha 0
with None
hide shadow
hide bg2
hide note
$ renpy.transition(dissolve, layer='master')
pause 1.5
play sound "sfx/paper_shuffling.mp3"
show eileen indoors_onhip disbelief frown at left2:
    zoom 1.05 yoffset 50
    xzoom 1 xpos 0.3
    linear 0.7 xzoom -1 xpos 0.25
"Eileen flips over the textbook page on cue to check my answer, looking a little dubious as she does so. Vindicated by the matching result, I feel a good bit of relief at not making a fool of myself in front of her."

show eileen indoors_crossed closed open at left2:
    xzoom -1 xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "At least one of us has a head for this stuff."

hide note
show eileen indoors_crossed closed neutral at left2:
    xzoom -1 xpos 0.25
allison "Does it make more sense to you now?"

play sound "sfx/paper_shuffling.mp3"
show eileen narrow at left2:
    xzoom -1 xpos 0.25
$ renpy.transition(dissolve, layer='master')
"She takes a thorough look at my scribbles on her notebook, eyebrows furrowed as she tries to pick up the reasoning."

"I can't help but glance between my notes and Eileen as she looks over them. If she didn't project an aura of wanting to be left alone all the time, just her looks and her style would probably attract people."

stop sound fadeout 1.0
show eileen narrow sadmouth at left2:
    xzoom -1 xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "I think so..."

allison "You don't sound too sure."

show eileen indoors_onhip normal open at left2:
    xzoom -1 xpos 0.25
$ renpy.transition(dissolve, layer='master')
eileen "This is about as confident as I ever get with math, so don't worry. I'll have to repay you some time."

play sound "sfx/creaking_chair.ogg"
show bg buildingmisc library blurred2
show eileen indoors_onhip normal neutral at offcenterleft:
    xzoom -1
    zoom 1.5 yoffset 500
    xpos 0.45
with dissolve
"Taking that as confirmation that my job is done, I return to my seat as Eileen leans back in her chair."

allison "It's nothing, really. You should ask your professor though, if you're not confident doing polynomials."

stop sound fadeout 1.0
show eileen indoors_onhip lookaway grumble at offcenterleft:
    xzoom -1
    zoom 1.5 yoffset 500
    xpos 0.45
$ renpy.transition(dissolve, layer='master')
eileen "Needing to ask them doesn't mean that I want to."

show eileen neutral at offcenterleft:
    xzoom -1
    zoom 1.5 yoffset 500
    xpos 0.45
$ renpy.transition(dissolve, layer='master')
"Given how frank she is, I guess this must be a matter of pride rather than shyness. Maybe that's where her stubbornness comes from."

show eileen indoors_crossed disbelief neutral at offcenterleft:
    xzoom -1
    zoom 1.5 yoffset 500
    xpos 0.45
$ renpy.transition(dissolve, layer='master')
eileen "Why're you wasting your time here with me, anyway? Don't you have some friends to do... friend things with?"

allison "I only really know you and Caprice. Met Wallace the other day, actually."

show eileen lookawaynarrow open at offcenterleft:
    xzoom -1
    zoom 1.5 yoffset 500
    xpos 0.45
$ renpy.transition(dissolve, layer='master')
eileen "So that brat was trying to drag him into the club too..."

show eileen lookawaynarrow frown at offcenterleft:
    zoom 1.5 yoffset 500
    xzoom -1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
"Wallace may think it might be a good experience for her, but Eileen's disdain for Caprice is going to be hard to overcome."

play sound "sfx/cell_phone_vibrate.ogg"
show eileen indoors_onhip normal neutral at offcenterleft:
    zoom 1.5 yoffset 500
    xzoom -1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
window show
"Hearing my phone vibrating on the table, I quickly pick it up to see who's messaged me. I quickly force myself to keep a poker face as the name comes into view."

show eileen indoors_onhip normal neutral blur as eileen2 at offcenterleft:
    zoom 1.5 yoffset 500 alpha 0
    xzoom -1 xpos 0.45
    ease 1.0 alpha 1
$ phone.message('caprice', '12:27 PM', 'hey!!!! wanna grab somethin at the cafeteria???')
$ phone.show('messages', who='caprice')

"She must have given up on art out of loneliness if Eileen's avoiding her and I'm here. I'm not terribly hungry, but I should probably get at least a sandwich or something from the cafeteria before classes begin."

show eileen indoors_onhip normal neutral blur as eileen2 at offcenterleft:
    zoom 1.5 yoffset 500 alpha 1
    xzoom -1 xpos 0.45
    ease 1.0 alpha 0
$ phone.hide()
window hide
"Quickly typing in an agreement to meet there, I lock the phone once more."

allison "I might go grab lunch. Want to come?"

show eileen indoors_fists normal open at offcenterleft:
    zoom 1.5 yoffset 500
    xpos 0.45
$ renpy.transition(dissolve, layer='master')
eileen "Sorry, already ate. Thanks for the offer though."

stop music fadeout 8.0
hide eileen
show bg buildingmisc library
with dissolve
"She's already back to concentrating on her textbook as she mumbles the reply. It's probably for the best, anyway."

scene bg buildingmisc library:
    subpixel True
    zoom 1.1 xalign 0.0 yalign 0.5 yoffset -50
    ease 4.0 zoom 1.0 xalign 0.5 yalign 0.5 yoffset 0
"Giving a quiet farewell, I grab my bag and put my phone back inside."

scene bg buildingmisc library:
    xalign 0.5 yalign 0.5
show bg buildingmisc library blurred2 as bg2:
    xalign 0.5 yalign 0.5 alpha 0.85
$camera_move(-2200,-500,800,0,0,'dissolve')
show eileen indoors_fists lookaway neutral at centerleft:
    xzoom -1
    zoom 1.3 yoffset 420
    xpos 0.35
with fadeInOut
"As I pull it over my shoulder though, Eileen looks up."

show eileen lookaway open at centerleft:
    xzoom -1
    zoom 1.3 yoffset 420
    xpos 0.35
$ renpy.transition(dissolve, layer='master')
eileen "By the way, I don't blame you for any of this stuff Caprice is pushing. You seem alright."

show eileen closed neutral at centerleft:
    xzoom -1
    zoom 1.3 yoffset 420
    xpos 0.35
$ renpy.transition(dissolve, layer='master')
"So I'm 'alright'. Perhaps I should accept that as praise, coming from her."

stop ambiance fadeout 3.0
scene black with midDissolve
$ camera_reset()
"Glad for our meeting having been somewhat successful, I wave goodbye and head out toward the cafeteria."

play ambiance "sfx/ambiance/crowd_cafetaria.ogg" fadein 3.0
scene bg buildingunion cafeteria counter with longDissolve
"The cafeteria's little less full than the library, the stocks of food behind the counter already running low on all the usual student favorites. With the line for food moving quickly, I manage to grab the last set of sandwiches and move on."
window hide dissolve

scene bg buildingunion cafeteria snow HD:
    xalign 0.5 yalign 0.5
$camera_move(-9800,350,-500,0,0,'dissolve')
show caprice indoors_behindback even normal neutral at leftedge:
    xzoom -1
    zoom 0.75 yoffset -220
    xpos -0.52
show bg buildingunion cafetaria left table as cafetaria_left_table:
    xalign 0.5 yalign 0.5
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.2 ycenter 0.03
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.2 ycenter 1.06
with fadeInOut
letterbox "Scanning about, I notice Caprice sipping her juice, an empty tray before her. She sure eats fast."

play music "music/whimsical_faster_m.ogg" fadein 5.0
scene bg buildingunion cafeteria snow:
    subpixel True
    yalign 0.5
    time 1
    ease 2.0 yoffset -30
show caprice indoors_wave even closedhappy neutral at center:
    subpixel True
    yoffset 50
    time 1
    ease 2.0 yoffset 0
with fadeInOut
$ camera_reset()
window show dissolve

"Glad for the company either way, I walk over and take a seat at her table."

show caprice indoors_wave even normal grin at center:
    bounce
caprice "Hey, Allie! Long time no see!"

"We saw each other yesterday..."

show caprice indoors_chintap even normal opensmile at center:
    xpos 0.5 yoffset 55
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "How's everything going? How're your classes?"

show caprice neutral at center:
    xpos 0.5 yoffset 55 rotate 0
$ renpy.transition(dissolve, layer='master')
allison "Not too bad. It's all familiar enough right now."

show caprice indoors_behindback even closedhappy at center
$ renpy.transition(dissolve, layer='master')
"Not that everyone's doing as well as I am. As I unpack my sandwich and begin to nibble, my thoughts turn to the woman in the library. I feel a little sorry for her, Eileen's struggle reminding me that I have it easier than some at times."

"Then there's the matter of her and the club. Setting my food back down, I decide to tackle this more directly than usual; if Eileen can be so direct with others, then so can I."

show caprice normal at center
$ renpy.transition(dissolve, layer='master')
allison "I was thinking; You meant for me to meet Eileen last week, didn't you?"

show caprice indoors_handonhip grin at center
$ renpy.transition(dissolve, layer='master')
caprice "She's fun, isn't she?"

allison "Something... like that. That painting of the girl in the water was really pretty."

show caprice indoors_pumped wink opensmile at center:
    xpos 0.5 yoffset 55
    easein .15 yoffset 40
    easeout .175 yoffset 55
    easein .15 yoffset 50
    easeout .175 yoffset 55
caprice "She's really good, huh? No wonder the other art club tried to grab her."

show caprice indoors_handonhip raised normal neutral at center
$ renpy.transition(dissolve, layer='master')
allison "About that. Well, more about Eileen."

allison "I’m not sure it's a good idea to be forcing people into this club. I know you're excited to get things started, but just because her art's good, doesn't mean she wants to be in a club."

show caprice indoors_chintap even normal pout at center
$ renpy.transition(dissolve, layer='master')
caprice "You sound like you're not really into it yourself."

show caprice indoors_behindback even closedhappy puffed at center:
    nod2
"She's sharper than I give her credit for. Caught off guard, I have to stop and think as she sips at the last of her juice. The sucking sound as she makes sure to get every last drop doesn't help."

"I can't say I'm enthusiastic about this; Eileen's studying is exactly what I need to be doing, lest I waste my scholarship. On the other hand, Caprice is my only friend right now, and I do enjoy spending time with her."

show caprice normal neutral at center:
    xpos 0.5 yoffset 55
    ease 0.5 yoffset 60
    ease 0.5 yoffset 50
    ease 0.2 yoffset 55
"As she puts down her drink with a satisfied breath, I know my answer."

allison "I can make time for it."

show caprice indoors_handonhip sad closedhappy open at center
$ renpy.transition(dissolve, layer='master')
"She gives a comically big sigh, missing my hesitation entirely. If this ends up only being between a couple of us, maybe it won't be too bad. Long as it's not a whole bunch of people getting involved."

show caprice sad normal neutral at center
$ renpy.transition(dissolve, layer='master')
caprice "I wanna do this for her sake as well, y'know. Eileen looks kinda lonely all by herself in that room!"

"Huh. I hadn't considered that Caprice was coming at it from that angle. It makes me think a little better of her."

"What she says makes me reconsider Eileen's actions in another light as well; I wonder how much of her reluctance around this isn't due to Caprice herself, but rather her feeling used by the other club for her art?"

show caprice indoors_pumped even wink at center:
    xpos 0.5 yoffset 55
    easein .15 yoffset 40
    easeout .175 yoffset 55
    easein .15 yoffset 50
    easeout .175 yoffset 55
caprice "Seeing that kind of talent makes you kinda envious though, right?"

allison "Well, I just drew a bit in high school for fun. I don't think I could ever manage something beautiful like that."

show caprice indoors_behindback closedhappy grin at center
$ renpy.transition(dissolve, layer='master')
stop music fadeout 3.0
stop ambiance fadeout 3.0
show shadow:
    alpha 0
    ease 3.0 alpha 0.4
"We keep chatting, but Caprice's earlier words stick firmly in my mind."

"We may meet every school day and talk quite a lot - at least, she does - but I realize just how little I really know her in spite of that."

$ _dismiss_pause = False
"Maybe spending more time together wouldn't be so bad after all."

window hide dissolve
scene black with longDissolve
return
