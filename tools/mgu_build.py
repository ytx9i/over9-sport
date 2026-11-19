#!/usr/bin/env python3
"""
mgu_build.py - the MGU Store's build entry (mgu-repo.json). The OVER 9 apps (over9, over9_reaction,
over9_scenes) build with their own copy of the app kit in kit-o9/; Cluster Themes and HUD Widgets with kit/.
Usage is the kits' own: python3 tools/mgu_build.py <app id> [build.py options].
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
O9 = {'over9', 'over9_reaction', 'over9_scenes'}


def main():
    app = next((a for a in sys.argv[1:] if not a.startswith('-')), '')
    kit = 'kit-o9' if app in O9 else 'kit'
    build = os.path.join(ROOT, kit, 'tools', 'build.py')
    sys.exit(subprocess.call([sys.executable, build] + sys.argv[1:], cwd=ROOT))


if __name__ == '__main__':
    main()
