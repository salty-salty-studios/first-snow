# init.rpy
# Initialization code for the game, and for when a new game is started.

init -9999 python:
    store.dlc_packages = []

# Persistence initialization, if ran for the first time.
default persistent.cue_music = False
default persistent.cue_sfx = False
default persistent.h = True
default persistent.font_mode = 'standard'
default persistent.high_contrast = False
default persistent.finished_story = False

default editing = False

default preferences.afm_time = 15

init -1 python hide:
    # fast skip is so fast that with our directing it crashes Ren'Py lol
    config.keymap['fast_skip'] = []

init 999 python hide:
    store.h_available = ('h' in store.dlc_packages)
    store.rabbl.allow_explicit = store.h_available and persistent.h

init python hide:
    # Cheater cheater cheateerrrrr
    if renpy.loadable('secret-unlock.txt'):
        achievement.grant('h')

    # Patch version management
    def store_patch_version(info):
        info['patch_version'] = config.patch_version
    config.save_json_callbacks.append(store_patch_version)

    if (persistent.patch_version or 1) < config.patch_version:
        store.patch_updated = True
    else:
        store.patch_updated = False
    persistent.patch_version = config.patch_version

    # Register appropriate extra channels.
    renpy.music.register_channel('sound2', 'sfx', False, tight=True)
    renpy.music.register_channel('loopsfx', 'sfx', True, tight=True)
    renpy.music.register_channel('ambiance', 'ambiance', True, tight=True)
    renpy.music.register_channel('ambiance2', 'ambiance', True, tight=True)

    # Sync progress.
    achievement.sync()


# Setup audio playback log.
default persistent.played_tracks = set()

init -1 python hide:
    def log_playback(track):
        persistent.played_tracks.add(track)

    add_audio_callback('music', log_playback)
    add_audio_callback('loopsfx', log_playback)


label splashscreen:
    scene black
    # needs to have an interaction before accessing renderer info
    pause 0

    # Determine if we're running a software renderer.
    if renpy.get_renderer_info()['renderer'] == 'sw':
        scene misc heres a nickel kid get yourself a better computer
        $ renpy.transition(dissolve)
        $ renpy.pause()
        scene black with dissolve
        $ renpy.quit()

    # Force Ren'Py to pin vital menus.
    $ renpy.cache_pin(*renpy_listdir('ui/main', full_path=True, recursive=True))
    $ renpy.cache_pin(*renpy_listdir('ui/pause', full_path=True, recursive=True))
    $ renpy.cache_pin(*renpy_listdir('ui/side', full_path=True, recursive=True))

    # Show a nice intro video.
    $ renpy.movie_cutscene("vfx/intro.ogv")
    $ renpy.transition(dissolve)
    return
