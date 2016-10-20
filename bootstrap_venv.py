# this script executes the virtualenv bootstrapping script.  Destination dir is projectroot/.venv
# requires python>=3.3
import os
import platform
import subprocess

venv_name = '.venv'
pip_ver = 'pip'
if platform.system() == 'Windows':
    os.system('python -m venv ' + venv_name)
    os.system(venv_name + '\\Scripts\\activate.bat')
    bin = 'Scripts'
else:
    if os.system('pyvenv ' + venv_name) != 0:
        os.system('python3.4 -m venv ' + venv_name)
        pip_ver = 'pip3.4'
    bin = 'bin'

print('installing packages')

pip = os.path.join(os.getcwd(), venv_name, bin, 'pip')
subprocess.call([pip, 'install', '-r', 'requirements.txt'])
