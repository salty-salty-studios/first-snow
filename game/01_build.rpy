init -1 python hide:
    # Distributions.
    build.directory_name = "FirstSnow"
    build.executable_name = "First Snow"
    build.include_update = False
    build.itch_project = 'salty-salty-studios/first-snow'

    # What not to pack.
    build.classify('README.md', None)
    build.classify('errors.txt', None)
    build.classify('log.txt', None)
    build.classify('traceback.txt', None)
    build.classify('**-e', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/.DS_Store', None)
    build.classify('**.rpy', None)
    build.classify('game/01_build.rpyc', None)  # VIRTUAL SELF
    build.classify('game/saves/**', None)
    build.classify('patches/**', None)
    build.classify('installer/**', None)
    if not config.developer and not config.testing:
        build.classify('game/lib/renedit/**', None)

    # Need this outside the archives.
    build.classify('game/presplash.png', 'all')
    build.classify('game/ui/icon*', 'all')

    # What to pack as DLC.
    for dlc in store.dlc_packages:
        build.archive('dlc_' + dlc, 'all')
        build.classify('game/dlc/' + dlc + '/**', 'dlc_' + dlc)

    # What to pack as data.
    build.archive('resources', 'all')
    build.classify('game/bgs/**', 'resources')
    build.classify('game/cgs/**', 'resources')
    build.classify('game/music/**', 'resources')
    build.classify('game/sfx/**', 'resources')
    build.classify('game/sprites/**', 'resources')
    build.classify('game/sprites-static/**', 'resources')
    build.classify('game/ui/**', 'resources')
    build.classify('game/voice/**', 'resources')
    build.classify('game/vfx/**', 'resources')

    # What to pack as the story.
    build.archive('story', 'all')
    build.classify('game/scripts/**', 'story')

    # What to pack as code.
    build.archive('code', 'all')
    build.classify('game/**.rpyb', 'code')
    build.classify('game/**.rpyc', 'code')
    build.classify('game/lib/**', 'code')
