label scene_1S2_en:
######################
# Act 1, Scene 2

stop music fadeout 2.0
scene bg texture with menuFade
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg aptallison road sketch with inkfade
scene bg aptallison road with inkfade2
window show dissolve
stop sound fadeout 0.1
play ambiance "sfx/ambiance/outside.ogg" fadein 2.0
play music "music/relaxing.ogg" fadein 10.0
pause 0.5
play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 2.0
$ _dismiss_pause = True
"The Saturday's morning air is brisk as I stagger back from the supermarket, hands full with bags. The apartment itself may be nothing to write home about, but it's certainly in a good location."

"I still don’t feel like I've been pulling my weight when it comes to daily life with Rose, but at least I can help with errands like groceries. Her attempts to teach me handiwork skills have been less successful."

"Even this much has been a learning experience, my parents usually doing the shopping back when I lived with them."

window hide dissolve
play loopsfx "sfx/toolbox-rustling.ogg" fadein 1.0
scene bg aptallison outside day HD:
    xzoom -1
$camera_move(-1000,-2700,500,0,0,'dissolve')
show rose outdoors_smokingmouth normal neutral at left2:
    zoom 0.42 yoffset -680
    xpos 0.455
    ease 0.5 xoffset 2
    ease 0.5 xoffset -2
    ease 0.2 xoffset 0
    repeat 3
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.17
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.58
with midDissolve

letterbox "Reaching the apartment, I find Rose crouched outside and working on her motorbike."

letterbox "She looks perfectly content as she whiles away her time with tools spread around her, as if a child happily playing with their favorite toys."

scene bg aptallison outside with dissolve
$ camera_reset()
window show dissolve
allison "Working on the bike again?"

stop loopsfx fadeout 1.0
rose "Hmm? Oh, hey. That was quick."

play sound "sfx/body_prod.ogg"
show rose outdoors_smokingmouth normal puzzled at centerright:
    xpos 0.6 yoffset 200
    ease 1.0 yoffset 0
with dissolve
"She levers herself up with a grunt, before pulling back the edge of one bag with a finger to peer in, then another. I'm a little worried as she checks over my work."

"Having to hold my breath as she does isn't exactly helping. I'm still not used to the acrid smell of her smoking, but maybe that's a good thing."

stop loopsfx
stop sound fadeout 1.0
show rose outdoors_smoking normal talking at centerright:
    xpos 0.6 yoffset 0
$ renpy.transition(dissolve, layer='master')
rose "Good work; everything we needed, and no weird impulse-buys. Did we need more window cleaner, though?"

allison "You said to grab necessities if they're on sale and don't spoil, right?"

show rose smirk at centerright:
    xpos 0.6
$ renpy.transition(dissolve, layer='master')
rose "You're learning."

show rose smile at centerright:
    xpos 0.6
$ renpy.transition(dissolve, layer='master')
rose "Could you help me down here once you've put everything away? I need another set of hands."

stop ambiance fadeout 3.0
scene black with dissolve
"Without anything in particular planned for today, I agree before heading inside."

play sound "sfx/door_lock_jiggle.ogg"
"The rickety stairs creak as I slowly head up with groceries in hand, fumbling with the door handle."

play sound "sfx/door_open2.ogg"
pause 1.0
play sound "sfx/muffled-drop.ogg"
scene bg aptallison livingroom with vpunch
"My arms are thankful for the relief once I manage to drop the bags in the apartment after opening the door."

show bg aptallison livingroom blurred2:
    xalign 0.5 yalign 0.5
$ renpy.transition(dissolve, layer='master')
$ renpy.pause(1.0, hard=True)
show bg aptallison apartment kitchen as apartment_kitchen:
    xzoom -1 yanchor -0.41 ypos 0
    size (1280, 300) crop (0, 240, 1280, 300)
$ renpy.transition(dissolve, layer='master')
$ renpy.pause(1.0, hard=True)

stop sound fadeout 1.0
"Opening the fridge, I get to work stuffing in the frozen and cold items first. Next, I open the cabinet doors and start ladling in the cans and boxes."

"As the empty shelves fill, I get an odd sense of satisfaction from caring for myself."
##Changed a later line from doors to cabinets. Left this one as cabinet doors, but not 100% on whether I should've left it or changed it to cabinets as well.

"Living as an adult is busy work, but it's rewarding in its own way. There's an odd and unexpected feeling of accomplishment from doing even simple tasks. I'm sure it'll wear off in time, but I'm holding onto it for now."

hide apartment_kitchen
show bg aptallison livingroom
$ renpy.transition(dissolve, layer='master')
"With the job done, I close the cabinets and get back up to look about the room. The apartment is barely any warmer inside than out..."

"I suppose there are downsides as well as upsides. Putting it out of mind as best I can, I head back down to Rose."

play ambiance "sfx/ambiance/outside.ogg" fadein 3.0
play sound "sfx/door_close3.ogg"
scene bg aptallison outside
$camera_move(200,-250,650,0,0,'dissolve')
show shadow:
    alpha 0.4
show bg aptallison outside blurred1 as bg2:
    yanchor -0.55
    size (1280, 270) crop (300, 200, 1280, 270)
