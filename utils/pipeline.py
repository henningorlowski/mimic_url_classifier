from sklearn.feature_extraction.text import CountVectorizer
import pickle as cPickle

#load url_preprocessing_pipeline
with open('assets/vectorizer_60percent', 'rb') as f: 
	vectorizer=cPickle.load(f)
#load model
with open('assets/rf_classifier_60percent', 'rb') as fid:
	model = cPickle.load(fid)

def model_predict(url):
	"""Load Pipeline and ML-Model and use it to predict the class [maliciour or ok] of the given URL. 

	Args:
		url (str): URL that will be predicted.

	Returns:
		rtype: (str, float)
	"""
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


def filter_numbers(url):
	"""Simplify digits within an URL: [0+9] is returned as 1

	Args:
		url (str): The URL which shall be simplified.

	Returns:
		str: Simplified URL without other numbers than 1.
	"""
	url = [item.replace('0', '1') for item in url]
	url = [item.replace('2', '1') for item in url]
	url = [item.replace('3', '1') for item in url]
	url = [item.replace('4', '1') for item in url]
	url = [item.replace('5', '1') for item in url]
	url = [item.replace('6', '1') for item in url]
	url = [item.replace('7', '1') for item in url]
	url = [item.replace('8', '1') for item in url]
	url = [item.replace('9', '1') for item in url]
	return url

def vectorize(url):
	"""Apply count-vectorization for an URL

	Args:
		url (str): URL that will be vectorized
	Returns:
		np.int64: Numpy-Array with the Count-Vectorized URL.
	"""
	if not isinstance(url,list):
		url = [url]

	url_vec = vectorizer.transform(url)
	return url_vec