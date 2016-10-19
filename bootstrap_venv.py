# this script executes the virtualenv bootstrapping script.  Destination dir is projectroot/.venv
import os

os.system(os.path.join(os.getcwd(), "util/venv/bootstrap.py") + " .venv")