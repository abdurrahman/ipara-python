# coding=utf-8

import ipara

json_body = {
    'userId': '123',
    'cardId': '002otAjVVcPhT5GqTXOn8smBkyASG4zOJZD5KFScE/AD8g=',
    'clientIp': '127.0.0.1'
}

result = ipara.WalletService().delete_bankcard(json_body)

print result.read().decode('utf-8')
