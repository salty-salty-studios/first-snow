label scene_3S2_en:
######################
# Act 3, Scene 2

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg colorado town HD sketch
$camera_move(1800,-5000,200,0,0,'dissolve')
with inkfade
scene bg colorado town HD
$camera_move(1800,-5000,200,0,0,'dissolve')
with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
"The two of us find ourselves in a surprisingly quaint little corner of America. A heavily forested town, with snow-covered pines visible no matter which direction you look. Wood seems to be the norm for building around here, rather than concrete."

"I find it quite charming, actually. I was worried I'd be awkwardly roaming through some manicured slice of suburbia, but this feels closer to a friendly country town. Almost something from one of Eileen's Westerns."

$ renpy.music.set_volume(0.75)
play music "music/snow.ogg" fadein 2.5
scene bg colorado house ext blurred4:
    xalign 0.0 yalign 1.0
show rose outdoors_handonhip normal talking at center:
    zoom 1.2 yoffset 180
    xzoom 1 xpos 0.5
with midDissolve
$ camera_reset()
rose "Just give me a call the day before you want to come back, alright?"

show rose outdoors_handonhip normal neutral at center
$ renpy.transition(dissolve, layer='master')
allison "I will. Thanks again for all this, I know it's a really long way."

show rose outdoors_handonhip laugh at center:
    xzoom 1 xpos 0.5
    linear 0.7 xzoom -1 xpos 0.52
rose "Don't worry, it's a nice ride out to here, anyway. Might stick around a bit before heading back."

show rose outdoors_handonhip at right2:
    xzoom -1 xpos 0.52
    ease 1.2 xpos 0.77
"As she walks back to her bike, she stops and turns around once more, raising her hand in farewell."

show rose outdoors_handonhip talking normal at right2:
    xzoom -1 xpos 0.77
    linear 0.7 xzoom 1 xpos 0.75
rose "If you ever want to give me a call, go ahead! It's no problem!"

show rose outdoors_handonhip smile halfclosed at right2:
    xzoom 1 xpos 0.75
    easein .15 yoffset 162
    easeout .175 yoffset 180
    easein .15 yoffset 172
    easeout .175 yoffset 180
rose "I'll be seein' ya, Allison!"

allison "Bye, Rose. Thanks for everything."

show rose outdoors_handonhip smile normal at right2:
    xzoom 1 xpos 0.75 alpha 1
    linear 0.7 xzoom -1 xpos 0.77
    ease 1.2 xpos 1.2 alpha 0
play sound "sfx/motorbike.ogg" fadein 2.0
"She beams a smile as she gets back on her bike, fitting her helmet before kicking back the stand."

"With a flick of her wrist and press of her foot, her bike roars to life, Rose sailing off down the road and around the corner out of sight."

play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 2.0
show bg colorado house ext blurred4:
    subpixel True
    xalign 0.0 yalign 1.0 alpha 1
    ease 3.0 xalign 0.5 yalign 0.0
show bg colorado house ext as bg2:
    subpixel True
    xalign 0.0 yalign 1.0 alpha 0.0
    ease 3.0 xalign 0.5 yalign 0.0 alpha 1.0
"I do my best to appear natural as I turn back to the house before me, duffel bag of clothes slung over my shoulder."

"The scenery around here is nice, and there's hardly a crowd. In fact, I'm the only person around at all."

window hide dissolve
scene bg colorado house ext
$camera_move(3000,-1900,600,0,0,'dissolve')
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter -0.07
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.655
with fadeInOut
$camera_move(-3000,-1900,600,0,15,'ease')
stop sound fadeout 1.0

letterbox "Now that I get a good look at it, Eileen's house sure is big."

letterbox "My eyes slowly scan around as I slowly make my way down the front garden path, taking in every detail."

letterbox "I guess being outside the city would make bigger houses a little more affordable."

stop loopsfx
scene bg colorado house ext HD
$camera_move(-8000,-2500,500,0,0,'dissolve')
with fadeInOut
window show dissolve
play sound "sfx/doorbell.ogg"

"With a gulp, I gingerly press the doorbell beside the solid oaken door, quickly brushing my clothes with my hands afterwards to look as presentable as possible."

"Even as muffled footsteps approach, I'm trying to flick a little snow from my hair."

show eileen indoors_fists smile normal at leftedge:
    zoom 0.7 yoffset -400
    xzoom 1 xpos -0.11 alpha 0
    ease 1.0 xpos -0.16 alpha 1
play sound "sfx/door_open.ogg"
"As Eileen opens the door, I'm greeted by a warm smile. That reflexive reaction at the sight of me makes me feel better already."

show eileen indoors_crossed smile narrow at leftedge:
    xzoom 1 xpos -0.16 alpha 1
    linear 0.7 xzoom -1 xpos -0.2
