label scene_2S1_en:
######################
$ achievement.grant('story_act2')
stop music fadeout 2.0
stop ambiance fadeout 2.0
scene title act2 with menuFade
$ renpy.pause(5.0, hard=True)
$ _dismiss_pause = True

scene black with longDissolve
play sound "sfx/car_breakdown.ogg"
$ renpy.pause(8.5, hard=True)
play ambiance "sfx/ambiance/outside.ogg" fadein 3.0
window show dissolve
voice "Eileen_Ugh2.ogg"
eileen "Alright, everyone out."

$ renpy.music.set_volume(1.5, channel='ambiance2')
window hide dissolve
play ambiance2 "sfx/ambiance/crowd_silent.ogg" fadein 1.5
play sound "sfx/car-door-exit.ogg"
scene bg downtown city
$camera_move(1500,-400,680,0,0,'dissolve')
show snow light
show misc letterbox1 as lb1:
    zoom 2.0 xcenter 0.5 ycenter 0.11
show misc letterbox2 as lb2:
    zoom 2.0 xcenter 0.5 ycenter 0.81
with midDissolve
$camera_move(-1000,-400,680,0,15,'ease')
letterbox "Caprice and I step out onto the busy sidewalk per Eileen's orders, the chatty girl leaning through the passenger door as Eileen tries to get the car going again. Giving a long stretch to help my stiff back, I do my best to keep out of the way."

stop sound fadeout 1.0
letterbox "After news of Eileen's owning a car leaked out, Caprice's mind immediately set about organizing the art club's first outing. 'Inspiration for our art' she called it, but it was obviously an excuse to hang out."

letterbox "With things having gone this awry, I feel a little bad for going along with the idea despite Eileen's reluctance."

play music "music/dozy_comfy.ogg" fadein 1.0
scene bg downtown city
show snow light
show caprice outdoors_handonhip grumble normal even at right2:
    xpos 0.8 yoffset 100
    ease 2.0 yoffset 0
    bounce
show eileen outdoors_crossed annoyed angry at left2:
    xzoom -1 xpos -0.1 alpha 0
    time 0.5
    ease 2.0 xpos 0.2 alpha 1
with fadeInOut
$ camera_reset()
play sound "sfx/car-door-slam.ogg"
window show dissolve

"Their investigations apparently coming to nothing, Caprice rights herself as the car falls silent. Eileen closes the door behind her with some force before plodding around to us, frustration written all over her face."

show eileen outdoors_crossed narrow angry at left2:
    xzoom -1 xpos 0.2 alpha 1
$ renpy.transition(dissolve, layer='master')
eileen "Looks like the engine won't idle at all. Serves me right for buying second-hand."

stop sound fadeout 1.0
show caprice outdoors_handonhip neutral normal sad at right2:
    xpos 0.8 yoffset 0
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hm2.ogg"
allison "Know why it's not working?"

show eileen outdoors_crossed frowning frown at left2:
    xpos 0.2 alpha 1
$ renpy.transition(dissolve, layer='master')
voice "Eileen_No1.ogg"
eileen "No idea."

show caprice outdoors_behindback pout normal raised at right2:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
"She looks a little sheepish for not having the answer on hand, but I can't say I blame her."

show caprice outdoors_chintap raised closedsad grin at right2:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
"As the two of us mull over our options, we become distracted by Caprice and her wide grin. She has a plan cooked up already, for better or worse."

show eileen outdoors_onhip lookaway open at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Caprice1.ogg"
eileen "What are you smiling about now?"

show eileen neutral at left2:
    xpos 0.2
show caprice outdoors_wave raised wink opensmile at right2:
    xpos 0.8
    nod
    linear 0.7 xzoom -1 xpos 0.775
caprice "I've got this! Just stay right here, I gotta make a call!"

show eileen outdoors_onhip narrow frown at left2:
    xpos 0.2
show caprice outdoors_wave raised wink opensmile at right2:
    xzoom -1 xpos 0.775
    ease 1.0 xpos 1.2
voice "Caprice_CatchYaLater1.ogg"
"Eileen and I grimace at each other in unison, but Caprice bounces off down the street before either of us can object. Getting the phone from her pocket as she walks, she flits between the people around her while unbothered by the ice on the sidewalk."

"The background hum of people chatting and cars passing by takes over once again as we find ourselves at loose ends."

hide caprice
show eileen outdoors_onhip neutral normal at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "Not like we could go anywhere else, anyway..."

allison "You're not going to try and stop her?"

