init -5 python:
    import time

    store._screenshot_taken = 0

    def screenshot_callback(filename):
        store._screenshot_taken = time.time()
        renpy.restart_interaction()

    def screenshot_overlay():
        if not renpy.has_screen('screenshot_indicator'):
            return
        if not renpy.get_screen('screenshot_indicator') and store._screenshot_taken:
            renpy.show_screen('screenshot_indicator')
        elif renpy.get_screen('screenshot_indicator') and time.time() - store._screenshot_taken > 4.0:
            renpy.hide_screen('screenshot_indicator')
            store._screenshot_taken = 0

    config.screenshot_callback = screenshot_callback
    config.overlay_functions.append(screenshot_overlay)