eileen "Fancy seeing you here."

stop sound fadeout 1.0
allison "I made it, in the end."

show eileen indoors_onhip normal open at leftedge:
    xzoom -1 xpos -0.2
$ renpy.transition(dissolve, layer='master')
eileen "Enjoy the bike ride?"

show eileen indoors_onhip neutral at leftedge:
    xpos -0.2
$ renpy.transition(dissolve, layer='master')
allison "Yeah, it was... great."

show eileen indoors_onhip disbelief angry at leftedge:
    xpos -0.2
$ renpy.transition(dissolve, layer='master')
"I don't think I managed to make that very convincing."

show eileen indoors_onhip lookaway at leftedge:
    xpos -0.2
$ renpy.transition(midDissolve, layer='master')
"Looking at each other, I think we both realize we're just making smalltalk."

$camera_move(-9500,-2800,800,0,3,'ease')
show eileen indoors_onhip closed smile at leftedge:
    xpos -0.2
    time 2
    ease 0.5 yoffset -395
    ease 0.5 yoffset -405
    ease 0.2 yoffset -400
"She leans forward, the two of us sharing a momentary kiss before she nods for me to come in."

show eileen indoors_onhip lookaway smile at leftedge:
    subpixel True
    zoom 0.7 yoffset -400
    xzoom -1 xpos -0.2 alpha 1
    ease 1.2 xpos -0.12 alpha 0
"It's strange how such a simple action can feel so nice every time, my heart skipping even from the most gentle peck."
stop music fadeout 8.0
$camera_move(-9200,-3000,900,0,2.5,'ease')
pause 1.5

stop ambiance fadeout 2.0
play sound "sfx/door_close.ogg"
scene black with dissolve
$ camera_reset()
scene bg colorado house livingroom with midDissolve
show eileen indoors_onhip normal neutral at left2:
    xzoom -1 xpos -0.2
    ease 1.2 xpos 0.24
"I obediently follow her inside, closing the door behind me as I do."

show eileen indoors_crossed open at left2:
    xzoom -1 xpos 0.24
$ renpy.transition(dissolve, layer='master')
eileen "Dad, she's he-!"

play sound "sfx/feet-shuffling.ogg"
show eve indoors surprised normal at right2:
    xpos 1.2
    ease 1.0 xpos 0.6
    shaking2
    ease 2.0 xpos 0.75
show eileen indoors_crossed lookaway neutral at left2:
    xpos 0.24
$ renpy.transition(dissolve, layer='master')
"Eileen's cut off by the sound of socked footsteps on carpet rapidly approaching. A small figure suddenly skips around the corner of the stairs and out into the entrance way, nearly barreling straight into Eileen before stopping herself."

show eve indoors unsure half at right2:
    xpos 0.75
$ renpy.transition(dissolve, layer='master')
"With both of us taken by surprise, the small girl examines me. Likely around 10 by the looks of her, it's difficult not to see a bit of Eileen in her face."

stop sound fadeout 1.0
allison "Hello there."

$camera_move(-1800,0,400,0,5,'ease')
show eileen indoors_onhip closed open at left2:
    xpos 0.24
show eve indoors shy behind eileen at right2:
    xpos 0.75
    ease 1.5 xpos 0.42
"She quickly shuffles behind Eileen in response, her apprehensive face peering out from safety. Eileen just gives a sigh in response."

stop music fadeout 2.0
show eve indoors shy behind eileen at offcenterleft:
    xpos 0.42
show eileen indoors_onhip frowning smile at left2:
    xpos 0.24
$ renpy.transition(dissolve, layer='master')
eileen "Welcome to the family."

$ renpy.music.set_volume(0.85)
scene black with circlewipe
play music "music/eileen_5_m.ogg" fadein 3.5
scene cg act3 familydinner 1 HD
$camera_move(600,5200,380,-2,0,'dissolve')
with circlewipe
"The smell of freshly-cooked chicken wafts in the air, the skin still steaming away with an appetizing glint. The line of plates down the center of the table hardly lacks for sides, either, with potato salad, coleslaw, lettuce, and other greens."

$camera_move(-6500,2800,250,2,8,'ease')
"While I'm thankful for the luxurious dinner before me, it's a rather quick introduction to her family. I can't help but feel intimidated when surrounded by everyone at once."

"With her father already preparing dinner as Eileen let me in, and her mother arriving from work only soon after, it was unavoidable. That being the case, here we all are, gathered around one big table."

"While not exactly a mansion, it's obvious Eileen's family lives very comfortably. I'd probably be green with envy at how well-off they are, if not for being so self-conscious of how to act in front of them."

