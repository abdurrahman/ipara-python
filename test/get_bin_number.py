# coding=utf-8

import iparapayment

json_body = {
    'binNumber': '498749'
}

print json_body

bin_number = iparapayment.PaymentServices().get_bin_number(json_body)

print bin_number.read().decode('utf-8')
