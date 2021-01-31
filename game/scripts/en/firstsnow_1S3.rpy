label scene_1S3_en:
######################

stop music fadeout 2.0
scene black with fadeInOut
play ambiance "sfx/ambiance/tv.ogg" fadein 2.0
$ renpy.sound.set_volume(0.6, channel='loopsfx')
play loopsfx "sfx/ambiance/water_boiling.ogg" fadein 2.0
scene bg aptallison livingroom blur with eye_open
window show dissolve
$ _dismiss_pause = True
"A loud yawn from Rose emanates from the couch, the droning of the television briefly overshadowed. The only other sound is the coffee pot boiling away from the kitchen, punctuated by the occasional passing car."

scene bg aptallison livingroom:
    subpixel True
    zoom 1.0 xalign 0.5 yalign 0.5
    parallel:
        ease 1.0 yoffset 1
        ease 1.0 yoffset -1
        repeat 3
    parallel:
        ease 6 zoom 1.77 xalign 0.208 yalign 0.328
show bg aptallison livingroom blurred5 as bg2:
    subpixel True
    zoom 1.0 xalign 0.5 yalign 0.5
    parallel:
        ease 1.0 yoffset 1
        ease 1.0 yoffset -1
        repeat 3
    parallel:
        ease 6 zoom 1.77 xalign 0.208 yalign 0.328
    parallel:
        ease 15 alpha 0
"Only half-awake and still acting on autopilot, I lazily wipe the sleep from my eyes as I stagger toward the door. The smell of Rose's toast wafts invitingly through the air, making me envious of her later start to work."

"I let out a loud yawn before I can stifle it, causing Rose to look over from the couch."

scene bg aptallison livingroom HD:
    xalign 0.5 yalign 0.5
$camera_move(-5000,-1650,-250,0,0,'dissolve')
show rose indoors_handonhip normal neutral at right2 as rose2:
    zoom 0.75 yoffset -400
    xpos 0.9
show bg aptallison sofa corner as livingroom_sofa_corner:
    xalign 0.5 yalign 0.5
show bg aptallison livingroom table as livingroom_table:
    xalign 0.5 yalign 0.5
show rose indoors_handonhip normal neutral at centerright:
    alpha 0 xpos 0.7
with dissolve
$camera_move(5800,-1650,-250,0,4,'ease')
$ renpy.music.set_volume(0.5, delay=0)
play music "music/whimsical_faster_m.ogg" fadein 8.0
pause 4.5
show rose indoors_handonhip halfclosed puzzled at right2 as rose2:
    zoom 0.75 yoffset -400
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
rose "Wow, you look like hell."

allison "Thank you."

show rose talking at rightedge as rose2:
    zoom 0.75 yoffset -400
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
rose "Stay up too late playing on your phone or something? Doesn't look like you got an hour of sleep."

show rose weaksmile at rightedge as rose2:
    zoom 0.75 yoffset -400
    xpos 0.9
$ renpy.transition(dissolve, layer='master')
"While Rose is less than tactful about this, it's true that I shouldn't be so tired. I'm usually a morning person, but right now I can barely remember where I even put my phone."

show rose normal weaksmile at rightedge as rose2:
    zoom 0.75 yoffset -400
    xpos 0.9
    ease 1.0 xpos 0.855
    easein .15 yoffset -410
    easeout .175 yoffset -400
    easein .15 yoffset -405
    easeout .175 yoffset -400
"Rose picks herself up from the couch as she finishes her breakfast, brushing toast crumbs off herself as she starts toward the kitchen."

show rose at rightedge as rose2:
    zoom 0.75 yoffset -400
    xpos 0.855
allison "Just the neighbors being loud again. I'm surprised you didn't hear them."

show rose normal neutral at rightedge as rose2:
    zoom 0.75 yoffset -400
    xpos 0.855
$ renpy.transition(dissolve, layer='master')
"I may say that, but it's hardly any real shock; she sleeps like a log, which I've always been jealous about."

stop loopsfx fadeout 10.0
stop ambiance fadeout 10.0
scene bg aptallison livingroom:
    zoom 1.2 yalign 0.45
show rose indoors_handonhip normal puzzled at offcenterright
with fadeInOut
$ camera_reset()
"Rose puts down the plate in her hand, giving the matter more thought than I'd intended."

