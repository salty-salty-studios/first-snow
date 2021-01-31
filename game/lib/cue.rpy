screen cue_overlay():
    python:
        for i in reversed(range(len(store._cues))):
            if store._cues[i].is_active():
                break
            store._cues.pop()

    vbox:
        xalign 1.0
        spacing 2

        for cue in store._cues:
            use expression cue.name pass (cue.is_active(), **cue.args)

screen cue(active, name, message):
    fixed:
        ysize 36
        if active:
            text message

init python:
    import collections

    CUE_DEFAULT_SCREEN = 'cue'
    store._cues = []

    class Cue:
        def __init__(self, name, args, timeout):
            self.name = name
            self.args = args
            self.until = time.time() + timeout

        def is_active(self):
            return time.time() < self.until

    def cue(name, timeout, **args):
        show_cue(name, timeout, args)
        t = threading.Timer(timeout, renpy.restart_interaction)
        t.start()
        renpy.restart_interaction()

    def show_cue(name, timeout, args=None):
        args = args or {}

        specific_screen = CUE_DEFAULT_SCREEN + '_' + name
        if renpy.has_screen(specific_screen):
            screen = specific_screen
        else:
            screen = CUE_DEFAULT_SCREEN
            args['name'] = name

        c = Cue(screen, args, timeout)
        store._cues.append(c)
        return c

    def hide_cue(c):
        c.until = 0.0
        renpy.restart_interaction()

    def cue_overlay_func():
        if not renpy.get_screen('cue_overlay') and store._cues:
            renpy.show_screen('cue_overlay')
        elif renpy.get_screen('cue_overlay') and not store._cues:
            renpy.hide_screen('cue_overlay')

    config.overlay_functions.append(cue_overlay_func)