show eileen outdoors_crossed narrow open at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble3.ogg"
eileen "Think she'd listen to me if I tried?"

show eileen neutral at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
"That's a fair point. Both of them are rather stubborn, so I suppose it's inevitable they'd clash sometimes."

scene bg downtown city
show snow light
$camera_move(4050,-1500,750,0,0,'dissolve')
with fadeInOut
$camera_move(1050,-1500,750,0,15,'ease')
"On the bright side, of all the places to break down, here isn't so bad. The weather's not too chilly, and it's nice to observe people sometimes. Especially when they're bundled up in cute winter outfits."

"Some city workers in the distance are already beginning to set up the downtown Christmas tree, providing some entertainment for the people walking by as they struggle with the unwieldy thing."

"Things will change as last-minute Christmas shoppers and sale hunters start rushing around, but right now, it's a pleasant atmosphere."

scene bg downtown city:
    subpixel True
    xalign 1.0
    time 1
    ease 3.0 xalign 0.0
show snow light
show eileen outdoors_crossed normal neutral at left2:
    subpixel True
    xzoom -1 xpos 0.1
    time 1
    ease 3.0 xpos 0.2
with fadeInOut
$ camera_reset()
"Turning back to Eileen, she doesn't seem as content to patiently pass the time people-watching as I am."

show bg downtown city:
    xalign 0.0
show eileen outdoors_onhip open at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
eileen "I'm going to go grab a coffee. Want one?"

show eileen neutral at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
allison "I'm fine. Probably having a bit too much of it lately."

show eileen outdoors_crossed lookawaynarrow open at left2:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
eileen "There's no such thing as too much."

show eileen outdoors_crossed closed neutral at left2:
    xzoom -1 xpos 0.2 alpha 1
    linear 0.7 xzoom 1 xpos 0.27
    pause 0.2
    ease 1.5 xpos -0.1 alpha 0
"As I shake my head at her offer, Eileen simply shrugs and begins strolling down the road in the opposite direction to Caprice. Rather than dance around the crowd, people make way for Eileen as she moves, her gaze fixed and noticeably taller than most."

stop music fadeout 2.0
"With little to do now but watch the car, I huff into my gloved hands a couple of times to try and warm them. At least the aquarium should be warmer, if we ever manage to finish the trip there."

$ renpy.music.set_volume(0.5)
hide eileen
play music "music/ringtone.ogg" fadein 1.0
play loopsfx "sfx/cell_phone_vibrate.ogg"
window show
"Just as I'm about to settle in and watch the passing crowds, the phone in my pocket begins to vibrate and ring."
show bg downtown city blurred3:
$ renpy.transition(dissolve, layer='master')
$ phone.show('call-in')
"Not sure who it could be, I quickly grab for it."

allison "Dad..."

stop music fadeout 1.0
stop loopsfx
play sound "sfx/phone-pickup.ogg"
"Without a second thought, I swipe my finger on the screen to pick up the call."

$ renpy.music.set_volume(1.0)
voice "Allison_NervousHi1.ogg"
allison "Dad! Hi."

stop sound fadeout 1.0
stop ambiance2 fadeout 12.5
play music "music/relaxing.ogg" fadein 5.5
dad "Hey, sweetie. It's good to hear your voice again. How are things?"

"The sound of the crowds fades away as I listen to him, a comfortable warmth coming over me as I feel insulated from their gazes and focused on the conversation."

allison "Things are good, I guess."

dad "Haven't caught you at a bad time, have I? I could call back later."

allison "No, no. Just out with friends."

"He gives his usual weird laugh, sounding more like air moving through closed teeth than a normal full-bellied chuckle. It never fails to make me smile all the same, though."
voice "Allison_SoftLaugh.ogg"
allison "What's that about?"

dad "Just a relief to hear that. We've all been worried about you finding new friends after such a big change. What with changing schools and moving out."

"Thinking to the people I've met in school, I guess I really have. Caprice pulled me into her orbit, Wallace seems nice and caring for all his intimidating size, and then there's Eileen. They might be a bit odd, but they're all caring in their own ways."

"It's funny how art seems to have drawn us all together, each in a different way. Before I respond, I vaguely hear my mother's voice in the background."

dad "Your mother said to ask if things are going okay at home."

allison "Everything's good. Rose has been a big help with everything."

"That's vastly understating things; if it weren't for her, I don't know how I would have coped. Not just for the constant housework and errands, but also for being away from everyone and everything I knew before."

"I might still have my ups and downs, but the last thing I want to do is stress them out over me."