scene cg act3 familydinner 1
$camera_move(-1600,-1400,750,2,0,'dissolve')
with fadeInOut
show cg act3 familydinner 2 with midDissolve
andrew "I suppose some proper introductions are in order, now that we're all together."

andrew "I'm Eileen's father, Andrew, and this is my lovely wife Elizabeth."

show cg act3 familydinner 3
$ renpy.transition(dissolve, layer='master')
elizabeth "A pleasure. And you would be Allison?"

allison "Oh, um, yes. Allison Merlo."

"My nerves seem to amuse her father as he gives a reassuring smile."

andrew "This isn't a job interview, you can relax."

allison "Right, yeah. Sorry."

show cg act3 familydinner 4
$ renpy.transition(dissolve, layer='master')
"I let out a long breath to try and relax a little, though it doesn't really work."

$camera_move(0,0,0,0,8,'ease')
andrew "Well now, let's dig in. I'm no chef, but it hopefully shouldn't give you food poisoning."

play ambiance "sfx/ambiance/dinner-table.ogg" fadein 0.1
"Smiling politely at his attempt to lighten the mood, I start to ladle this and that from the large plates. My mouth's already watering at the prospect of so much wonderful smelling food; Rose might be many things, but she isn't a cook."

show cg act3 familydinner 3
$ renpy.transition(dissolve, layer='master')
"Satisfied with my selection of meat and salads, I pile some potato salad onto my fork and tentatively have a taste. My reactions seem to draw some smiles as I make progress on the meal, but I'm so enamored with the food, I can't help but keep going."

elizabeth "It's nice to see Eileen's already made friends in college."

$ renpy.music.set_volume(0.5, delay=0.3)
"A brief panic comes over me as I realize we haven't talked this over. Is she out to her parents? Are we going to play this as simply friends? As I mull over how to handle things, Eileen's voice cuts through."

eileen "Allison's my girlfriend. I probably should've mentioned that earlier."

stop ambiance fadeout 2.0
stop music fadeout 2.0
show cg act3 familydinner 10 with hpunch
"Everything seems to stop for a moment."

show cg act3 familydinner 5
$ renpy.transition(dissolve, layer='master')
elizabeth "Yes, you should have."

eileen "I thought you said having a girlfriend wouldn't be a problem."

$ renpy.music.set_volume(1.0)
play music "music/questioning.ogg" fadein 8.0
$camera_move(-1600,-1400,750,0,20,'ease')
elizabeth "You know that isn't what I'm talking about. This isn't the first time you've kept us in the dark since moving out."

"I have to admit that I can sympathize with her mother, which puts me in a delightfully awkward spot. Eileen's father makes no attempt to mediate as he eats, which is probably the best approach."

eileen "I didn't think I needed to report back on everything I did."

elizabeth "Don't you think this is important enough to warrant a phone call?"

"Neither Eileen nor her mother raise their voice, even eating the odd bit of food as they quibble. The argument almost feels routine, which going by her father's reaction, might well be the case. Even her sister is still eating, albeit with badly-hidden glances."

show cg act3 familydinner 6
$ renpy.transition(dissolve, layer='master')
elizabeth "I mean, our daughter's first girlfriend! Isn't it nice she's gained something from college?"

"She looks pointedly to her husband with just an edge of snark to her voice, but he - perhaps smartly - simply acknowledges her with a smile. Dropping that on them here and now is quite the decision."

"I'm beginning to wonder why I thought this was a good idea. I can't read her parents at all, but I can already tell my presence here is only increasing a tension that usually permeates this household."

eileen "Well, you know now."

stop music fadeout 4.0
play ambiance "sfx/ambiance/dinner-table.ogg" fadein 3.0
scene cg act3 familydinner 2 with fadeInOut
$ camera_reset()
"At least Eileen dating a girl isn't a problem, in and of itself. Eileen's father finally pipes up as their argument peters out, taking a swig of his wine to wash down his food."

show cg act3 familydinner 2 with midDissolve
andrew "Setting all that aside, it sounds like college in Utah is working out well for the both of them."

"Her father gives a brief chuckle, maybe sensing my tense mood. He seems down to earth and relaxed, especially compared to her mother."

"That said, I get a vague feeling of being a foreigner, and not just because I'm in a different city. As if there's a certain social etiquette that I'm not quite aware of, but everyone else is following naturally."

$ renpy.music.set_volume(1.0)
play music "music/relaxing.ogg" fadein 2.0
show cg act3 familydinner 7
$ renpy.transition(dissolve, layer='master')
elizabeth "Quite. So tell us about yourself, Allison."

$camera_move(-4000,1500,980,2,6,'ease')
"Attention now focused on me, I freeze up. I must have expected this would come up."

"Judging by their conversation, Eileen probably told them nothing about me. This feels like introductions on the first day of elementary school all over again."

