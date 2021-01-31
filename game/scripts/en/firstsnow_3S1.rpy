label scene_3S1_en:
######################
# Act 3, Scene 1

stop music fadeout 2.0
$ achievement.grant('story_act3')
scene title act3 with menuFade
$ renpy.pause(5.0, hard=True)
$ _dismiss_pause = True

scene black with longDissolve
window show dissolve

"One thing I hadn't counted on when asking Eileen if I could come over, was how large the distances involved were. I'm already feeling the difference from home."

"Colorado and Utah might be right next to each other on a map, but all to be seen between them are vast plains of utterly nothing."

"With noon approaching and little else around for miles as we motored down the endless strip of tarmac, Rose made the executive decision to chance this place for some lunch."

$ renpy.sound.set_volume(0.8, channel="ambiance")
play ambiance "sfx/ambiance/dinner-table.ogg" fadein 1.0
$ renpy.sound.set_volume(0.0, channel="ambiance2")
play ambiance2 "sfx/ambiance/outside.ogg" fadein 1.0
play music "music/anxiety_2_m.ogg" fadein 3.0
scene cg act3 roadtrip 1
$camera_move(-2800,-1600,800,0,0,'dissolve')
with midDissolve
$camera_move(2800,-1600,800,0,14,'ease')
"It's a little chintzy for my tastes - the faux-fifties interior decorated with a mishmash of cheap Americana - but Rose is in her element as she stuffs down another hunk of meat. At least it's quiet beyond the cheerful music, given we have the diner to ourselves."

"I'd barely slept all night, not only at the prospect of seeing Eileen's home, but at this being my first trip so far from my own."

"Right now, though, I'm just glad to be free of the motorbike's vibration and noise. I've finally become used to the odd short trip around the city, but this road trip is something else entirely."

scene cg act3 roadtrip 1 with midDissolve
$ camera_reset()
rose "Still getting your bike legs, huh?"

show cg act3 roadtrip 6 with dissolve
allison "It's been four hours, give me a break..."

show cg act3 roadtrip 2
rose "Three more to go."

show cg act3 roadtrip 6
"She digs in once more as I groan and try to swing my legs back to life."

rose "Man, the steaks here are amazing. You're missing out."

allison "I think I'll be fine."

scene cg act3 roadtrip 1
$camera_move(-2700,0,650,0,0,'dissolve')
with midDissolve
"I take a sip of my milkshake while gauging how best to tackle the huge plate of steaming nachos before me, buried in cheese, sauce, and sour cream. The jalapeños are carefully picked off and sitting to the side."

$ renpy.sound.set_volume(0.01, channel="ambiance", delay=7.0)
$ renpy.sound.set_volume(1.5, channel="ambiance2", delay=7.0)
$ renpy.music.set_volume(0.3, delay=7.0)
show cg act3 roadtrip 1 blurred4 as cg2:
    alpha 0
    ease 7.0 alpha 1
show cg act3 roadtrip window as act3_roadtrip_window
show bg texture:
    alpha 0
    ease 7.0 alpha 0.35
show snow light starting:
    alpha 0
    ease 7.0 alpha 1
with None
$camera_move(0,0,0,0,7,'ease')
$ renpy.pause(6.0, hard=True)
"There's not much to see out here as I glance out the window."

$camera_move(0,0,0,0,0,'dissolve')
show bg colorado park as colorado_park behind act3_roadtrip_window:
    xzoom -1 zoom 2.05 xcenter 0.5 ycenter 1.05 alpha 0.4
with midDissolve
"Just an endless plain stretching out to the horizon, an enthusiastic welcome sign at the otherwise invisible border being all that indicated we'd entered a different state."

"I'm not sure what I expected, really. I knew there are no rivers or anything defining the border, but it's a different thing to see that for yourself. It's just so... arbitrary. A line on a map, nothing more."

"Far from being any sort of revelation, it just makes me feel rather silly about being so sheltered. This all probably barely registered to Eileen as she drove along the lonely highway."

$ renpy.sound.set_volume(0.8, channel="ambiance", delay=2.0)
$ renpy.sound.set_volume(0.0, channel="ambiance2", delay=2.0)
$ renpy.music.set_volume(1.0, delay=2.0)
scene cg act3 roadtrip 1 with longDissolve
stop ambiance fadeout 2.0
show cg act3 roadtrip 2 with midDissolve
"Rose picks up her phone to check the address I gave her once again, forcing down the current chunk of steak she's eating with a giant gulp."

$camera_move(2850,-650,680,-2,10,'ease')
rose "Still have a while to go, huh? If it's as close to the big city as you've said, we shouldn't have a problem finding the place."

rose "So she's never told you anything about her home? Her family?"

allison "She mentioned her sister once."

stop ambiance fadeout 2.0
show cg act3 roadtrip 4 with midDissolve
"She scratches the back of her head as she thinks."

rose "I don't mean to pry, but I still don't get why she'd come all the way from outside the state to live in Utah. Not that I have anything against the place, I do like it, but it's not exactly where I'd choose if I were her."

rose "But coming here just for a community college? That's the part that gets me."

rose "I'm not exactly an artist, but from what you've said, she could probably get a scholarship at a proper college. Sounds like she could probably afford tuition even without one."

