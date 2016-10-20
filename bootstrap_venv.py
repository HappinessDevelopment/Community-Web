# this script executes the virtualenv bootstrapping script.  Destination dir is projectroot/.venv
# requires python>=3.3
import os
import platform
import subprocess

venv_name = '.venv'

if platform.system() == 'Windows':
    os.system('python -m venv ' + venv_name)
    os.system(venv_name + '\\Scripts\\activate.bat')
    bin = 'Scripts'
else:
    os.system('pyvenv ' + venv_name)
    os.system('source ' + venv_name + '/bin/activate')
    bin = 'bin'

print('installing packages')

pip_packages = ['django==1.10.2', 'djangorestframework==3.4.7']
pip = os.path.join(os.getcwd(), venv_name, bin, 'pip')
for package in pip_packages:
    subprocess.call([pip, 'install', package])
