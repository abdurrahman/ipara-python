# coding=utf-8

import iparapayment

card_xml = """
<cardOwnerName>Abdurrahman Işık</cardOwnerName>
<cardNumber>5571135571135575</cardNumber>
<cardExpireMonth>12</cardExpireMonth>
<cardExpireYear>22</cardExpireYear>
<cardCvc>000</cardCvc>
"""

cardAndUserId_xml = """
<cardId></cardId>
<userId></userId>
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
    <name>Abdurrahman</name>
    <surname>Işık</surname>
    <email>murat@kaya.com</email>
    <clientIp>123.58.7.4</clientIp>
    <birthDate>1976-07-11</birthDate>
    <gsmNumber>5881231212</gsmNumber>
    <tcCertificate>1234567890</tcCertificate>
    <invoiceAddress>
        <name>Murat</name>
        <surname>Kaya</surname>
        <address>Mevlüt Pehlivan Mah. Multinet Plaza Şişli</address>
        <zipcode>34782</zipcode>
        <city>34</city>
        <tcCertificate>12345678901</tcCertificate>
        <country>tr</country>
        <taxNumber>123456890</taxNumber>
        <taxOffice>Şişli</taxOffice>
        <companyName>iPara</companyName>
        <phoneNumber>2123886600</phoneNumber>
    </invoiceAddress>
    <shippingAddress>
        <name>Murat</name>
        <surname>Kaya</surname>
        <address>Mevlüt Pehlivan Mah. Multinet Plaza Şişli</address>
        <zipcode>34782</zipcode>
        <city>34</city>
        <country>tr</country>
        <phoneNumber>2123886600</phoneNumber>
    </shippingAddress>
</purchaser>
"""

mode_xml = "<mode>{}</mode>".format(iparapayment.mode)
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

result = iparapayment.PaymentServices().pay_without_3d(xml_body)

print result.read().decode('utf-8')
