# coding=utf-8

import iparapayment

request_data = """<?xml version='1.0' encoding='utf-8'?>
<inquiry>
    <orderId>2891820171005205506</orderId>
    <mode>P</mode>
</inquiry>
"""
payment_info = iparapayment.PaymentServices().get_payment_info(request_data)

print payment_info.read().decode('utf-8')
