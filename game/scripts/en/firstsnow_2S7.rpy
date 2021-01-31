label scene_2S7_en:
######################

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg buildingunion cafeteria snow sketch with inkfade
scene bg buildingunion cafeteria snow with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

play ambiance "sfx/ambiance/crowd_loud.mp3" fadein 2.0
"With the day wearing on, I let out a badly-hidden yawn as I leave the cafeteria."

scene bg buildingunion foyer with wiperight
"I clutch my bag tightly as I walk, both from the cold and trying not to take up too much space given all the people milling about. I can't help but eavesdrop on the conversations around me as I walk, the building humming with activity."

"One conversation from the groups idling about catches my ear; the chatter between some girls about their plans to be with their families again for the holidays. It makes me excited for Christmas all over again."

stop ambiance fadeout 4.0
play sound "sfx/door_open.ogg"
"As I push through the heavy door and step outside, I wonder if Eileen would be as eager."

play sound "sfx/door_close2.ogg"
scene bg buildingunion outside snow with dissolve
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
"The fact she doesn't get on with her parents is a worry, but surely they can't be too bad if they're paying for her to live in such a place."

"For all I enjoy Christmas, it doesn't sound like Eileen has much reason to."

play sound "sfx/cell_phone_vibrate.ogg"
window show
"A sudden vibration from my pocket grabs my attention, my hand instinctively diving in to pluck my phone out."

show bg buildingunion outside snow blurred2
$ renpy.transition(dissolve, layer='master')
$ phone.clear('eileen')
$ phone.message('eileen', '2:05 PM', 'Hey, I\'m in the coffee shop if you want to meet.')
$ phone.show('messages', who='eileen')
"She hasn't admitted it, but I think Eileen's enjoying playing with her new toy."

stop sound fadeout 1.0
$ renpy.transition(hpunch, layer='master')
"I quickly text her in agreement and hit send as I step off the stairs, dodging a student I nearly bump into as I do. If only I had an extra set of eyes so I could use this while walking more easily."

$ phone.hide()
window hide
show bg buildingunion outside snow
$ renpy.transition(dissolve, layer='master')
"Heading towards the cafe, I muse on how normal things still feel. I'm happy for us being together of course, yet life goes on. She enters my thoughts more and more these days, but schoolwork, chores around home, and the club don't stop."

stop ambiance fadeout 4.0
"One thing has changed through; I feel more sure of myself then ever. Knowing what my own feelings are is oddly liberating."

scene black with circlewipe
play sound "sfx/door_open_bell.ogg"
play ambiance "sfx/ambiance/crowd_cafe.ogg" fadein 1.5
scene bg cafe inside with circlewipe
"The rush of warmth as I step through the door makes my shoulders slump in relief. Thank goodness for the interior heating being cranked right up."

window hide dissolve
scene bg cafe inside HD
$camera_move(-8650,-200,-200,0,0,'dissolve')
show eileen indoors_crossed lookawaynarrow neutral at left2:
    zoom 0.8 yoffset -112
    xpos -0.25
show bg cafe cafe table as cafe_table:
    xalign 0.5 yalign 0.5
show cutin cup small2 as cup2 at leftedge:
    zoom 0.85 yoffset -220
    xpos -0.16
show cutin cup small at leftside:
    zoom 0.85 yoffset -230
    xpos 0.02
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.4 ycenter 0.0
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.4 ycenter 0.955
with midDissolve
stop sound fadeout 1.0

letterbox "It doesn't take long to notice Eileen sitting alone at a table with her coat and scarf in her lap, cooly staring out the window to pass the time. Walking up, I notice not one, but two coffees sitting on the table before her."

$ renpy.sound.set_volume(0.4, channel="ambiance", delay=4.5)
$ renpy.music.set_volume(0.8)
play music "music/eileen_5_m.ogg" fadein 5.0
scene bg cafe inside:
    subpixel True
    xalign 0.0 yalign 0.5
    time 0.5
    ease 4.0 xalign 0.0 yalign 0.5 zoom 1.5
show eileen indoors_crossed lookaway angry at leftside:
    subpixel True
    xpos 0.15 yoffset -225 zoom 0.65
    time 0.5
    ease 4.0 xpos 0.23 yoffset 50 zoom 1.0
with dissolve
$ camera_reset()
window show dissolve
$ renpy.pause(3.0, hard=True)

