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
        self.message = message
        super().__init__(self.message)

    @property
    def message(self):
        return self.message  # TODO duda si valido sin __

    @message.setter
    def message(self, value):
        self.message = value
