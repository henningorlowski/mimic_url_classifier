from sklearn.feature_extraction.text import CountVectorizer
import pickle as cPickle
from pathlib import Path
parent = Path(__file__).resolve().parents[1]

#load url_preprocessing_pipeline
with open(parent / 'assets/vectorizer_60percent', 'rb') as f:
	vectorizer=cPickle.load(f)

#load model
with open(parent / 'assets/rf_classifier_60percent', 'rb') as fid:
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

#simplify digits within the url
def filter_numbers(data):
	data = [item.replace('0', '1') for item in data]
	data = [item.replace('2', '1') for item in data]
	data = [item.replace('3', '1') for item in data]
	data = [item.replace('4', '1') for item in data]
	data = [item.replace('5', '1') for item in data]
	data = [item.replace('6', '1') for item in data]
	data = [item.replace('7', '1') for item in data]
	data = [item.replace('8', '1') for item in data]
	data = [item.replace('9', '1') for item in data]
	return data

#apply count-vectorizer for url
def vectorize(url):
	url_vec = vectorizer.transform(url)
	return url_vec
