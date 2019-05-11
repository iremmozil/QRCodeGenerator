from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)

 
@app.route('/')
def home():
	values = []
	POST_QR = ""
	color_qr = "000"
	background_qr = "fff"
	values.append(POST_QR)
	values.append(color_qr)
	values.append(background_qr)
	if not session.get('generate_qr'):
		return render_template('qrGenerator.html', values=values)
	else:
		return "Error"
 
@app.route('/generate', methods=['POST'])
def do_generate():

	if request.form['text']:
		values = []
		POST_QR = request.form['text']
		color_qr = request.form['dropDownList']
		background_qr = request.form['dropDownList2']
		values.append(POST_QR)
		values.append(color_qr)
		values.append(background_qr)

		return render_template("qrGenerator.html", values = values)
	else:
		values = []
		POST_QR = ""
		color_qr = "000"
		background_qr = "fff"
		values.append(POST_QR)
		values.append(color_qr)
		values.append(background_qr)
		return render_template("qrGenerator.html", values = values)
 
if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=4000)