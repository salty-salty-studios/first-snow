label scene_4S2_en:
######################

$ ui_season = 'fall'
scene black with midDissolve
stop music fadeout 2.0
$ _dismiss_pause = True
voice "01_cap_b.mp3"
caprice "This is so exciting, Hayley!"

$ achievement.grant('story_hayley')
$ renpy.music.set_volume(0.5)
play music "music/diner_2_m2.ogg" fadein 5.0
$camera_move(2900,1200,680,0,0,'dissolve')
show cg act4 vacg1:
    alpha 0.0
    ease 5 alpha 1.0
voice "02_hay_a.mp3"
hayley "Uh huh."

voice "03_cap_b.mp3"
caprice "It's a long time coming too. Do you know if Millie knows yet?"

voice "04_hay_c.mp3"
hayley "I haven't talked to her since this morning."

voice "05_cap_a.mp3"
caprice "I can't wait to see her reaction. I'm gonna say something as soon as she gets home."

voice "06_hay_b.mp3"
hayley "Don't you think maybe she should hear it from them?"

voice "07_cap_c.mp3"
caprice "Ahh! But I really wanna tell her!"

voice "08_hay_b.mp3"
$camera_move(500,650,600,0,4,'ease')
hayley "I get it, but you know..."

play sound "sfx/door_open2.ogg"
show cg act4 vacg2 with smoothDissolve
voice "09_cap_b.mp3"
caprice "Millie!"

voice "10_mil_a.mp3"
millie "Hello. Got some stuff."

$camera_move(0,0,0,0,8,'ease')
voice "11_hay_a.mp3"
hayley "Welcome back, took a while."

voice "12_mil_b.mp3"
millie "There's so many people out there today."

voice "13_hay_b.mp3"
hayley "Guess it's the post-holiday rush."

voice "14_mil_b.mp3"
millie "That's not..."

voice "15_cap_b.mp3"
caprice "Millie! Millie! Have you heard the news?"

play sound "sfx/sack_drop.ogg"
scene cg act4 vacg3 with dissolve
voice "16_mil_a.mp3"
millie "Hm? I was at my dad's shop half the day."

voice "17_cap_b.mp3"
caprice "And?"

voice "18_mil_a.mp3"
millie "And what?"

voice "19_hay_c.mp3"
hayley "Car trouble again?"

scene cg act4 vacg background with smoothDissolve
show cg act4 vacg millie as cgm:
    subpixel True
    ycenter -0.5
    ease 1.5 ycenter 0.5
$ renpy.pause(1.5, hard=True)
voice "20_mil_a.mp3"
millie "Unfortunately."

show cg act4 vacg hayley as cgh:
    xalign 0 yalign 0
    xpos 372 ypos -20
with dissolve
voice "21_hay_a.mp3"
hayley "Maybe it's time for a new one?"

voice "22_mil_b.mp3"
millie "That's what dad said too. He even offered to help pay for it."

voice "23_hay_b.mp3"
hayley "You don't sound too thrilled."

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
with dissolve
voice "24_cap_b.mp3"
caprice "But what would you do with this one? Trash it?"

voice "25_mil_a.mp3"
millie "Well, sell it. Probably."

voice "26_hay_b.mp3"
hayley "If it still functions."

voice "27_mil_a.mp3"
millie "I don't want to, though."

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
    bounce
voice "28_cap_b.mp3"
caprice "Yeah, you can't!"

voice "29_hay_a.mp3"
hayley "Why not?"

voice "30_mil_a.mp3"
millie "I'd rather not accept something like that from him. He's already given me so much."

voice "31_cap_a.mp3"
caprice "And you can't just abandon it!"

voice "32_hay_b.mp3"
hayley "Sure you can, just leave it on the side of the road."

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
    nod2
voice "33_cap_b.mp3"
caprice "That car is like family!"

voice "34_mil_b.mp3"
millie "As I said, if I was upgrading I'd at least try to sell it."

show cg act4 vacg hayley as cgh:
    xalign 0 yalign 0
    xpos 372 ypos -20
    nod
voice "35_hay_a.mp3"
hayley "Hold on, let's go back to what Caprice said."

voice "36_cap_a.mp3"
caprice "Yeah! Listen. You've had that car since high school! Think of all the places it's taken us!"

voice "37_mil_a.mp3"
millie "We have spent quite a bit of time in that car. And besides..."

voice "38_hay_c.mp3"
hayley "It's like family?"

voice "39_mil_a.mp3"
millie "Dad and I worked on it together a lot. I'm kind of attached to the little thing."

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
    bounce
voice "40_cap_c.mp3"
caprice "Exactly!"

voice "41_hay_b.mp3"
hayley "I know the feeling. But you can't hold on to everything forever."

voice "42_mil_a.mp3"
millie "I know."

scene cg act4 vacg background
show cg act4 vacg millie as cgm
with midDissolve
$ renpy.music.set_volume(0.2, delay=1.0)
voice "43_cap_b.mp3"
caprice "I guess."

#There's a moment of quiet.
pause 1.5
$ renpy.music.set_volume(0.5, delay=1.0)
voice "44_mil_a.mp3"

