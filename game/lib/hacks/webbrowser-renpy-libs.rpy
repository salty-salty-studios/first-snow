# hotfix to prevent Ren'Py library environment from messing with running web browsers on Linux
init python:
    import contextlib
    import os

    @contextlib.contextmanager
    def without_renpy_libs():
        libpath = os.getenv('LD_LIBRARY_PATH')
        gamedir = os.path.dirname(config.gamedir)
        if libpath:
            paths = libpath.split(os.pathsep)
            filtered_paths = [p for p in paths if not p.startswith(gamedir)]
            os.environ['LD_LIBRARY_PATH'] = os.pathsep.join(filtered_paths)
        yield
        if libpath:
            os.environ['LD_LIBRARY_PATH'] = libpath

    @renpy.pure
    class OpenURL(Action):
        def __init__(self, url):
            self.url = url

        def __call__(self):
            try:
                with without_renpy_libs():
                    import webbrowser
                    webbrowser.open_new(self.url)
            except:
                pass