show rose smirk at offcenterright
$ renpy.transition(dissolve, layer='master')
rose "The ones above us, right? Man, I'm sick of them."

show rose halfclosed at offcenterright
$ renpy.transition(dissolve, layer='master')
rose "I'll go have a talk to 'em later today and get them to knock it off. Making a racket during the day is one thing, but the night's another."

allison "You don't have to do that. They might be quiet from now on, anyway."

show rose normal concerned at offcenterright
$ renpy.transition(dissolve, layer='master')
"She looks surprisingly disappointed at my attempts to wave off her concern."

show rose talking at offcenterright
$ renpy.transition(dissolve, layer='master')
rose "You have to stand up for yourself sometimes, Allison. Waiting for things to blow over ain't always going to work."

show rose normal concerned at offcenterright
$ renpy.transition(dissolve, layer='master')
"I wind up rubbing my neck and avoid outright answering."

show rose normal concerned at offcenterright:
    xzoom 1 xpos 0.55
    linear 0.7 xzoom -1 xpos 0.54
    pause 0.5
    ease 1.8 xpos 1.5
"Apparently dropping the topic, she sighs and disappears into the kitchen after taking her plate again."

"I just don't want to cause a fuss, especially on my behalf. Is that really so bad?"

"With time rolling by, I glance about and see my phone on the corner of the table. Slipping it into my coat pocket, I skip over and grab my bag sitting by the door."

hide rose
"As I stretch a bit to try and wake myself up before facing the cold outside, Rose calls out from behind me."

show bg:
    subpixel True
    ease 2.0 xalign 1.0 yalign 0.45
show rose indoors_handonhip normal smile:
    alpha 0.0 xanchor 0.5 xpos 1.2 yalign 1.0
    ease 2.0 xpos 0.8 alpha 1.0
"Turning to see her shows a fistful of crumpled dollar bills in the hand thrust out towards me."

show rose indoors_handonhip normal smile at rightside:
    xpos 0.8 alpha 1.0
    nod2
rose "Here. Go buy yourself an espresso or something on the way."

allison "It's fine, you don't have to-"

show rose halfclosed smirk at rightside:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
rose "Just take it. You look awful."

"She really does have a way with words."

show bg:
    subpixel True
    xalign 1.0 yalign 0.45
    ease 2.0 xalign 0.0
show rose indoors_handonhip halfclosed laugh at rightside:
    xpos 0.8 alpha 1.0
    ease 2.0 xpos 1.2
stop music fadeout 5.0
pause 2.0
play sound "sfx/door_open2.ogg"
"I reluctantly take the cash and slip it into my pocket, thanking Rose as I leave."

play sound "sfx/door_close3.ogg"
scene black with dissolve
scene bg aptallison outside
show snow light
play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
with fadeInOut
"As soon as I get out the door, the weather hits me. Looks like it's going to be a harsh winter this year, with the cold of the snow dumping down being made all the worse by the chilly fog hanging in the air."

$ renpy.sound.set_volume(1.0, channel='loopsfx')
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 0.5
show bg:
    subpixel True
    xalign 0.5 yalign 0.5
    parallel:
        ease 30 zoom 2.0 xalign 1.0 yalign 0.3
    parallel:
        ease 1 yoffset 1
        ease 1 yoffset -1
        repeat 20
"Twisting my head to and fro to bury it in my scarf a little better, I set off down the road with hands firmly lodged in my coat pockets. There don't seem to be many people around that're braving the weather, not that I blame them."

play sound "sfx/dumptruck.mp3"
"As the muffled sound of snow under tires rings out, a garbage truck rumbles by. It's only after a worrying few seconds that I remember I did indeed put the garbage out for collection yesterday."

scene bg campus outskirts snow
show snow light
with midDissolve
"Reaching the campus, the welcome sight of a café nearby lifts my spirits. I've overheard students mention the coffee here is good, and it's conveniently right next to campus."

"It looks homely enough from the outside, and only has a handful of people inside at this hour as I peer through the windows. With a quick brush of the fallen snow off my shoulders and bag, I take a breath and walk in."

stop loopsfx fadeout 0.5
stop ambiance fadeout 1.0
play sound "sfx/door_open_bell.ogg"
$ renpy.music.set_volume(0.5, channel='ambiance')
play ambiance "sfx/ambiance/crowd_cafe.ogg" fadein 0.5
scene bg cafe inside with midDissolve
"A bell above the door rings out as I enter, the smell of coffee on the air combining with the homely styling inside making for an immediately cozy atmosphere."

