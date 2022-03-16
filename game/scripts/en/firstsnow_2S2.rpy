label scene_2S2_en:
######################

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg buildingart hallway2f sketch with inkfade
scene bg buildingart hallway2f with inkfade2
stop sound fadeout 0.1
window show dissolve
$ _dismiss_pause = True

play loopsfx "sfx/ambiance/crowd_inner.ogg" fadein 2.0
"I briefly wonder who's in the art room as I proceed along the second floor hallway. Well, less wonder, and more hope."

"Caprice will be there, I've little doubt of that, but I'm starting to enjoy being around Eileen. Her paintings are so nice to see, and any time I manage to make her warm to me feels somehow rewarding."

"Someone like Caprice smiles all the time, and the moment we sat beside each other in a biology lecture, my fate was sealed as she began chatting to me without prompting."

"While I don't mind that at all, finding her bubbly attitude uplifting if a little overbearing, there's little about her that she keeps to herself."

"When Eileen gives praise, or even just smiles, it feels genuinely earned. I think that's the difference."

play sound "sfx/door_open2.ogg"
$ renpy.sound.set_volume(0.5, channel="loopsfx", delay=0.5)
scene bg buildingart art dusk bustsketch
show caprice indoors_behindback even normal neutral at left2:
    xzoom -1 xpos 0.18
with midDissolve
"Upon reaching the door and opening it, the otherwise empty room is filled with the greetings of a certain loud girl. Sitting at a table with a sketchbook in front of her, she takes a brief break from her work."

play sound "sfx/door_close.ogg"
$ renpy.music.set_volume(0.8, delay=0.0)
play music "music/art_club_a.ogg" fadein 5.0
$ renpy.sound.set_volume(0.2, channel="loopsfx", delay=0.5)
show caprice indoors_wave raised normal opensmile at left2:
    xpos 0.18
    bounce
voice "Caprice_Hi1.ogg"
caprice "Good afternoon, Allison!"

show caprice neutral at left2:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
voice "Allison_Hey2.ogg"
allison "Hi. You look cheerful as usual."

stop sound fadeout 1.0
show caprice indoors_pumped raised normal grin at left2:
    xpos 0.18
    bounce
caprice "I'm super ready for today's art club meeting!"

"She pumps her fist as I walk in, earning a sincere if weary smile. I feel a little bad for my first reaction upon entering being disappointment, given her earnest sense of friendship with me."

show caprice indoors_behindback even closedhappy neutral at left2:
    xpos 0.18
$ renpy.transition(dissolve, layer='master')
"Shrugging it off, I pile my books onto another table and take a couple of pencils from the side of the table which Caprice has commandeered."

show bg buildingart art dusk bustsketch blurred2
show misc cutins capshading:
    subpixel True
    xalign 0.8 yoffset 0
$ renpy.transition(dissolve, layer='master')
pause 1.0

"A glance at the sketchbook Caprice has been sketching in makes me stop in my tracks."

"I have to look up at her and back down again, just to confirm that this was done by the same person. Her casual doodles were cute, but she has a real talent for this stuff now that I see her more serious work."

"I never really questioned how much Caprice has practiced her art, now that I think of it. I'm left a little chastened for underestimating how much effort she puts into this hobby."

play sound "sfx/ambiance/painting.ogg" fadein 0.1
show misc cutins capshading:
    subpixel True
    xalign 0.8 yoffset 0 alpha 1
    ease 1.5 alpha 0
show misc cutins allisondoodles as misc2:
    subpixel True
    xalign 0.8 yoffset -550
    ease 1.5 yoffset -20
"Motivated to try a bit harder myself, I take a seat and open one of my notebooks. Flipping to a mostly empty page, I ponder for a moment before setting about sketching a cat. They were always a favorite subject to doodle."

play sound "sfx/door_open2.ogg"
show misc cutins allisondoodles as misc2:
    subpixel True
    xalign 0.8 yoffset -20
    ease 1.5 yoffset -600
with None
show bg buildingart art dusk bustsketch
show caprice indoors_wave raised normal open at left2:
    xzoom -1 xpos 0.18
$ renpy.transition(midDissolve, layer='master')
stop sound fadeout 0.1