allison "Um, let's see... I go to the same college as Eileen. I've lived in the same city my whole life, but I moved a little closer to campus before semester started, so I'm still getting used to that."

elizabeth "So you are an, ah, art student like Eileen?"

allison "Oh, no. I'm nowhere near her level. I'm actually on a science scholarship."

$camera_move(-1600,-1400,750,0,5,'ease')
pause 4.0
show cg act3 familydinner 3
$ renpy.transition(dissolve, layer='master')
elizabeth "Science, huh?"

"She sounds immediately interested, her eyebrows raised, but all I can offer is a evasive dodge. I don't know how to say that I'm not really excited about it, even if I apparently have some talent."

allison "We are in the art club together, though. We met through the mutual friend who made it."

elizabeth "I see."

show cg act3 familydinner 7
$ renpy.transition(dissolve, layer='master')
"Her previous curiosity suddenly hits a wall, her entire demeanor changing. Did I say something wrong? The abrupt change in tone completely breaks my train of thought, unsure whether to continue or clear things up."

$camera_move(3000,-750,780,-8,5,'ease')
"The other problem I have is the feeling of someone's eyes drilling into me. Eileen's mother notices as my eyes shift beside her, hand holding the little girl's back to reassure her."

show cg act3 familydinner 9
$ renpy.transition(dissolve, layer='master')
elizabeth "Come on dear, be polite."

"The effort doesn't seem to move her, the girl resisting as her suspicious face shrinks behind her daintily patterned children's plate."

eileen "Don't be silly."

eve "My name's Eve."

allison "Nice to meet you, Eve. That's a lovely name."

show cg act3 familydinner 4
$ renpy.transition(dissolve, layer='master')
"I keep smiling, but her pouting shows my charm offensive isn't working out. Once again Eileen comes to the rescue, speaking up as I try to think of another way to overcome her distrust."

eileen "Are you going to be like this all night?"

show cg act3 familydinner 9
$ renpy.transition(dissolve, layer='master')
"Eve just huffs and starts shoveling food into her mouth. The size of her spoon and the table before her makes the attempt at seriousness look more amusing than anything else."

scene cg act3 familydinner 9 with fadeInOut
$ camera_reset()
eileen "Don't mind her, she'll come around."

show cg act3 familydinner 1 with midDissolve
"She might say that, but I was hoping her cute little sister might be a little warm towards me. At least her mother has given up questioning me for now."

scene cg act3 familydinner 7
$ renpy.transition(dissolve, layer='master')
elizabeth "Oh, I almost forgot to tell you - The spare guest room's just been cleaned out a few days ago, so you can use that while you're here."

allison "Thank you very much. I'm really sorry to impose so much on you."

stop music fadeout 2.0
stop ambiance fadeout 2.0
scene cg act3 familydinner 3
$ renpy.transition(dissolve, layer='master')
elizabeth "You have charm going for you. Wouldn't you say, Eileen?"

"Eileen grimaces, her mother embarrassing her in that particular way only a parent knows how."

scene black with longDissolve
$ renpy.sound.set_volume(0.4, channel='ambiance')
play ambiance "sfx/ambiance/fire.ogg" fadein 2.0
play music "music/dozy_comfy.ogg" fadein 2.0
scene bg colorado house livingroom night HD
$camera_move(-4000,-2000,-400,0,0,'dissolve')
with longDissolve
"I can already feel my eyelids getting heavy as I lean back into the wonderfully soft couch, the exhaustion of the trip and meeting with Eileen's folks finally catching up to me as I rest in the living room."

$camera_move(-8700,-2000,-400,0,5,'ease')
"The fireplace happily crackles away near the Christmas tree, the cozy room all the warmer thanks to the heat of the shower still lingering on my skin."

"All that can be heard are the fire and the faint clanking of dishes as Eileen's parents wash up, recounting the day's events between them."

show eileen pjs_onhip closed open at leftedge:
    zoom 0.88 yoffset -300
    xzoom -1 xpos -0.5 alpha 0
    ease 1.0 xpos -0.45 alpha 1
"I very nearly succumb to my doziness before Eileen walks in, pulling back her still slightly wet hair."

scene black with dissolve
scene bg colorado house livingroom night blur:
    zoom 1.05
$camera_move(-2200,1850,480,0,0,'dissolve')
show eileen pjs_onhip closed open at centerleft:
    zoom 1.2 yoffset 180
    xzoom -1 xpos 0.3
with midDissolve
$camera_move(-2200,-850,480,0,8,'ease')
"The sight of her in pajamas wakes me up a little, though I quickly try to move my gaze elsewhere."

play sound "sfx/sack_drop.ogg"
show eileen pjs_onhip lookawaynarrow frown at centerleft:
    xzoom -1 yoffset 180 xpos 0.3
    nod2
