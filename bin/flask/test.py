import unittest
from flask import Flask
from flask.testing import FlaskClient
import json


from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_process(self):
        input_data = "資料科學"
        #expected_output = "HELLO"

        # * 接 /process 我也不知道他怎麼過去的 但他過去app.py了
        response = self.app.post('/process', data=input_data)
        # * 查回應
        data = response.data.decode('utf-8')
        response_str = str(data)
        
        # ! 下面這行可把回應轉為中文的list
        response_list = json.loads(response_str)
        print(response_list)
        #self.assertEqual(response_list, expected_output)

if __name__ == '__main__':
    unittest.main()
