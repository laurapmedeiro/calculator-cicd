import http.client
import os
import unittest
from urllib.request import urlopen
import requests

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # Test API REST: add operation
    def test_api_add_timeout(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_add_ok_request(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = requests.get(url)
        self.assertEqual(
            response.status_code, http.client.OK, f"4"
        )
    
    def test_api_add_bad_request(self):
        url = f"{BASE_URL}/calc/add/2/s"
        response = requests.get(url)
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)

     # Test API REST: substract operation
    def test_api_substract_timeout(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_add_ok_request(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = requests.get(url)
        self.assertEqual(
            response.status_code, http.client.OK, f"0"
        )
    
    def test_api_substract_bad_request(self):
        url = f"{BASE_URL}/calc/substract/2/s"
        response = requests.get(url)
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)

    # Test API REST: multiply operation
    def test_api_multiply_timeout(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_add_ok_request(self):
        url = f"{BASE_URL}/calc/multiply/3/2"
        response = requests.get(url)
        self.assertEqual(
            response.status_code, http.client.OK, f"6"
        )
    
    def test_api_multiply_bad_request(self):
        url = f"{BASE_URL}/calc/multiply/naan/s"
        response = requests.get(url)
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)

    # Test API REST: division operation
    def test_api_division_timeout(self):
        url = f"{BASE_URL}/calc/division/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_add_ok_request(self):
        url = f"{BASE_URL}/calc/division/10/2"
        response = requests.get(url)
        self.assertEqual(
            response.status_code, http.client.OK, f"5"
        )
    
    def test_api_division_bad_request(self):
        url = f"{BASE_URL}/calc/division/3/s"
        response = requests.get(url)
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)
    

    # Test API REST: power operation
    def test_api_power_timeout(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_power_ok_request(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = requests.get(url)
        self.assertEqual(
            response.status_code, http.client.OK, f"8"
        )
    
    def test_api_power_bad_request(self):
        url = f"{BASE_URL}/calc/power/3/s"
        response = requests.get(url)
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)
    
    # Test API REST: power operation
    def test_api_power_timeout(self):
        url = f"{BASE_URL}/calc/square/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_power_ok_request(self):
        url = f"{BASE_URL}/calc/square/4"
        response = requests.get(url)
        self.assertEqual(
            response.status_code, http.client.OK, f"16"
        )
    
    def test_api_power_bad_request(self):
        url = f"{BASE_URL}/calc/square/s"
        response = requests.get(url)
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)
    
    # Test API REST: log10 operation
    def test_api_log10_timeout(self):
        url = f"{BASE_URL}/calc/log10/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_log10ok_request(self):
        url = f"{BASE_URL}/calc/log10/10"
        response = requests.get(url)
        self.assertEqual(
            response.status_code, http.client.OK, f"1"
        )
    
    def test_api_log10_bad_request(self):
        url = f"{BASE_URL}/calc/log10/s"
        response = requests.get(url)
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)
    
    # Test BAD URL
    def test_api_no_exist(self):
        url = f"{BASE_URL}/calc/noexiste"
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)
