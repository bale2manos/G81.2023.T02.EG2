"""
Autores:    Miguel Lucena Belmonte (XXXXXXXXXXX)
            Javier Pallarés de Bonrostro (100472252)
Fecha: 17/02/2023
Curso: Desarrollo de Software
Descripción: Encargado de gestionar los pedidos
"""

import json
import re
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest



class OrderManager:
    """Gestión de pedidos"""
    def __init__(self):
        pass

    def validate_ean13(self, ean13: str) -> bool:
        """This function validates an EAN13 barcode"""
        validStructure = re.search("^[0-9]{13}$", ean13)
        if not validStructure:
            return False

        digitCounter = 1
        sumTotal = 0
        while digitCounter <= 12:
            parPosition = digitCounter % 2 == 0
            digit = int(ean13[digitCounter - 1])
            if parPosition:
                sumTotal += digit * 3
            else:
                sumTotal += digit
            digitCounter += 1

        mod = sumTotal % 10
        checkDigit = 10 - mod
        if checkDigit == 10:
            checkDigit = 0

        if checkDigit != int(ean13[12]):
            return False
        return True

    def read_product_code_from_json(self, fileName: str): # TODO return?
        """Lee el código del producto desde un archivo JSON"""
        try:
            with open(fileName, encoding='UTF-8') as file:
                data = json.load(file)
        except FileNotFoundError as error:
            raise OrderManagementException("Wrong file or file path") from error
        except json.JSONDecodeError as error:
            raise OrderManagementException("JSON Decode Error - "
                                           "Wrong JSON Format") from error


        try:
            product = data["id"]
            phoneNumber = data["phoneNumber"]
            req = OrderRequest(product, phoneNumber)
        except KeyError as error:
            raise OrderManagementException("JSON Decode Error - "
                                           "Invalid JSON Key") from error
        if not self.validate_ean13(product):
            raise OrderManagementException("Invalid product code")

        # Close the file
        return req