dad "That's good to hear, hopefully it'll take a bit of stress off a certain someone. Tell Rose hello for us if you remember."
voice "Allison_SureThing.ogg"
allison "Can do. How's everyone there?"

dad "Your brothers are a pain in the ass like always, for one."

"Right on cue, one of them loudly complains in the background."

dad "As you can tell."

allison "How's Lucy?"

dad "Same as always. She's sleeping in the other room."

"I hear my mother's voice again in the background."

dad "Ah, right. She knocked a mug off the counter the other day. Your mom gave her a good scolding. I think she's acting out without you around."

"I can't help but laugh imagining it, my mom exasperated with my cat."

dad "Anyway, we're getting by. It ain't the same without you, though."

"In a whispered voice, he continues."

dad "It's hard to get a moment's peace around here. Make sure to give your mother a call sometime, okay?"

allison "I'll call her, don't worry."

dad "'Atta girl. Anything worrying you? On your mind?"

allison "No, things are good."

"I realize my mistake the moment I answer, having spoken just a little too quickly to make it seem natural. My mind starts to replay embarrassing situations I've been in, the constant concerns and worries of living alone, the loneliness..."

"Dad's calming voice cuts through, interrupting my spiraling thoughts."

dad "I'd better let you get back to your friends. I hope I'm not keeping you away."

allison "It's fine. I'm just happy to hear you again."

stop music fadeout 8.5
dad "We miss you too. Christmas around here will be a lot warmer once you're back for the holidays. We're going to miss you at Nana's this year."

allison "I really can't wait to see all of you again."

dad "I'll be looking forward to it, too. I love you, Allison."
voice "Allison_TakeCare2.ogg"
allison "I love you, too. Bye."

play sound "sfx/phone-hangup.ogg"
"A few seconds pass, before the familiar beeping of the ended call tone rings in my ear. I just couldn't bring myself to do it."

$ renpy.music.set_volume(1.0, channel='ambiance2')
$ phone.hide()
window hide
show shadow:
    alpha 0
    ease 4.0 alpha 0.4
stop sound fadeout 1.0
"Putting away the phone, I feel like I should be happy to have spoken to my family again. That couldn't be any further from what I feel, though. The horrible lump in my throat only gets worse as I stare down glumly at the dirty snow on the sidewalk."

"My heart hurts. The taste of my mother's food, my old bedroom, all the friends I left behind when I went to this college, my cat, they all come flooding back."

"It's just homesickness. I've dealt with this before, and more than once. The fact it'll pass doesn't help right now, though."

show bg downtown city
hide shadow
$ renpy.transition(dissolve, layer='master')
voice "Allison_Sigh1.ogg"
"Noticing Eileen through the crowd, coffee cup in hand as she sips away, I take a long breath and try to steady myself. I don't want to look weird in front of her, getting all sulky in the middle of the street."

show eileen outdoors_onhip normal neutral at offcenterleft:
    xzoom -1 zoom 1.05 yoffset 50
    xpos 0.2 alpha 0
    ease 1.5 xpos 0.45 alpha 1
allison "That was quick."

play sound "sfx/car-arriving.ogg"
show eileen outdoors_crossed disbelief open at offcenterleft:
    xpos 0.45 alpha 1
$ renpy.transition(dissolve, layer='master')
eileen "Hey. The cavalry's here, too."

show eileen outdoors_crossed closed neutral at offcenterleft:
    xpos 0.45 alpha 1
    ease 0.5 xpos 0.44
    ease 0.5 xpos 0.45
"She jerks her head towards the top of the street in answer to my confusion."
$camera_move(-3050,-1500,750,0,5,'ease')
play music "music/millie_2.ogg" fadein 5.0
pause 2.0

scene bg downtown city HD
show snow light:
    zoom 1.5 xcenter 0.05 ycenter 0.12
$camera_move(-7500,-3000,-250,0,0,'dissolve')
show caprice outdoors_wave even closedhappy neutral at leftedge:
    xzoom -1
    zoom 0.62 yoffset -580
    xpos -0.3
    time 2
    easein .15 yoffset -598
    easeout .175 yoffset -580
    easein .15 yoffset -588
    easeout .175 yoffset -580
with fadeInOut
"Caprice frantically waves to flag someone down, their little car sliding into a parking spot not far from where Eileen's ended up. It looks well-cared for, despite its age."

play sound "sfx/car-door-slam.ogg"
show millie outdoors_neutral even closedhappy neutral at leftside:
    zoom 0.62 yoffset -580
    xpos -0.005 alpha 0
    ease 1.4 xpos -0.07 alpha 1
