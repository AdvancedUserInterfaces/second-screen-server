from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

import time

app = Flask(__name__)
CORS(app)

name = 'John'
lastname = 'Doe'
zip_code = '0000'
timestamp = str(time.time())
state = -1

@app.route('/name')
def get_name():
	return name

@app.route('/lastname')
def get_lastname():
	return lastname

@app.route('/zip')
def get_zip():
	return zip_code

@app.route('/timestamp')
def get_timestamp():
	return timestamp

@app.route('/state')
def get_state():
	return str(state)

@app.route('/reset')
def reset_state():
	global state
	state = -1

	global name
	name = 'Jane'

	global lastname
	lastname = 'Doe'

	global zip_code
	zip_code = '0000'

	global timestamp
	timestamp = str(time.time())

	return get_data()

@app.route('/data')
def get_data():
	data = dict(name=get_name(), lastname=get_lastname(), zip_code=get_zip(), timestamp=get_timestamp(), state=get_state())
	return jsonify(data)

###########################################################

@app.route('/', methods=['GET'])
def get_landing_page():
	global timestamp
	timestamp = time.time()

	return render_template('index.html')

@app.route('/', methods=['POST'])
def post_landing_page():
	global timestamp
	timestamp = time.time()

	global name
	name = request.form['name']
	print(name)

	global state
	state = 0

	return render_template('lastname.html')
	#return render_template('thanks.html')

@app.route('/1', methods=['POST'])
def post_lastname_page():
	global timestamp
	timestamp = time.time()

	global lastname
	lastname = request.form['lastname']
	print(lastname)

	global state
	state = 1

	return render_template('zip_code.html')

@app.route('/2', methods=['POST'])
def post_zip_code_page():
	global timestamp
	timestamp = time.time()

	global zip_code
	zip_code = request.form['zip_code']
	print(zip_code)

	global state
	state = 2

	return render_template('thanks.html', name=get_name())

#@app.route('/user/<username>')
#@app.route('/login', methods=['GET', 'POST'])

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)