allison "Hi, Eileen. Is someone else with you?"

show eileen indoors_crossed normal angry at leftside:
    zoom 1.0 yoffset 50
    xzoom 1 xpos 0.23
    linear 0.7 xzoom -1 xpos 0.17
"Eileen's apathetic expression barely changes as she turns to see me sit before her."

play sound "sfx/chair_scrape_fast.ogg"
show bg:
    subpixel True
    zoom 1.5 xalign 0.0 yalign 0.5
    ease 1.5 yoffset -20
show eileen normal angry at leftside:
    subpixel True
    zoom 1.0 yoffset 50
    xzoom -1 xpos 0.17
    ease 1.5 yoffset 0
"I'm a little disappointed, but I know her well enough by now to expect it. She's not the type to show her emotions easily."

show eileen indoors_onhip lookawaynarrow open at leftside:
    xzoom -1 xpos 0.17 yoffset 0
$ renpy.transition(dissolve, layer='master')
eileen "The second's for you. You helped me out earlier with life drawing, so I wanted to return the favor."

stop sound fadeout 1.0
show eileen closed neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
allison "It's fine, you don't need to repay me."

"So that debt was still lingering on her mind, huh? Now that she's bought it for me though, I suppose I can't exactly say no. The coffee proves too hot as I bring it near my mouth, so I settle for blowing on it a bit."

show eileen indoors_crossed normal open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "How's your day been?"

show eileen neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
allison "Good! I mean... normal, I guess."

"I might think everything's still normal, but my nerves around Eileen haven't quite settled yet. We have only been together a matter of days. I gingerly take a sip to calm myself down before continuing."

allison "Physics was good. Kinda basic right now, but I think we're going to get to some interesting stuff next year."

show eileen neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
allison "So what're you doing?"

show eileen indoors_crossed lookawaynarrow open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "Trying to stay awake, mainly. What a day."

show eileen neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
allison "Caprice?"

show eileen narrow open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "You're getting too good at this."

show eileen neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
"I just awkwardly smile."

$ renpy.music.set_volume(0.6, delay=4.0)
scene bg cafe inside blurred2:
    xalign 0.5 yalign 0.5
$camera_move(-2500,-450,400,0,0,'dissolve')
show eileen indoors_crossed normal neutral at leftside:
    zoom 1.1 yoffset 100
    xzoom -1 xpos 0.17
show millie outdoors_neutral even normal neutral at right2:
    zoom 0.75 yoffset -180
    xzoom 1 xpos 1.2 alpha 0
    time 2
    ease 2.5 xpos 0.72 alpha 1
with fadeInOut
play sound "sfx/door_open_bell.ogg"
$camera_move(-650,-450,400,0,4,'ease')
"As I do, my eyes drift to the side after noticing a sharply-dressed familiar figure breeze into the cafe and up to the counter. Eileen follows my gaze, an eyebrow lifting."

show eileen indoors_onhip lookaway open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "Oh, it's that mechanic girl."

show eileen neutral at leftside:
    xpos 0.17
show millie outdoors_neutral even closedsad neutral at right2:
    xzoom 1 xpos 0.72 alpha 1
    linear 0.7 xzoom -1 xpos 0.7
"She's appalling with names..."

allison "She's Millie. You should at least remember who fixed your car."

show eileen disbelief open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "Did you want to talk to her or something? You keep looking at her."

show eileen neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
allison "Ah, well... I dont want to annoy her. She might be busy. I barely know her, anyway."

show eileen narrow at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
"Eileen looks at me a moment, unimpressed. I used every excuse in the book to not bother Millie, too. Then again, I suppose that's the problem."

show eileen indoors_onhip closed open at leftside:
    xzoom -1 xpos 0.17
    nod2
eileen "Hey, Millie!"

show eileen indoors_onhip normal neutral at leftside:
    xpos 0.17
show millie outdoors_neutral raised normal speaking at right2:
    zoom 0.75 yoffset -180
    xzoom -1 xpos 0.7
    linear 0.7 xzoom 1 xpos 0.72
"I shrink in my seat at Eileen's casual calling out across the cafe, taken completely off guard."

show millie outdoors_neutral even closedhappy neutral at right2:
    xzoom 1 xpos 0.72
    ease 0.5 yoffset -175
    ease 0.5 yoffset -185
    ease 0.2 yoffset -180