millie "While we're on the topic, maybe some other people here should think about getting their licenses?"

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
with dissolve
voice "45_cap_a.mp3"
caprice "Umm..."

show cg act4 vacg hayley as cgh:
    xalign 0 yalign 0
    xpos 372 ypos -20
with dissolve
voice "46_hay_a.mp3"
hayley "I'm a supporter of public transit, actually."

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
    nod2
voice "47_cap_b.mp3"
caprice "Yes, that! Me too."

voice "48_mil_a.mp3"
millie "Oh really? Then you won't mind taking the tram from now on?"

voice "49_hay_a.mp3"
hayley "We like riding in your car, though."

voice "50_cap_b.mp3"
caprice "It's fun going together."

voice "51_mil_a.mp3"
millie "So much for that. At least consider it. It'd be good for the both of you."

voice "52_mil_a.mp3"
millie "Especially you, Caprice. I know you're getting your new club members to drive you around places now."

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
    bounce
voice "53_cap_a.mp3"
caprice "Hey! They want to go just as much as me."

voice "54_mil_a.mp3"
millie "Oh really? Did they say that?"

voice "55_cap_a.mp3"
caprice "More or less! Plus, I've helped them out too, you know. Thanks to me, love is blooming in the art room."

show cg act4 vacg hayley as cgh:
    xalign 0 yalign 0
    xpos 372 ypos -20
with dissolve
voice "56_hay_a.mp3"
hayley "How much of that was you?"

voice "57_cap_a.mp3"
caprice "Fifty--no--at least sixty percent!"

voice "58_hay_a.mp3"
hayley "Really? Only sixty?"

voice "59_mil_a.mp3"
millie "Please, just promise me. As much as I love you two, I won't always be there for you to rely on."

voice "60_cap_a.mp3"
caprice "You're not going anywhere, are you?"

show cg act4 vacg hayley as cgh:
    xalign 0 yalign 0
    xpos 372 ypos -20
with dissolve
voice "61_hay_a.mp3"
hayley "Don't worry. We promise. Right, Caprice?"

voice "62_cap_a.mp3"
caprice "Yes ma'am."

voice "63_mil_a.mp3"
millie "Thank you. I won't be going anywhere anytime soon. After all, I suppose you'll still be needing rides to class this semester."

voice "64_cap_b.mp3"
caprice "It's almost here! I'm getting excited."

show cg act4 vacg hayley as cgh:
    xalign 0 yalign 0
    xpos 372 ypos -20
    nod
voice "65_hay_b.mp3"
hayley "I'm not, really."

voice "66_mil_a.mp3"
millie "Ah, I've a full slate of classes. Plus there's a club to run."

show cg act4 vacg caprice as cgc:
    xalign 0 yalign 0
    xpos 1025 ypos 42
    bounce
voice "67_cap_a.mp3"
caprice "I'm gonna recruit so many more members! At least double the size!"

scene cg act4 vacg3
$camera_move(-1800,200,450,0,0,'dissolve')
with fadeInOut
voice "68_mil_a.mp3"
millie "I don't even want to think about it right now. Are you two hungry?"

voice "69_cap_a.mp3"
caprice "Starving!"

voice "70_hay_a.mp3"
hayley "You gonna cook, Millie?"

voice "71_mil_a.mp3"
millie "Oh, ugh."

voice "72_cap_c.mp3"
caprice "Not it!"

voice "73_hay_a.mp3"
hayley "What about the food you just bought?"

voice "74_mil_a.mp3"
millie "Today was exhausting. How about you, Hayley?"

voice "75_hay_b.mp3"
hayley "Er, let's just order something..."

voice "76_mil_a.mp3"
millie "Hmm, why don't we go out somewhere? Take the car together?"

voice "77_hay_c.mp3"
hayley "Weren't you just saying there's a lot of people out?"

voice "78_mil_a.mp3"
millie "Yes. But it's nice out, too."

voice "79_cap_b.mp3"
caprice "Oh, yeah! So about that news..."

voice "80_mil_a.mp3"
millie "Let's talk about it over dinner."

show cg act4 vacg4 with midDissolve
stop music fadeout 20.0
show cg act4 vacg ending as cg2:
    alpha 0
    ease 20.0 alpha 1
$camera_move(0,0,0,0,20,'ease')
voice "81_cap_c.mp3"
caprice "Okay! You drive! I call shotgun!"

voice "82_mil_a.mp3"
millie "I'm the only one who can drive."

voice "83_hay_a.mp3"
hayley "And we're very appreciative."

voice "84_mil_b.mp3"
millie "I'm looking forward to removing my tire chains. It's a little warmer today, so the snow is starting to let up..."

voice "85_hay_d.mp3"
hayley "Finally."

voice "86_cap_c.mp3"
caprice "It's about time!"

stop music fadeout 2.0
scene misc credits vo
with fadeInOut
$ renpy.pause()

scene black with longDissolve
$ camera_reset()
$ renpy.music.set_volume(1.0, delay=2.0)
return
