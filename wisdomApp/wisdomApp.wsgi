#! /usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/wisdomApp/")

from wisdomApp import app as application

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
