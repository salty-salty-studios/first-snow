init python:
    import collections

    class Phone:
        def __init__(self):
            self.messages = {}
            self.waiting = False

        def message(self, who, time, message, to=False):
            self.messages.setdefault(who, [])
            self.messages[who].append((to, time, message))
            renpy.restart_interaction()

        def clear(self, who):
            self.messages[who] = []
            renpy.restart_interaction()

        def show(self, mode, **kwargs):
            renpy.show_screen('phone', mode=mode, **kwargs)
            if renpy.showing('phone', layer='screens'):
                renpy.transition(dissolve, layer='screens')

        def hide(self):
            renpy.hide_screen('phone')

        def wait(self):
            self.waiting = True
            renpy.pause()
            self.waiting = False


default phone = Phone()
