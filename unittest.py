import unittest
import json
from flask import Flask
from app import home, predict, predict_api

app = Flask(__name__)

class PredictionUnitTests(unittest.TestCase):

    tester = None

    def __init__(self, *args, **kwargs):
        super(PredictionUnitTests, self).__init__(*args, **kwargs)
        global tester
        tester = app.test_client()

    def test_classify_single(self):
        response = tester.post(
            '/predict'
            
        )
        
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()