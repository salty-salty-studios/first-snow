init 1 python:
    ## User-defined keymap functionality.
    # Copyright (C) 2014-2016 Shiz.
    # Tested on Ren'Py v6.99.8.
    # Released under the terms of the WTFPL; see http://sam.zoy.org/wtfpl/COPYING for details.
    #
    # Usage: Loop over ukm_event_order in a screen for a list of events to bind to.
    #  Skip None entries, they are there for adding spacing if you want to.
    #  For every event entry, loop over ukm_get_bindings(event) for a list of current bindings for that event as (binding, name, joy) tuples.
    #
    #  ukm_add_binding(event, binding, joy) is function that will add the given keymap binding.
    #  AddUserKeyBinding(event, binding, joy) is the equivalent screen action.
    #  ukm_remove_binding(event, binding, joy) is a function that will remove the given keymap binding.
    #  RemoveUserKeyBinding(event, binding, joy) is the equivalent screen action.
    #  `event` is an event name as in ukm_event_order, `binding` and `joy` are the variables stored by KeyBindingGrabBehaviour (see below).
    #
    #  To add a key binding, add KeyBindingGrabBehaviour('target_var', exclude_displayables=[...])
    #  to a dedicated screen where the user can input their desired keybind.
    #  The exclude_displayables parameter should be a list of displayable IDs that the code should ignore when grabbing input.
    #  This should usually be the confirm and cancel buttons at the least, so the user can exit the screen properly.
    #  The last pressed key binding will be stored in the store variable whose name is given as the first argument.
    #  For instance, if the string 'key_binding' is given, the binding will be stored in store.key_binding.
    #  The key binding stored is a tuple of (binding, name, joy). `binding` and `joy` are the parameters
    #  that should be passed to ukm_add_binding()/AddUserKeyBinding().
    #
    #  Trimmed-down example from Twofold code:
    #
    # screen preferences_keymap:
    #     on "hide" action Hide('preferences_kemap_add')
    #     on "replaced" action Hide('preferences_keymap_add')
    #
    #     ...
    #
    #                 for event in ukm_event_order:
    #                     if event is None:
    #                         null height 25
    #                     else:
    #                         label ukm_event_descriptions[event]:
    #                             ...
    #
    #                         hbox:
    #                             ...
    #
    #                             for binding, name, joy in ukm_get_bindings(event):
    #                                 label name:
    #                                     ...
    #                                 imagebutton:
    #                                     ...
    #                                     action RemoveUserKeyBinding(event, binding, joy)
    #
    #                             imagebutton:
    #                                 ...
    #                                 action Show('preferences_keymap_add', dissolve, event)
    #
    # screen preferences_keymap_add(event):
    #     python:
    #         if not hasattr(store, '_keymap_captured_key'):
    #             store._keymap_captured_key = (None, None, None)
    #
    #         binding, name, joy = store._keymap_captured_key
    #         if not name:
    #             name = '(nothing)'
    #
    #     frame id "preferences_keymap_add_frame":
    #         ...
    #
    #         add KeyBindingGrabBehaviour('_keymap_captured_key', exclude_displayables=['keymap_add_ok', 'keymap_add_cancel'])
    #
    #         text "Please press the keys or buttons you want to bind.":
    #             ...
    #
    #         text name:
    #             ...
    #
    #         imagebutton id "keymap_add_ok":
    #             ...
    #             action [ AddUserKeyBinding(event, binding, joy), Hide('preferences_keymap_add', dissolve) ]
    #
    #         imagebutton id "keymap_add_cancel":
    #             ...
    #            action Hide('preferences_keymap_add', dissolve)
    #
    import copy
    import renpy as rpy
    import pygame
    import collections

    def ukm_restore_bindings():
        if not persistent._ukm_default_keymap:
            persistent._ukm_default_keymap = copy.deepcopy(config.keymap)
        if persistent._ukm_user_keymap:
            config.keymap = copy.deepcopy(persistent._ukm_user_keymap)

        if not persistent._ukm_default_joymap:
            persistent._ukm_default_joymap = copy.deepcopy(config.pad_bindings)
        if persistent._ukm_user_joymap:
            config.pad_bindings = copy.deepcopy(persistent._ukm_user_joymap)

    def ukm_save_bindings():
        persistent._ukm_user_keymap = copy.deepcopy(config.keymap)
        persistent._ukm_user_joymap = copy.deepcopy(config.pad_bindings)

    def ukm_reset_bindings():
        config.keymap = copy.deepcopy(persistent._ukm_default_keymap)
        config.pad_bindings = copy.deepcopy(persistent._ukm_default_joymap)

    # Event types.
    UKM_MOUSE_EVENT_TYPES = { pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEWHEEL }
    UKM_KEYBOARD_EVENT_TYPES = { pygame.KEYDOWN, pygame.KEYUP }
    UKM_CONTROLLER_EVENT_TYPES = { rpy.display.core.EVENTNAME }
    UKM_INPUT_EVENT_TYPES = UKM_MOUSE_EVENT_TYPES | UKM_KEYBOARD_EVENT_TYPES | UKM_CONTROLLER_EVENT_TYPES
    UKM_KEYBOARD_MODIFIERS = collections.OrderedDict([
        ('meta', pygame.KMOD_META),
        ('ctrl', pygame.KMOD_CTRL),
        ('alt', pygame.KMOD_ALT),
        ('shift', pygame.KMOD_SHIFT)
    ])

    # Human-readable keymap descriptions.
    ukm_event_descriptions = dict(
        rollback=_('Roll back text'),
        screenshot=_('Take screenshot'),
        toggle_fullscreen=_('Toggle fullscreen'),
        game_menu=_('Menu'),
        text_log=_('Text log'),
        hide_windows=_('Hide UI'),
        quit=_('Quit'),
        iconify=_('Minimize'),
        help=_('Help'),

        rollforward=_('Roll forward text'),
        dismiss=_('Advance text'),
        dismiss_hard_pause=_('Force advance text'),
        toggle_afm=_('Toggle auto-advance'),

        skip=_('Skip text'),
        toggle_skip=_('Toggle skipping text'),

        save_delete=_('Delete save file'),

        developer=_('Developer menu'),
        launch_editor=_('Launch editor'),
        choose_renderer=_('Renderer choice'),
        reload_game=_('Reload game'),
        inspector=_('Style inspector'),

        focus_up=_('Up'),
        focus_down=_('Down'),
        focus_left=_('Left'),
        focus_right=_('Right')
    )

    # Keymap order. None indicates vertical spacing.
    ukm_event_order = [
        'dismiss',
        'rollback',
        'rollforward',
        'toggle_afm',
        'skip',
        'toggle_skip',
        None,

        'hide_windows',
        'screenshot',
        'game_menu',
        'text_log',
        'help',
        'toggle_fullscreen',
        'iconify',
        'quit',
        None,

        'focus_left',
        'focus_right',
        'focus_up',
        'focus_down'
    ]
    if config.developer:
        ukm_event_order.extend([
            None,

            'developer',
            'reload_game',
            'inspector',
            'launch_editor'
        ])

    # Name for keysyms.
    ukm_keysym_names = {
        'EXCLAIM': u'!',
        'QUOTE': u"'",
        'QUOTEDBL': u'"',
        'HASH': u'#',
        'DOLLAR': u'$',
        'AMPERSAND': u'&',
        'LEFTPAREN': u'(',
        'RIGHTPAREN': u')',
        'ASTERISK': u'*',
        'PLUS': u'+',
        'COMMA': u',',
        'MINUS': u'-',
        'PERIOD': u'.',
        'SLASH': u'/',
        'COLON': u':',
        'SEMICOLON': u';',
        'LESS': u'<',
        'EQUALS': u'=',
        'GREATER': u'>',
        'QUESTION': u'?',
        'AT': u'@',
        'LEFTBRACKET': u'[',
        'BACKSLASH': u'\\',
        'RIGHTBRACKET': u']',
        'CARET': u'^',
        'UNDERSCORE': u'_',
        'BACKQUOTE': u'`',
        'UP': _('Up'),
        'LEFT': _('Left'),
        'RIGHT': _('Right'),
        'DOWN': _('Down'),
        'NUMLOCK': _('Num lock'),
        'CAPSLOCK': _('Caps lock'),
        'SCROLLOCK': _('Scroll lock'),
        'LSHIFT': u'Shift',
        'RSHIFT': u'Right shift',
        'LCTRL': _('Ctrl'),
        'RCTRL': _('Right ctrl'),
        'LALT': _('Alt'),
        'RALT': _('Right alt'),
        'LMETA': _('Ctrl') if sys.platform != 'darwin' else _('Cmd'),
        'RMETA': _('Right ctrl') if sys.platform != 'darwin' else _('Cmd'),
        'LGUI': _('Menu') if sys.platform != 'darwin' else _('Cmd'),
        'RGUI': _('Right menu') if sys.platform != 'darwin' else _('Cmd'),
        'LSUPER': _('Win'),
        'RSUPER': _('Win'),
        'EURO': u'€',
        'RETURN': 'Enter',
        'PAGEUP': 'Page up',
        'PAGEDOWN': 'Page down',
        'ESCAPE': 'Esc',
        'DELETE': 'Del'
    }

    ukm_mouse_button_names = {
        '1': 'Left click',
        '2': 'Middle click',
        '3': 'Right click',
        '4': 'Scroll up',
        '5': 'Scroll down'
    }

    ukm_position_names = {
        'pos':  'up',
        'neg':  'down',
        'None': 'neutral'
    }

    ukm_keysym_values = { val: name for name, val in pygame.__dict__.items() if name.startswith('K_') }


    def ukm_binding_to_friendly(name):
        keyname = []
        suffix = ''

        # Modifier keys.
        if name.lower().startswith('repeat_'):
            name = name[len('repeat_'):]
            suffix += ' (held down)'
        if name.lower().startswith('noshift_'):
            name = name[len('noshift_'):]

        while any(name.lower().startswith(meta + '_') for meta in ('super', 'meta', 'ctrl', 'alt', 'shift')):
            meta, name = name.split('_', 1)
            keyname.append(ukm_keysym_names['L' + meta.upper()])

        # Joystick keys.
        if name.startswith('pad_'):
            _, interface, position = name.split('_', 2)
            interface = interface\

            if position in ('pos', 'neg', 'None'):
                interface = interface\
                            .replace('left', 'left stick ')\
                            .replace('right', 'right stick ')
                name = '{} {}'.format(interface.capitalize(), ukm_position_names[position])
                name = name.replace('x down', 'left')\
                           .replace('x up', 'right')\
                           .replace('y down', 'up')\
                           .replace('y up', 'down')
            else:
                interface = interface\
                            .replace('left', 'left ')\
                            .replace('right', 'right ')\
                            .replace('dp', 'd-pad ')\
                            .replace('guide', 'home')
                name = '{}-button'.format(interface.capitalize())

            keyname.append(name)
            return ' + '.join(keyname)

        # Keyboard key name mangling.
        if name.startswith('K_'):
            # K_ENTER, K_ESCAPE...
            name = name[2:]
        if name.startswith('KP'):
            # KP0, KP_DIVIDE...
            name = name[2:].lstrip('_')
            suffix += ' (keypad)'
        if name.startswith('AC_'):
            # AC_BACK, AC_HOME...
            name = name[3:]
            suffix += ' (media)'

        if not name:
            return None

        if len(name) == 1:
            # a, A, 0...
            keyname.append(name.upper() + suffix)
        elif name.startswith('mousedown') or name.startswith('mouseup'):
            # Mouse names.
            _, button = name.split('_', 1)
            keyname.append(ukm_mouse_button_names.get(button, 'Mouse button #{}'.format(button)))
        elif name.startswith('F'):
            # F1, F2...
            keyname.append(name + suffix)
        elif name in ukm_keysym_names:
            # Known keyboard symbols.
            keyname.append(ukm_keysym_names[name] + suffix)
        else:
            # Fallback, simply capitalize the raw name.
            keyname.append(name.capitalize() + suffix)

        return ' + '.join(keyname)

    def ukm_extract_binding(event):
        if event.type in UKM_MOUSE_EVENT_TYPES:
            if event.type != pygame.MOUSEBUTTONUP:
                return (False, None)
            return (False, 'mouseup_{}'.format(event.button))
        elif event.type in UKM_KEYBOARD_EVENT_TYPES:
            if event.type != pygame.KEYDOWN:
                return (False, None)

            base = ukm_keysym_values.get(event.key)
            mods = []
            for name, mod in UKM_KEYBOARD_MODIFIERS.items():
                if event.mod & mod:
                    mods.append(name)

            if base and mods:
                return (False, '_'.join(mods) + '_' + base)
            elif base:
                return (False, base)
            elif mods:
                return (False, '_'.join(mods))
            else:
                return (False, None)
        elif event.type in UKM_CONTROLLER_EVENT_TYPES:
            return (True, event.controller)

    def ukm_get_bindings(command):
        syms = [(sym, ukm_binding_to_friendly(sym), False) for sym in config.keymap.get(command, [])]
        for sym, commands in config.pad_bindings.items():
            if command in commands:
                syms.append((sym, ukm_binding_to_friendly(sym), True))
        return syms

    def ukm_add_binding(event, binding, joy):
        if joy:
            config.pad_bindings.setdefault(binding, [])
            config.pad_bindings[binding].append(event)
        else:
            config.keymap.setdefault(event, [])
            config.keymap[event].append(binding)

        ukm_save_bindings()
        renpy.clear_keymap_cache()
        renpy.restart_interaction()

    def ukm_remove_binding(event, binding, joy):
        if joy:
            if binding in config.pad_bindings and event in config.pad_bindings[binding]:
                config.pad_bindings[binding].remove(event)
        else:
            if event in config.keymap and binding in config.keymap[event]:
                config.keymap[event].remove(binding)

        ukm_save_bindings()
        renpy.clear_keymap_cache()
        renpy.restart_interaction()

    def ukm_reset_all_bindings():
        ukm_reset_bindings()
        ukm_save_bindings()
        renpy.clear_keymap_cache()
        renpy.restart_interaction()

    class KeyBindingGrabBehaviour(Null):
        def __init__(self, target, excludes=None, exclude_displayables=None, **kwargs):
            super(KeyBindingGrabBehaviour, self).__init__(**kwargs)
            self.target = target
            self.excludes = excludes or []
            self.exclude_displayables = exclude_displayables or []

        def event(self, ev, x, y, st):
            # Check event types.
            if ev.type not in UKM_INPUT_EVENT_TYPES:
                return

            # Check excluded events.
            for exclude in self.excludes:
                if renpy.map_event(ev, exclude):
                    return

            # Check for a mouse event in excludes displayables.
            if ev.type in UKM_MOUSE_EVENT_TYPES:
                evx, evy = ev.pos

                for displayable in self.excludes:
                    x, y, width, height = renpy.get_image_bounds(displayable)
                    # Within bounds?
                    if evx >= x and evy >= y and evx <= x + width and evy <= y + height:
                        return

            # Store event and tell Ren'Py to ignore it.
            joy, sym = ukm_extract_binding(ev)
            if sym is not None:
                setattr(store, self.target, (sym, ukm_binding_to_friendly(sym), joy))

            renpy.restart_interaction()
            raise renpy.IgnoreEvent()

    class AddUserKeyBinding(object):
        def __init__(self, command, binding, joy):
            self.command = command
            self.binding = binding
            self.joy = joy

        def __call__(self):
            if self.binding:
                ukm_add_binding(self.command, self.binding, self.joy)

    class RemoveUserKeyBinding(object):
        def __init__(self, command, binding, joy):
            self.command = command
            self.binding = binding
            self.joy = joy

        def __call__(self):
            ukm_remove_binding(self.command, self.binding, self.joy)

    class ResetUserKeyBindings(Action):
        def __call__(self):
            ukm_reset_all_bindings()

    ukm_restore_bindings()
