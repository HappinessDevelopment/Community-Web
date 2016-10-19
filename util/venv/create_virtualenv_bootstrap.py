# this script generates the virtualenv bootstrap.py for creating and bootstrapping a virtual env
import virtualenv
import os
s = virtualenv.create_bootstrap_script('''
import subprocess
import os
def after_install(options, home_dir):
    if sys.platform == 'win32':
        bin = 'Scripts'
    else:
        bin = 'bin'
    # packages to bootstrap
    pip = join(home_dir, bin, 'pip')
    subprocess.call([pip, 'install', 'django'])
    subprocess.call([pip, 'install', 'djangorestframework'])
''')
open('bootstrap.py','w').write(s)