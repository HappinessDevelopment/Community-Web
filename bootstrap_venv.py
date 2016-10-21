# this script executes the virtualenv bootstrapping script.  Destination dir is projectroot/.venv
# requires python>=3.3
import os
import platform
import subprocess
import sys

req_version = (3,4)
cur_version = sys.version_info
if cur_version < req_version:
	print('python >= 3.4 required')
	exit()
venv_name = '.venv'
pip_ver = 'pip'
if os.system('python -m venv ' + venv_name) != 0:
	os.system('python3.4 -m venv ' + venv_name)
	pip_ver = 'pip3.4'
if platform.system() == 'Windows':
    os.system(venv_name + '\\Scripts\\activate.bat')
    bin = 'Scripts'
else:
    bin = 'bin'

print('installing packages')

pip = os.path.join(os.getcwd(), venv_name, bin, pip_ver)
subprocess.call([pip, 'install', '-r', 'requirements.txt'])