play ambiance "sfx/ambiance/dinner-table.ogg" fadein 1.0
scene cg act3 roadtrip 4
show bg colorado park as colorado_park:
    xzoom -1 zoom 2.05 alpha 0.4
    xcenter 0.5 ycenter 1.05
show cg act3 roadtrip window as act3_roadtrip_window
show bg texture:
    alpha 0.35
$camera_move(-2800,500,800,0,0,'dissolve')
with fadeInOut
$camera_move(-2800,-1200,800,0,8,'ease')
"Rose looks to me for answers, but I have none. When she puts it that way, there are vast stretches of Eileen's past that are total black spots to me."

"She leaves me to stew a little as we eat our respective meals, piping up again as she chews."

scene cg act3 roadtrip 4
show bg colorado park as colorado_park:
    xzoom -1 zoom 2.05 alpha 0.4
    xcenter 0.5 ycenter 1.05
show cg act3 roadtrip window as act3_roadtrip_window
show bg texture:
    alpha 0.35
$camera_move(2800,280,800,0,0,'dissolve')
with fadeInOut
stop ambiance fadeout 2.0
$camera_move(2800,-1500,800,0,10,'ease')
rose "Remember when you asked me about my family a few weeks ago, and I blew you off? I feel like I should probably explain that."

rose "Not to get too deep into things, I ended up cutting ties with my mom and pop. Given what my family was like, I wanted to have a clean break from them."

allison "Oh. Um, I'm sorry for bringing it up."

stop music fadeout 8.0
scene cg act3 roadtrip 6
$camera_move(2800,-1500,800,0,0,'dissolve')
with midDissolve
rose "I've made peace with it, don't worry. My point is..."

"Failing to remember, she starts circling her fork in the air."

rose "The point of all this was..."

play sound "sfx/fork_table.ogg"
with vpunch
pause 0.1
show cg act3 roadtrip 5 with dissolve
rose "Right, Eileen."

rose "I'm just sayin' that there might be a reason she's cagey about her personal life."

stop sound fadeout 1.0
$camera_move(0,0,0,0,10,'ease')
play music "music/snow_4_m.ogg" fadein 10.0
"I guess that makes sense. My nod earns a comforting grin."

rose "You're a good kid, Allison. I'm sure you'll do fine."

rose "In fact, you even taught me a little something."

rose "To be honest, I expected to be mothering you around when you first arrived to live with me. That you were some kid I already knew everything about, who I'd be left teaching adult life to."

rose "Yeah... I was kinda wrong there."

allison "But you've helped me so much! I couldn't have managed without you around."

rose "And you've surprised me so much. You made me rethink how much I know about the world and other folks as an adult. I got a little arrogant without even realizing it, and you brought me down to Earth."

rose "I thought adulthood was about knowing everything, but it's actually about admitting how much you don't know. I wanted to thank you for teaching me that."

play ambiance "sfx/ambiance/dinner-table.ogg" fadein 1.0
scene cg act3 roadtrip 1 with dissolve
"Satisfied with her explanation, Rose quickly gets back to her precious steak."

$ renpy.sound.set_volume(0.01, channel="ambiance", delay=5.0)
$ renpy.sound.set_volume(1.2, channel="ambiance2", delay=5.0)
$ renpy.music.set_volume(0.4, delay=5.0)
show cg act3 roadtrip 1 blurred4 as cg2:
    alpha 0
    ease 5.0 alpha 1
show bg colorado park as colorado_park:
    xzoom -1 zoom 2.05 alpha 0
    xcenter 0.5 ycenter 1.05
    ease 5.0 alpha 0.4
show cg act3 roadtrip1 nobg as act3_roadtrip1_nobg:
    alpha 0
    ease 5.0 alpha 1
show bg texture:
    alpha 0
    ease 5.0 alpha 0.35
"Left in thought, I get back to my own food."

"I didn't realize I could have such an impact on another's life, let alone Rose's. I looked up to her so much that I forgot we're both just muddling through life together."

"Eileen's lived so much of her life in a solitary manner, that maybe opening up to me isn't as easy. Maybe she just doesn't want to, given her past experiences."

$ renpy.sound.set_volume(0.8, channel="ambiance", delay=2.0)
$ renpy.sound.set_volume(0.0, channel="ambiance2", delay=2.0)
$ renpy.music.set_volume(1.0, delay=2.0)
stop ambiance fadeout 2.0
scene cg act3 roadtrip 1 with longDissolve
$ camera_reset()
rose "Eileen aside, this trip's probably a good thing; it'll push you out of your own comfort zone a little."

rose "You've already grown in the time I've been bunking with you. Just hang in there, alright?"

play ambiance "sfx/ambiance/dinner-table.ogg" fadein 1.0
show cg act3 roadtrip 3 with dissolve
allison "Thanks. I will."

rose "'Atta girl."

"Sharing a smile, we get back to our food."

stop ambiance fadeout 5.0
stop ambiance2 fadeout 5.0
stop music fadeout 5.0
scene black with longDissolve
$ _dismiss_pause = False
"Of all the people I might've ended up with as a roommate, someone like Rose was among the last I expected. Maybe she's just the sort of person who was best for me."

window hide dissolve
scene black with midDissolve
$ renpy.sound.set_volume(1.0, channel="ambiance2")
$ achievement.grant('story_act3_roadtrip')

return
