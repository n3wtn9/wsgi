# http://www.fabfile.org/

from datetime import datetime

from fabric.api import *


def setup():
    """creates the virtual environments and installs the requirements"""
    local('python virtualenv.py env')
    _virtualenv('pip install -r requirements.txt')

def _virtualenv(command, *args):
  return local('. env/bin/activate&& ' + command + ' ' + ' '.join(args), capture=False)