with vpunch
"She practically collapses onto the couch beside me, staring up at the ceiling for a while to collect herself."

"I catch myself staring at her, but if she minds, she doesn't show it."

stop sound fadeout 1.0
scene black with dissolve
$ camera_reset()
scene bg colorado house livingroom night
show eileen pjs_crossed lookawaynarrow open at offcenterleft:
    xzoom -1 xpos 0.42
with midDissolve
voice "Eileen_Ugh1.ogg"
eileen "What a day."

show eileen pjs_crossed lookawaynarrow angry at offcenterleft:
    xzoom -1 xpos 0.42
$ renpy.transition(dissolve, layer='master')
voice "Allison_Sigh2.ogg"
allison "That goes for both of us."

"I almost mention the argument Eileen had with her mother, but I can't work out how I want to phrase it. Maybe it's for the best that Eileen preempts me."

show eileen pjs_onhip open normal at offcenterleft:
    xzoom -1 xpos 0.42
    linear 0.7 xzoom 1 xpos 0.47
eileen "So how was the trip, now that we can talk properly?"

show eileen pjs_onhip neutral normal at offcenterleft:
    xzoom 1 xpos 0.47
$ renpy.transition(dissolve, layer='master')
allison "The times we stopped were good."

show eileen pjs_crossed lookawaynarrow sadmouth at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "You're braver than I am; couldn't pay me enough to get on one of those things."
voice "Allison_SoftLaugh.ogg"
allison "Hah, come on. I'm sure you'd be a natural at it."

show eileen pjs_crossed disbelief open at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
eileen "No way. Your roommmate's crazy for using it as her only transportation."

show eileen neutral at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
allison "Your parents seem nice."

show eileen narrow at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
"Eileen just shrugs."

show eileen pjs_onhip lookawaynarrow open at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
eileen "I wish they were a little more subtle."

show eileen neutral at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
allison "About what?"

show eileen closed at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
eileen "Being so specific that you'll use the guest room, not mine."

"My cheeks flush scarlet as I connect the dots."

show eileen pjs_crossed normal open at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "Did you just realize what that was about?"

show eileen neutral at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
voice "Allison_Oh.ogg"
allison "No, but I--!"

show eileen pjs_onhip smile normal at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
"I'm still embarrassed to talk about it. Eileen finds amusement in how flustered I am."

scene black with eye_shut
"I bury my face in my hands."

eileen "Never change."

eileen "If I had lied and said we were just friends, I wonder if they would've been so adamant about the two of us not sharing a room."

scene bg colorado house livingroom night
show eileen pjs_onhip lookaway angry at offcenterleft:
    xpos 0.47
with eye_open
"I peek at her from behind my hands. I don't really know what to say. I don't know enough about her parents to say anything."

show eileen pjs_onhip frowning open at offcenterleft:
    xpos 0.47
$ renpy.transition(dissolve, layer='master')
eileen "Maybe that would have been better, huh?"

$ renpy.music.set_volume(0.5, delay=5.0)
$camera_move(-200,-400,350,0,5,'ease')
show eileen pjs_onhip smile at offcenterleft:
    subpixel True
    zoom 1.0 xpos 0.47
    ease 5.0 zoom 1.2 ypos 1.28 xpos 0.5
with None
show bg colorado house livingroom night blurred4
$ renpy.transition(verylongDissolve, layer='master')
"Her smile returns and she leans in toward me. I can feel my face go redder."

"My heart burning in my chest, all I can do is lean in to meet her."

show eileen pjs_onhip closed at offcenterleft:
    ease 2.5 zoom 1.2 ypos 1.28 xpos 0.5
"Eileen closes her eyes, our lips meeting for one brief moment."

$ renpy.music.set_volume(1.0, delay=5.0)
$camera_move(0,0,0,0,5,'ease')
show eileen pjs_onhip smile normal at offcenterleft:
    subpixel True
    zoom 1.2 ypos 1.28 xpos 0.5
    ease 5.0 zoom 1.0 ypos 1.0 xpos 0.47
with None
show bg colorado house livingroom night
$ renpy.transition(verylongDissolve, layer='master')
"As I pull back, the two of us look at each other and smile, partly from happiness, and partly from our sheepishness."

"It's going to be a while before this comes naturally, I guess."

stop music fadeout 3.0
$camera_move(0,0,0,0,0,'dissolve')
show eileen pjs_crossed neutral narrow at offcenterleft:
    zoom 1.0 xpos 0.47
$ renpy.transition(midDissolve, layer='master')
"As I watch her though, Eileen's face slowly collapses into frustration."

allison "What's wrong?"

show eve indoors normal annoyedopen at rightside:
    xpos 1.2
    ease 1.0 xpos 0.82
