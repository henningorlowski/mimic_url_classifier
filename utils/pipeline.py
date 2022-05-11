from sklearn.feature_extraction.text import CountVectorizer
import pickle as cPickle

#load url_preprocessing_pipeline
with open('assets/vectorizer_60percent', 'rb') as f:
	vectorizer=cPickle.load(f)

#load model
with open('assets/rf_classifier_60percent', 'rb') as fid:
	model = cPickle.load(fid)

#Load Pipeline and ML-Model and use it on the given URL. 
def model_predict(url):

	if not isinstance(url,list):
		url = [url]

	#All numbers become 1 as a simplified NLP-Feature
	url = filter_numbers(url)

	#N-Gram Vectorization with trained vectorizer
	url_vec = vectorize(url)

	#prediction of classes "malicious" or "normal"
	pred = model.predict(url_vec)[0]
	
	#get prediction_confidence / probability for each class
	pred_prob = model.predict_proba(url_vec)[0]
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
	if not isinstance(url,list):
		url = [url]

	url_vec = vectorizer.transform(url)
	return url_vec
