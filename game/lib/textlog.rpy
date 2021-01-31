# textlog.rpy
# Maintains a nice little text log. Works through rollback and roll-forward.
# Tested in Ren'Py v6.17.3.
# Copyright (C) 2012-2014 Shiz.
# Released under the terms of the WTFPL; see http://sam.zoy.org/wtfpl/COPYING for details.

# USAGE:
# Place in your game, then call screen text_log to show the text log.
#
# Config variables:
#   - config.text_log_size:
#     Text log size. -1 for unlimited.
#   - config.text_log_blocked_tags:
#     Do not log the text if it contains one of these tags.
#   - config.text_log_filtered_tags:
#     Tags to filter for the log.

python early:
    import re

    # Create configuration variables.
    locked = config.locked
    config.locked = False
    config.text_log_size = 100
    config.text_log_blocked_tags = [ 'nw' ]
    config.text_log_filtered_tags = [ '', 'w', 'fast', 'cps', 'p' ]
    config.locked = locked

    # Simple buffer to hold the text log;
    # will automatically delete older logs once the limit has reached.
    class TextLog(NoRollback):
        def __init__(self):
            self.given_size = config.text_log_size
            self.hooks = []
            if self.given_size == -1:
                self.size = 0
                self.data = []
            else:
                self.size = self.given_size
                self.data = [ (None, None, None) for i in xrange(self.size) ]

            self.block_regexp = re.compile('(' + '|'.join(u'\{%s\}|\{%s=.*?\}|\{/%s\}' % (tag, tag, tag) for tag in config.text_log_blocked_tags) + ')')
            self.filter_regexp = re.compile('(' + '|'.join('\{%s\}|\{%s=.*?\}|\{/%s\}' % (tag, tag, tag) for tag in config.text_log_filtered_tags) + ')')

        def add_dialogue(self, who, what):
            if not what or self.block_regexp.search(what):
                return
            fwho = self.filter_regexp.sub('', who) if who else None
            fwhat = self.filter_regexp.sub('', what)
            if self.data and self.data[-1] == ('dialogue', fwho, fwhat):
                return

            if self.given_size != -1:
                self.data.pop(0)
            else:
                self.size += 1

            self.data.append(('dialogue', fwho, fwhat))
            for f in self.hooks:
                f('dialogue', who, what)

        def add_choice(self, choice):
            if self.block_regexp.search(choice):
                return

            if self.given_size != -1:
                self.data.pop(0)
            else:
                self.size += 1

            self.data.append(('choice', None, self.filter_regexp.sub('', choice)))
            for f in self.hooks:
                f('choice', choice)

        def all(self):
            return self.data

        def get(self, i):
            return self.data[i]

        def add_hook(self, func):
            self.hooks.append(func)

init -1501 python:
    # Replace character classes with logging ones.
    class LoggingADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            if not renpy.is_seen(ever=False):
                store.text_log.add_dialogue(who, what)
            super(LoggingADVCharacter, self).do_done(who, what)


    ADVCharacter = LoggingADVCharacter
    # Straight outta Ren'Py.
    adv = ADVCharacter(None, kind=adv)

    # Override the menu handler to store choices.
    def menu(items, *args, **kwargs):
        rv = renpy.display_menu(items, *args, **kwargs)

        if not renpy.is_seen(ever=False) and (not 'interact' in kwargs.keys() or kwargs['interact']) and rv is not None:
            store.text_log.add_choice(items[rv][0])
        return rv

    # wrapper around renpy.filter_text_tags() to remove 'em all
    def remove_text_tags(s):
        return renpy.filter_text_tags(s, allow=[])

init -1500 python hide:
    config.keymap['text_log'] = ['l']

define _text_log_close = False

init -1000 python hide:
    def toggle_text_log():
        if not main_menu:
            ToggleScreen('text_log', dissolve)()

    config.underlay.append(renpy.Keymap(text_log=toggle_text_log))
