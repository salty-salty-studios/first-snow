# 00_config.rpy
# Basic Ren'Py game options.

python early:
    config.save_directory = "FirstSnow"
    config.testing = False
    config.patch_version = None

init -1 python:
    def get_menu_theme():
        return 'music/snow-eileen.ogg' if persistent.finished_story else 'music/snow.ogg'

init -1 python hide:
    # Basic settings.
    config.name = "First Snow"
    config.version = "1.0.1"
    config.patch_version = 3
    config.developer = False

    # Window.
    config.screen_width = 1280
    config.screen_height = 720
    config.window_title = u"First Snow"
    config.window_icon = "ui/icon.png"
    config.windows_icon = "ui/icon-win.png"
    config.default_fullscreen = False
    config.framerate = 60

    # Capabilities.
    config.gl_resize = False
    config.has_sound = True
    config.has_music = True
    config.has_voice = True
    config.main_menu_music = get_menu_theme()
    config.has_autosave = False
    config.has_quicksave = False

    # Misc.
    config.voice_filename_format = "voice/{filename}.mp3"
    config.default_text_cps = 25
    config.thumbnail_width = 193
    config.thumbnail_height = 108

    # Theme.
    theme.marker(
        widget = "#003c78",
        widget_hover = "#0050a0",
        widget_text = "#c8ffff",
        widget_selected = "#ffffc8",
        disabled = "#404040",
        disabled_text = "#c8c8c8",
        label = "#ffffff",
        frame = "#6496c8",
        mm_root = "#000000",
        gm_root = "#dcebff",
        rounded_window = False
    )
    style.default.font = "ui/SetFireToTheRain.ttf"

    # Keymap.
    config.keymap['choose_renderer'] = []

    # Default transitions.
    config.enter_transition = None
    config.exit_transition = dissolve
    config.intra_transition = None
    config.main_game_transition = dissolve
    config.game_main_transition = dissolve
    config.end_splash_transition = None
    config.end_game_transition = dissolve
    config.after_load_transition = dissolve
    config.window_show_transition = None
    config.window_hide_transition = None

    # Customizations/hacks.
    config.image_cache_size = 16
    store._game_menu_screen = "pause_menu"
    config.quit_action = Quit()