"Millie turns towards the source of her name, giving her usual calm smile upon recognising us."

show millie outdoors_neutral even normal neutral at right2:
    xzoom 1 xpos 0.72
$camera_move(-3500,-450,650,0,4,'ease')
pause 3.0
stop music fadeout 4.0
show eileen indoors_crossed narrow smile at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "See? It's not that hard. This is a good opportunity to know her better."

$ renpy.music.set_volume(0.8)
scene bg cafe inside:
    subpixel True
    zoom 1.5  xalign 0.0 yalign 0.5 yoffset -20
show eileen indoors_crossed lookaway neutral at leftside:
    subpixel True
    xzoom -1 xpos 0.17 yoffset 0
show millie outdoors_neutral even closedsad neutral at rightside:
    subpixel True
    zoom 1.0 yoffset -50 xpos 1.2
    time 1
    ease 1.8 xpos 0.71
    ease 1.0 yoffset 0
with fadeInOut
$ camera_reset()
play sound "sfx/chair_scrape_fast.ogg"
play music "music/millie_2.ogg" fadein 4.0
"Millie takes her coffee as the barista slides it across the counter, before strolling over and daintily taking a seat at our table."

show millie indoors_neutral even normal speaking at rightside:
    xpos 0.71 yoffset 0
    nod2
$ renpy.transition(dissolve, layer='master')
millie "Good afternoon, Allison, Eileen."

stop sound fadeout 1.0
show millie indoors_neutral neutral at rightside:
    xpos 0.71 yoffset 0
show eileen indoors_onhip closed open at leftside:
    xzoom -1 xpos 0.17 yoffset 0
$ renpy.transition(dissolve, layer='master')
eileen "'Afternoon. Welcome to Friday."

show eileen lookaway neutral at leftside:
    xpos 0.17
show millie indoors_tented raised closedhappy speaking at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
millie "Finally so, yes. Any plans for the weekend?"

show eileen normal neutral at leftside:
    xpos 0.17
show millie neutral at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
"Eileen and I exchange a brief glance. Both of us are looking forward to plans we made for Saturday, but there's still the day after."

show eileen indoors_crossed normal open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "Depends on the weather. I was thinking of heading out to the mountains with Wallace if it's not too bad."

show eileen indoors_crossed closed neutral at leftside:
    xpos 0.17
show millie indoors_neutral even normal at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
"As Eileen takes a long drink of her coffee, the majestic mountain ranges and foothills around the city float to mind. They'd be freezing cold this time of year, but she seems to be made of stern stuff. I hadn't taken her to be the outdoorsy type, though."

allison "That sounds nice. Hiking?"

play sound "sfx/mug-put-down.ogg"
show eileen indoors_onhip at leftside:
    xpos 0.17
    nod2
"Eileen shakes her head as she sets down her cup."

show eileen normal open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "We bought some permits for deer hunting."

stop sound fadeout 1.0
show millie raised frown at rightside:
    xpos 0.71
show eileen neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
allison "Deer hunting? As in, killing them?"

show eileen disbelief angry at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
"She stares at me for a moment before looking downward, trying to make sense of the words. It takes an awfully long time for her to formulate a response."

show eileen indoors_crossed lookawaynarrow angry at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
$ renpy.music.set_volume(0.2, delay=5.0)
eileen "...Well, we don't pet them. Wallace taught me how to shoot down at a range, and I take a loaner whenever we head out."

show millie indoors_neutral sad normal speaking at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
millie "So that's what Wallace gets up to outside the writing club. I did wonder about that."

show millie neutral at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
"It's nice that they found a way bond as friends, but to think of a big, proud deer lying dead on the grass..."

show eileen indoors_onhip lookawaynarrow open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "You do know how meat goes from an animal into a pretty little package at the supermarket, don't you?"

show eileen neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
"Of course I do, but I wouldn't want to personally involve myself at that level. Is that the point of a big day out for them?"

show millie raised closedsad neutral at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
"I have to admit that I'm little jealous of how they share this whole little world, but I don't think I could ever be a part of it. Millie reads the room quickly as I take another sip of my coffee."

$ renpy.music.set_volume(0.8, delay=2.0)
show millie indoors_tented raised normal speaking at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
millie "...Any plans yourself, Allison?"

show eileen normal neutral at leftside:
    xpos 0.17
