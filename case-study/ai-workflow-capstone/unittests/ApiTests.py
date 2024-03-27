#!/usr/bin/env python
"""
Test API
"""

import sys
import os
import unittest
import requests
import re
from ast import literal_eval
import numpy as np

port = 8080

try:
    requests.post(f'http://0.0.0.0:{port}/ping')
    server_available = True
except requests.ConnectionError as e:
    #print(e)
    server_available = False

# test class for the main window function


class ApiTest(unittest.TestCase):
    """
    test the essential functionality
    """

    @unittest.skipUnless(server_available, "local server is not running")
    def test_01_train(self):
        """
        test the train functionality
        """

        request_json = {'mode': 'test'}
        r = requests.post(f'http://0.0.0.0:{port}/train', json=request_json)
        train_complete = re.sub("\W+", "", r.text)
        self.assertEqual(train_complete, 'true')

    @unittest.skipUnless(server_available, "local server is not running")
    def test_02_predict_empty(self):
        """
        ensure appropriate failure types
        """

        # provide no data at all
        r = requests.post(f'http://0.0.0.0:{port}/predict')
        self.assertEqual(re.sub('\n|"', '', r.text), "[]")

        # provide improperly formatted data
        r = requests.post(
            f'http://0.0.0.0:{port}/predict', json={"key": "value"})
        self.assertEqual(re.sub('\n|"', '', r.text), "[]")

    @unittest.skipUnless(server_available, "local server is not running")
    def test_03_predict(self):
        """
        test the predict functionality
        """

        query_data = {'country': 'united_kingdom',
                      'year': '2019',
                      'month': '06',
                      'day': '05'
                      }

        request_json = {'query': query_data,
                        'mode': 'test'}

        r = requests.post(
            f'http://0.0.0.0:{port}/predict', json=request_json)
        print(r.text)
        response = literal_eval(r.text)

        for p in response['united_kingdom']['y_pred']:
            self.assertTrue(p is not None)

    @unittest.skipUnless(server_available, "local server is not running")
    def test_04_predict_all(self):
        """
        test the predict functionality
        """
        query_data = {'country': 'all',
                      'year': '2017',
                      'month': '11',
                      'day': '13'
                      }

        request_json = {'query': query_data,
                        'mode': 'test'}

        r = requests.post(
            f'http://0.0.0.0:{port}/predict', json=request_json)
        print(r.text)
        response = literal_eval(r.text)

        for p in ['united_kingdom', 'portugal']:
            self.assertTrue(response[p]['y_pred'] is not None)

    @unittest.skipUnless(server_available, "local server is not running")
    def test_05_predict_multiple(self):
        """
        test the predict functionality
        """
        query_data = {'country': 'united_kingdom,portugal',
                      'year': '2019',
                      'month': '06',
                      'day': '05'
                      }

        request_json = {'query': query_data,
                        'mode': 'test'}

        r = requests.post(
            f'http://0.0.0.0:{port}/predict', json=request_json)
        print(r.text)
        response = literal_eval(r.text)

        for p in ['united_kingdom', 'portugal']:
            self.assertTrue(response[p]['y_pred'] is not None)

    @unittest.skipUnless(server_available, "local server is not running")
    def test_06_logs(self):
        """
        test the log functionality
        """

        file_name = 'unittests-train-2020-6.log'
        r = requests.get(f'http://0.0.0.0:{port}/logs/{file_name}')

        with open(file_name, 'w') as f:
            f.write(r.content)

        self.assertTrue(os.path.exists(file_name))

        if os.path.exists(file_name):
            os.remove(file_name)


# Run the tests
if __name__ == '__main__':
    unittest.main(failfast=True)