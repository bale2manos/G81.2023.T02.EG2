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
    def __init__( self, idcode, phoneNumber ):
        self.phoneNumber = phoneNumber #TODO igual que antes quitar __ valido?
        self.idCode = idcode
        justnow = datetime.utcnow()
        self.timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def phone( self ):
        return self.phoneNumber
    @phone.setter
    def phone( self, value ):
        self.phoneNumber = value

    @property
    def productCode( self ):
        return self.idCode
    @productCode.setter
    def productCode( self, value ):
        self.idCode = value
