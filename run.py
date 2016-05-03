# Runs web app
from application import app
import sys

if __name__ == '__main__':

    port = 8080

    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        app.debug = True
        app.run(port=port)
    else:
        app.run(port=port)
