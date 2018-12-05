from flask import Flask, request, render_template, jsonify
import time

app = Flask(__name__)

name = 'John'
lastname = 'Doe'
zip_code = '0000'
timestamp = str(time.time())

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

@app.route('/data')
def get_data():
	data = dict(name=get_name(), lastname=get_lastname(), zip_code=get_zip(), timestamp=get_timestamp())
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
	return render_template('lastname.html')
	#return render_template('thanks.html')

@app.route('/1', methods=['POST'])
def post_lastname_page():
	global timestamp
	timestamp = time.time()

	global lastname
	lastname = request.form['lastname']
	print(lastname)
	return render_template('zip_code.html')

@app.route('/2', methods=['POST'])
def post_zip_code_page():
	global timestamp
	timestamp = time.time()

	global zip_code
	zip_code = request.form['zip_code']
	print(zip_code)
	return render_template('thanks.html', name=get_name())

#@app.route('/user/<username>')
#@app.route('/login', methods=['GET', 'POST'])

