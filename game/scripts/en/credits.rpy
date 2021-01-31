label scene_4S1_en:
##############################
    # Credits.
    # Congratulations!
    $ achievement.grant('story_done')
    $ persistent.finished_story = True
    $ renpy.music.play('music/credits.ogg', fadein=2.0, if_changed=True)

    $ _dismiss_pause = True
    hide cg
    show misc credits:
        xalign 0.0
    with longDissolve

    show misc credits:
        subpixel True
        xalign 0.0
        ease_subtle 180 xalign 1.0
    $ renpy.pause(180, hard=True)
    $ renpy.pause()

    stop music fadeout 4.0
    scene black with longDissolve
    return
