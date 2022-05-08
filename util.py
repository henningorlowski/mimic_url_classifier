from sklearn.feature_extraction.text import CountVectorizer
import pickle as cPickle

#load url_preprocessing_pipeline
with open('assets/vectorizer_60percent', 'rb') as f:
	vectorizer=cPickle.load(f)

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
