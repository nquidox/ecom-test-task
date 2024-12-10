import requests
import unittest


class TestPostRequests(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:9000/get_form"

    # Full data tests
    def test_post_request_1(self):
        data = {
            "name": "Ivan",
        }
        expected_response = b"username_only"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_2(self):
        data = {
            "name": "Ivan",
            "date": "1980-07-24",
            "email": "john@mail.box",
            "phone": "+71234567890"
        }
        expected_response = b"user_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_3(self):
        data = {
            "name": "Ivan",
            "date": "1980-07-24",
            "email": "john@mail.box",
            "phone": "+79876543210",
            "address": "Saratov"
        }
        expected_response = b"user_more_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_4(self):
        data = {
            "name": "Ivan",
            "date": "1980-07-24",
            "email": "john@mail.box",
            "phone": "+79876543210",
            "address": "Saratov",
            "age": 20
        }
        expected_response = b"user_maximum_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    # Partial data tests

    def test_post_request_5(self):
        data = {
            "name": "Ivan",
            "date": "1980-07-24",
            "email": "john@mail.box",
            "phone": "+71234567890"
        }
        expected_response = b"user_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_6(self):
        data = {
            "name": "Ivan",
            "email": "john@mail.box",
            "phone": "+71234567890"
        }
        expected_response = b"user_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_7(self):
        data = {
            "name": "Ivan",
            "date": "1980-07-24",
            "phone": "+71234567890"
        }
        expected_response = b"user_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_8(self):
        data = {
            "phone": "+71234567890"
        }
        expected_response = b"user_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_9(self):
        data = {
            "age": 20
        }
        expected_response = b"user_maximum_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    def test_post_request_10(self):
        data = {
            "address": "Saratov"
        }
        expected_response = b"user_more_info"

        response = requests.post(self.url, json=data)
        self.assertEqual(response.content, expected_response)

    # No template match tests

    def test_post_request_11(self):
        data = {
            "Surname": "Ivanov",
            "Married": "true",
        }
        expected_response = {"Surname": "string", "Married": "boolean"}

        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_post_request_12(self):
        data = {
            "Children": {"Son": "Denis", "Daughter": "Alisa"},
            "JustDigits": [1, 2, 3],
            "Pi": 3.14,
            "PiString": "3.14",
        }
        expected_response = {"Children": "object", "JustDigits": "array", "Pi": "number", "PiString": "string"}

        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    # Empty body request

    def test_post_request_empty(self):
        data = {}
        expected_response = {}

        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)


if __name__ == "__main__":
    unittest.main()
