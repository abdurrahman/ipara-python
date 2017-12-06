# iPara API Client
# Author :
# Abdurrahman <isikabdurrahman[at]yahoo.com>

# Setting variables
public_key = "Your public store key"
private_key = "Your private store key"
base_url = "api.ipara.com"
version = "1.0"
# Request Mode
# For more information -> https://dev.ipara.com.tr/#requestType
# T - Test
# P - Production
mode = "T"

# Resource
from iparapayment.ipara_client import (
    PaymentServices
)