$camera_move(-2800,-1550,650,0,5,'ease')
"Joining the couple of people in line, I quickly rehearse the order in my mind to make sure I get it right. The barista's nice smile toward the other patrons keeps making me trip over myself, and I've never been great in dealing with strangers."

"Coming to the front of the line, I manage to blurt out my order of a latte with sugar before I can mess it up. She smiles and takes my payment, leaving me to wait to the side as it's prepared."

$camera_move(2800,-1550,650,0,5,'ease')
"I briefly consider having it here, given how relaxing the café is."

window hide dissolve
$ renpy.music.set_volume(1.0, delay=0)
play music "music/caprice_default_m.ogg" fadein 10.0
scene bg cafe inside HD
$camera_move(-8650,-200,-200,0,0,'dissolve')
show caprice indoors_behindback even closedhappy opensmile at left2:
    xzoom -1
    zoom 0.8 yoffset -115
    xpos -0.255 rotate -4
    time 1.5
    ease 0.5 yoffset -110
    ease 0.5 yoffset -120
    ease 0.2 yoffset -115
show wallace indoors even open frown at right2:
    zoom 0.8 yoffset -100
    xpos 0.12 rotate 0
show bg cafe cafe table as cafe_table:
    xalign 0.5 yalign 0.5
show cutin cup small at leftedge:
    zoom 0.85 yoffset -220
    xpos -0.16
show cutin cup small2 as cup2 at leftside:
    zoom 0.85 yoffset -230
    xpos 0.02
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.4 ycenter 0.0
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.4 ycenter 0.955
with fadeInOut

letterbox "That's before I notice Caprice, loudly chatting with the tall man sitting across from her."

letterbox "I'm surprised I didn't notice them; I must really be out of it."

scene bg cafe tablesurface blur with fadeInOut
$ camera_reset()
play sound "sfx/mug-put-down.ogg"
show cutin cup:
    subpixel True
    xalign 0.5 yoffset -600 alpha 0
    ease 1.5 yoffset 0 alpha 1
window show dissolve

"As the cute barista slides the coffee cup towards me, I decide I'd better leave the two in peace and drink outside."

scene bg cafe inside blurred2:
    xalign 0.5 yalign 0.5
show caprice indoors_behindback raised normal open at center:
    xpos 0.5
    bounce
    bounce
with fadeInOut
stop sound fadeout 1.0
"Before I can, Caprice catches sight of me and begins excitedly waving her hand in the air."

show caprice indoors_wave even closedhappy grin at center:
    xpos 0.5 yoffset 55
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "Allie! Hey, Allie! Over here! Allie!"

hide caprice
show bg cafe inside
$ renpy.transition(dissolve, layer='master')
show bg:
    subpixel True
    xalign 0.5 yalign 0.5
    parallel:
        ease 5.0 xalign 0.0 yalign 0.5 zoom 1.5
    parallel:
        ease 1.0 yoffset 1
        ease 1.0 yoffset -1
        repeat 2
pause 4.0
"So much for that. Coffee in hand, I wearily walk over to their table and look from one to the other."

show bg cafe inside:
    xalign 0.0 yalign 0.5 zoom 1.5
show caprice indoors_behindback even normal neutral at leftside:
    xzoom -1.0 yoffset 50
    xpos 0.17
show wallace indoors even open neutral at rightish:
    yoffset 50
    xpos 0.7
$ renpy.transition(dissolve, layer='master')
allison "Morning, Caprice. Um..."

show wallace indoors even closed neutral at rightish:
    yoffset 50 xpos 0.7
$ renpy.transition(dissolve, layer='master')
wallace "Wallace."

play sound "sfx/chair_scrape_fast.ogg"
show bg:
    subpixel True
    zoom 1.5 xalign 0.0 yalign 0.5
    ease 1.5 yoffset -20
show caprice at leftside:
    yoffset 50 xpos 0.17
    ease 1.5 yoffset 0
show wallace at rightish:
    yoffset 50 xpos 0.7
    ease 1.5 yoffset 0
"Upon Caprice moving her backpack off a chair and placing it on the floor, I take a seat."

