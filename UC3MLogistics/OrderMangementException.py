"""
Autores:    Miguel Lucena Belmonte (XXXXXXXXXXX)
            Javier Pallarés de Bonrostro (100472252)
Fecha: 17/02/2023
Curso: Desarrollo de Software
Descripción: Manejar las excepciones de OrderManager.py
"""


class OrderManagementException(Exception):
    """Manejar las excepciones del gestor de pedidos"""

    def __init__(self, message):
        self.__message = message
        super().__init__(self.__message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
