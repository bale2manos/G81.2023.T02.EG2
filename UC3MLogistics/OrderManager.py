import json
import re
##from .OrderMangementException import OrderManagementException
##from .OrderRequest import OrderRequest


class OrderManager:
    def __init__(self):
        pass

def ValidateEAN13(eAn13:str) -> bool:


    x = (re.search("^[0-9]{13}$", eAn13))
    # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
    # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
    digit_counter = 1
    suma = 0
    while digit_counter < 13:
        par = digit_counter % 2 == 0
        if not par:
            suma += eAn13[digit_counter]
        else:
            suma += eAn13[digit_counter]*3

    if not x:
        return False
    print(x)
    return True
print(ValidateEAN13("1234567891123"))

"""
    def ReadproductcodefromJSON(self, fi: str) -> None: # DUDA AQUI PREGUNTAR

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            PRODUCT = DATA["id"]
            PH = DATA["phoneNumber"]
            req = OrderRequest(PRODUCT, PH)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateEAN13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req
        """