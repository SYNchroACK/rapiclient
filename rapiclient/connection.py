import requests
import json

from rapiclient import DEFAULT_OPTIONS
from rapiclient import utils


class RESTResource(object):

    _store = {}

    def __init__(self, *args, **kwargs):
        self._store = kwargs

    def __call__(self, id=None):
        url = utils.join_url([self._store['base_url'], str(id)+"/"])
        self._store['base_url'] = url
        return self

    def __header(self):
        headers = DEFAULT_OPTIONS['HEADERS']
        if self._store['token']:
            headers['Authorization'] = self._store['token_format'].format(token=self._store["token"])
        return headers

    def __url(self, args=None):
        if not args:
            return self._store["base_url"]
        params = []
        for key, value in args.items():
            params.append('{0}={1}'.format(key, value))
        return self._store["base_url"] + "?" + "&".join(params)

    def get(self, **kwargs):
        args = None
        if 'extra' in kwargs:
            args = kwargs['extra']
        resp = requests.get(self.__url(args), headers=self.__header())
        return utils.process_response(resp)

    def post(self, data=None, **kwargs):
        payload = json.dumps(data) if data else None
        resp = requests.post(self.__url(), data=payload, headers=self.__header())
        return utils.process_response(resp)

    def patch(self, data=None, **kwargs):
        payload = json.dumps(data) if data else None
        resp = requests.patch(self.__url(), data=payload, headers=self.__header())
        return utils.process_response(resp)

    def put(self, data=None, **kwargs):
        payload = json.dumps(data) if data else None
        resp = requests.put(self.__url(), data=payload, headers=self.__header())
        return utils.process_response(resp)

    def delete(self, **kwargs):
        resp = requests.delete(self.__url(), headers=self.__header())
        return utils.process_response(resp)


class RESTAPI(object):

    __base_url = None
    __settings = None
    __token = None
    

    def __init__(self, settings={}):
        for option in DEFAULT_OPTIONS.keys():
            if option not in settings:
                settings[option] = DEFAULT_OPTIONS[option]

        self.__settings = settings

        if self.__settings['PREFIX_PATH'] == DEFAULT_OPTIONS['PREFIX_PATH']:
            self.__base_url = self.__settings['DOMAIN']
        else:
            self.__base_url = utils.join_url([self.__settings['DOMAIN'], self.__settings['PREFIX_PATH']])

    def __getattr__(self, item):
        if item.startswith("_"):
            raise AttributeError(item)

        kwargs = {
            'token': self.__token,
            'token_format': self.__settings['TOKEN_FORMAT'],
            'base_url': utils.join_url([self.__base_url, item+"/" ]),
        }
        return RESTResource(**kwargs)

    def token(self, value: str):
        self.__token = value

    def login(self, credentials: dict):
        if credentials is None:
            raise Exception("Credentials not provided.")

        url = utils.join_url([self.__base_url, self.__settings['LOGIN_PATH']])
        data = json.dumps(credentials)

        resp = requests.post(url, data=data, headers=self.__settings['HEADERS'])
        response = utils.process_response(resp)

        if response.status != 200:
            response.ok = False
            return response

        if self.__settings['TOKEN_KEY'] not in response.data:
            raise Exception("Token not found on response")

        self.__token = response.data[self.__settings['TOKEN_KEY']]
        return response

    def logout(self):
        url = utils.join_url([self.__base_url, self.__settings['LOGOUT_PATH']])

        headers = self.__settings['HEADERS']
        headers['Authorization'] = self.__settings['TOKEN_FORMAT'].format(token=self.__token)

        resp = requests.post(url, headers=headers)
        response = utils.process_response(resp)
        
        if response.status_code != 204:
            response.ok = False
            return response

        self.__token = None
        return response

