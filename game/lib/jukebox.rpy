init python:
    ## Jukebox support functions.

    # Register channel.
    renpy.music.register_channel('jukebox', 'jukebox', False, tight=True)

    # Reload the screen when the queue became empty to update play status.
    def jukebox_empty():
        if not renpy.music.get_playing('jukebox'):
            if jukebox_empty.was_playing:
                jukebox_empty.was_playing = False
                renpy.restart_interaction()
        elif not jukebox_empty.was_playing:
            jukebox_empty.was_playing = True

    jukebox_empty.was_playing = False
    renpy.music.set_queue_empty_callback(jukebox_empty, channel='jukebox')

    def JukeboxEnter():
        return Stop('music', fadeout=1.0)

    def JukeboxLeave():
        return Stop('jukebox', fadeout=1.0)

    def jukebox_is_playing():
        return jukebox_now_playing() is not None

    def jukebox_now_playing():
        return renpy.music.get_playing('jukebox')

    def JukeboxPosition():
        return AudioPositionValue('jukebox')

    def jukebox_pos():
        return renpy.music.get_pos('jukebox')

    def JukeboxPlay(track=None):
        if track:
            pl = Play('jukebox', track, fadein=2.0) 
        else:
            pl = PauseAudio('jukebox', False)
        return [ Stop('music', fadeout=1.0), pl ]

    def JukeboxPause():
        return PauseAudio('jukebox', True)

    def JukeboxToggle():
        return PauseAudio('jukebox', 'toggle')

    def JukeboxStop(fadeout=None):
        return Stop('jukebox', fadeout=None)

    def JukeboxVolume():
        return Preference('jukebox volume')

    def jukebox_is_paused():
        return renpy.music.get_pause('jukebox')

    def jukebox_volume():
        return game.preferences.get_volume('jukebox')
