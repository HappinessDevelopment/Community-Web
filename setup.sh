alias python='python3'

pip install virtualenv
# create clean virtual environment
python -m venv .venv

# activate the environment
source .venv/bin/activate

# install pip
easy_install pip

# install from requirements.txt (currently only django and djangorestframework)
echo "installing requirements..."
pip install -r requirements.txt

deactivate 

