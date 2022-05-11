import unittest
from unittest import result
import numpy as np
from app import app
import requests
from utils.pipeline import filter_numbers, model_predict, vectorize

class TestBase(unittest.TestCase):
    #Reference started app
    def setUp(self):
        self.app = app.test_client()
        return app

    #Tear down after test
    def tearDown(self):
        pass

# -----------------  Tests -------------------------

#Test GET HTML response
class TestBasicHTML(TestBase):
    #Test if HTML is properly shown by searching for the word malicious in the description
    def test_HTML(self):
        temp_response = self.app.get("/")
        self.assertIn("malicious",temp_response.data.decode("utf-8"))

    #Test Basic Response from Mainpage. Status Code 200 is normal
    def test_mainpage(self):
        temp_response = self.app.get("/")
        self.assertEqual(temp_response.status_code, 200) 

class TestAPI(TestBase):
    #Test Basic Response from API. Status Code 200 is normal
    def test_APIResponse(self):
        temp_response = self.app.post("/prediction", json={"url" : "google.de"})
        self.assertEqual(temp_response.status_code, 200) 

    #Test prediction functionality for google.de = normal URL 
    def test_normal_prediction(self):
        temp_response = self.app.post("/prediction", json={"url" : "google.de"})
        self.assertIn('"prediction":"secure"', temp_response.data.decode("utf-8")) 
           
    #Test prediction functionality for pool.bitcoin.ml = malicious URL
    def test_malicious_prediction(self):
        temp_response = self.app.post("/prediction", json={"url" : "pool.bitcoin.ml"})
        self.assertIn('"prediction":"malicious"', temp_response.data.decode("utf-8")) 
        temp_response = self.app.post("/prediction", json={"url" : "facebook.de"})    
        self.assertNotIn('"prediction":"malicious"', temp_response.data.decode("utf-8"))     


#Test individual functions
class Test_Functions(TestBase):
    
    #Test numberfiltering
    def test_filter_number(self):
        result = filter_numbers(["testsite3123.de"])[0]
        expected = "testsite1111.de"
        self.assertEqual(result,expected)

    #Test malicious prediction 
    def test_model_predict_malicious(self):
        #test case with array enclosure
        result_predictions , prob = model_predict(["pool.bitcoin.ml"])
        expected_predictions = 0
        self.assertEqual(result_predictions,expected_predictions)

    #Test non-malicious prediction
    def test_model_predict_non_malicious(self):
        #test case without array enclosure
        result_predictions , prob = model_predict("google.de")
        expected_predictions = 1
        self.assertEqual(result_predictions,expected_predictions)

    #Test count vectorization of urls
    def test_vectorizer(self):
        #normal test case for vectorization
        result = vectorize(["google.de"]).toarray()
        test_array = np.zeros((1,726))
        test_array[0,0] = 10
        test_array[0,11] = 1
        test_array[0,26] = 1
        test_array[0,27] = 1
        test_array[0,195] = 1
        test_array[0,203] = 1
        test_array[0,217] = 2
        test_array[0,219] = 1
        test_array[0,283] = 2
        test_array[0,292] = 1
        test_array[0,294] = 1
        test_array[0,381] = 1
        test_array[0,388] = 1
        test_array[0,389] = 1
        test_array[0,472] = 2
        test_array[0,483] = 1
        test_array[0,500] = 1
        self.assertIsNone(np.testing.assert_array_equal(result,test_array))  
        #empty string vectorization without array enclosure
        result = vectorize("").toarray()
        test_array = np.zeros((1,726))
        test_array[0,0] = 1
        self.assertIsNone(np.testing.assert_array_equal(result,test_array)) 


if __name__ == "__main__":
    unittest.main()