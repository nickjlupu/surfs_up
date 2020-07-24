# import dependencies
from flask import Flask

# create a new Flask app instance
app = Flask(__name__)

# create our first route
@app.route('/')
def hello_world():
	return 'Hola mundo'