show rose outdoors_smokingmouth normal neutral as rose2:
    yanchor 0.975
    size (1920, 325) crop (-420, 10, 1920, 325)
show rose outdoors_smokingmouth normal neutral at center:
    alpha 0 xpos 0.5
with fadeInOut
play loopsfx "sfx/toolbox-rustling.ogg" fadein 0.5
"Slipping back outside and closing the door behind me, familiar clangs and bangs carry on the air as Rose still works away."

stop sound fadeout 1.0
show rose halfclosed as rose2
$ renpy.transition(dissolve, layer='master')
rose "Pass a rag, would you?"

"I quickly take a seat near her on a patch cleared of snow, grabbing one of the turn-up pieces of old shirt and handing it to her. She seems to be cleaning out some part of the engine or another."

show rose normal smile as rose2
$ renpy.transition(dissolve, layer='master')
rose "Anything interesting happening at school?"

allison "Not really; the schoolwork isn't too hard so far. A friend wants to start a club."

show rose outdoors_handonhip talking as rose2
$ renpy.transition(dissolve, layer='master')
rose "A club, huh? That's cool. What kind?"

allison "An art club, apparently. I'm not really sold on it though. I need to study, and she basically came up with the whole idea by herself."

show rose outdoors_smokingmouth neutral as rose2
$ renpy.transition(dissolve, layer='master')
"Rose passes the rag back and puts the part in place, motioning for me to hold it while she wrenches it back in. After a few grunts, the job appears to be done as she puts the wrench down with a clunk and turns back toward me."

show rose outdoors_handonhip halfclosed concerned as rose2
$ renpy.transition(dissolve, layer='master')
rose "Life's not about studying. I know you were a teacher's pet back in high school, but you could stand to be a bit more social."

"So it's this again. This is another downside of living here. With so much of my time spent alone with Rose, there's - for better or worse - no easy way to escape her questioning."

"I know she has my best interests in mind, though. I'm glad to have someone around to help me get to grips with adult life, even if I did find her intimidating at first."

allison "What was your college life like?"

show rose outdoors_smokingmouth halfclosed smirk2 as rose2
$ renpy.transition(dissolve, layer='master')
rose "Never had the chance to go."

"I'm left a little surprised as she gets back to her bike. I've only known Rose for a couple of months now, so I'm still finding out new things about her all the time."

show rose outdoors_handonhip halfclosed laugh as rose2
$ renpy.transition(dissolve, layer='master')
rose "Maybe you get why I'm on your case about this stuff now?"

rose "Not everyone gets the chances you have, so make the most of it. Go to parties, get some friends, and find a boyfriend sometime. Even if it doesn't last, it'll be a start."

$ renpy.music.set_volume(0.0, delay=8)
hide bg2
hide rose
hide rose2
with dissolve
show shadow:
    alpha 0.4
    ease 8.0 alpha 0.8
show bg aptallison outside
$ renpy.transition(dissolve, layer='master')
"My family always pushed me to put such things aside and focus on my education, so that’s what I did. The simplicity of life back then suited me just fine, and it worked out well going by my scholarship."

"I was never really interested in boys because I was so caught up in learning... is what I'd like to say, but I'm honest enough with myself to know that's not the whole story."

show misc rendered eileen first meeting sepia:
    xalign 0.5 yalign 0.5
    zoom 0.75 alpha 0.8
with midDissolve
"Seeing Eileen last week reminded me of that. Women like her keep catching my eye, and then there was that painting of hers. As time goes on, that difference in what I like looking at gets harder and harder to explain away."

stop loopsfx fadeout 3.0
rose "Rag, Allison?"

hide shadow
hide misc
with vpunch
"I hastily place a rag in her outstretched hand, Rose using it to try and rub some of the oil and grease off her hands."

"I'm sure she wouldn't mind if I'm not straight, if that's truly the case. While I'd like to talk with her about it, I can never quite seem to find the right time."

$ renpy.music.set_volume(1.0, delay=5)
scene bg aptallison outside with fadeInOut
$ camera_reset()
show rose outdoors_smokingmouth normal puzzled at centerright:
    xpos 0.6 alpha 0 yoffset 200
    ease 1.0 alpha 1 yoffset 0
rose "You alright?"

allison "Yeah. I was just thinking how life is complicated."

show rose neutral at centerright:
    xpos 0.6 alpha 1 yoffset 0
$ renpy.transition(dissolve, layer='master')
rose "Sure is."

show rose outdoors_smoking smile at centerright:
    xpos 0.6
$ renpy.transition(dissolve, layer='master')
rose "Hey, you bought that ice cream I asked for while you were out?"

allison "It's in the freezer now. Why?"

show rose halfclosed at centerright:
    xpos 0.6
$ renpy.transition(dissolve, layer='master')
rose "How about we have some. Could use a treat after working all morning on this thing."

"She has strange ideas about what makes a good dessert in the cold of winter, but I'm not going to stop her."

hide rose with dissolve
stop music fadeout 3.0
stop ambiance fadeout 3.0
"As the two of us start packing up, another peaceful day rolls by."

window hide dissolve
scene black with longDissolve
return
