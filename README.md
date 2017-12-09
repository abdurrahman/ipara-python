# ipara-python

[![Build Status](https://travis-ci.org/abdurrahman/ipara-python.svg?branch=master)](https://travis-ci.org/abdurrahman/ipara-python)

A python library for integration with iPara Online Payment Services

## Getting Started

iPara uses both XML and JSON in api requests according to service structures.
Make sure you sending requests are in test mode during test.
Be sure to check [the documentation](https://dev.ipara.com.tr/) for using the API. (I mean like how to create hash value or deployment to production for example)
For more information - https://dev.ipara.com.tr/

## Usage

A sample adding bank card to the wallet

```python
json_body = {
    'userId': '123',
    'cardOwnerName': 'Card Holder Name',
    'cardNumber': '5571135571135575',
    'cardAlias': 'MyVisa',
    'cardExpireMonth': '12',
    'cardExpireYear': '22',
    'clientIp': '127.0.0.1'
}

result = ipara.WalletService().insert_bankcard(json_body)

print result.read().decode('utf-8')
```

A sample getting bank card/s from wallet

```python
import ipara

json_body = {
    'userId': '123',
    'cardId': '',
    'clientIp': '127.0.0.1'
}

result = ipara.WalletService().get_bankcard(json_body)

print result.read().decode('utf-8')
```

You can take a look the other usages in samples folder

## Test Cards

You can use the following card numbers during your tests.

| Card Number    	    | Exp. Date   	| CVC 	|
|------------------	    |---------- 	|-----	|
| 4282209004348015 	    | 12/22         | 123 	|
| 5571135571135575 	    | 12/22         | 000 	|
| 4355084355084358 	    | 12/22         | 000 	|
| 4662803300111364 	    | 10/25         | 000 	|
| 5166570072166334 	    | 10/25         | 000 	|
| 4022774022774026 	    | 12/18         | 000 	|
| 5456165456165454 	    | 12/18         | 000 	|
| 4531444531442283 	    | 12/18         | 000 	|
| 5818775818772285 	    | 12/18         | 000 	|
| 4508034508034509 	    | 12/18         | 000 	|
| 5406675406675403 	    | 12/18         | 000 	|
| 4025903160410013 	    | 07/20         | 123 	|
| 5345632006230604 	    | 03/19         | 310 	|
| 4282209027132016 	    | 05/18         | 358 	|
| 4029400154245816 	    | 03/24         | 373 	|
| 4029400184884303 	    | 01/23         | 378 	|