play music "music/eve_3_m.ogg" fadein 2.0
pause 1.0
eve "Everything's wrong!"

show eve indoors normal annoyed at rightside:
    xpos 0.82
show eileen pjs_crossed closed open at offcenterleft:
    xzoom 1 xpos 0.47
    linear 0.7 xzoom -1 xpos 0.42
"Eileen makes no secret of her displeasure as she sighs and takes to her feet, confronting the small and very unhappy girl before us. It stings to be so close, only to be interrupted."

show eileen pjs_crossed sad open at offcenterleft:
    xzoom -1 xpos 0.42
$ renpy.transition(dissolve, layer='master')
eileen "Eve..."

show eileen frown at offcenterleft:
    xzoom -1 xpos 0.42
$ renpy.transition(dissolve, layer='master')
"Eileen's sister takes little notice, directing her pouting towards the object of her annoyance: me."

show eve indoors half sadopen at rightside:
    xpos 0.82
    bounce
eve "She's my sister! I finally get to play with Eileen after so long and you keep hogging her!"

show eve indoors sad at rightside:
    xpos 0.82
show eileen pjs_onhip lookawaynarrow smile at offcenterleft:
    xzoom -1 xpos 0.42
$ renpy.transition(dissolve, layer='master')
eileen "Want to play, do you?"

show eileen pjs_onhip lookawaynarrow smile at offcenterleft:
    xpos 0.42
    ease 1.0 xpos 0.65
show eve indoors unsure at rightside:
    xpos 0.82
    time 0.7
    ease 1.0 yoffset -80
"Eileen flits behind Eve while she's busy ranting at me, bringing her arms around the child's midsection and lifting her up against her chest with ease."

show eileen pjs_onhip narrow smile at centerright
show eve indoors surprised normal at rightside:
    subpixel True
    xpos 0.82 yoffset -25 rotate 0
    ease 1.0 rotate -2
    ease 1.0 rotate 0
"As Eve finds her feet dangling a couple of inches from the carpet, she begins flailing about to grab a foothold."

show eve indoors surprised normal at rightside:
    xpos 0.82 rotate 0
    shaking2
eve "Let go of me!"

show eileen pjs_onhip closed at centerright
$ renpy.transition(dissolve, layer='master')
eileen "Wow, you haven't grown at all."

"That'll definitely help calm her down."

show eve indoors surprised normal at rightside:
    subpixel True
    xpos 0.82 yoffset -25 rotate 0
    ease 1.0 rotate -2
    ease 1.0 rotate 0
$ renpy.transition(hpunch, layer='master')
"To no surprise, the two start fighting, Eve's slight body jerking this way and that as Eileen plants her feet and refuses to let go despite her squirming around."

show eve indoors annoyed normal at rightside:
    xpos 0.82
    shaking2
eve "I'll tell mom on you!"

show eileen pjs_onhip narrow open at centerright
$ renpy.transition(dissolve, layer='master')
eileen "And what, she'll ground me?"

show eileen pjs_onhip narrow smile at centerright
show eve indoors surprised normal at rightside:
    subpixel True
    xpos 0.82 yoffset -25 rotate 0
    ease 1.0 rotate -2
    ease 1.0 rotate 0
"Eve fruitlessly continues to struggle, arms and legs flailing about in the air."

"For all her frustration and growling, her acting out just makes Eileen all the more amused as she teases her little sister."

stop music fadeout 4.0
stop ambiance fadeout 4.0
play sound "sfx/sack_drop.ogg"
show eve indoors half shy at rightside:
    xpos 0.82 yoffset -25 rotate 0
    ease 1.0 yoffset 55
show eileen pjs_crossed normal smile at centerright with dissolve
"Watching the two having their little sibling scuffle, it reminds me of my brothers at home. For the first time, my nerves about being here fade a little."

scene black with circlewipe
stop sound fadeout 1.0
$ renpy.sound.set_volume(1.2, channel='ambiance')
play ambiance "sfx/ambiance/tv.ogg" fadein 1.0
scene bg colorado house guestbedroom
$camera_move(-3200,850,600,0,0,'dissolve')
with circlewipe
$camera_move(1000,850,600,0,15,'ease')
$ renpy.music.set_volume(0.5)
play music "music/night_2.ogg" fadein 15.0
"Sitting on the side of the bed I'll be using for a week, I idly watch the news on the small television placed on a cabinet. The little speakers on the device try valiantly, but the voices are so tinny I can barely understand them."

"It's ten-thirty in the evening, going by the clock in the corner of the broadcast. Adulthood's weird; now that I can go to sleep whenever I want without my parents disapproving, I dutifully do so at a reasonable time anyway so I can be fresh for school."

