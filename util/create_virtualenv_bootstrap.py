import virtualenv
s = virtualenv.create_bootstrap_script('''
import subprocess
def after_install(options, home_dir):
  subprocess.call(['pip', 'install', 'django'])
  subprocess.call(['pip', 'install', 'djangorestframework'])
''')
open('bootstrap.py','w').write(s)