show caprice indoors_handonhip closedhappy neutral at leftside:
    yoffset 0 xpos 0.17
$ renpy.transition(dissolve, layer='master')
caprice "Allison here's a good friend, and one of the founding members of the art club!"

show wallace heightened halfopen frown at rightish:
    yoffset 0 xpos 0.7
$ renpy.transition(dissolve, layer='master')
stop sound fadeout 1.0
wallace "The new art club."

"This is Caprice's rodeo, so I'm content to let her deal with the club as she wants to at this point."

"It takes me a moment to realize she referred to me as a 'good' friend in particular. We've only known each other for the couple of months since the semester started, but I'm a little glad she thinks of me like that."

show wallace forward even neutral at rightish
$ renpy.transition(dissolve, layer='master')
wallace "Hi. I'm some guy Caprice found."

show caprice indoors_behindback at leftside:
    xpos 0.17
    bounce
caprice "He's our fourth member!"

show wallace closed even frown at rightish
$ renpy.transition(dissolve, layer='master')
"As he sighs forlornly, all I can offer is a stilted smile in response. Caprice looked so comfortable dealing with him that I assumed they knew each other already."

"Come to think of it, Caprice had no problem dealing with Eileen either despite barely knowing her. I'm impressed at how she can talk to strangers with just the same confidence as friends. Maybe she even considers him one already."

show caprice indoors_chintap normal at leftside:
    xpos 0.17
show wallace even open neutral at rightish
$ renpy.transition(dissolve, layer='master')
caprice "So what'd you get up to over the weekend, Allie?"

allison "Just housework and errands. It's surprising how much time I spend on that sort of thing now that I've moved out."

show caprice indoors_behindback wink at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
caprice "I get what you mean. Thankfully I split the work with my roommates."

show caprice closedhappy at leftside:
    xpos 0.17
show wallace forward at rightish
$ renpy.transition(dissolve, layer='master')
"It's my roommate that makes me want to pick up the slack. Caprice looks to Wallace for his input, making him part of the conversation."

show wallace open smile at rightish
$ renpy.transition(dissolve, layer='master')
wallace "I look after the family gun shop on weekends. Nothing glamorous, but enough to get by on."

show caprice indoors_handonhip open at leftside:
    xpos 0.17
    bounce
show wallace forward neutral at rightish
"Caprice continues on chatting, mostly with him. Wallace quietly nods along, adding a 'yeah' or 'I see' as needed. I get the distinct feeling he's being talked at more than being talked to."
stop music fadeout 5.0
$camera_move(3500,-850,650,0,5,'ease')
pause 2.0

scene bg cafe inside HD:
    xalign 0.5 yalign 0.5
show bg cafe inside HD blurred2 as bg2:
    xalign 0.5 yalign 0.5 alpha 0.65
$camera_move(-6500,-850,850,0,0,'dissolve')
show bg cafe cafe table as cafe_table_full:
    xalign 0.5 yalign 0.5
show wallace indoors even forward neutral at right2:
    zoom 0.78 yoffset -105
    xpos 0.12 rotate 0
show bg cafe cafe table as cafe_table:
    xalign 0.5 yalign 0.5
show cutin cup small2 at leftside:
    zoom 0.8 yoffset -230
    xpos 0.01
with fadeInOut
"Now that that we're both sitting across from each other, I can fully appreciate how much of a bear the man is, cutting more of a foreboding figure thanks to his beard."

show wallace closed at right2:
    zoom 0.78 yoffset -105
    xpos 0.12
$ renpy.transition(dissolve, layer='master')
"I can already feel myself shrinking in response."

$camera_move(-6500,450,850,0,5,'ease')
"For want to not stare at him, I turn to the coffee steaming away before him."

"A flat black, with the lid taken off to let it cool faster. I can taste how bitter it is just by looking at it."

$ renpy.sound.set_volume(0.2, channel='loopsfx')
play loopsfx "music/caprice_ringtone.ogg"
scene bg cafe inside:
    xalign 0.0 yalign 0.5 zoom 1.5 yoffset -20
show caprice indoors_handonhip raised normal grumble at leftside:
    xzoom -1
    xpos 0.17
    time 2
    shaking2
show wallace indoors even closed neutral at rightish
with fadeInOut
$ camera_reset()
"The conversation is suddenly interrupted by a phone going off."

