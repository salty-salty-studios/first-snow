label scene_3S3_en:
######################
# Act 3, Scene 3

    perform "3S3_a"
    perform "3S3_b" explicit
    perform "3S3_c"
    return

label scene_3S3_a_en:

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg colorado house livingroom sketch HD
$camera_move(8500,-2500,-500,0,0,'dissolve')
with inkfade
scene bg colorado house livingroom fire HD
$camera_move(8500,-2500,-500,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
$ _dismiss_pause = True

play music "music/relaxing.ogg" fadein 2.0
$ renpy.sound.set_volume(0.4, channel='ambiance')
play ambiance "sfx/ambiance/fire.ogg" fadein 1.0
scene bg colorado house livingroom fire HD
$camera_move(8500,-2500,-500,0,0,'dissolve')
show eve outdoors normal neutral at left2:
    zoom 1.2 yoffset -200
    xzoom -1 xpos 0.22
with dissolve
$camera_move(-2000,-2500,-500,0,15,'ease')
window show dissolve

"Rubbing sleep from my eyes as I slowly drag myself to the living room, a restrained yawn heralds my entrance. I thought I might have trouble getting to sleep in an unfamiliar place, but after everything that happened, I crashed almost immediately."

"Looks like Eileen's family are early risers, noises from the kitchen presumably being from her parents, while the television blares away just ahead. The fire's crackling would make it quite a cosy scene, if not for being interspersed with cartoon voices."

show eve outdoors normal grin at left2:
    zoom 1.2 yoffset -200
    xzoom -1 xpos 0.22
    ease 0.8 yoffset -150
"Eve sits on the couch as I glance down, already bundled up in her winter outfit like a puffy ball of clothing. Eagerly watching the morning cartoons, her legs swing away as she happily munches on a bowl of brightly-colored cereal."

"I can't help but smile, reminded of my own childhood. The show and the setting might be different, but the innocence is just the same. I forgot what this simple experience felt like."

scene bg colorado house livingroom fire blurred2:
    zoom 1.5 xalign 0.1 yalign 0.25
show eve outdoors normal grin at centerright:
    zoom 1.4 yoffset 150
    xzoom -1 xpos 0.625
show eileen pjs_onhip neutral normal blur at leftside as eileen2:
    zoom 0.67 yoffset -235
    xpos 0.155
with fadeInOut
$ camera_reset()
"I take a seat beside the oversized hamster, Eve barely acknowledging my presence, before Eileen pops in from the kitchen and calls out to me. Looks like the coffee in her hand hasn't kicked in quite yet."

show bg colorado house livingroom fire
show eve outdoors normal grin blur at centerright:
    zoom 1.4 yoffset 150
    xzoom -1 xpos 0.625
show eileen pjs_onhip open normal at leftside:
    zoom 0.67 yoffset -235
    xpos 0.155
hide eileen2
with dissolve
voice "Eileen_Allison1.ogg"
eileen "Want any food? There's toast and cereal if you want any."

show eileen pjs_onhip neutral at leftside:
    xpos 0.155
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hm2.ogg"
allison "I don't usually eat breakfast. Thanks, though."

show eileen pjs_onhip neutral closed at leftside:
    xzoom 1 xpos 0.155 alpha 1
    linear 0.7 xzoom -1 xpos 0.11
    ease 1.0 xpos 0.17 alpha 0
"Shrugging in response, the tired Eileen heads back out."

$camera_move(-4000,-150,680,0,5,'ease')
"Despite settling down to watch Eve's cartoons with her, I can't help but eavesdrop as the conversation between Eileen and her mother can be heard from the other room."

stop ambiance fadeout 4.0
scene black with midDissolve
scene cg act3 kitchen
$camera_move(2500,250,650,0,0,'dissolve')
with midDissolve
elizabeth "Any plans for the day?"

$camera_move(-3400,450,800,0,4,'ease')
play sound "sfx/mug-put-down.ogg"
eileen "Was going to study for school."

stop music fadeout 8.0
elizabeth "Real studying? Not just drawing?"

stop sound fadeout 1.0
"The cartoon's loud exclamations punctuate the short silence that forms Eileen's reply."

$camera_move(2500,250,650,0,4,'ease')
elizabeth "Should have known."

elizabeth "I've seen your marks from high school. I just want you to do well."

elizabeth "Maybe you can have Allison help? She seems to have a good head on her shoulders."

$camera_move(0,0,0,0,5,'ease')
eileen "She's been helping me with my math already."

elizabeth "And here I was worrying about who you might end up with for a girlfriend."

eileen "You know I can handle myself fine, why worry?"

elizabeth "Because I'm your mother, that's why."

"Eileen doesn't exactly sound buoyed by the comments, but I have to admit that the praise is nice to hear."

play ambiance "sfx/ambiance/fire.ogg" fadein 1.0
$ renpy.music.set_volume(0.75)
play music "music/painter.ogg" fadein 4.0
scene bg colorado house livingroom fire
$camera_move(-500,200,300,0,0,'dissolve')
show eve outdoors neutral normal at offcenterleft:
    xzoom -1 xpos 0.45
with fadeInOut
"It is a bit sad to hear her mother doesn't approve of her pursuing art, though. I wonder how tempered this exchange is, thanks to them keeping things together since I'm around."

show cutin andrew1 as andrew:
    zoom 0.85 xoffset 62 yoffset 68
with dissolve
andrew "Morning, you two."

show cutin elizabeth1 as elizabeth:
    zoom 0.85 xoffset 62 yoffset 68
with dissolve
elizabeth "Going out, dear?"

andrew "Just swinging into town to grab paper and milk. Want to come along?"

show cutin elizabeth2 as elizabeth:
    zoom 0.85 xoffset 62 yoffset 68
with dissolve
elizabeth "Eve, Allison! We're heading out for a moment."

show eve outdoors happy at offcenterleft:
    xzoom -1 xpos 0.45
$ renpy.transition(dissolve, layer='master')
voice "Eve_Okay1.ogg"
eve "'Kay!"

show cutin andrew2 as andrew:
    zoom 0.85 xoffset 62 yoffset 68
with dissolve
andrew "We're going by your favorite shop, Eve!"

hide andrew
hide elizabeth
play sound "sfx/sack_drop.ogg"
show eve outdoors surprised normal at center:
    xzoom -1 xpos 0.45
    shaking2
with vpunch
eve "I'm coming! I'm coming!"

show eve outdoors surprised2 normal at center:
    xpos 0.45
    bounce
    ease 1.2 xpos 1.2
play sound "sfx/feet-shuffling.ogg"
"She drops her almost-finished bowl onto the coffee table so hastily that it nearly spills, skittering out to the door with a faint pitter-patter on the carpet. It's amazing how much energy kids have."

"Eileen's parents give a short farewell as they escort Eve out, the girl racing out straight to the car. To be a child again, filled with excitement for the next car trip or television show."

play sound "sfx/door_close2.ogg"
hide eve
show eileen pjs_crossed neutral lookaway at leftedge:
    xzoom -1 xpos 0.1
with dissolve
"With her family out the door, Eileen watches them drive off before heading over."

show eileen pjs_crossed neutral closed at offcenterleft:
    xzoom -1 xpos 0.1
    ease 1.5 xpos 0.42
play sound "sfx/mug-put-down.ogg"
"I shift over a little as she drops onto the couch, setting her coffee down with somewhat more care than her sister's cereal."

$camera_move(0,0,0,0,5,'ease')
show bg colorado house livingroom fire blurred2 as bg2 behind eileen:
    xalign 0.5 yalign 0.5 alpha 0
    ease 5.0 alpha 0.85
stop sound fadeout 1.0
"I give a loud stretch, but rather than being out of tiredness, it's more to calm myself as my heart starts beating in anticipation. We're finally alone, for real this time."

show eileen pjs_crossed lookawaynarrow smile at offcenterleft:
    xpos 0.42
$ renpy.transition(dissolve, layer='master')
"As I look over to Eileen, it's obvious that she has the same idea as she turns off the television."

show eileen pjs_onhip open narrow at offcenterleft:
    xpos 0.42
$ renpy.transition(dissolve, layer='master')
eileen "Want to pick up where we left off last night?"

show eileen pjs_onhip angry at offcenterleft:
    xpos 0.42
$ renpy.transition(dissolve, layer='master')
allison "I want to, but... isn't it kind of early for this?"

show eileen pjs_onhip closed at offcenterleft:
    xpos 0.42
$ renpy.transition(dissolve, layer='master')
"She has to think that one through."

stop music fadeout 4.0
show eileen pjs_onhip smile narrow at offcenterleft:
    xpos 0.42
$ renpy.transition(dissolve, layer='master')
eileen "...It'll wake us up."

scene black with vpunch
"I'm not given a chance to respond as she presses her lips to mine, not that I particularly wanted to argue the fact. This'll likely be the last time we can share a moment like this for a good while."

return

label scene_3S3_b_clean_en:
    return

label scene_3S3_b_en:

$ renpy.music.set_volume(1.0)
$ renpy.sound.set_volume(0.3, channel="ambiance", delay=4.0)
play music "music/romance_2_m.ogg" fadein 4.0
scene cg act3 mast1
$camera_move(400,-2000,850,0,0,'dissolve')
with longDissolve
stop sound fadeout 1.0
"Words dispensed with, we lean into each other and begin to make out, hands busily exploring each other."

"I feel like I'm melting, between the warmth of Eileen and the fire, the soft couch we sink into, and her tongue against mine."

show cg act3 mast2 with smoothDissolve
"Needing air from all the excitement, we break from our kiss as I take a breath."

$camera_move(400,205,600,0,5,'ease')
"Eileen's hand slips down and rests on my thigh, a long breath from her nose playing on my lips as it slowly begins to move up my leg."

"Giving myself to the flow of things, I move my hand over to Eileen, the both of us beginning to slowly stroke each other."

"Long sighs fill the air as we enjoy the feeling of each other, all our worries being forgotten. I'm really sure how long we go, but time has completely escaped both of us by now. For this one brief time, all my worries seem to evaporate."

show cg act3 mast3 with midDissolve
"As we start to squirm and become less focused in our movements, my body starts yearning for more."

"Eileen's clumsy movements are endearing; her pride won't let me take the lead, but she's not as used to this as she thinks."

$camera_move(-50,-450,200,0,5,'ease')
pause 5.0
show cg act3 mast4 with midDissolve
eileen "Allison..."

"As the fire crackles away, we find a good pace and manage to get some sort of comfortable movement going."

"The sight of her smiling as she dreamily lets the pleasure flow through her etches itself into my memory, the fire casting shadows across her face."

show cg act3 mast5 as cg2:
    alpha 0
    ease 0.8 alpha 1
show white:
    alpha 0
    ease 0.8 alpha 0.2
$camera_move(-50,450,200,0,0.8,'ease')
"My own noises are cut short as pleasure overwhelms me, my throat tending along with my entire body. Oh, Eileen. All I can think of is her beautiful body as I frantically clutch at the ecstasy filling me up."


"All too soon, though, it begins to ebb. While I savor the last shudders of joy, it eventually, sadly, ends."

scene black with midDissolve
show cg act3 mast6
show white:
    alpha 0.2
$camera_move(400,-2000,850,0,0,'dissolve')
with midDissolve
stop music fadeout 4.0
"Try as I might to catch on to any specific train of thought, I can't focus at all. Both of us are simply left to gaze at each other with dreamy eyes. Speaking proves impossible, too, with Eileen not even trying try as she sits back and recovers herself."

show cg act3 mast7 with smoothDissolve
show white:
    alpha 0.2
    ease 3.0 alpha 0
"All we do, all we want to do, is hold each other as the afterglow wears off."

return

label scene_3S3_c_en:

stop ambiance fadeout 4.0
scene black with longDissolve
$ camera_reset()

$ renpy.sound.set_volume(1.0, channel='ambiance')
play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
scene bg colorado house ext blur:
    xalign 0.0 yalign 1.0
show cg act3 snowmen allison as act3_snowmen_allison:
    xoffset -200
$camera_move(3000,1600,650,0,0,'dissolve')
with midDissolve
$camera_move(-1500,1600,650,0,15,'ease')
play music "music/snow_4_m.ogg" fadein 15.0
"The snow makes a satisfying sound as I pat it down, each handful making the sphere before me that little bit larger. It's surprising how much physical work putting a snowman together is, but this is my first time making one this size."

"Standing out on the front lawn in the cold of early morning, I keep patiently patting away at my creation, slowly but surely building him up. I've been wanting to make a snowman for a while now, but between moving, studying, and hanging out with others, there just hasn't been much time."

"While I might have wanted to keep lazing around with Eileen, her family probably won't take much longer to get back, and she wanted to keep practicing her art. If nothing else, at least we're both a lot more awake now."

$camera_move(-1500,-800,650,0,15,'ease')
"It's rather nice to be out here, despite the cold, and given some much-needed time to unwind. I think I'm living up to the expectations of Eileen's family, but living in another's home under the gaze of strangers is still stressful."

"Not that I'm alone out here; the odd squirrel flits about in the distance between the trees, and birds can be heard chirping away from the pines. I wonder if Eileen, for her love of the outdoors, appreciates the sounds of nature around here. Even if you're the only person around, you're never really alone."

"The air is nice here, too. Fresh, with just a hint of pine wafting from the trees."

scene bg colorado house ext with fadeInOut
$ camera_reset()
play sound "sfx/car-door-slam.ogg"
"It's only when a car door clangs shut behind me that I realize I've become so distracted with my surroundings."

show eve outdoors neutral normal at rightedge with dissolve
"Her father makes idle mention of how little traffic they encountered as they pass into the house, with her mother guessing that that the cars must be going in the direction of the city instead."

stop sound fadeout 1.0
show eve outdoors neutral normal at center:
    xpos 0.95
    bounce
    ease 1.5 xpos 0.5
"Eve bounces out of the car after them, before stopping to spy at what I'm up to."

show eve outdoors happy normal at center
$ renpy.transition(dissolve, layer='master')
voice "Eve_Oooh.ogg"
eve "Ah, a snowman!"

allison "Yup! Never had the time to make one back home. Want to build one too?"

show eve outdoors grin at center:
    bounce
eve "Yeah!"

$camera_move(250,400,350,0,3,'ease')
"Needing no further prompting, she enthusiastically rushes past me and crouches down, pushing together snow with her tiny gloved hands."

scene black with midDissolve
scene cg act3 snowmen
$camera_move(-3500,1850,820,0,0,'dissolve')
with midDissolve
$camera_move(-3500,500,820,0,8,'ease')
"The two of us start working away, with her snowman slowly starting to take form next to mine."

"There's almost a therapeutic feel to it all, relaxing outside as I see the large snowman coming together with each little step. Even Eve seems to have quieted down, focused wholly on her work. Maybe this is a bit what sculpture is like."

"It's satisfying to build something with my own hands, and see an object form where there was nothing before."

"Looking over to Eve's snowman as I go, I'm impressed with how quickly she's managed to get something together, the slightly lopsided figure roughly equal to her height."

$camera_move(0,0,0,0,10,'ease')
allison "Wow, you must have lots of practice."

"She continues working away at it, making a bit of a show of pounding the snow into shape with both hands, her entire upper body being put into it."

eve "Eileen taught me how to make snowmen."

"There's a bit of hesitation still, as if reminding herself that she shouldn't talk too much to the stranger suddenly hanging around her sister. Hopefully the fun of sharing the experience might help distract her."

scene bg colorado house ext
show bg colorado house ext blurred4 as bg2:
    xalign 0.5 yalign 0.5 alpha 0.9
show eve outdoors neutral normal at center:
    zoom 1.4 yoffset 150
with fadeInOut
$ camera_reset()
allison "It sounds like you and Eileen are really close."

show eve outdoors unsure at center
$ renpy.transition(dissolve, layer='master')
eve "I don't get to play with her much now that she's moved out."

eve "I miss her when she goes away, but mom and Eileen always argue when she's home."

allison "You could visit her back in Utah, maybe? I'm sure she'd like the company."

show eve outdoors half at center
$ renpy.transition(dissolve, layer='master')
eve "Dad says we will, but he's always got work."

show eve outdoors shy normal at center
$ renpy.transition(dissolve, layer='master')
eve "I wanna see her paintings, she was always making them before she went away."

allison "Her paintings are really pretty, aren't they?"

show eve outdoors sad normal at center
$ renpy.transition(dissolve, layer='master')
eve "Yeah, but mom said it's not a real job, so Eileen gets mad."

allison "What about dad?"

show eve outdoors sad half at center
$ renpy.transition(dissolve, layer='master')
eve "Dad said he thinks the same, but that they shouldn't fight so much over it."

allison "Sounds like they don't get along very well."

show eve outdoors neutral normal at center
$ renpy.transition(dissolve, layer='master')
eve "Hey, can you make Eileen happier?"

allison "I'll certainly do my best."

show eve outdoors grin normal at center
$ renpy.transition(dissolve, layer='master')
"Satisfied with the best answer I could drum up, she goes back to work on her snowman, little hands collecting some more snow to pat on."

stop music fadeout 5.0
scene black with midDissolve
scene cg act3 snowmen
show cg act3 snowmen blurred4 as cg2
show cg act3 snowmen allison as act3_snowmen_allison
$camera_move(-750,400,350,0,0,'dissolve')
with midDissolve
"I might say that, but I don't really know where to begin, now that I think about it. She's done a lot for me, but when I think back to when we've been together, all I've been able to do around her is watch as she draws and paints."

"I'm just getting myself worried over her; as she said, Eileen's perfectly capable of looking after herself. It's not like she needs me to be happy."

"Trying to stop myself from dwelling, I focus on patting the head of my snowman some more to make it a bit less rectangular."

hide cg2 with midDissolve
eve "Do you paint too?"

scene bg colorado house ext blurred4:
    xalign 0.5 yalign 0.5 alpha 0.9
show eve outdoors neutral normal at center:
    zoom 1.4 yoffset 150
with fadeInOut
$ camera_reset()
allison "Not really. I just draw cute things."

play music "music/eve_3_m.ogg" fadein 3.0
show eve outdoors happy normal at center:
    zoom 1.4 yoffset 150
    easein .15 yoffset 132
    easeout .175 yoffset 150
    easein .15 yoffset 142
    easeout .175 yoffset 150
eve "I draw too! Can I show you my drawings later?"

allison "Sure, that'd be great!"

show eve outdoors grin normal at center
$ renpy.transition(dissolve, layer='master')
"As she beams a grin, I'm glad to finally be making headway with her. I never thought I'd be bonding through messing about in the snow."

allison "Have you shown Mom and Dad?"

show eve outdoors unsure normal at center
$ renpy.transition(dissolve, layer='master')
voice "Eve_Grumble1.ogg"
eve "They're always busy, so I can't always show them. My nanny's seen all of them, though! She's nice."

"A nanny, huh? I suppose you don't get to live this nicely without some sacrifices. I wonder if Eileen was raised by a nanny too."

"I wonder if either of them ever really connected with their parents."

scene bg colorado house ext
show eve outdoors neutral normal at right2:
    xzoom -1
with fadeInOut
play sound "sfx/door_open.ogg"
"As we work away on our creations, the door opens once more."

show eileen indoors_onhip neutral normal at leftside:
    xpos -0.2 xzoom -1
    ease 1.5 xpos 0.15
"Looking around to see who it is, a familiar figure strides up. I do worry about her long boots in the slippery snow, but she doesn't seem bothered."

stop sound fadeout 1.0
show eileen indoors_crossed open disbelief at leftside:
    xzoom -1 xpos 0.15
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "What are you two doing?"

show eileen indoors_crossed neutral at leftside:
    xpos 0.15
show eve outdoors grin normal at right2:
    xzoom -1 xpos 0.775
    linear 0.7 xzoom 1 xpos 0.79
    bounce
doublespeak allison eve "Making snowmen!"

show eileen indoors_crossed narrow angry at leftside:
    xpos 0.15
$ renpy.transition(dissolve, layer='master')
eileen "You don't say."

show eileen indoors_onhip open lookaway at leftside
$ renpy.transition(dissolve, layer='master')
eileen "Well if you want some lunch instead of freezing out here making snowmen all day, come in from the cold already."

show eve outdoors unsure normal at right2:
    xpos 0.79
show eileen indoors_onhip neutral at leftside
$ renpy.transition(dissolve, layer='master')
voice "Eve_SadOh3.ogg"
eve "But I wanna make him better..."

show eileen indoors_crossed neutral normal at leftside:
    zoom 1.2 yoffset 180
with smoothDissolve
"Eileen studies her work for a moment, before reaching over towards me."

show eve outdoors unsure half at right2:
    xpos 0.79
show eileen indoors_crossed neutral normal at leftside:
    zoom 1.0 yoffset 0
with vpunch
"Too confused to respond, I just stand there as Eileen's hands reach over and... take my scarf in their grip."

show eileen indoors_onhip neutral lookaway at leftside:
    xpos 0.15
    ease 1.5 xpos 0.5
    nod2
"Unwinding it from my neck, she silently walks over to Eve's snowman and smartly wraps it around what's probably supposed to be the neck."

show eileen indoors_onhip smile closed at center
show eve outdoors happy normal at right2:
    xpos 0.79
$ renpy.transition(dissolve, layer='master')
voice "Eve_Giggle.ogg"
eve "That looks cool!"

show eileen indoors_crossed normal open at center
show eve outdoors neutral normal at right2:
    xpos 0.79
$ renpy.transition(dissolve, layer='master')
eileen "There, he'll be happier now that he's less cold. He'll still be here when you get back, so go and eat something."

show eileen indoors_crossed smile narrow at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh3.ogg"
eileen "...Your show is starting, you know."

show eve outdoors surprised normal at right2:
    xpos 0.79 alpha 1
    bounce
    ease 1.0 xpos 0.25 alpha 0
play sound "sfx/feet-shuffling.ogg"
stop music fadeout 8.0
"Shocked that she might be missing even a minute, she completely drops any attention she had on the snowman and stomps off as quickly as her restricting clothing allows. It's obvious Eileen has Eve wrapped around her little finger."

show bg colorado house ext:
    subpixel True
    xalign 0.5
    ease 2.0 xalign 0.44
show eileen indoors_onhip angry normal at center:
    subpixel True
    xpos 0.5
    ease 2.0 xpos 0.45
"All I'm left to do is stare at Eileen, pouting."

hide eve
show eileen indoors_onhip neutral disbelief at offcenterleft
$ renpy.transition(dissolve, layer='master')
stop sound fadeout 1.0
eileen "You can grab your scarf back when Eve gets bored of making him."

voice "Allison_Sigh2.ogg"
allison "I was going to use it on my own snowman..."

show eileen indoors_crossed narrow open at offcenterleft
$ renpy.transition(dissolve, layer='master')
stop ambiance fadeout 4.0
$ _dismiss_pause = False
voice "Eileen_Seriously3.ogg"
eileen "I swear, you're worse than her sometimes."

window hide dissolve
scene black with longDissolve
return