"I lose track of time as I start to get into it, trying to replicate Caprice's shading from memory. It's only when Caprice pipes up with another greeting that I take a break."

play sound "sfx/door_close.ogg"
show eileen outdoors_onhip closed open at rightside:
    zoom 0.8 ypos 0.8 xpos 1.2
    ease 1.5 xpos 0.85
"Eileen strides through the doorway as I look up, giving a quick perfunctory wave to the both of us. She looks barely awake, but given how tired she always looks, it's hard to say if it's any worse than usual."

show eileen outdoors_onhip normal neutral at rightside:
    zoom 0.8 ypos 0.8 xpos 0.85
show caprice indoors_handonhip raised closedsad neutral at left2:
    xzoom -1 xpos 0.18
    linear 0.7 xzoom 1 xpos 0.2 alpha 1
    ease 1.5 xpos -0.2 alpha 0
hide misc cutins capshading
hide misc cutins allisondoodles
stop sound fadeout 1.0
"As we exchange greetings and Caprice gets back to her sketching, Eileen's eyes fall on my notebook."

stop music fadeout 5.0
show eileen outdoors_onhip normal neutral at rightside:
    subpixel True
    xpos 0.85 zoom 0.8 ypos 0.8 alpha 1
    parallel:
        ease 4.0 xpos 0.5 zoom 1.0 ypos 1.0
    parallel:
        ease 0.5 yoffset -1
        ease 0.5 yoffset 1
        repeat 4
"Without breaking stride, she turns on the ball of her high boots to take a detour from her easel and peer at my work."

show eileen outdoors_onhip disbelief neutral at center:
    zoom 1.0 ypos 1.0 xpos 0.5
$ renpy.transition(dissolve, layer='master')
"Eileen's figure looms above as she stands in front of me, fingers pressed to the top of my sketchbook as she looks down. It conjures up feelings I haven't felt since middle school, as if a student shrinking before her teacher."

scene bg buildingart art dusk bustsketch
show eileen outdoors_crossed lookaway open at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "Haven't done this in a while, have you?"

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
voice "Allison_Sorry1.ogg"
allison "Sorry..."

show eileen narrow at center
$ renpy.transition(dissolve, layer='master')
eileen "Why're you apologizing? If you haven't, you haven't."

show eileen closed at center
$ renpy.transition(dissolve, layer='master')
eileen "You have the fundamentals right at least, which only comes with practice."

show eileen outdoors_onhip normal at center
$ renpy.transition(dissolve, layer='master')
"Her fingertip skates back and forth on the paper, pointing out this and that."

show eileen open at center
$ renpy.transition(dissolve, layer='master')
eileen "Musculature looks off, but that's a pain at the best of times for animals. Try to draw from references, instead of relying on what your mind thinks something looks like."

play music "music/anxiety_2_m.ogg" fadein 5.0
show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
"A weight feels as if it's been lifted from my shoulders. It's not exactly high praise, but the fact she's willing to give me pointers feels like validation."

show eileen closed smile at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh3.ogg"
eileen "You like cats?"

allison "I have one back home."

show eileen outdoors_crossed lookaway open at center
$ renpy.transition(dissolve, layer='master')
eileen "Explains it. More of a dog person myself, really."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "Ever had one?"

show eileen lookawaynarrow at center
$ renpy.transition(dissolve, layer='master')
eileen "Would've been nice, but my parents weren't interested in the idea."
voice "Allison_Hm1.ogg"
allison "Sounds like you and your parents don't get along very well."

show eileen narrow frown at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_No1.ogg"
eileen "We don't."

show eileen outdoors_onhip open at center
$ renpy.transition(dissolve, layer='master')
eileen "The pet thing's nothing to do with it; they wanted me to go into one of their approved careers, and I didn't."

show eileen neutral at center
$ renpy.transition(dissolve, layer='master')
allison "Oh. I thought it would be something more complicated."

show eileen closed frown at center
$ renpy.transition(dissolve, layer='master')
eileen "Sometimes things really are as simple as they seem."

allison "I'm sure things will work out eventually."

show shadow behind eileen:
    alpha 0.0
    ease 3.0 alpha 0.4
