# create blueprint in wisdomApp/__init__.py
from flask import Blueprint

wisdomApp = Blueprint('wisdomApp', __name__)
import views

# create blueprint in reviewApp/__init__.py
from flask import Blueprint

reviewApp = Blueprint('reviewApp', __name__)
import views

# add views (endpoints) in wisdomApp/views.py
from . import wisdomApp

@wisdomApp.route('/')
def Home():
    return 'Home'

# add views (endpoints) in reviewApp/views.py
from . import reviewApp

@chat.route('/blog')
def blog():
    return 'blog'

# register blueprint and start flask app
from flask import Flask
from expense import expense
from budget import budget

app = Flask(__name__)
app.register_blueprint(wisdomApp)
app.register_blueprint(reviewApp)
app.run(debug=True)