show millie neutral at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
allison "Nothing so exciting; just shopping for groceries."

show millie indoors_neutral even half pout at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
millie "Sounds like my weekend plans. I'm the only one of my roommates with a car, so it's easiest if I do the groceries myself."

show eileen indoors_crossed lookaway open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "Speaking of roommates, what are your thoughts on this new club of Caprice's?"

show eileen neutral at leftside:
    xpos 0.17
show millie indoors_tented raised closedhappy speaking at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
millie "At first I thought it was just a diversion, but she really does want her art club to work out. She's talked a lot about you two as well, actually."

show eileen sad at leftside:
    xpos 0.17
show millie smile at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
"Eileen and I look to each other in concern, Millie offering no further explanation beyond an indulgent smile."

show eileen indoors_onhip normal at leftside:
    xpos 0.17
show millie even half at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
millie "For all I tease her, I am sincerely glad to see Caprice so happy. She shines brightest when she has something to work on."

show millie closedsad at rightside:
    xpos 0.71
$ renpy.transition(dissolve, layer='master')
"It's nice to see Millie care so much. They strike me as caring for each other as more than roommates, almost sisters or such."

"While I still feel the familiar pangs of homesickness from time to time, I'm finally seeing that sometimes family is more than who you grow up with. We all have people around to support us, and help in what we set ourselves to doing."

play sound "sfx/cell_phone_vibrate.ogg"
show eileen lookaway at leftside:
    xpos 0.17
show millie indoors_neutral raised normal mouthopen at rightside:
    xpos 0.71
    shaking2
"A ping from Millie's phone rings out, Eileen and I going silent as she hastily takes it from her coat pocket."

show eileen disbelief at leftside:
    xpos 0.17
show millie sad closedsad frown at rightside:
    xpos 0.71
$ renpy.transition(smoothDissolve, layer='master')
"The resigned frown spreading on her face shows it's not good news."

play sound "sfx/chair_scrape_fast.ogg"
show millie normal frown at rightside:
    xpos 0.71 yoffset 0
    ease 1.0 yoffset -50
"Noticing our concerned expressions, she soon moves to allay our worries."

show millie outdoors_neutral normal speaking at rightside:
    xpos 0.71 yoffset -50
    nod2
$ renpy.transition(dissolve, layer='master')
millie "Sorry, I have to go; affairs in my own club need attention. Sometimes I wonder why I do this to myself."

stop sound fadeout 1.0
show millie neutral at rightside:
    xpos 0.71
show eileen indoors_crossed closed open at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
eileen "I ask myself that question all the time. Take it easy."

show eileen lookaway neutral at leftside:
    xpos 0.17
$ renpy.transition(dissolve, layer='master')
allison "Take care in the snow; it's starting to pile up."

stop music fadeout 5.0
show millie outdoors_tented raised normal speaking at rightside:
    xzoom 1 xpos 0.71
    linear 0.7 xzoom -1 xpos 0.69
millie "I'll make sure to. See you around."

show millie even closedhappy neutral at rightside:
    xpos 0.69 alpha 1
    ease 1.7 xpos 1.2 alpha 0
pause 1.0
play sound "sfx/door_close_bell.ogg"
"The two of us wave her off, Millie quickly doubling back to fetch her still-full cup and take it with her."

scene bg cafe inside blurred2:
    zoom 1.5 xalign 0.25 yalign 0.5
show eileen indoors_fists closed neutral at offcenterright:
    zoom 1.2 yoffset 180
    xpos 0.55
with fadeInOut
"A brief silence ensues between the two of us as we sip at our own, the quiet chatter of other students and staff at the cafe providing background noise as we do."

play sound "sfx/mug-put-down.ogg"
allison "Sorry for being so weird. About the hunting, that is."

play music "music/painter.ogg" fadein 3.0
show eileen indoors_crossed lookawaynarrow sadmouth at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "I was shooting my mouth off. Forgot you liked animals and that sort of thing."

stop sound fadeout 1.0
allison "I didn't take you for liking the great outdoors."

show eileen indoors_onhip normal open at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "Being stuck indoors all the time is easy to do when focusing on painting, but it gets stifling after a while."

show eileen neutral at offcenterright
$ renpy.transition(dissolve, layer='master')
"It'd be nice to take a trip somewhere with Eileen, to the mountains or wherever else. Seeing the places she likes to go, and how it influences her art. Probably not to go hunting, though."