$ renpy.transition(dissolve, layer='master')
"All Eileen and I can do is stare as the driver opens the door and steps out. I'm more than a little surprised when I recognize her as being another student from college."

scene bg downtown city blurred3:
    zoom 1.05
show snow light
$camera_move(2200,1200,400,0,0,'dissolve')
show millie outdoors_neutral even normal neutral at right2:
    zoom 1.1 yoffset 85
    xpos 0.775
$ renpy.transition(dissolve, layer='master')
$camera_move(2200,-950,400,0,10,'ease')
"She looks to be about our age despite her ladylike appearance, her tall figure dressed in a smart trench coat and scarf."

"It's quite a fashionable look, and hardly who I expected to arrive."

scene bg downtown city
show snow light
show eileen outdoors_crossed disbelief angry at leftside:
    xzoom -1 xpos 0.15
show caprice outdoors_handonhip even closedhappy neutral at right2:
    xpos 0.82
show millie outdoors_neutral even normal neutral at offcenterright:
    xpos 0.54
with fadeInOut
$ camera_reset()
"As Caprice excitedly chats to her, I feel myself shrinking behind Eileen a little out of shyness. She looks much more apathetic about the whole affair, simply taking a long sip of her coffee. Getting on Eileen's good side made me forget how unsociable she could be."

show millie at offcenterright:
    xpos 0.54
show caprice outdoors_wave even normal open at right2:
    xpos 0.82
    bounce
caprice "Ta-da! Found a mechanic right nearby!"

show caprice outdoors_handonhip neutral at right2:
    xpos 0.82
$ renpy.transition(dissolve, layer='master')
"I feel a little sheepish for assuming the worst of her little mission. Caprice seems to be very friendly with the woman, but it's hard to read much into that given Caprice's personality."

show millie outdoors_neutral even closedhappy neutral at offcenterright:
    xpos 0.54
    nod
millie "Hi, I'm Millie. The two of us are roommates."

show eileen normal at leftside
show millie outdoors_neutral speaking at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
millie "'Mechanic'... might be stretching things a bit far, but I should be able to help."

show caprice outdoors_wave wink opensmile at right2:
    xpos 0.82
show millie neutral at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
caprice "And now Millie, it's time for you to meet... my art club! Introducing Eileen and Allison!"

show caprice neutral at right2:
    xpos 0.82
show eileen outdoors_crossed narrow frown at leftside
$ renpy.transition(dissolve, layer='master')
"All I can do is give a weak smile as Eileen snorts in weary disapproval. Like it or not, looks like we're a part of this misadventure for good."

show millie outdoors_tented raised half mouthopen at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
millie "I could have sworn there was already an art club?"

$camera_move(2950,-480,500,0,4,'ease')
show millie neutral at offcenterright:
    xpos 0.54
show caprice outdoors_chintap raised half grin at right2:
    xpos 0.82 yoffset 55 rotate 0
    time 1
    ease 1.0 rotate -5
    ease 1.0 rotate 0
caprice "Pfft. That one is garbage. Mine is the cool art club."

show millie closedhappy smile at offcenterright:
    xzoom 1 xpos 0.54
    linear 0.7 xzoom -1 xpos 0.5
millie "So that's what you've been so happy about lately."

show caprice outdoors_handonhip even normal neutral at right2:
    xpos 0.82
show millie sad closedhappy pout at center:
    xzoom -1 xpos 0.5
$ renpy.transition(dissolve, layer='master')
millie "Shame on me for thinking you were ever jealous of my position in the writing club."

show eileen outdoors_crossed normal neutral at leftside
$ renpy.transition(dissolve, layer='master')
"Is that what all of this is about? Caprice wanted to be on level with her friend? I guess it worked out well for us, anyway."

$camera_move(0,0,0,0,4,'ease')
allison "So you're in charge of the writing club?"

show millie outdoors_neutral even neutral normal at offcenterright:
    xzoom -1 xpos 0.5
    linear 0.7 xzoom 1 xpos 0.54
millie "The current leader's graduating at the end of this semester, so he's handing the reigns to me. Seems I made a good impression on him."

show millie normal at offcenterright:
    xzoom 1 xpos 0.54
show eileen outdoors_onhip disbelief open at leftside
$ renpy.transition(dissolve, layer='master')
eileen "And the rest of the club doesn't get a say?"

show eileen neutral at leftside
show caprice outdoors_behindback even closedhappy neutral at right2:
    xpos 0.82
