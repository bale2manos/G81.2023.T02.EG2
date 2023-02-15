import json
import re
from .OrderMangementException import OrderManagementException # TODO solve this
from .OrderRequest import OrderRequest


class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13(self, eAn13:str) -> bool:
        """This function validates an EAN13 barcode"""
        valid_structure = (re.search("^[0-9]{13}$", eAn13))
        if not valid_structure:
            return False

        digit_counter = 1
        sum = 0
        while digit_counter <= 12:
            par_position = (digit_counter % 2 == 0)
            digit = int(eAn13[digit_counter - 1])
            if par_position:
                sum += digit * 3
            else:
                sum += digit
            digit_counter += 1

        mod = sum % 10
        check_digit = 10 - mod
        if check_digit == 10:
            check_digit = 0

        if check_digit != int(eAn13[12]):
            return False

        return True

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