stop music fadeout 8.0
show eileen outdoors_crossed annoyed frown at center
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Grumble5.ogg"
eileen "That's nice."

"I open my mouth to respond, but the tone behind her words makes it clear that she considers this discussion over."

"The air goes cold between us, leaving me at a loss for words as my shoulders slump in defeat. All I meant to do was cheer her up..."

scene bg buildingart art dusk bustsketch
$camera_move(-2800,-250,600,0,0,'dissolve')
show eileen outdoors_onhip closed neutral at midright:
    alpha 0
show eileen outdoors_onhip closed neutral at center as eileen2:
    zoom 0.65 yoffset -300
    xpos 0.52
with fadeInOut
show eileen indoors_onhip closed neutral at center as eileen2 with dissolve:
    zoom 0.65 yoffset -300
    xpos 0.52
    nod2
"As she steps over to another table and pulls off her coat, Caprice gleefully fills the awful silence with her bubbly voice."

play music "music/caprice_default_m.ogg" fadein 3.0
show eileen indoors_onhip normal neutral at center as eileen2:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
show caprice indoors_wave raised normal opensmile at leftside:
    xzoom -1 zoom 0.65 yoffset -300
    xpos 0.0 alpha 0.0
    ease 1.5 xpos 0.12 alpha 1.0
voice "Caprice_Allie1.ogg"
caprice "Hey, have you tried doing other stuff as well?"

show caprice neutral at leftside:
    xpos 0.12 alpha 1.0
$ renpy.transition(dissolve, layer='master')
voice "Allison_Huh1.ogg"
allison "What do you mean?"

show caprice indoors_chintap closedhappy neutral at leftside:
    xpos 0.12
$ renpy.transition(dissolve, layer='master')
caprice "Y'know, other kinds of art. There's oils, watercolor, pottery, fletching..."

show eileen indoors_crossed disbelief open at center as eileen2:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "I both paint and do sketch work, so it's not like you need to keep to one thing or another."

show eileen neutral at center as eileen2:
    xpos 0.52
show caprice indoors_handonhip raised normal open at leftside:
    zoom 0.65 yoffset -300
    xpos 0.12
    easein .15 yoffset -318
    easeout .175 yoffset -300
    easein .15 yoffset -308
    easeout .175 yoffset -300
caprice "I can get some pottery stuff if you want!"

show eileen narrow angry at center as eileen2:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Eileen barely restrains herself from rolling her eyes."

show eileen lookawaynarrow open at center as eileen2:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
eileen "By harassing the poor professor into giving you some kiln time and clay..."

show eileen angry at center as eileen2:
    xpos 0.52
show caprice indoors_behindback even half pout at leftside:
    xpos 0.12
$ renpy.transition(dissolve, layer='master')
voice "Caprice_No3.ogg"
caprice "It's not harassment, it's negotiating!"

show caprice indoors_handonhip even half puffed at leftside:
    xzoom -1 xpos 0.12 alpha 1
    linear 0.7 xzoom 1 xpos 0.14
    ease 1.5 xpos 0.0 alpha 0
allison "I... think I'll be fine for now."

show eileen indoors_onhip normal neutral at center as eileen2:
    zoom 0.65 yoffset -300
    xzoom 1 xpos 0.52
    linear 0.7 xzoom -1 xpos 0.5
"Eileen gives one final piece of advice as she turns towards the cupboard, taking advantage of the lull from Caprice focusing her own work."

show eileen normal open at center as eileen2:
    xzoom -1 xpos 0.5
$ renpy.transition(dissolve, layer='master')
eileen "Don't worry about her; just keep at it. Practice might not make perfect, but it'll get you close."

show eileen closed neutral at center as eileen2:
    xzoom -1 xpos 0.5 alpha 1
    ease 1.8 xpos 0.8 alpha 0
"I'm sure Eileen means well with her efforts at teaching, but it's a vast change to the way I used to draw as a kid and in high school, being little more than the occasional scribble when an idea struck."

stop music fadeout 8.0
play sound "sfx/door_jiggle.ogg"
scene bg buildingart art dusk bustsketch with fadeInOut
$ camera_reset()
"Barely having time to put pencil to paper, a clatter at the front of the room draws the attention of both Caprice and I. As Eileen fiddles, both of us get up to see what's happening."