show millie outdoors_tented raised half smile at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
millie "That's how it works. I like to call it a 'stable line of succession'."

show millie even closedsad speaking at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
millie "Speaking of which, I need to get back to the writing I was doing before I got that phone call. Your car had issues?"

show eileen outdoors_crossed closed open at leftside
show millie outdoors_neutral even normal neutral at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
eileen "Yeah. Engine died without any warning, managed to coast it to the side of the road."

show eileen neutral at leftside
$ renpy.transition(dissolve, layer='master')
"Eileen doesn't seem exactly taken with the situation, Millie's explanation of her being a writer not explaining her ability to fix a car. We don't have much option but to put our faith in her, at this point."

show eileen outdoors_onhip lookaway open at leftside
$ renpy.transition(dissolve, layer='master')
eileen "I'm guessing Caprice gave you the briefing. Need me around to start the thing?"

show eileen neutral at leftside
show caprice outdoors_pumped raised normal opensmile at right2:
    xpos 0.82 yoffset 55
    easein .15 yoffset 38
    easeout .175 yoffset 55
    easein .15 yoffset 48
    easeout .175 yoffset 55
voice "Caprice_AH.ogg"
caprice "Oh! Oh! Let me!"

show eileen lookawaynarrow frown at leftside
show caprice outdoors_handonhip even frown at right2:
    xpos 0.82
show millie closedhappy at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
"Eileen narrows her eyes, but eventually sighs and chucks her keys at the girl. Caprice's momentary hesitation shows she expected that to work no more than I did."

show caprice outdoors_behindback raised at right2:
    xpos 0.82
show eileen outdoors_crossed narrow open at leftside
$ renpy.transition(dissolve, layer='master')
voice "Eileen_OkayFine3.ogg"
eileen "Just don't go for a drive or something. I assure you, you haven't seen me actually angry yet."

show eileen frown at leftside
show caprice even half pout at right2:
    xpos 0.82
show millie normal at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
"The seriousness of her tone seems to penetrate a little. Of course, Caprice being Caprice, it doesn't take long for her to bounce back."

$camera_move(2950,-480,500,0,4,'ease')
show caprice outdoors_pumped even closedhappy open at right2:
    xpos 0.82 yoffset 55
    easein .15 yoffset 38
    easeout .175 yoffset 55
    easein .15 yoffset 48
    easeout .175 yoffset 55
caprice "Now then, let's fix this thing!"

show millie outdoors_tented raised closedhappy smile at offcenterright:
    xzoom 1 xpos 0.54
    linear 0.7 xzoom -1 xpos 0.5
voice "Millie_LetsSeeWhatICanDo.ogg"
millie "Right, let's have a look."

play sound "sfx/car-hood-open.ogg"
$camera_move(2950,-480,500,0,0,'dissolve')
show eileen outdoors_onhip normal open at leftside:
    xpos 0.175
show caprice outdoors_handonhip even normal neutral at rightedge:
    zoom 0.65 yoffset -300
    xpos 0.8
show millie outdoors_neutral even normal speaking at centerright:
    zoom 0.65 yoffset -300
    xzoom -1 xpos 0.6
$ renpy.transition(dissolve, layer='master')
"She gives us a confident smile before popping the hood, Caprice taking on the job of her assistant. To Millie's credit, she looks like a natural as she quickly moves this and that around about to peer inside."

$camera_move(-250,-450,250,0,4,'ease')
eileen "If you don't need us, we'll just go for a short walk, alright?"

show eileen neutral at leftside:
    xpos 0.175
show caprice outdoors_wave angry closedhappy grin at rightedge:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
voice "Caprice_Yeah4.ogg"
caprice "Got it!"

stop sound fadeout 1.0
stop music fadeout 3.0
scene black with midDissolve
$ camera_reset()
"The meaning of 'we' becomes clear as Eileen puts a hand around my shoulder to direct me, the two of us walking off beside each other and leaving the two to their work."

play loopsfx "sfx/ambiance/snowwalk.ogg" fadein 0.5
scene bg downtown park:
    subpixel True
    xalign 0.0
    parallel:
        ease 1.0 yoffset -1
        ease 1.0 yoffset 1
        repeat 10
    parallel:
        ease 20 xalign 1.0
show snow light
show eileen outdoors_onhip normal neutral at offcenterleft:
    subpixel True
    xzoom -1 xpos 0.4
    ease 1.0 yoffset 1
    ease 1.0 yoffset -1
    repeat 10
