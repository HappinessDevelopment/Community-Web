# this script generates the virtualenv bootstrap.py for creating and bootstrapping a virtual env
import virtualenv
import os
s = virtualenv.create_bootstrap_script('''
import subprocess
def after_install(options, home_dir=os.path.join(os.pardir, 'venv')):
  # packages to bootstrap
  subprocess.call(['pip', 'install', 'django'])
  subprocess.call(['pip', 'install', 'djangorestframework'])
''')
open('bootstrap.py','w').write(s)