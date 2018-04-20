from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	user = 'Andrew K.'
	repeat = "dont forget to be awesome"
	return 	render_template('index.html', user = user)

