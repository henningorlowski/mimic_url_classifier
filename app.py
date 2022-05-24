from flask import Flask, jsonify, request, render_template, redirect, url_for
from utils.pipeline import filter_numbers, vectorize, model_predict
from sklearn.ensemble import RandomForestClassifier 
import pickle as cPickle
from waitress import serve

#Start Flask Server
app = Flask(__name__)

@app.route('/')
def index():
    # Main page
	return render_template('index.html')	

@app.route("/prediction", methods=["POST"])
def predict():
	try:
		#Retrieve URL from post request
		url = [request.json['url']]
		
		# Make prediction
		pred, prob = model_predict(url)
		pred_str = "secure" if pred == 1 else "malicious"

		# Serialize the result and the probabilities for the two classes "malicious" and "normal". The probabilities are multiplied by 100 to match the % notation
		# which simplifies the readability.
		return jsonify({"prediction":pred_str, "probability_malicious":str(round(prob[0]*100)), "probability_normal":str(round(prob[1]*100))})
	except Exception as e: 
		print(e)
		return e

if __name__ == "__main__":
	print("Waitress started.. App running.")
	#run WSGI deployment server. Listen @port 5000
	serve(app, host='0.0.0.0', port=5000)
	print("App closed.")