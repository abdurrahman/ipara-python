# coding=utf-8

import ipara

json_body = {
    'userId': '123',
    'cardId': '',
    'clientIp': '127.0.0.1'
}

result = ipara.WalletService().get_bankcard(json_body)

print result.read().decode('utf-8')