show eileen indoors_onhip disbelief neutral at left2:
    xzoom 1 xpos 0.26
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Hmm1.ogg"
eileen "Hmm."

show caprice indoors_chintap raised normal frown at right2
$ renpy.transition(dissolve, layer='master')
caprice "What's up?"

play sound "sfx/door_jiggle.ogg"
show eileen indoors_fists disbelief neutral at left2:
    xzoom 1 xpos 0.26
    nod2
"Standing at the old wooden cabinet at the front of the room, Eileen gives a couple more sharp tugs at the door with all her usual gentleness, before turning to Caprice."

stop sound fadeout 1.0
play music "music/questioning.ogg" fadein 3.0
show eileen indoors_onhip lookaway frown at left2:
    xzoom 1 xpos 0.26
    linear 0.7 xzoom -1 xpos 0.225
eileen "The door to the cabinet's locked."

show caprice indoors_wave even closedhappy open at right2
$ renpy.transition(dissolve, layer='master')
voice "Caprice_Hmm2.ogg"
caprice "Nah, they never lock it after class."

show eileen indoors_onhip lookaway grumble at left2:
    xzoom -1 xpos 0.225
show caprice indoors_wave even closedhappy open at right2:
    nod2
play sound "sfx/door_jiggle.ogg"
"She bounces over to Eileen and takes the handle in her grip, giving it several pulls at various creative angles in case it's jammed. After one last try, hard enough to have her feet slipping on the floor..."

stop sound fadeout 1.0
show caprice indoors_behindback puffed half even at right2
show eileen indoors_crossed narrow open at left2
$ renpy.transition(dissolve, layer='master')
eileen "Could you say that again? I didn't quite catch what you said."

show eileen neutral at left2
show caprice flat at right2
$ renpy.transition(dissolve, layer='master')
"As they face off, I take a look at the cabinet between them. It's a type of lock I've tried before, and not particularly high-end. Then again, I've never done this with two people peering over my shoulder."
voice "Allison_Um2.ogg"
allison "Umm..."

show eileen indoors_onhip normal neutral at left2
show caprice indoors_handonhip even normal neutral at right2
$ renpy.transition(dissolve, layer='master')
"As they both look to me, I realize there isn't any backing down now. Glancing out the door to make sure there isn't anyone listening in, I continue on."

allison "I could maybe try picking it?"

show caprice indoors_behindback raised normal open at right2:
    yoffset 55 rotate 0
    ease 1.0 rotate -5
voice "Caprice_What1.ogg"
caprice "You can do that!?"

show eileen indoors_onhip disbelief open at left2
show caprice raised neutral at right2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Seriously3.ogg"
eileen "Someone sure has a knack for skills that upstanding people shouldn't have."

show eileen neutral at left2
show caprice indoors_handonhip even neutral at right2:
    yoffset 55 rotate -5
    ease 1.0 rotate 0
"All I can do in response is wilt. Eileen's not exactly wrong, even if I do like to think I only use such things when I should."

show eileen indoors_crossed closed open at left2
show caprice pout at right2:
    yoffset 55 rotate 0
$ renpy.transition(dissolve, layer='master')
eileen "We don't really have much of an option. Think you can do it?"

show eileen neutral at left2
$ renpy.transition(dissolve, layer='master')
"Accepting my fate, I get up and hold my hand towards them."
voice "Allison_Hm4.ogg"
allison "I'll need a couple of paperclips."

# Timeskip
stop loopsfx fadeout 1.5
scene black with circlewipe
play sound "sfx/picking_lock.ogg"
scene bg buildingart art dusk bustsketch
show eileen indoors_crossed lookawaynarrow neutral at left2:
    xzoom -1
show caprice indoors_chintap pout normal sad at right2
with circlewipe
"Taking to my feet once more, Eileen and Caprice look more dubious than impressed."

show caprice frown at right2
$ renpy.transition(dissolve, layer='master')
voice "Caprice_Allie6.ogg"
caprice "Well? Did you get it?"

