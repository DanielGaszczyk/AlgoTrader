import configparser
import urllib.request
import json
import logging.handlers
import logging.handlers
import logging.handlers
import logging.handlers
import ssl
import urllib.parse
import urllib.parse
import urllib.parse
import urllib.parse
import urllib.parse
import urllib.parse
import urllib.parse
import urllib.parse
import urllib.request
import urllib.request
import urllib.request
import urllib.request
from logging.handlers import RotatingFileHandler

import urllib3


def binanceApi(action, symbol, quantity, price):
    # Disable SSL warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler('binanceAction.log', maxBytes=5000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set up config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Set up API key
    apiKey = config['Binance']['apiKey']
    secretKey = config['Binance']['secretKey']

    # Set up Binance API
    api = 'https://api.binance.com'
    apiVersion = 'v3'
    apiUrl = api + '/' + apiVersion

    # Set up Binance headers
    headers = {
        'X-MBX-APIKEY': apiKey
    }

    # Set up Binance params
    params = {
        'symbol': symbol,
        'side': action,
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': quantity,
        'price': price
    }

    # Set up Binance data
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')

    # Set up Binance request
    req = urllib.request.Request(apiUrl + '/order', data, headers)

    # Set up Binance context
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    # Set up Binance response
    response = urllib.request.urlopen(req, context=context)
    response = response.read()
    response = response.decode('utf-8')
    response = json.loads(response)

    # Return response
    return response


# WARNING: This is a test function. Do not use with real account api key!
def binanceApiTest():
    # Disable SSL warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler('binanceAction.log', maxBytes=5000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set up config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Set up API key
    apiKey = config['Binance']['apiKey']
    secretKey = config['Binance']['secretKey']

    # Set up Binance API
    api = 'https://api.binance.com'
    apiVersion = 'v3'
    apiUrl = api + '/' + apiVersion

    # Set up Binance headers
    headers = {
        'X-MBX-APIKEY': apiKey
    }

    # Set up Binance params
    params = {
        'symbol': 'BTCUSDT',
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': '0.001',
        'price': '9000'
    }

    # Set up Binance data
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')

    # Set up Binance request
    req = urllib.request.Request(apiUrl + '/order' + '/test', data, headers)

    # Set up Binance context
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    # Set up Binance response
    response = urllib.request.urlopen(req, context=context)
    response = response.read()
    response = response.decode('utf-8')
    response = json.loads(response)

    # Return response
    return response


def getBinanceAccountInfo():
    # Disable SSL warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler('binanceAction.log', maxBytes=5000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set up config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Set up API key
    apiKey = config['Binance']['apiKey']
    secretKey = config['Binance']['secretKey']

    # Set up Binance API
    api = 'https://api.binance.com'
    apiVersion = 'v3'
    apiUrl = api + '/' + apiVersion

    # Set up Binance headers
    headers = {
        'X-MBX-APIKEY': apiKey
    }

    # Set up Binance request
    req = urllib.request.Request(apiUrl + '/account', headers=headers)

    # Set up Binance context
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    # Set up Binance response
    response = urllib.request.urlopen(req, context=context)
    response = response.read()
    response = response.decode('utf-8')
    response = json.loads(response)

    # Return response
    return response


def getBinancePrice(ticker):
    # Disable SSL warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler('binanceAction.log', maxBytes=5000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set up config
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Set up API key
    apiKey = config['Binance']['apiKey']
    secretKey = config['Binance']['secretKey']

    # Set up Binance API
    api = 'https://api.binance.com'
    apiVersion = 'v3'
    apiUrl = api + '/' + apiVersion

    # Set up Binance headers
    headers = {
        'X-MBX-APIKEY': apiKey
    }

    # Set up Binance request
    req = urllib.request.Request(apiUrl + '/ticker/price?symbol=' + ticker, headers=headers)

    # Set up Binance context
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    # Set up Binance response
    response = urllib.request.urlopen(req, context=context)
    response = response.read()
    response = response.decode('utf-8')
    response = json.loads(response)

    # Return response
    return response
