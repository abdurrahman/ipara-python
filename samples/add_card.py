# coding=utf-8

import ipara

json_body = {
    'userId': '123',
    'cardOwnerName': 'Abdurrahman Işık',
    'cardNumber': '5571135571135575',
    'cardAlias': 'MyVisa',
    'cardExpireMonth': '12',
    'cardExpireYear': '22',
    'clientIp': '127.0.0.1'
}

result = ipara.WalletService().create(json_body)

print result.read().decode('utf-8')
