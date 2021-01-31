label scene_3S6_en:
######################
# Act 3, Scene 6

stop music fadeout 2.0
scene bg texture with midDissolve
play sound "sfx/ambiance/painting.ogg" fadein 0.1
scene bg colorado park sketch:
    xalign 0.0
with inkfade
scene bg colorado park:
    xalign 0.0
with inkfade2
stop sound fadeout 0.1
$ _dismiss_pause = True

play ambiance "sfx/ambiance/outside.ogg" fadein 1.0
show eve outdoors normal shy at centerright:
    xpos 0.6
show eileen outdoors_onhip neutral normal at left2:
    xzoom -1
$ renpy.transition(dissolve, layer='master')
play music "music/relaxing.ogg" fadein 2.0
window show dissolve

"The park makes for a peaceful sight as we enter, the three of us slipping between the low wooden barriers as we step from the rough concrete carpark onto the snow-covered grass."

"A bundled-up Eve clings tightly to Eileen and I with both of her little hands, each of us on either side of her. A bag of old bread swings away at Eileen's other side, destined for the local wildlife. I'll feel like a killjoy to say bread isn't good for them."

"With the two of us acting as babysitters thanks to Eileen's parents working, we decided it'd be better to head outside than let her vegetate on the couch watching cartoons all day."

scene bg colorado park blurred2:
    zoom 1.05 xalign 0.5 yalign 0.5
$camera_move(-2400,1400,300,0,0,'dissolve')
show eileen outdoors_fists closed angry at left2:
    subpixel True
    zoom 1.3 yoffset 300
    xzoom -1 xpos 0.22
show eve outdoors normal neutral at offcenterright:
    subpixel True
    zoom 1.3 yoffset 300
    xpos 0.55
with midDissolve
$camera_move(-2400,250,300,0,8,'ease')
"Tired from the walk, I take a seat on the swings facing the lake as Eileen mothers around Eve."

show eileen outdoors_fists closed angry at left2:
    subpixel True
    xzoom -1 xpos 0.22
    ease 1.2 xpos 0.32
    nod2
    ease 1.2 xpos 0.22
show eve outdoors normal annoyed at offcenterright with dissolve
"Tugging at the girl's scarf to pull it tight, Eileen hands over the bag of bread for the ducks before ruffling her hair affectionately."

"I wonder if that's why Eileen does that to me, now that I think of it."

show eileen outdoors_onhip narrow angry at left2:
    xzoom -1 xpos 0.22
$ renpy.transition(dissolve, layer='master')
"With her sister having finished her fussing, Eve turns and starts for the shore while Eileen watches her intently."

scene bg colorado park
show eve outdoors neutral normal at centerright:
    xpos 0.6
show eileen outdoors_crossed narrow open at left2:
    xzoom -1
with fadeInOut
$ camera_reset()
eileen "Be careful around the water, Eve!"

show eve outdoors normal happy at centerright:
    xpos 0.6
    bounce
show eileen neutral at left2 with dissolve:
    xzoom -1
eve "'Kay!"

play sound "sfx/ducks_quacking.ogg"
show eve outdoors normal grin at centerright:
    xzoom 1 xpos 0.6
    linear 0.7 xzoom -1 xpos 0.58
show eileen outdoors_onhip frowning smile at left2 with dissolve:
    xzoom -1
"The ducks peacefully floating about the still lake start flapping about excitedly, quickly realizing that the girl waddling towards them comes bearing food."

show eve outdoors normal grin at centerright:
    xzoom -1 xpos 0.58
    ease 1.5 xpos 1.2
"Satisfied that Eve isn't going to topple over in her rush and flop in, Eileen wanders back towards me and seats herself on the other swing, all the while keeping a keen eye out."

