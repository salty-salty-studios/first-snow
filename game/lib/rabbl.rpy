# rabbl.rpy
# The RABBL script manager.
# RABBL: Righteous Alternative to Blisteringly Bad Logic.
# Copyright (C) 2012-2014 Shiz.

python early:
    import renpy.exports as renpy
    import renpy.store as store
    import renpy.game as game


    # The script manager.
    class RABBL(renpy.python.NoRollback):
        def __init__(self):
            self.current_language = game.persistent.language or config.rabbl_default_language
            self.seen_scenes = set()
            self.act_titles = {}
            self.scene_titles = {}
            self.allow_explicit = True

        def get_act_title(self, name):
            return self.act_titles.get(name, str(name))
    
        def get_title(self, name):
            return self.scene_titles.get(name, self.scene_titles.get(name.split('_', 1)[0]))

        def get_label(self, name, name_evaled=None, explicit=False, independent=False, menu=False):
            if explicit and not self.allow_explicit:
                return (
                    self.get_label(None, name_evaled + '_clean', False, False) or
                    self.get_label(None, 'special_explicit', False, False)
                )

            if independent:
                l = ('choice' if menu else 'scene') + '_' + name_evaled
            else:
                l = ('choice' if menu else 'scene') + '_' + name_evaled + '_' + self.current_language
            return l if renpy.has_label(l) else None

        def in_playthrough(self):
            return not game.context().init_phase and not main_menu

        def in_replay(self):
            return self.in_playthrough() and store.rabbl_playthrough.oneshot

        # Change language.
        def change_language(self, name):
            game.persistent.language = name
            self.current_language = name
            # Re-initialize script.
            renpy.call('script_init')

        # Compile scene name.
        def eval_scene(self, info):
            try:
                info['name_evaled'] = eval(info['name'])
            except:
                if 'name_evaled' not in info:
                    raise

        def seen_scene(self, scene):
            return scene in self.seen_scenes

        # Perform scene statement.
        def perform_parse(self, lexer):
            label = lexer.simple_expression()
            independent = False
            explicit = False
            while not lexer.eol():
                if lexer.keyword('independent'):
                    independent = True
                elif lexer.keyword('explicit'):
                    explicit = True
                else:
                    renpy.error('unexpected keyword {0}'.format(lexer.word()))

            return { 'name': label, 'independent': independent, 'explicit': explicit }

        def perform_predict(self, info):
            return []

        def perform_lint(self, info):
            try:
                self.eval_scene(info)
                label = self.get_label(**info)
            except:
                return

            if not label or not renpy.has_label(label):
                renpy.error('Unknown script label "{0}" called.'.format(info['name']))

        def perform_next(self, info):
            return None

        def perform(self, info):
            self.eval_scene(info)
            label = self.get_label(**info)

            # Hacky way of determining if it's a proper scene.
            proper_scene = hasattr(store, 'scene_titles') and info['name_evaled'] in store.scene_titles
            skipping_scene = False

            if False and proper_scene and not self.in_replay() and store.rabbl_playthrough.seen_scene(info['name_evaled']):
                name = self.get_title(info['name_evaled'])
                skipping_scene = renpy.call_screen('yesno_prompt', message=name + '\nSkip scene?', yes_action=Return(True), no_action=Return(False))

            self.seen_scenes.add(info['name_evaled'])
            if self.in_playthrough():
                store.rabbl_playthrough.current_scene = info['name_evaled']
                store.rabbl_playthrough.seen_scenes.add(info['name_evaled'])

            if not skipping_scene:
                renpy.call(label)

        # Perform choose statement.
        def choose_parse(self, lexer):
            label = lexer.simple_expression()

            explicit = False
            while not lexer.eol():
                if lexer.keyword('explicit'):
                    explicit = True
                else:
                    renpy.error('unexpected keyword {0}'.format(lexer.word()))

            return { 'name': label, 'explicit': explicit }

        def choose_predict(self, info):
             return []

        def choose_lint(self, info):
            info['menu'] = True
            self.eval_scene(info)
            label = self.get_label(**info)

            if not label or not renpy.has_label(label):
                renpy.error('Unknown script label "{0}" called.'.format(info['name']))

        def choose_next(self, info):
            return None

        def choose(self, info):
            if info['explicit'] and not self.allow_explicit:
                return None

            self.eval_scene(info)
            if not self.in_playthrough() or info['name_evaled'] not in store.rabbl_playthrough.menu_choices:
                info['menu'] = True
                label = self.get_label(**info)
                renpy.call('rabbl_choice_trampoline', info['name_evaled'], label)
            else:
                store.choice = store.rabbl_playthrough.menu_choices[info['name_evaled']]

        # Set correct values after a choice.
        def after_choose(self, name):
            if self.in_playthrough():
                store.rabbl_playthrough.menu_choices[name] = store._return
            store.choice = store._return
            store._return = None

        # Setup.
        @classmethod
        def setup(cls):
            config.rabbl_default_language = "en"

            store.rabbl = cls()
            renpy.statements.register('perform',
                parse=store.rabbl.perform_parse,
                execute=store.rabbl.perform,
                predict=store.rabbl.perform_predict,
                lint=store.rabbl.perform_lint,
                next=store.rabbl.perform_next
            )
            renpy.statements.register('choose',
                parse=store.rabbl.choose_parse,
                execute=store.rabbl.choose,
                predict=store.rabbl.choose_predict,
                lint=store.rabbl.choose_lint,
                next=store.rabbl.choose_next
            )

        @classmethod
        def setup_init(cls):
            if not persistent.rabbl_seen_scenes:
                persistent.rabbl_seen_scenes = set()
            store.rabbl.seen_scenes = persistent.rabbl_seen_scenes


    class RABBLPlaythrough(renpy.python.NoRollback):
        def __init__(self):
            self.menu_choices = {}
            self.seen_scenes = persistent.rabbl_seen_scenes
            self.current_scene = None
            self.oneshot = False

        def seen_scene(self, scene):
            return scene in self.seen_scenes

    RABBL.setup()

init -999 python:
    RABBL.setup_init()

init -25 python hide:
    # Register save game callback.
    def store_scene(info):
        if store.rabbl_playthrough:
            info['scene'] = store.rabbl_playthrough.current_scene
        info['playtime'] = renpy.get_game_runtime()
        return info
    config.save_json_callbacks.append(store_scene)

init -25 python:
    # Register PlayScene() action.
    class PlayScene(Action):
        def __init__(self, scene):
            self.scene = scene

        def __call__(self):
            persistent._rabbl_scene = self.scene
            renpy.run(Start())

init -10:
    call script_init

init 1 python:
    # Define characters.
    # The characters dict is defined in scripts/init.rpy,
    # the names in scripts/<lang>/init.rpy
    for short, meta in characters.iteritems():
        name = character_names[short]
        globals()[short] = Character(name, image=short, voice_tag=short, **meta)