with midDissolve
$ renpy.music.set_volume(0.6, delay=0.0)
play music "music/painter.ogg" fadein 2.5
"It feels a little weird to have Eileen's arm around my back and holding my shoulder as we walk side by side. Even if it is to guide me, she takes a long while to let go."
voice "Allison_Um1.ogg"
allison "You sure you're alright leaving them alone?"

show eileen outdoors_crossed frowning angry at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "Not at all. Not like I can do anything to actually help, though."

"All I can do is awkwardly laugh it off. I don't have the first clue on even day to day maintenance for a car after all, so maybe just staying out of the supposed mechanic's way might be for the best."

show shadow:
    alpha 0
    ease 2.0 alpha 0.5
show eileen closed at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
"At least it broke the ice a bit, as I still feel a little unsure when I'm alone with her."

"I can never seem to get a read on Eileen. Every time we talk, I end up getting caught in her pace. Even now, I'm not sure why she pulled me away to walk with her."

"No, that's not quite true; she must have noticed me being depressed earlier, even if she isn't saying anything about it. Given how she also invited me over for dinner when I was hungry, it seems she really does care for me despite her stoic exterior."

stop loopsfx
show bg downtown park:
    xalign 1.0
show eileen outdoors_onhip normal neutral at offcenterleft:
    yoffset 0 xpos 0.4
$ renpy.transition(dissolve, layer='master')
"As she drops her emptied coffee cup into a bin as we pass, I realize it's going to be up to me to raise the subject."

show shadow:
    alpha 0.5
    ease 2.0 alpha 0
voice "Allison_Sigh2.ogg"
allison "So you saw me earlier, huh?"

show eileen outdoors_crossed lookaway open at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm2.ogg"
eileen "You did look a bit bummed when you got off the phone. Didn't want to bring it up if you didn't, though."

show eileen neutral at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
"She left me no choice..."
voice "Allison_Sorry2.ogg"
allison "I missed talking to my family after so long. Sorry for being so flustered."

show eileen frowning neutral at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "Nothing to be sorry for, it's only natural."

show eileen outdoors_onhip normal neutral at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "So you're homesick, huh?"

allison "Sometimes."

show eileen outdoors_onhip closed open at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "Moving out for the first time's a big deal. You don't need to beat yourself up over feeling stressed."

show eileen normal neutral at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
voice "Allison_ThankYou.ogg"
allison "Thanks. I thought I was doing okay, but when I heard my dad's voice again..."

show eileen lookaway frown at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "It reminded you of what you're away from."

"I give a simple nod. She doesn't seem to be speaking in an overly soft or caring tone, but she is listening carefully. I appreciate it, really. She doesn't come off as patronizing."

allison "I can't imagine living alone. I have no idea how you do it."

show eileen outdoors_crossed closed angry at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
"She gives an absentminded shrug."

show eileen outdoors_crossed disbelief at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "I'm not really fussed about that sort of thing. Besides, Wallace drops by sometimes, and you're welcome as well."

show eileen normal neutral at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "It's good that you have a roommate you get along with, though. That'd help."

"I get the feeling Eileen's circling around what she actually wants to say. As she looks to me, I think she realizes that the game is up, the two of us stopping as she turns in front of me."

show eileen outdoors_onhip normal open at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Allison2.ogg"
eileen "We're all freshmen, here. You, me, Caprice, we're all away from our families and trying to find our niche. If you want to talk or vent, we're around. Wallace told me you talked, so you have that big oaf as well."

show eileen lookaway neutral at offcenterleft:
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
eileen "That's it, I guess."

"I might have thought I didn't want to worry her, but her reassurances are more comforting than I'd guessed they'd be. Even as I manage to gather myself, I can't help but smile."

allison "I know it's a little bit selfish, but... it's sort of nice to have someone worried over me."

show bg downtown park blurred3 as bg2 behind eileen:
    xalign 1.0 yalign 0.5 alpha 0.9
show eileen narrow smile at offcenterleft:
    zoom 1.3 yoffset 300
    xpos 0.45
    ease 0.5 yoffset 305
    ease 0.5 yoffset 295
    ease 0.5 yoffset 300
with dissolve
"To my surprise, she brings her hand to my head and starts ruffling my hair. It's hard to read her expression as she does so, but I don't feel put off at all. Quite the opposite."

show eileen lookaway neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"She pauses for a moment, face stuck."

show eileen outdoors_fists frowning open at offcenterleft
$ renpy.transition(dissolve, layer='master')
eileen "Sorry, if you don't..."

allison "It's fine."