scene black with midDissolve
scene cg act3 swings
$camera_move(-3200,1000,750,0,0,'dissolve')
show cg act3 swings foreground blurred0 as cgf
with midDissolve
$camera_move(3200,1000,750,0,20,'ease')
"It looks like nobody else is here at all. It is getting rather cold, but it's more likely people being busy with the holiday sales. I'd think the lake to be frozen over given how still it is, save for the birds floating about."

allison "She's cute."

eileen "Yeah."

"While Eileen smiles warmly at her sister, I struggle to do the same. I'll soon have to make the call for Rose to pick me up, after all, leaving behind this lovely town. Eileen, Eve, their parents; I'm not sure when I'll get to see them again."

"Eve clumsily crumbs the bread in her gloved hands, chucking it out into the lake with varying degrees of success. Half the crumbs end up dropping to the ground at her feet, but she doesn't seem to notice."

stop sound fadeout 1.0
show cg act3 swings foreground blurred0 as cgf:
    alpha 1
    ease 20.0 alpha 0
$camera_move(0,0,0,0,20,'ease')
eileen "Is something up? You've been kind of quiet over the last couple of days."

eileen "I really don't get how you're such an upbeat person in general, though."

"Nor do I get how she's so comfortable being so alone. So apart. The more I'm around her, the more different I feel we are."

allison "I just think it's better to see the best in people."

eileen "I have to admit, I wish I could be like that."

allison "Why not try being more friendly in general? Every time I see you, you're closing yourself off to focus on painting or trekking out in the wilderness."

eileen "The more I get tied up with people, the harder it is to do what I want to do. You should know that better than most, with Caprice and all."

scene cg act3 swings blurred2
show cg act3 swings foreground as cgf
$ camera_reset()
with vpunch
stop music fadeout 4.0
allison "You shouldn't talk so badly about her all the time. She just wants everyone around her to enjoy themselves."

"I'm a little taken aback at how firm my tone is, but I'm starting to get tired of how she's always so critical."

"I force myself to keep my eyes on Eileen, despite her own surprise. Maybe it's for the best if I clear the air and talk about this directly."

play sound "sfx/ducks_quacking.ogg"
"Our concentration is broken by Eve giggling loudly in the distance, the birds enthusiastically crowding around in front of her and occasionally flapping away at the water."

scene bg colorado park blurred2:
    xalign 0.5 yalign 0.5
show eileen outdoors_crossed sad neutral at right2:
    zoom 1.3 yoffset 300
with fadeInOut
$ camera_reset()
stop sound fadeout 1.0
eileen "C'mon, what's this about? I get the feeling something's on your mind."

$ renpy.sound.set_volume(0.5, channel='ambiance', delay=5.0)
$ renpy.music.set_volume(0.8)
play music "music/more_sad_m.ogg" fadein 5.0
$ renpy.sound.set_volume(0.35, channel='ambiance2')
play ambiance2 "sfx/ambiance/soft-tonal-wind.ogg" fadein 30.0
allison "It feels like we're hanging around each other, but not actually..."

show eileen frown at right2
$ renpy.transition(dissolve, layer='master')
"I pause for a moment to phrase my thoughts correctly, trying not to let emotions cloud my thinking. Eileen - thankfully - patiently waits for me."

allison "I guess it feels like I'm along for the ride. It doesn't feel like I'm really there with you."

show eileen outdoors_onhip disbelief open at right2
$ renpy.transition(dissolve, layer='master')
eileen "What, here? We've been spending a lot of time together, and we've had some nice time to ourselves, right?"

show eileen outdoors_onhip neutral at right2
$ renpy.transition(dissolve, layer='master')
allison "Is that all this is to you?"

show eileen narrow angry at right2
$ renpy.transition(midDissolve, layer='master')
"As silence reigns, the fact that she even needs to think about this is a bit upsetting."

"I don't know how relationships are supposed to go, but it feels like we both have very different ideas about it."

show eileen outdoors_onhip lookawaynarrow angry at right2
$ renpy.transition(dissolve, layer='master')
eileen "What am I supposed to say? Is there something more you want from me? I'm just not as clingy as you are."