"The fact I'm actually watching the news nowadays too is strange."

"Bored of the reports about trucks being stuck after sliding around on the roads, I let myself flop back onto the soft blankets as it drones on. Lacking the energy to do much else, I lazily stare upwards."

scene bg colorado house guestbedroom with fadeInOut
$ camera_reset()
show bg colorado house guestbedroom blurred4 as bg2:
    xalign 0.5 yalign 0.5 alpha 0
    ease 5.0 alpha 0.85
show shadow:
    alpha 0
    ease 5.0 alpha 0.35
"Yet another unfamiliar ceiling above me. It feels like everything is constantly changing these days."

"My old home sure didn't have a guest bedroom, let alone one that's so nicely furnished. Here I was thinking I'd be squeezing into Eileen's bed, not that I'd have minded that at all."

"For all the lovely things she has here, though, Eileen seems to be intentionally trying to distance herself from her parents. I don't understand it at all."

"She might have told me not to pry into her life, but it's hard to ignore what's right in front of my face."

play sound "sfx/door_open.ogg"
$ renpy.sound.set_volume(0.4, channel='ambiance')
scene bg colorado house guestbedroom with vpunch
stop music fadeout 10.0
"I quickly shuffle myself up at the sound of the opening door sliding across the carpet."

show eileen pjs_onhip lookaway sadmouth at rightedge:
    zoom 0.9 yoffset -50
    xpos 1.2
    ease 1.2 xpos 0.92
play sound "sfx/door_close.ogg"
"With a gentle touch, Eileen gingerly closes the door behind her. I'd thought everyone to be asleep by now, but maybe I should've expected her of all people to still be up."

show eileen pjs_onhip normal at rightedge:
    xpos 0.92
$ renpy.transition(dissolve, layer='master')
voice "Allison_Eileen3.ogg"
allison "Eileen?"

show eileen pjs_onhip at rightedge:
    xpos 0.92
    ease 2.0 xpos 0.5
"She puts a finger over her lips as she turns back, before walking up, climbing onto the bed, and facing me as I twist around. The two of us end up sitting in its center."

allison "Shouldn't you be sleeping?"

show eileen pjs_crossed disbelief open at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "Same goes for you."

show eileen lookaway neutral at center
$ renpy.transition(dissolve, layer='master')
"She has me there. Far from the quiet feeling awkward, I find myself smiling at our secret rendezvous."

allison "It feels like we're kids having a sleepover."

show eileen pjs_onhip lookawaynarrow angry at center
$ renpy.transition(dissolve, layer='master')
eileen "Too bad the movie's just news instead of some horror movie we snuck past our parents."

allison "You did that?"

show eileen pjs_onhip narrow open at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh4.ogg"
eileen "Once. My friends were so freaked out we went back to the usual horrible romance stuff."

show eileen pjs_crossed frown at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hm2.ogg"
allison "There's nothing wrong with romance movies..."

"Her face makes it abundantly clear this is a difference of opinion that'll never be bridged."

show eileen normal neutral at center
$ renpy.transition(dissolve, layer='master')
"I have to admit, there is one thing different to back then, too; Eileen's body is really hard to ignore when we're like this. As much as I try to distract myself from the subject, she did sneak into my bedroom at night."

show eileen frowning open at center
$ renpy.transition(dissolve, layer='master')
eileen "What's wrong?"

allison "Nothing, it's just... you're really pretty."

show eileen pjs_onhip smile sad blush at center
$ renpy.transition(dissolve, layer='master')
"It isn't often I catch her being bashful, but I think this might finally be one of those times."

$ renpy.music.set_volume(1.0)
play music "music/romance_2_m.ogg" fadein 4.0
scene bg colorado house guestbedroom blur
show eileen pjs_onhip smile sad blush at center:
    zoom 1.3 yoffset 300
    xpos 0.5
with vpunch
"My moment of victory is brief, though, with Eileen's quick movement towards me taking me all the more off guard."

play sound "sfx/sack_drop.ogg"
scene black with vpunch
"Unable to make sense of the girl suddenly lunging at me, the both of us are sent falling backwards into the soft mattress."

scene cg act3 pinned allisontalk
$camera_move(-3200,-1800,800,0,0,'dissolve')
with midDissolve
$camera_move(2200,1000,800,0,3,'ease')
"It takes a couple of seconds to collect myself and work out what's happened, time seeming to stop as I'm left staring upwards at the pair of emerald eyes above me."

"I'm pinned, I think. A brief attempt to right myself ends in little more than a couple of weak jerks, Eileen holding my arms to the thick sheets with her body weight."

"Silence reigns, my vision filled with her face looking downwards. I have no idea what to say as my heart beats wildly in my chest, yet she doesn't say a word."