show wallace indoors heightened forward at rightish
show caprice raised closedhappy open at leftside:
    xzoom -1 xpos 0.17
    linear 0.7 xzoom 1 xpos 0.2
"Apparently Caprice's, as her hand dives into the front pocket of her hoodie and retrieves it."

stop loopsfx fadeout 2.0
play sound "sfx/chair_scrape_fast.ogg"
show wallace even open at rightish
show caprice raised closedhappy open at leftside:
    xzoom 1 xpos 0.2
    ease 1.2 xoffset -300 alpha 0.0
"Wallace and I just look to each other as she wanders off a few steps to take the call, unsure exactly what to do with ourselves."

"It only takes a few seconds before she returns."

$ renpy.music.set_volume(1.0)
play music "music/energetic.ogg" fadein 2.0
show caprice indoors_chintap sad normal open at leftside:
    xzoom -1 xoffset -300 alpha 0
    ease 1.2 xoffset 0 xpos 0.15 alpha 1
pause 1.2
show wallace heightened forward neutral at rightish
$ renpy.transition(dissolve, layer='master')
stop sound fadeout 1.0
caprice "Sorry guys, gotta go. Roommates need me."

allison "Uh, wait-"

show caprice indoors_pumped even wink grin at leftside:
    xzoom -1 xpos 0.15 alpha 1
    bounce
caprice "I'll see you two around! We've got much more to discuss!"

show wallace even open frown at rightish
show caprice outdoors_pumped even wink grin at leftside:
    nod2
$ renpy.transition(dissolve, layer='master')
"With that, she grabs her backpack and skips out into the winter air without another word."

show caprice outdoors_wave even closedhappy neutral behind wallace at leftside:
    xpos 0.15
    ease 1.5 xpos 1.5
pause 1.0
play sound "sfx/door_close_bell.ogg"
"Going by her face, I'm more worried about this than she is."

stop music fadeout 10.0
show bg:
    subpixel True
    xalign 0.0 yalign 0.5 zoom 1.5 yoffset -20
    ease 3.0 xalign 0.3
show wallace at rightish:
    subpixel True
    xpos 0.7
    ease 3.0 xpos 0.48
"Left alone with Wallace, I sip my coffee for something to do. Glancing in his direction, he looks more relieved than anything."

stop sound fadeout 1.0
show bg:
    xalign 0.3 yalign 0.5 zoom 1.5 yoffset -20
show wallace upturned halfopen frown at center:
    xpos 0.48
$ renpy.transition(dissolve, layer='master')
wallace "She means well."

"I know she does."

show wallace closed neutral at center:
    xpos 0.48
$ renpy.transition(dissolve, layer='master')
wallace "Even if Eileen doesn't think so, I just have to keep telling myself that."

"And now I'm glad I didn't say that."

"Much as I would like to leap to her defense, she is pushing this awfully hard. If he's trying to start conversation, I feel I should at least try to reciprocate rather than letting him twist in the wind."

scene bg cafe inside blurred2:
    zoom 1.5 xalign 0.25 yalign 0.5
show wallace indoors even open neutral at center:
    zoom 1.2 yoffset 180
    xpos 0.52
with fadeInOut
play music "music/relaxing.ogg" fadein 3.0
allison "So... you and Eileen know each other?"

show wallace indoors even closed neutral at center:
    zoom 1.2 yoffset 180
    xpos 0.52
    ease 0.5 yoffset 185
    ease 0.5 yoffset 175
    ease 0.2 yoffset 180
"He gives a nod after taking a long sip of his coffee. That must be so awfully bitter."

show wallace forward at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
wallace "We're friends. Met when she was a freshman in high school. Caprice saw us together and made the connection."

allison "Oh."

show wallace upturned open frown at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
wallace "She's filled me in on this club business. I'm going to guess you were pulled into it?"

allison "Something like that. It kinda spiraled out of control, sorry."

show wallace even closed neutral at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Wallace simply shrugs."

wallace "Not the first time clubs have been pushy about scouting members. I was actually thinking the whole thing might be good for Eileen; her single-mindedness is her best and worst trait, really."

show wallace upturned neutral at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
wallace "I don't want to say 'please put up with Eileen', but I'm having trouble working out a better way to word that."