show eileen outdoors_onhip closed smile at offcenterleft
$ renpy.transition(dissolve, layer='master')
"I only just manage to splutter the words out, my dumb smile better at getting the message across."

show eileen closed smile at offcenterleft:
    xpos 0.45 yoffset 300
    ease 0.5 yoffset 305
    ease 0.5 yoffset 295
    ease 0.5 yoffset 300
"Taking the cue, she begins petting my head once more. I forgot how much I missed simple physical interaction, as awkward as she might be about it."

"A hug might be a bit more normal, but somehow it's hard to imagine Eileen doing that."

hide bg2
show eileen outdoors_crossed lookawaynarrow angry at offcenterleft:
    zoom 1.0 yoffset 0
    xpos 0.4
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble2.ogg"
eileen "It's not a secret I'm not great at this kind of thing. Just keep what I said in mind, alright?"

show eileen normal at offcenterleft:
    xzoom -1 xpos 0.4
    linear 0.7 xzoom 1 xpos 0.45
allison "I will. Everyone's here to help me. I'll remember that."

show bg:
    subpixel True
    xalign 1.0
    parallel:
        ease 1.0 yoffset -1
        ease 1.0 yoffset 1
        repeat 10
    parallel:
        ease 20 xalign 0.0
show eileen outdoors_onhip closed neutral at offcenterleft:
    subpixel True
    xzoom 1 xpos 0.45
    ease 1.0 yoffset 1
    ease 1.0 yoffset -1
    repeat 10
play loopsfx "sfx/ambiance/snowwalk.ogg"
"Removing her hand, Eileen and I start heading back towards the car side by side. It's easy for someone who's outgoing to comfort another, but it feels somehow more sincere from a loner like Eileen. She's making an extra effort for my sake."

"Somehow, I feel a little warmer than I did before as we walk back. Maybe the weather's improved, but I doubt that's it."
voice "Allison_Hm2.ogg"
allison "I guess you've had experience living alone, haven't you?"

show eileen normal open at offcenterleft
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh1.ogg"
eileen "Me? Just moved out for college, same as you."

show eileen neutral at offcenterleft
$ renpy.transition(dissolve, layer='master')
"So we're in just the same situation, yet Eileen has everything so together that she can offer me help like this. Moreover, she's known so this entire time. I just sigh in defeat."

stop music fadeout 5.0
scene bg downtown park blur:
    xalign 0.0
show snow light
show eileen outdoors_onhip normal neutral at center:
    zoom 1.35 yoffset 300
    xpos 0.48
$ renpy.transition(midDissolve, layer='master')
allison "College has really driven home how everyone's different."

show eileen outdoors_crossed lookawaynarrow open at center:
    xpos 0.48
$ renpy.transition(midDissolve, layer='master')
eileen "Sure has."

stop loopsfx
scene black with midDissolve
"The reason for the dreariness in her voice becomes apparent as I follow her gaze, Caprice happily bouncing out of the car and shutting the door as we stroll up. Everyone sure is different."

$ renpy.music.set_volume(1.0, delay=0.0)
play music "music/caprice_default_m.ogg" fadein 3.0
scene bg downtown city
show snow light
show eileen outdoors_crossed narrow frown at leftside:
    xzoom -1 xpos 0.14
show caprice outdoors_wave raised closedhappy grin at rightedge:
    xpos 0.84
    time 1
    bounce
with midDissolve
voice "Caprice_HEY.ogg"
caprice "Hey, guys!"

play sound "sfx/car-hood-close.ogg"
show eileen normal neutral at leftside:
    xzoom -1 xpos 0.14
show millie outdoors_neutral even normal speaking at offcenterright:
    xpos 0.54 yoffset 100
    ease 1.0 yoffset 0
show caprice outdoors_behindback even normal neutral at rightedge:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"The impromptu mechanic appears finished as well, righting herself and closing the hood after poking around inside."

show millie raised frown oilneutral at offcenterright:
    xpos 0.54 yoffset 0
    nod2
$ renpy.transition(dissolve, layer='master')
"She absentmindedly wipes the sweat off her forehead, leaving some grease on her face before realizing her error."

stop sound fadeout 1.0
$camera_move(-2500,-480,500,0,4,'ease')
show millie closedhappy smile at offcenterright:
    xpos 0.54
millie "Whoops. Well, it's fixed for now."

show millie outdoors_tented even normal speaking oiltent at offcenterright:
    xpos 0.54
show caprice grin at rightedge:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
millie "Looks like the fuse went, nothing major. I've done what I can out here, but it needs a proper fix back at a shop. This'll get you going, though."