allison "Eileen, what are you...?"

show cg act3 pinned eileentalk with dissolve
eileen "I missed you."

show cg act3 pinned allisontalk
$camera_move(0,0,0,0,10,'ease')
"How am I supposed to respond to that? Were her face any different, I'd think it an invitation, but there's a sincerity there that takes me off guard."

"I wonder how often I've seen her face, or anyone's, from this close, and for so long. I can't help but stare upwards, trying my best to read that face I so often can't."

"As I do, though, I realize something. She's doing just the same."

"Maybe she's scared of forcing me to do something I don't want to do, or afraid of getting too close too fast. Maybe she's simply like I am, unused to being looked at this intently. Either way, she isn't leering over me; Eileen's genuinely unsure what to do next."

"Whatever the reason, I can't help but smile a little."

show cg act3 pinned shocked with midDissolve
eileen "Did I say something wrong?"

allison "I was just thinking how you're still the same as ever."

show cg act3 pinned eileentalk with dissolve
eileen "What's that supposed to mean?"

"I answer her confusion by lifting my chin a little in invitation, not that I can move much more."

$camera_move(1500,1050,450,0,4,'ease')
pause 4.0
show cg act3 pinned kiss with midDissolve
"Without any further prompting needed, she presses her lips to mine with a satisfied sigh. It isn't long before our tongues move about, her breath tingling on my face."

"I squirm about roughly as the atmosphere gets heavier between us, Eileen easily keeping me down. It's a little exciting to be playing like this, and she shows no signs of letting up."

"A shiver runs up my spine as I find her thigh between my legs in my fidgeting about, my heart beginning to race with ideas of this and that."

"With lips affectionately breaking and meeting, Eileen barely letting me take so much as a breath, I can't help but think back to the first time we did this."

play sound "sfx/door-knock.ogg"
stop music fadeout 1.0
pause 0.5
show cg act3 pinned shocked with vpunch
"Then several sharp thuds against the door ring out."

"My entire body freezes, my heart nearly jumping out of my chest. The both of us freeze up as I break from our kissing to look over, hoping against hope that the door doesn't creak open."

$camera_move(0,0,0,0,15,'ease')
elizabeth "It's getting late, Allison."

"Why now, of all times? I can only thank my lucky stars that we've been quiet, but being one door handle turn from being seen like this is far too close for comfort."

allison "Ah, right. Sorry, I'll... go to bed soon."

"That was remarkably more natural than I thought I'd be able to pull off."

elizabeth "Thank you. If you need anything, just ask. Sleep well."

allison "Thanks. Good night."

"As her footsteps go down the hallway, the both of us heave a great sigh."

"The mood's completely gone as the both of us look to each other. I suppose this is one benefit of Eileen having her own apartment..."

scene bg colorado house guestbedroom
show eileen pjs_crossed lookawaynarrow angry at center:
    zoom 1.3 yoffset 300
    xpos 0.5
with fadeInOut
$ renpy.sound.set_volume(0.7, channel='ambiance')
play ambiance "sfx/ambiance/nightfall.ogg" fadein 1.0
"I run my hands through my hair to settle myself down as Eileen sits back on the bed, wisely letting a few minutes go by before trying to slip out of my room."

show eileen pjs_crossed lookawaynarrow open at center
$ renpy.transition(dissolve, layer='master')
eileen "I also missed living alone..."

show eileen pjs_onhip closed open at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble1.ogg"
eileen "Well that was annoying."

show eileen pjs_onhip neutral normal at center:
    xzoom 1 xpos 0.5
    linear 0.7 xzoom -1 xpos 0.44
eileen "See you tomorrow, I guess. Have a good sleep."

show eileen pjs_onhip neutral normal at center:
    xzoom -1 xpos 0.44
    ease 1.5 xpos 0.8
pause 1.0
play sound "sfx/door_open.ogg"
"With that, she slips off the bed, quietly shuffling across the room before pausing a moment before turning the handle. As I pick myself up to wish her a good night, she curtly turns back."

show eileen pjs_onhip lookaway smile at rightside:
    xzoom -1 xpos 0.8
$ renpy.transition(dissolve, layer='master')
voice "Eileen_AwkwardGiggle2.ogg"
eileen "...To be honest, I think you look really pretty too."

show eileen pjs_onhip closed smile at rightside:
    xzoom -1 xpos 0.8
    ease 1.5 xpos 1.25
pause 1.0
play sound "sfx/door_close.ogg"
stop ambiance fadeout 4.0
$ _dismiss_pause = False
"I don't manage to form a reply before she skitters out of the room. Then again, my scarlet cheeks probably did the job for me."

window hide dissolve
scene black with longDissolve
$ renpy.sound.set_volume(1.0, channel='ambiance')
return
