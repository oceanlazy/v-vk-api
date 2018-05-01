# VVK API

VK API wrapper

## Description

With VK API wrapper you can use all possible VK API methods and pass all traffic through proxy. 
More detailed information about VK API you can see in the official [documentation](https://vk.com/dev/methods).

![Python3](https://img.shields.io/badge/Python-3-brightgreen.svg)
[![Release](https://img.shields.io/github/release/vadimk2016/v-vk-api.svg)](https://github.com/vadimk2016/v-vk-api/releases)
[![Documentation Status](https://readthedocs.org/projects/v-vk-api/badge/?version=latest)](http://v-vk-api.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/vadimk2016/v-vk-api.svg?branch=master)](https://travis-ci.org/vadimk2016/v-vk-api)
[![Coverage Status](https://coveralls.io/repos/github/vadimk2016/v-vk-api/badge.svg)](https://coveralls.io/github/vadimk2016/v-vk-api)
### Install

```
$ pip3 install v_vk_api
```

## Usage

#### Create VK APP
    
To interact with the API, you need to [create](https://vk.com/editapp?act=create) an Standalone application and save the following app data for later use: app id, service token, login and password.


#### Authorization by access token

    import v_vk_api
    
    api = v_vk_api.create(app_id=1234567890, 
                            login='login', 
                            password='pass')
    api.request_method('users.get', users_id=1)
    {'response': [{'first_name': 'John', 'id': 123, 'last_name': 'Doe'}]}
    
#### Authorization by service token

    import v_vk_api
    
    api = v_vk_api.create(service_token='service token')
    api.request_method('users.get', users_id=1)    
    {'response': [{'first_name': 'Pavel', 'id': 1, 'last_name': 'Durov'}]}

## Tests

Tests will check API connection and method requesting and some other helper functions like utils and exceptions, 
also to tun tests you need to provide a file `tests/config_test.json`. Run tests:
```
$ python -m unittest discover tests
```
**NOTE:** Tests can't handle CAPTCHA