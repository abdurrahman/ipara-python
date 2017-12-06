import sys
import hashlib
import base64
import xml.etree.ElementTree as ET
import json
from datetime import datetime

import ipara

class IParaClient:
    def __init__(self):
        pass

    # Todo: JSON and XML request methods has to be separate
    def api_request(self, method, url, random_string, accept_type, request=None):
        if sys.version_info < (3, 0):
            import httplib
            connection = httplib.HTTPSConnection(ipara.base_url)
        else:
            import http.client
            connection = http.client.HTTPSConnection(ipara.base_url)
        if accept_type == 'xml':
            request_body = request
        if accept_type == 'json':
            request_body = json.dumps(request)
        connection.request(method, url, request_body, self.get_headers(random_string, accept_type))
        return connection.getresponse()

    def get_headers(self, random_str, accept_type):
        header = {"Content-type": "application/json"}
        if accept_type == "xml":
            header.update({"Content-type": "application/xml"})
        header.update({'transactionDate': self.get_transaction_date()})
        header.update({'version': ipara.version})
        header.update({'token': self.generate_token(random_str)})
        return header

    def get_transaction_date(self):
        return "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())

    @staticmethod
    def generate_token(token_string):
        if sys.version_info < (3, 0):
            sha1_digest = hashlib.sha1(token_string).digest()
        else:
            sha1_digest = hashlib.sha1(token_string.encode()).digest()
        hashed_str = base64.b64encode(sha1_digest)
        return "{0}:{1}".format(ipara.public_key, hashed_str.decode('utf-8'))

class PaymentService(IParaClient):
    # Todo: Refactor this method for more efficient
    def pay_without_3d(self, request):
        xml_data = ET.fromstring(request)
        order_id = xml_data.find('./orderId')
        amount = xml_data.find('./amount')
        mode = xml_data.find('./mode')
        card_owner_name = xml_data.find('./cardOwnerName')
        card_number = xml_data.find('./cardNumber')
        card_expire_month = xml_data.find('./cardExpireMonth')
        card_expire_year = xml_data.find('./cardExpireYear')
        cvc = xml_data.find('./cardCvc')
        user_id = xml_data.find('./userId')
        card_id = xml_data.find('./cardId')
        purchaser_name = xml_data.find('./purchaser/name')
        purchaser_surname = xml_data.find('./purchaser/surname')
        purchaser_email = xml_data.find('./purchaser/email')

        random_str = ipara.private_key + order_id.text.encode('utf-8').strip() + amount.text + mode.text
        random_str += card_owner_name.text + card_number.text + card_expire_month.text
        random_str += card_expire_year.text + cvc.text
        if user_id.text is not None:
            random_str += user_id.text
        if card_id.text is not None:
            random_str += card_id.text
        random_str += purchaser_name.text + purchaser_surname.text + purchaser_email.text
        random_str += self.get_transaction_date()
        random_str = u''.join(random_str).encode('utf-8').strip()
        return self.api_request('POST', '/rest/payment/auth', random_str, 'xml', request)

    def get_payment_info(self, request):
        xml_data = ET.fromstring(request)
        order_id = xml_data.find('./orderId')
        mode = xml_data.find('./mode')
        random_str = ipara.private_key + str(order_id.text) + mode.text + self.get_transaction_date()
        return self.api_request('POST', '/rest/payment/inquiry', random_str, 'xml', request)

    def get_bin_number(self, request):
        random_str = ipara.private_key + request['binNumber'] + self.get_transaction_date()
        return self.api_request('POST', '/rest/payment/bin/lookup', random_str, 'json', request)

class WalletService(IParaClient):
    def create(self, request):
        random_str = ipara.private_key + request['userId'] + request['cardOwnerName']
        random_str += request['cardNumber'] + request['cardExpireMonth'] + request['cardExpireYear']
        random_str += request['clientIp'] + self.get_transaction_date()
        return self.api_request('POST', '/bankcard/create', random_str, 'json', request)