allison "Millie's nice. Keeping the writing club going sounds like a lot of work."

show eileen indoors_crossed narrow smile at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "See? Could never have had that nice chat if I hadn't called her over."

show eileen lookaway at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "You could stand to be a bit more social, you know. You're a good person; you'd get on perfectly fine with most."

"I'm flattered by what she's saying, but I'm not sure exactly how to put that into practice."

show eileen closed open at offcenterright
$ renpy.transition(dissolve, layer='master')
"Without a reply forthcoming, Eileen gives a flustered sigh."

show eileen indoors_onhip narrow angry at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "Allison, why do you think I joined this dumb club?"

"When she mentions it like that, I realize I never did give her a compelling reason. Caprice and I just pushed it on her until she broke, or at least that's how I understood it."

show eileen lookawaynarrow open at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "I actually thought about joining the existing art club for a while, back when they first offered. They seemed interested in me, and I was just some bewildered freshman who didn't know anything at that point."

show eileen narrow grumble at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "Over time, I realized they didn't give a damn about me. They just wanted my paintings, and my skills. I was a trophy for their club; something to be shown off. That was when I gave up on them."

allison "So you joined this one because Caprice was better?"

show eileen closed open at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "She's the last person I'd do this for."

show eileen indoors_crossed lookaway sadmouth at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "I joined the club for you, Allison."

show eileen lookawaynarrow at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "You just wanted to hang out while I did my thing. I liked that; there were no mental games and no need to worry about ulterior motives. I had someone to share my interests with. That's all I really wanted."

show eileen sad smile at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "Worked out pretty well, in the end. I got someone to share my love of painting with, and thought that maybe the club would help you open up a bit."

"She joined... for my sake, as well as her own? I awkwardly fiddle with my coffee cup, trying to think of how to reply as my cheeks flush."

allison "I don't know what to say."

show eileen indoors_onhip normal open at offcenterright
$ renpy.transition(dissolve, layer='master')
eileen "Well, I do: 'We need to get to class.'"

show eileen neutral at offcenterright
$ renpy.transition(dissolve, layer='master')
"Raising an eyebrow at the change of topic, I grab my phone and check the time."

scene bg cafe inside:
    subpixel True
    zoom 1.5 xalign 0.0 yalign 0.5 yoffset -20
    time 0.5
    easein 0.5 yoffset 30
show eileen indoors_onhip normal neutral at leftside:
    subpixel True
    xzoom -1 xpos 0.17 yoffset 0
    time 0.5
    easein 0.5 yoffset 50
with vpunch
$ camera_reset()
play sound "sfx/chair_scrape_fast.ogg"
stop music fadeout 2.0
$ renpy.sound.set_volume(1.0, channel="ambiance", delay=3.0)
"I really had completely lost track of time while relaxing here with Eileen."

show eileen outdoors_onhip closed neutral at leftside:
    xpos 0.17 yoffset 50
    nod2
$ renpy.transition(dissolve, layer='master')
"I quickly jump up from my seat, pushing it in as Eileen collects her things and swings her coat and scarf around her."

stop sound fadeout 1.0
show bg cafe inside:
    subpixel True
    zoom 1.5 xalign 0.0 yalign 0.5 yoffset 30
    time 1
    ease 2.0 xalign 0.25
show eileen outdoors_onhip normal neutral at leftside:
    subpixel True
    xzoom -1 xpos 0.17 yoffset 50
    ease 1.0 yoffset 0
    ease 2.0 xpos 0.68
$ renpy.pause(3.0, hard=True)
allison "Aah! Chemistry's just about to start! What class did you have coming up?"

$camera_move(2500,200,400,0,4,'ease')
pause 3.5
show eileen outdoors_crossed lookawaynarrow open at centerright:
    xpos 0.68 yoffset 0
$ renpy.transition(dissolve, layer='master')
eileen "...Math."

show eileen angry at centerright:
    xpos 0.68
$ renpy.transition(dissolve, layer='master')
"All energy dissipates from the situation as I pat her shoulder in sympathy."

stop ambiance fadeout 4.0
$ _dismiss_pause = False
allison "Hang in there, Eileen."

window hide dissolve
scene black with longDissolve
$ renpy.music.set_volume(1.0)
$ camera_reset()
return
