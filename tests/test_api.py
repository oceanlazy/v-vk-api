import os
import configparser
from unittest import TestCase
from unittest.mock import patch

import v_vk_api


def get_credentials():
    cfg_path = os.path.join(os.path.dirname(__file__), 'test.cfg')
    if not os.path.isfile(cfg_path):
        raise FileNotFoundError('Please provide "test.cfg" '
                                'file with your credentials')
    config = configparser.ConfigParser()
    config.read(cfg_path)
    return config['CREDENTIALS']


class TestApi(TestCase):
    credentials = get_credentials()
    make_inp = iter(('',))  # for captcha input

    def test_request_method(self):
        with patch('builtins.input', lambda prompt: next(self.make_inp)):
            proxies = {'http': self.credentials.get('http_proxy'),
                       'https': self.credentials.get('https_proxy')}
            api = v_vk_api.create(
                app_id=self.credentials.get('app_id'),
                login=self.credentials.get('login'),
                password=self.credentials.get('password'),
                service_token=self.credentials.get('service_token'),
                proxies=proxies if proxies.get('https') else None)
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