allison "Clingy! I just want to be by your side. You'd have gone off without me the other day if you felt like you could."

show eileen outdoors_crossed disbelief open at right2
$ renpy.transition(dissolve, layer='master')
eileen "Yeah, but I was being considerate of your feelings. Is that a problem?"

show eileen angry at right2
$ renpy.transition(dissolve, layer='master')
allison "It... it just feels like you'd rather I wasn't there."

show eileen outdoors_crossed lookaway open at right2
$ renpy.transition(dissolve, layer='master')
eileen "I like being with you, you know that. But I've been fine on my own all this time, too. I don't need you to be there."

show eileen neutral at right2
$ renpy.transition(dissolve, layer='master')
"Even though I always want to spend more time with her, she doesn't even care whether or not I'm there."

allison "You have it so together. I've always admired that about you. Maybe you have it too together."

show eileen outdoors_crossed lookawaynarrow at right2
$ renpy.transition(dissolve, layer='master')
allison "Before coming here, I didn't realize how good a life you left behind when you moved away. To drop everything here, including Eve, to pursue art at a community college..."

allison "From the way you talked about your family, I thought they must be really hard on you. They just want what's best. I mean, the apartment you have seems like it wouldn't be cheap for them to cover, for one."

show eileen outdoors_crossed narrow frown at right2
$ renpy.transition(dissolve, layer='master')
eileen "Because I don't hear that enough from them every time I'm around here..."

show eileen outdoors_onhip sad open at right2
$ renpy.transition(dissolve, layer='master')
eileen "Can we just drop this? I like being around you because you don't bring up that stuff."

show eileen outdoors_onhip angry at right2
$ renpy.transition(dissolve, layer='master')
allison "Is that all you want from me? A quiet girlfriend, who doesn't ask questions and leaves you alone?"

show eileen outdoors_onhip annoyed at right2
$ renpy.transition(dissolve, layer='master')
"Eileen takes to her feet, her mood significantly souring. While I freeze up, I don't feel like shrinking from her for once."

allison "Am I only here to distract you from your parents?"

show eileen outdoors_fists annoyed open at right2
$ renpy.transition(dissolve, layer='master')
eileen "You're the one who begged to come! I told you that you could come precisely because I didn't think you'd go sticking your nose into my life."

show eileen outdoors_fists sadmouth at right2
$ renpy.transition(dissolve, layer='master')
allison "But I want to learn more about you! That's what having a relationship is!"

show eileen outdoors_fists open annoyed at right2:
    nod2
with hpunch
eileen "That's up to me, not you!"

show eileen outdoors_onhip lookawaynarrow sadmouth at right2
$ renpy.transition(dissolve, layer='master')
eileen "This is why you shouldn't have come in the first place."

"She points in the general direction of her house."

show eileen outdoors_onhip lookawayangry open at right2
$ renpy.transition(dissolve, layer='master')
eileen "I'm used to enduring their crap already. I didn't need you here to make things worse; I'm already hearing from them about how my girlfriend has a better life path than I do."

show eileen outdoors_onhip sadmouth at right2
$ renpy.transition(dissolve, layer='master')
"So that's my fault?"

"I think I'm shaking. My eyes are stinging from salt waiting to flood out."

allison "Maybe they have a point. Did you think any of this through beyond just escaping them? Is that all our relationship is, too?"

show eileen outdoors_fists annoyed open at right2
$ renpy.transition(dissolve, layer='master')
eileen "I had my life on track before I even met you. Just because you and Caprice want to come along and try to push me around, it doesn't mean I'm going to derail myself."

stop music fadeout 4.0
stop ambiance2 fadeout 4.0
play sound "sfx/ambiance/snowwalk.ogg" fadein 1.0
show eileen outdoors_crossed annoyed frown at right2
$ renpy.transition(dissolve, layer='master')
"Is that how she thinks of it? Didn't she agree to the art club? Didn't she agree to date me? Didn't she say she loves me?"

