from hashlib import sha256
import urllib.request
import urllib.parse
import time


class UltraGeoPoint:

    url = ''
    api_secret = ''
    params = {}

    def __init__(self, api_key, api_secret,
                 host='api.sec.neustar.biz',
                 service_name='ipi',
                 service_category='gpu',
                 version='v1',
                 output_format=None,
                 cb_function=None):

        self.api_secret = api_secret

        self.params['apikey'] = api_key
        self.params['format'] = output_format
        self.params['sig'] = self.signature()

        if cb_function is not None:
            self.params['callback'] = cb_function

        self.url = "/".join(['https:/', host, service_name, service_category, version])

    def signature(self):

        timestamp = str(int(time.time()))
        self.params['sig'] = sha256((self.params['apikey'] + self.api_secret + timestamp).encode('utf-8')).hexdigest()
        return self.params['sig']

    def ipinfo(self, ip_address):

        self.signature()
        params = urllib.parse.urlencode(self.params)
        url = ('/'.join([self.url, 'ipinfo', ip_address])) + '?' + params
        req = urllib.request.Request(url=url, method='GET')

        return urllib.request.urlopen(req)

    def schema(self):
        pass


if __name__ == "__main__":

    import configparser
    import argparse
    import json

    # Get API credential material
    config = configparser.ConfigParser()
    config.read('config.ini')

    key = config['GEOPOINT']['api_key']
    secret = config['GEOPOINT']['api_secret']

    # Get parameters from CL for API
    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('format')

    args = parser.parse_args()

    print("Testing call to 'ipinfo'.")
    client = UltraGeoPoint(key, secret, output_format=args.format)
    print("CLIENT:", client.url)
    result = client.ipinfo(args.ip)

    j_obj = json.loads(result.read().decode('utf-8'))
    print("RESULT:", json.dumps(j_obj, indent=4))