stop music fadeout 2.0
stop sound fadeout 1.0
"Little more confident than Caprice - her face having been plastered right beside the lock out of curiosity as I worked - I take a long breath and reach out to the handle, giving it a timid tug."

play sound "sfx/door_creak.ogg"
show eileen indoors_onhip disbelief open at left2
show caprice indoors_handonhip raised open at right2
$ renpy.transition(dissolve, layer='master')
"The relief in the room is palpable as the old door creaks open, revealing shelf upon shelf of supplies."

play music "music/art_club_a.ogg" fadein 3.0
show eileen indoors_onhip disbelief frown at left2
show caprice indoors_pumped opensmile closedhappy raised at right2:
    bounce
voice "Caprice_AH.ogg"
caprice "Awesome!"

stop sound fadeout 1.0
show bg buildingart art dusk bustsketch blurred2 as bg2 behind eileen, caprice:
    xalign 0.5 yalign 0.5 alpha 0.9
show eileen indoors_onhip disbelief frown at left2:
    zoom 0.8 yoffset -150
    xzoom -1
    xpos 0.225
show caprice indoors_pumped grin closedhappy raised at right2:
    zoom 1.35 yoffset 300
    xpos 0.75
with hpunch
"Caprice gives a tight hug from behind in appreciation and excitement, leaving me to awkwardly laugh off the praise as Eileen starts taking her paints and brushes."

hide bg2
show eileen indoors_crossed closed neutral at left2:
    zoom 1.0 yoffset 0
    xzoom -1
    xpos 0.225
    time 0.5
    nod
show caprice indoors_behindback neutral normal even at right2:
    zoom 1.0 yoffset 0
    xpos 0.775
with smoothDissolve
"As she rights herself and Caprice detaches herself from me, Eileen gives a couple of claps on the shoulder with her free hand."

show eileen indoors_onhip normal open at left2
show caprice indoors_behindback closedhappy at right2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Heh1.ogg"
eileen "You did good. Where, or maybe I should say why, did you pick up skills like that?"

show eileen neutral at left2
$ renpy.transition(dissolve, layer='master')
voice "Allison_NervousLaugh.ogg"
allison "I just like learning things."

show eileen indoors_onhip normal neutral at left2
show caprice indoors_chintap raised normal at right2:
    xpos 0.775
    ease 1.0 xpos 0.6
"Taking an interest in the conversation, Caprice leans back towards us."

show caprice opensmile at centerright:
    xpos 0.6
$ renpy.transition(dissolve, layer='master')
caprice "What kinda things? Other cool stuff like that?"

show caprice neutral at centerright:
    xpos 0.6
$ renpy.transition(dissolve, layer='master')
allison "Just... things. Schoolwork wasn't too hard, so instead of studying, I ended up teaching myself stuff like how to pick locks and tinker with different machines to keep myself occupied."

show eileen indoors_crossed lookawaynarrow neutral at left2
$ renpy.transition(dissolve, layer='master')
voice "Eileen_Huh2.ogg"
eileen "Are you aware of how sketchy that sounds?"

show caprice indoors_handonhip even closedhappy grin at centerright:
    xpos 0.6
$ renpy.transition(dissolve, layer='master')
voice "Allison_Oh.ogg"
allison "It's not about doing bad things! They're just puzzles. The point is working them out, not getting free stuff."
voice "Allison_Sigh2.ogg"
allison "When I put it that way, I guess it is pretty useless to learn."

show caprice indoors_behindback neutral wink even at centerright:
    xpos 0.6
show eileen narrow at left2
$ renpy.transition(dissolve, layer='master')
caprice "That's pretty funny to be saying right now."

show eileen disbelief at left2
show caprice behind eileen at centerright:
    xpos 0.6
    ease 1.0 xpos 0.45
    nod2
"Caprice nudges Eileen, who just raises an eyebrow. She makes a decent point."

show caprice indoors_handonhip closedsad at offcenterleft:
    xpos 0.45 alpha 1
    ease 1.5 xpos -0.2 alpha 0
show eileen normal at left2:
    xpos 0.225 alpha 1
    time 0.5
    ease 1.0 xpos 0.5 alpha 0
