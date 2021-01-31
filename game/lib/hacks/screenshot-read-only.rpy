# _screenshot variant that tries multiple directories before giving up,
# in case the usre has no permission to write to the game directory
init -1500 python:
    # Called to make a screenshot happen.
    def _screenshot():
        import os.path
        import os
        import __main__

        # Primary directory: the game.
        paths = [config.renpy_base]
        if renpy.macapp:
            paths = []

        # Secondary directories: the destkop.
        for p in [os.path.expanduser(b"~/Desktop")]:
            if os.path.isdir(p):
                paths.append(p)

        for dest in paths:
            # Try to pick a filename.
            i = 1
            while True:
                fn = os.path.join(dest, config.screenshot_pattern % i)
                if not os.path.exists(fn):
                    break
                i += 1

            try:
                dn = os.path.dirname(fn)
                if not os.path.exists(dn):
                    os.makedirs(dn)
            except:
                pass

            try:
                if renpy.screenshot(fn):
                    break
            except:
                import traceback
                traceback.print_exc()
        else:
            renpy.notify(__("Failed to save screenshot as %s.") % ','.join(fn))
            return

        if config.screenshot_callback is not None:
            config.screenshot_callback(fn)
