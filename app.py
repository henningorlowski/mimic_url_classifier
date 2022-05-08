#Flask Server and Request-utilities
from flask import Flask, jsonify, request, render_template, redirect, url_for
#Custom Pipeline functions
from util import filter_numbers, vectorize
#Used ML-Classifier
from sklearn.ensemble import RandomForestClassifier 
#Pickle to import model
import pickle as cPickle
#waitress server for deployment
from waitress import serve

################Start#################
app = Flask(__name__)

#load model
with open('assets/rf_classifier_60percent', 'rb') as fid:
	model = cPickle.load(fid)

#Load Pipeline and ML-Model and use it on the given URL. 
def model_predict(url, model):
	#All numbers become 1 as a simplified NLP-Feature
	url = filter_numbers(url)

	#N-Gram Vectorization with given vectorizer
	url_vec = vectorize(url)

	#prediction of classes "malicios" or "normal"
	pred = model.predict(url_vec)

	#get prediction_confidence / probability for each class
	pred_prob = model.predict_proba(url_vec)
	return pred, pred_prob

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
		pred, prob = model_predict(url, model)

		# Serialize the result and the probabilities for the two classes "malicious" and "normal". The probabilities are multiplied by 100 for improved readability.
		return jsonify({"prediction":str(pred[0]), "probability_malicious":str(round(prob[0][0]*100)), "probability_normal":str(round(prob[0][1]*100))})
	except Exception as e: 
		print(e)
		return e

if __name__ == "__main__":
	#run WSGI deployment server. Listen @port 5000
	serve(app, host='0.0.0.0', port=5000)
	print("Waitress started.. App running.")
	
	#development_server
	#app.run(host='0.0.0.0')
