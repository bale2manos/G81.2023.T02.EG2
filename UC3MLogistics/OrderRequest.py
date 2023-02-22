"""
Autores:    Miguel Lucena Belmonte (XXXXXXXXXXX)
            Javier Pallarés de Bonrostro (100472252)
Fecha: 17/02/2023
Curso: Desarrollo de Software
Descripción: Crear un pedido nuevo
"""

import json
from datetime import datetime


class OrderRequest:
    """Crear pedido con los atributos necesarios"""
    def __init__(self, idCode: str, phoneNumber: str):
        self.__phoneNumber = phoneNumber
        self.__idCode = idCode
        justNow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justNow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def phone(self):
        return self.__phoneNumber
    @phone.setter
    def phone(self, value):
        self.__phoneNumber = value

    @property
    def productCode(self):
        return self.__idCode
    @productCode.setter
    def productCode(self, value):
        self.__idCode = value
