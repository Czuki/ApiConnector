import requests
from types import SimpleNamespace
import json


class ApiTemplate():
    base_url = None

    def __init__(self, auth=None):
        self.auth = auth

    @staticmethod
    def _set_authorization_header(auth, headers):
        headers.update({'x-api-key': auth.token})

    @staticmethod
    def _prepare_response(response):
        prepared_response = {'response': None}
        try:
            prepared_response['response'] = response.json()
        except Exception:
            print('Error converting to JSON')
        return json.dumps(prepared_response)

    @staticmethod
    def _get_query_suffix(query_data):
        query_list = []
        for query, value in list(query_data.items()):
            query_list.append(f'{query}={value}')
        return '?' + '&'.join(query_list)

    def _get_response(self, url, query_data):
        response = None

        if query_data:
            url += self._get_query_suffix(query_data)
        try:
            headers = {}
            if self.auth:
                self._set_authorization_header(self.auth, headers)
            print(url)
            response = requests.get(url, headers=headers)
        except Exception:
            print('Error fetching data')
        if response.status_code == 200:
            return response
        else:
            print('Error: {}'.format(response.status_code))
        return response

    def objectify_response(self, endpoint, query_data=None):
        response = self._get_response(self.base_url.format(endpoint), query_data)
        prepared_response = self._prepare_response(response)
        response_obj = json.loads(prepared_response, object_hook=lambda d: SimpleNamespace(**d))
        return response_obj


class ApiAuth():

    def __init__(self, token=None):
        self.token = token

    @property
    def get_auth(self):
        return {
            'x-api-key': self.token
        }
