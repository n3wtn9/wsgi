import sys

activate_this = '/var/local/apps/d6/wip-demo/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/var/local/apps/d6/wip-demo/app')

from hello import app as application
