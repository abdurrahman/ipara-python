# coding=utf-8

import ipara

card_xml = """
<cardOwnerName></cardOwnerName>
<cardNumber></cardNumber>
<cardExpireMonth></cardExpireMonth>
<cardExpireYear></cardExpireYear>
<cardCvc></cardCvc>
"""

cardAndUserId_xml = """
<cardId>002qpbSITNoioYSxU7wwOYpoHlNm6tlj7J1A/Wzt5D2avA=</cardId>
<userId>123</userId>
"""

products_xml = """
<products>
    <product>
        <productCode>Product Code 1</productCode>
        <productName>Product Name 1</productName>
        <quantity>1</quantity>
        <price>750</price>
    </product>
    <product>
        <productCode>Product Code 2</productCode>
        <productName>Product Name 2</productName>
        <quantity>1</quantity>
        <price>250</price>
    </product>
</products>
"""

purchaser_xml = """
<purchaser>
    <name>Murat</name>
    <surname>Kaya</surname>
    <email>murat@kaya.com</email>
    <clientIp>123.58.7.4</clientIp>
</purchaser>
"""

mode_xml = "<mode>{}</mode>".format(ipara.mode)
# echo_xml = "<echo></echo>"  # optional
threeD_xml = "<threeD>false</threeD>"
installment_xml = "<installment>1</installment>"
orderId_xml = "<orderId>b3091d88-6320-4446-be6c-7a1f8e6e73c7</orderId>"
amount_xml = "<amount>1000</amount>"

xml_body = """<?xml version='1.0' encoding='utf-8'?>
<auth>
{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}
</auth>
""".format(
    card_xml.strip(),
    cardAndUserId_xml.strip(),
    products_xml.strip(),
    purchaser_xml.strip(),
    mode_xml.strip(),
    # echo_xml.strip(),
    threeD_xml.strip(),
    installment_xml.strip(),
    orderId_xml.strip(),
    amount_xml.strip(),
)

result = ipara.PaymentService().pay_without_3d(xml_body)

print result.read().decode('utf-8')