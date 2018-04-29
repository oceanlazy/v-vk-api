import os
from unittest import TestCase

from v_vk_api.exceptions import VVKPageWarningException
from v_vk_api.utils import \
    get_base_url, get_url_params, check_page_for_warnings

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def get_fixture(filename):
    file_path = '/'.join((FIXTURES_PATH, filename))
    with open(file_path) as f:
        return f.read()


class TestUtils(TestCase):
    def test_get_base_url(self):
        html = get_fixture('get_from_url.html')
        result = get_base_url(html)
        self.assertEqual('https://login.vk.com/?act=login&_origin='
                         'https://m.vk.com&ip_h=472h8b51096ead429&lg_h='
                         '31bd0323fc779020a&role=pda&utf8=1', result)

    def test_get_url_params(self):
        url = 'https://oauth.vk.com/blank.html' \
              '#access_token=1234567890&expires_in=0&user_id=1'
        result = get_url_params(url, fragment=True)
        self.assertEqual(result['access_token'], '1234567890')
        self.assertEqual(result['user_id'], '1')
        self.assertEqual(len(result), 3)
        url = 'https://m.vk.com/login' \
              '?role=fast&to=&s=0&sid=1234567890&dif=1&email=%2B0987654321'
        result = get_url_params(url)
        self.assertEqual(result['sid'], '1234567890')
        self.assertEqual(result['email'], '+0987654321')
        self.assertEqual(len(result), 5)

    def test_check_page_for_warnings(self):
        html = get_fixture('check_page_for_warnings.html')
        with self.assertRaises(VVKPageWarningException):
            check_page_for_warnings(html)
        check_page_for_warnings('some clean html')
