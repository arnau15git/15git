
#!usr/bin/env python
#-*- coding: utf-8 -*-


abc = "abcdefghijklmopqvrstxyz"

  
def crypt(cadena, clave):
    text_cifrado = ''

    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])

    return text_cifrado

def decrypt(cadena, clave):
    text_cifrado = ''

    for letra in cadena:
        resta = abc.find(letra) - clave
        modulo = int(resta) %len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])


def main():
    c = str(raw_input("Pon aquí la cadena de texto para encriptar:")).lower()
    n = int(raw_input("Pon aquí la clave:"))
    print crypt(c,n)
    nc = str(raw_input("Pon aquí la clave para desencriptar: ")).lower()
    nn = int(raw_input("Pon aquí la clave: "))
    print decrypt(nc, nn)




if __name__ == '__main__':
    main()
