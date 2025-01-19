from flask import Flask
from flask import make_response, redirect
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.post("/on")
def light_on():
	print("light on!")
	return make_response('', 200)

@app.post("/off")
def light_off():
	print("light off!")
	return make_response('', 200)
