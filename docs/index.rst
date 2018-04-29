.. VVK API documentation master file, created by
   sphinx-quickstart on Mon Apr 30 00:13:42 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to VVK API's documentation!
===================================

With VK API wrapper you can use all possible VK API methods and pass all
traffic through proxy. More detailed information about VK API you can
see in the official `documentation <https://vk.com/dev/manuals>`__.

Install
~~~~~~~

::

    $ pip3 install v_vk_api

Usage
-----

Authorization by access token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    import v_vk_api

    api = v_vk_api.create(app_id=1234567890, login='login', password='pass')
    api.request_method('users.get', user_ids=1)
    {'response': [{'first_name': 'John', 'id': 123, 'last_name': 'Doe'}]}

Authorization by service token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    import v_vk_api

    api = v_vk_api.create(service_token='service token')
    api.request_method('users.get', user_ids=1)    
    {'response': [{'first_name': 'Pavel', 'id': 1, 'last_name': 'Durov'}]}

Tests
-----

Tests will check API connection and method requesting and some other
helper functions like utils and exceptions, also API needs some data to
authorize, which you can provide in the file ``test.cfg``, to run tests
execute:

::

    $ python -m unittest discover tests

**NOTE:** Tests can't handle CAPTCHA
