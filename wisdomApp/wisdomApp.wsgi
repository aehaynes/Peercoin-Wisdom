#! /usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/wisdomApp/")

from wisdomApp import app as application
application.secret_key = '71472D2BB01783E5C6D65667E7F0B066AC7D343CF6129432169E3B99E63076AF'

if __name__ == '__main__':
    app.run(debug=True)
