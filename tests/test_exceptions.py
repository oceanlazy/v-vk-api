import os
import json
from unittest import TestCase

from v_vk_api.exceptions import VVKApiException

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


class TestExceptions(TestCase):
    def test_api_exception(self):
        with open(os.path.join(FIXTURES_PATH, 'api_response_error.json')) as f:
            response = json.load(f)

        api_error = VVKApiException(response['error'])
        with self.assertRaises(VVKApiException) as context:
            raise api_error
        self.assertEqual('CAPTCHA needed', str(context.exception))
        self.assertEqual(14, api_error.code)
