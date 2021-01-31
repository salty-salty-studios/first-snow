## Get git version.
init python:
    def git_version():
        from os import path

        if hasattr(store, 'git_revision'):
            return store.git_revision

        git_dir = path.join(config.gamedir, '..', '.git')
        if path.isdir(git_dir):
            head = path.join(git_dir, 'HEAD')
            with open(head, 'r') as f:
                parts = f.read().strip().split()

            if parts[0] == 'ref:':
                ref = path.join(git_dir, parts[1])
                with open(ref, 'r') as f:
                    rev = f.read().strip()
            else:
                rev = parts[0]

            return rev[:7]

        return '[unknown]'
