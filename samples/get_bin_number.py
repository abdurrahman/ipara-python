# coding=utf-8

import ipara

json_body = {
    'binNumber': '498749'
}

print json_body

bin_number = ipara.PaymentService().get_bin_number(json_body)

print bin_number.read().decode('utf-8')