$ renpy.sound.set_volume(1.0, channel='ambiance', delay=2.0)
show bg colorado park
show eileen lookaway frown at right2
show eve outdoors normal unsure at left2:
    xzoom -1 xpos 0.225
$ renpy.transition(smoothDissolve, layer='master')
"Hearing the sound of footsteps on the snow, the two of us turn in unison towards Eve, standing a few yards away with an empty bread bag held in her hands."

show eve outdoors half sadopen at left2:
    xpos 0.225
$ renpy.transition(dissolve, layer='master')
stop sound fadeout 1.0
eve "Is something wrong?"

show eve outdoors half sad at left2:
    xpos 0.225
show eileen outdoors_crossed annoyed frown at right2
$ renpy.transition(dissolve, layer='master')
"Eileen looks to me for a long while, her face full of frustration. I don't think either of us really knows what we should say next, even without Eve being around."

$ renpy.music.set_volume(0.65)
play music "music/painter.ogg" fadein 2.0
show eileen outdoors_onhip closed neutral at rightish:
    zoom 1.0 yoffset 0
    xpos 0.7
$ renpy.transition(smoothDissolve, layer='master')
"Settling herself with a long breath, Eileen smiles as she turns back to Eve. I don't think I'll ever get used how she shifts her entire demeanor like that."

show eileen outdoors_onhip sad open at right2:
    xpos 0.7
    ease 1.5 xpos 0.45
    nod2
show eve outdoors unsure normal at left2:
    xzoom -1 xpos 0.225
    time 1.4
    linear 0.7 xzoom 1 xpos 0.24
eileen "Everything's fine, don't worry. It's about time we headed back home."

show eileen outdoors_onhip neutral at offcenterleft
show eve outdoors normal surprised at left2:
    xzoom 1 xpos 0.24
    bounce
eve "But I wanna keep feeding the ducks!"

show eve outdoors normal surprised2 at left2:
    xzoom 1 xpos 0.24
show eileen outdoors_onhip smile sad at offcenterleft:
    nod2
eileen "That's going to be hard without any more bread. C'mon, it's about time we had some food ourselves."

show eve outdoors normal unsure at left2:
    xzoom 1 xpos 0.24
    ease 1.8 xpos -0.25
show eileen outdoors_onhip lookawaynarrow sadmouth at offcenterleft:
    xpos 0.45
    ease 2.5 xpos -0.2
"She gives one final glance back, before taking Eve's hand in her own and walking on ahead."

scene black with midDissolve
stop music fadeout 5.0
scene cg act3 swings2 with midDissolve
$ renpy.sound.set_volume(0.4, channel='ambiance2')
play ambiance2 "sfx/ambiance/soft-tonal-wind.ogg" fadein 10.0
"I thought I was someone important to Eileen, but I feel more like I'm just being used to make herself feel better while she lives for her work."

"I know I have my faults; I'm not good enough at art to share the hobby with her, and I was barely even able to help cook a simple dinner. I'm trying to get better though, and that's thanks in part to her."

"The image I had of her is starting to become difficult to see. Who was the Eileen I admired? The beautiful girl in the beautiful apartment with the beautiful paintings? This Eileen is someone so at odds with her family, she decided to only care about herself."

stop ambiance fadeout 2.0
show cg act3 swings2 sepia as cg2:
    alpha 0.65
show shadow:
    alpha 0.2
with midDissolve
$ _dismiss_pause = False
"As I watch her leave hand-in-hand with Eve, she looks ever farther away from me. Maybe she's only so far away because we aren't walking on the same path."

stop ambiance2 fadeout 2.0
window hide dissolve
scene black with longDissolve
$ renpy.music.set_volume(1.0)
$ renpy.sound.set_volume(1.0, channel='ambiance2', delay=3.0)
return
