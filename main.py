"""
Autores:    Miguel Lucena Belmonte (XXXXXXXXXXX)
            Javier Pallarés de Bonrostro (100472252)
Fecha: 17/02/2023
Curso: Desarrollo de Software
Descripción: Código principal para la creación de un código de barras
"""
import string
from barcode import EAN13
from barcode.writer import ImageWriter
from UC3MLogistics import OrderManager

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3

def encode(word):
    """Codifica la palabra indicada"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            letterEncoded = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[letterEncoded]
    return encoded

def decode(word):
    """Descodifica la palabra indicada"""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            letterEncoded = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[letterEncoded]
    return encoded

def main():
    """Código principal del programa"""
    mng = OrderManager()
    res = mng.read_product_code_from_json("test_valid.json")
    #strRes = res.__str__() esto se puede sustituir por lo de abajo?
    strRes = str(res)
    print(strRes)
    encodeRes = encode(strRes)
    print("Encoded Res "+ encodeRes)
    decodeRes = decode(encodeRes)
    print("Decoded Res: " + decodeRes) # TODO hay q hacerlo para el codigo malo y el bueno
    print("Codew: " + res.productCode)
    with open("./barcodeEan13.jpg", 'wb') as fileImage:
        imageWriter = ImageWriter()
        EAN13(res.productCode, writer=imageWriter).write(fileImage)


if __name__ == "__main__":
    main()
