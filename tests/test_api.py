import os
import json
from unittest import TestCase
from unittest.mock import patch

import v_vk_api


def get_credentials():
    cfg_path = os.path.join(os.path.dirname(__file__), 'config_test.json')
    if os.path.isfile(cfg_path):
        with open('config_test.json') as f:
            return json.load(f)
    return {}


class TestApi(TestCase):
    credentials = get_credentials()
    make_inp = iter(('', ''))  # for captcha input

    def test_method(self):
        with patch('builtins.input', lambda prompt: next(self.make_inp)):
            api = v_vk_api.create(
                app_id=self.credentials.get('app_id'),
                login=self.credentials.get('login'),
                password=self.credentials.get('password'),
                service_token=self.credentials.get('service_token'),
                proxies=self.credentials.get('proxies'))
            response = api.request_method(
                'users.search',
                q='Pavel Durov',
                fields='bdate, city, occupation, photo_50',
                count=5)

        self.assertIsInstance(response, dict)
        self.assertIn('response', response)
        self.assertIn('items', response['response'])
        self.assertIsInstance(response['response']['items'], list)
        self.assertEqual(len(response['response']['items']), 5)
        workplace = response['response']['items'][0]['occupation']['name']
        self.assertEqual(workplace, 'Telegram')

    def test_open_method(self):
        with patch('builtins.input', lambda prompt: next(self.make_inp)):
            api = v_vk_api.create(proxies=self.credentials.get('proxies'))
            response = api.request_method('users.get', user_ids=1)

        self.assertIn('response', response)
        self.assertIn('last_name', response['response'][0])
        self.assertEqual(response['response'][0]['last_name'], 'Durov')