show wallace even open smile at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
wallace "She isn't a bad person. Just... driven. I'm sure you know someone similar."

"I do shudder what her reaction would be to being told she and Caprice are 'similar' in any way. I'm still not sure about dealing with her, but it's hard to deny someone worried about their friend."

show wallace even closed smile at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Wallace seems content that he's managed to get his point across, silence hanging in the air as he thoughtfully sips his coffee. It reminds me that I should drink my own before it gets too cold as well."

show shadow:
    alpha 0.4
show bg campus outskirts snow as bg2:
    yanchor -0.31
    ypos 0
    size (1280, 350) crop (0, 100, 1280, 350)
show snow light:
    yanchor -0.31
    size (1280, 350) crop (0, 100, 1280, 350)
with midDissolve
"The weather outside is a harsh contrast to the nice atmosphere in here, which might be why more students are starting to file in before classes start."

"The coffee's nice as well, so maybe I'll make this a regular spot. If I can afford to, that is."

hide snow light
hide bg2
hide shadow
show wallace forward neutral at center:
    zoom 1.2 yoffset 180
    xpos 0.52
with midDissolve
"As for my companion, I think I'm starting to see him in a better way; he's just concerned about his friend. Maybe he's the gentle giant type, who isn't that threatening at all."

show wallace closed at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"With his cup empty as he sets it down, Wallace sits back to savor the last of its taste."

show wallace open mopen at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
wallace "Well, I've said my piece. Caprice will probably give up on me, but you and Eileen are another matter."

allison "Caprice is a good friend; I can handle her. It was nice meeting you, Wallace."

show wallace open smile at center:
    zoom 1.2 yoffset 180
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"I carefully repeat his name to try and engrave it in my memory. I have no doubt I'd instantly forget it otherwise. He's perhaps overly hopeful when it comes to Caprice, though."

show wallace open smile at center:
    zoom 1.0 yoffset 0
    xpos 0.48
$ renpy.transition(dissolve, layer='master')
wallace "Thanks. You seem nice, so hopefully Eileen will ease off a bit."

play sound "sfx/chair_scrape_fast.ogg"
show wallace closed smile at center:
    xpos 0.48 yoffset 0
    ease 1.0 yoffset -40
"He levers himself off the chair with a grunt, taking a glance outside before grabbing his scarf and hat once more."

show bg cafe inside:
    zoom 1.5 xalign 0.25
$ renpy.transition(dissolve, layer='master')
show wallace outdoors even open smile at center with dissolve:
    xpos 0.48 yoffset -40
    nod2
wallace "Good luck with class."

stop sound fadeout 1.0
show wallace outdoors even open smile at center:
    xzoom 1 xpos 0.48 yoffset -40
    linear 0.7 xzoom -1 xpos 0.44
allison "Thanks. You too."

stop music fadeout 3.0
show wallace outdoors even closed smile at center:
    xzoom -1 xpos 0.44
    ease 1.8 xpos 1.5
pause 1.2
play sound "sfx/door_close_bell.ogg"
"With that, he leaves the café while sliding past someone coming in, staggering through the terrible weather outside as he goes."

show bg:
    subpixel True
    zoom 1.5 xalign 0.25 yalign 0.5
    parallel:
        ease 5.0 xalign 0.5 yalign 0.5
    parallel:
        ease 5.0 zoom 1.0
show bg cafe inside blurred2 as bg2:
    subpixel True
    zoom 1.5 xalign 0.25 yalign 0.5 alpha 0
    parallel:
        ease 5.0 xalign 0.5 yalign 0.5 alpha 0.5
    parallel:
        ease 5.0 zoom 1.0
"With my next class so soon, I'd better finish this coffee off quickly. With that in mind, I concentrate on taking as big gulps as I can without looking unsightly."

stop sound fadeout 1.0
hide wallace
show shadow:
    alpha 0
    ease 5.0 alpha 0.25
"It's funny how one thing leads to another, though. It feels like a snowball's begun to start rolling, meeting new and interesting people since I started here."

stop ambiance fadeout 3.0
$ _dismiss_pause = False
"It might have taken a couple of months, but maybe I will manage to find some new friends."

window hide dissolve
scene black with longDissolve
$ renpy.sound.set_volume(1.0, channel='loopsfx')
$ renpy.music.set_volume(1.0, channel='ambiance')
return