"Hoping that no staff were around to notice what just happened, I throw the twisted paperclips into the bin, before heading to my table as Caprice takes to hers and Eileen sits herself at her easel. Without further ado, we each set to work."

stop music fadeout 5.0
scene bg buildingart art dusk bustwip with midDissolve
"It's a nice atmosphere, with the three of us working away at our own little projects. I'm not sure sketching cats in a notebook really counts as much of a project, but having friends around makes it somehow more meaningful."

# Timeskip
scene black with longDissolve
play ambiance "sfx/ambiance/tv.ogg" fadein 2.0
$ renpy.sound.set_volume(1.0, channel="loopsfx")
scene bg aptallison livingroom with dissolve
"With winter setting in, I find myself settled in for the evening on the couch watching a movie on the television, a blanket draped over me to try and keep warm."

"Rose still isn't back from work, and with the garbage taken out and washing-up done, it probably won't hurt to take things easy for the rest of this evening."

# TODO: improve sfx
play sound "sfx/cell_phone_vibrate.ogg"
window show
"A loud ping comes from beside me, my hand automatically reaching for the phone sitting on the couch in response. Probably Rose saying she'll be late, dooming me to microwave noodles for dinner again."

$ phone.message('eileen', '8:27 PM', 'Is this Allison?')
$ phone.show('messages', who='eileen')
show bg aptallison livingroom blurred2
$ renpy.transition(fastDissolve, layer='master')
stop sound fadeout 1.0
"...Or perhaps not. I don't recognize the number or user avatar at all."

window hide
"I briefly consider saying no, but that would be mean. I can barely make out their picture, beyond what I think to be yellow hair. I don't even know any blondes besides Eileen and Millie, and the latter's unlikely to be messaging me."

stop ambiance fadeout 5.0
play music "music/eileen_5_m.ogg" fadein 5.0
$ phone.message('eileen', '8:28 PM', 'eileen?', to=True)
$ phone.wait()

$ phone.message('eileen', '8:30 PM', 'Wallace helped me set this thing up.')
$ phone.wait()

$ phone.message('eileen', '8:30 PM', 'what\'s with your profile pic? :s', to=True)
$ phone.wait()

$ phone.message('eileen', '8:31 PM', 'It took a photo when I was setting up.')
$ phone.wait()

$ phone.message('eileen', '8:32 PM', 'find any nice apps yet?', to=True)
$ phone.wait()

$ phone.message('eileen', '8:33 PM', 'I haven\'t tried looking. I don\'t really get it.')
$ phone.wait()

"I can't help but giggle a little. I'm happy she's making the effort, when she made it clear she wasn't interested before."

$ phone.message('eileen', '8:34 PM', 'i\'ll help you with it tomorrow :)', to=True)
$ phone.wait()

$ phone.message('eileen', '8:35 PM', 'That would be good, thanks.')
$ phone.wait()
$ phone.message('eileen', '8:38 PM', 'Sorry if I type slowly. This keyboard is weird.')
$ phone.wait()

$ phone.message('eileen', '8:38 PM', 'practice makes perfect!', to=True)
$ phone.wait()

$ phone.message('eileen', '8:40 PM', 'About that.')
$ phone.wait()
$ phone.message('eileen', '8:42 PM', 'Wanted to say sorry about the parents thing.')
$ phone.wait()
$ phone.message('eileen', '8:43 PM', 'I was too touchy.')
$ phone.wait()

$ phone.message('eileen', '8:44 PM', 'it\'s okay.', to=True)
$ phone.wait()
$ phone.message('eileen', '8:44 PM', 'wasn\'t really my business.', to=True)
$ phone.wait()

$ phone.message('eileen', '8:46 PM', 'Life doesn\'t always have a happy ending.')
$ phone.wait()
$ phone.message('eileen', '8:47 PM', 'Things don\'t work out, and that\'s that.')
$ phone.wait()

$ phone.message('eileen', '8:48 PM', 'you still have to try though!', to=True)
$ phone.wait()
$ phone.message('eileen', '8:48 PM', 'people are good', to=True)
$ phone.wait()
$ phone.message('eileen', '8:48 PM', 'you just need to have faith', to=True)
$ phone.wait()
$ phone.message('eileen', '8:49 PM', 'at least, that\'s what i think :)', to=True)
$ phone.wait()

