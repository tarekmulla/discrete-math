"""import the webapp module"""

import os
import sys

webapp_module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(webapp_module)
sys.path.append(webapp_module)
