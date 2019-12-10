#!/usr/bin/python
# -*- coding: utf-8 -*-


#
# PGS review API endpoint by Andre Goncalves
#

# Global dependencies
import re
import requests
import sys
from datetime import datetime

try:
    from urllib.parse import urlencode
except ImportError:
    # support python 2
    from urllib import urlencode
from .error import raise_error


# Global method
def generate_querystring(params):
    """
    Generate a querystring
    """
    if not params:
        return None
    parts = []
    for param, value in sorted(params.items()):
        parts.append(urlencode({param: value}))

    if parts:
        return '&'.join(parts)


class APIConnection(object):

    #
    # Local definitions to the API connection
    #
    BASE_URL = "https://api.c-feed.nl/api/v1/"
    ENDPOINTS = { 
        "reviews": "reviews"
    }
    HTTP_METHOD = "get"
    TIMEOUT = 10
    #
    # Initialisation methods
    #
    def __init__(self, api_settings):
        self.api_settings = api_settings

    def get_reviews(self, icin=None):
        if icin:
            endpoint_type = "reviews"
            params = {"icin": icin}

            response = self.perform_api_call(self.HTTP_METHOD, endpoint_type=endpoint_type, params=params)
            return response
        else:
            raise_error("requestSetupError", "Required field 'ICIN' is missing.")

    def get_api_key(self):
        return self.api_settings['api_key']

    def get_api_url(self):
        return self.BASE_URL
    
    #   
    # API call methods
    #
    def _format_request_data(self, endpoint_type, params):
        params['api_token'] = self.get_api_key()
        querystring = generate_querystring(params)

        url = self.get_api_url()

        if endpoint_type:
            url = "%s/%s" %(url, self.ENDPOINTS[endpoint_type])

        if querystring:
            url += '?' + querystring
            params = None

        return url

    def perform_http_call(self, http_method, endpoint_type=None, params=None):
        try:
            url = self._format_request_data(endpoint_type, params)

            response = requests.request(
                http_method, url,
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0',
                },
                timeout=self.TIMEOUT
            )
        except Exception as err:
            raise_error("requestError", 'Unable to communicate with PGS API: {error}'.format(error=err))

        return response

    def perform_api_call(self, http_method, endpoint_type=None, params=None):
        resp = self.perform_http_call(http_method, endpoint_type=endpoint_type, params=params)

        try:
            result = resp.json() if resp.status_code != 204 else {}
        except Exception:
            raise_error("requestHandlingError",
                "Unable to decode PGS API response (status code: {status}): '{response}'.".format(
                    status=resp.status_code, response=resp.text))

        return result
        