show eileen disbelief open at leftside:
    xpos 0.14
show millie neutral at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
"Eileen's impressed look is shared by me. Being so handy is a good trait to have, and she did come all the way here just to help us."

show eileen outdoors_onhip at leftside:
    xpos 0.14
$ renpy.transition(dissolve, layer='master')
eileen "I'm impressed. Fixed cars before?"

show eileen normal neutral at leftside:
    xpos 0.14
show millie closedhappy at offcenterright:
    xpos 0.54
$ renpy.transition(dissolve, layer='master')
voice "Millie_SmallLaugh.ogg"
millie "I was about to recommend taking it to my dad's auto shop, actually."

show eileen closed at leftside:
    xpos 0.14
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Sure1.ogg"
eileen "Your dad's shop is as good as any other. I'll sort something out this afternoon."

show eileen outdoors_fists frowning smile at leftside:
    xpos 0.14
$ renpy.transition(dissolve, layer='master')
eileen "This is where I'd shake your hand in thanks but, you know..."

show millie outdoors_neutral sad half neutral oilneutral at offcenterright:
    xpos 0.54
show caprice outdoors_handonhip angry normal neutral at rightedge:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
"Millie gives a self-deprecating smile in response."

$camera_move(2950,-480,500,0,4,'ease')
show caprice outdoors_handonhip at rightedge:
    xpos 0.84
    time 2
    ease 0.8 xpos 0.8
    ease 0.8 xpos 0.84
show millie outdoors_neutral even closedhappy neutral oilneutral at offcenterright:
    xzoom 1 xpos 0.54
    linear 0.7 xzoom -1 xpos 0.5
    time 2.5
    nod2
"Caprice passes her a handkerchief from her pocket, which Millie quickly uses to wipe her hands as best she can."

show millie outdoors_neutral oilnone at offcenterright:
    xzoom -1 xpos 0.5
    nod2
show eileen outdoors_crossed normal neutral at leftside:
    xpos 0.14
show caprice outdoors_chintap raised normal open at rightedge:
    xpos 0.84
$ renpy.transition(dissolve, layer='master')
caprice "Hey, since you're already here-"

show millie outdoors_tented even half speaking at center:
    xzoom -1 xpos 0.5
$ renpy.transition(dissolve, layer='master')
millie "I'll let you all get on with your art club adventure. I have other things I need to do, sorry."

$camera_move(0,0,0,0,4,'ease')
show eileen closed at leftside:
    xpos 0.14
show millie raised closedhappy mouthopen at center:
    xpos 0.5
    nod
show caprice outdoors_handonhip sad grumble at rightedge:
    xpos 0.84
millie "Have fun."

stop music fadeout 8.0
show millie smile behind caprice at center:
    xpos 0.5
    ease 1.5 xpos 1.2
"With that, we give our farewells to Millie as she heads back towards her car. Her momentary churlish grin towards the deflated Caprice doesn't go unnoticed."

$ achievement.grant('story_millie')
show eileen outdoors_crossed normal neutral at leftside:
    xzoom -1 xpos 0.14
    ease 1.0 xpos 0.2
show caprice outdoors_handonhip closedsad at rightedge:
    xpos 0.84
    ease 1.0 xpos 0.8
"Eileen snatches her keys back from the girl's hand, wasting no time in addressing the both of us."

show eileen lookawaynarrow angry at leftside:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
eileen "Now, are we finally going to the aquarium?"

show caprice outdoors_pumped raised normal opensmile at rightedge:
    xpos 0.8
    bounce
voice "Caprice_Yeah3.ogg"
caprice "Yeah!"

show caprice raised closedhappy opensmile at rightedge:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
"She beams brightly, her smile proving infectious."

show eileen outdoors_onhip normal neutral at leftside:
    xpos 0.2
$ renpy.transition(dissolve, layer='master')
"Turning to me, Eileen's emerald eyes stare into my own, checking my reaction after the day's events. As rough as she might be, Eileen really does care about others."

show caprice outdoors_behindback neutral at rightedge:
    xpos 0.8
$ renpy.transition(dissolve, layer='master')
voice "Allison_Eileen3.ogg"
allison "Let's go, Eileen."

show eileen smile at leftside:
    xpos 0.2
$ renpy.transition(midDissolve, layer='master')
stop ambiance fadeout 3.0
$ _dismiss_pause = False
"With this, she gives one of those few smiles she dares give. It feels like a reward to see them, and I find myself wanting to see them more and more."

window hide dissolve
scene black with longDissolve
return