$ phone.message('eileen', '8:51 PM', 'I don\'t get you at all.')
$ phone.wait()

show rose indoors_smokingmouth smile halfclosed at farright:
    alpha 0
show rose outdoors_smokingmouth smile halfclosed at right2 as rose2:
    xpos 1.0 alpha 0
    ease 1.0 xpos 0.75
show rose outdoors_smokingmouth normal neutral blur at right2 as rose3:
    xpos 1.0 alpha 1
    ease 1.0 xpos 0.75
$ phone.message('eileen', '8:51 PM', 'i think that goes both ways.', to=True)
$ phone.wait()

window show
voice "Rose_UhHuh3.ogg"
rose "I see..."

$ phone.hide()
show bg aptallison livingroom
show rose outdoors_smokingmouth smile halfclosed at right2 as rose2:
    xpos 0.75 alpha 1
$ renpy.transition(fastDissolve, layer='master')
hide rose3
with vpunch
window hide
"Taken completely unawares, I leap off the couch and spin around, barely keeping a hold of the phone in my hand."
voice "Allison_Oh.ogg"
allison "When did you get in!?"

show rose outdoors_smokingmouth normal smile at right2 as rose2:
    xpos 0.75 alpha 1
$ renpy.transition(dissolve, layer='master')
rose "Just now. Sorry, couldn't help myself."

show rose outdoors_smokingmouth halfclosed laugh at right2 as rose2:
    xzoom 1 xpos 0.75 alpha 1
    linear 0.7 xzoom -1 xpos 0.78
    ease 1.2 xpos 1.25
"I let out a long breath to steady myself as my heart slowly returns to its normal pace. Rose just grins churlishly as she walks off to hang up her coat."

show bg aptallison livingroom blurred2:
$ renpy.transition(fastDissolve, layer='master')
$ phone.show('messages', who='eileen')
pause 1.0
hide rose2
hide rose
$ phone.message('eileen', '8:54 PM', 'roommate\'s back.', to=True)
$ phone.wait()
$ phone.message('eileen', '8:54 PM', 'catch you tomorrow.', to=True)
$ phone.wait()

$ phone.message('eileen', '8:55 PM', 'See you.')
$ phone.wait()

$ phone.show('unlock')
$ renpy.pause(1.0, hard=True)
window show
$ phone.hide()
show bg aptallison livingroom
$ renpy.transition(dissolve, layer='master')

"With that, I tap the side button to lock the phone once more, putting it on the counter beside me."

show rose indoors_smoking smile halfclosed at center:
    zoom 1.35 yoffset 300
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
voice "Rose_Heh2.ogg"
rose "You look happy."

"All I can do is grimace, my face becoming flushed from embarrassment at her bullying. Thanks to my cheeks mildly hurting, I can tell she isn't wrong."

show rose indoors_smoking normal talking at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
rose "I mean it. Does me good to see you managing to get yourself a social circle and all."

show rose neutral at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
allison "You were worried?"

show rose indoors_smoking puzzled normal at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
rose "Can you blame me? No guys around, no friends, always being so nervous. You've changed a lot."

"I guess Eileen was right, everyone really is there for me. Rose isn't wrong, either; I do have friends now, and the art club's starting to become a welcome little slice of familiarity in the campus."

show rose indoors_smoking halfclosed neutral at center:
    xpos 0.52
$ renpy.transition(dissolve, layer='master')
"Caprice, Wallace, Eileen, everyone's really nice to me. Yet, it's Eileen I can't stop thinking about. Behind that cold exterior of hers, there's a genuinely kind person."
voice "Allison_Hm4.ogg"
allison "What’s with that face?"

stop music fadeout 2.0
show rose indoors_smoking halfclosed smile at center:
    zoom 1.35 yoffset 300
    xzoom 1 xpos 0.52
    linear 0.7 xzoom -1 xpos 0.54
$ _dismiss_pause = False
rose "Nothin'. Gonna come eat, or play with your phone all day?"

window hide dissolve
scene black with longDissolve
return
