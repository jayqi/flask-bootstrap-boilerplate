from flask import Flask
import os
from application.paths import *

def initialize_application():
    app = Flask('application')
    
    # Startup stuff
    pass

    return app

app = initialize_application()

from application.controllers import *
