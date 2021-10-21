#Matías González Moroso
#Felipe Martínez Gajardo

import random
import os
from typing import Text
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from secrets import token_bytes
from Crypto.Random import get_random_bytes

def cmd(commando):
    os.system(commando)
cmd("python -m pip install --upgrade pip")
cmd("pip install wheel")
cmd("pip install pycryptodome")

ValorP = 0 #ValorP
VariableNumeroG = 0 #ValorG
b = 0
A_Usuario = 0
nonce = 0
abcdario = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.-_!""#$%&/()=?+*~[{^]}- "

def Primo(Numero):
    for n in range(2, Numero):
        if Numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def MayorMenor(VariableNumero, VariableNumeroG):
   if VariableNumero > VariableNumeroG and VariableNumeroG > 0:
      return True
   else:
      return False
      
######################### DES ########################################
def encriptarDes(Mensaje):
    global nonce
    print("------ENCRIPTANDO DES-----")
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(Mensaje.encode('ascii'))
    TextoEnBytes = ciphertext
    MensajeDeEntrada=open("mensajeentrada.txt", "ab")
    MensajeDeEntrada.write(TextoEnBytes)
    MensajeDeEntrada.close()
    return nonce, ciphertext, tag


def descifrarDES(Mensaje):
    global nonce
    try:
        texto = open('mensajeentrada.txt', 'rb')
        TextoCifrado = texto.readline()
        cipher = DES.new(key, DES.MODE_EAX, nonce = nonce)
        print("------DESCIFRANDO DES-----")
        plaintext = cipher.decrypt(TextoCifrado)
        TextoDescifrado = plaintext.decode('ascii')
        MensajeDeSalida=open("mensajerecibido.txt", "w")
        MensajeDeSalida.write(TextoDescifrado)
        MensajeDeSalida.close()
        if TextoDescifrado == Mensaje:
            print("Es seguro")
        else:
            print("El mensaje fue alterado")
    except:
        print("El mensaje fue alterado.")

########################## 3DES #######################################
def encriptar3Des(Mensaje):
    global nonce
    print("------ENCRIPTANDO 3DES-----")
    cipher = DES3.new(key2, DES3.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(Mensaje.encode('ascii'))
    TextoEnBytes = ciphertext
    print(ciphertext)
    MensajeDeEntrada=open("mensajeentrada.txt", "ab")
    MensajeDeEntrada.write(TextoEnBytes)
    MensajeDeEntrada.close()
    return nonce, ciphertext

def descifrar3DES(Mensaje):
    global nonce
    try:
        texto = open('mensajeentrada.txt', 'rb')
        TextoCifrado = texto.readline()
        cipher = DES3.new(key2, DES3.MODE_EAX, nonce = nonce)
        print("------DESCIFRANDO 3DES-----")
        plaintext = cipher.decrypt(TextoCifrado)
        TextoDescifrado = plaintext.decode('ascii')
        MensajeDeSalida=open("mensajerecibido.txt", "w")
        MensajeDeSalida.write(TextoDescifrado)
        MensajeDeSalida.close()
        if TextoDescifrado == Mensaje:
            print("Es seguro")
            
        else:
            print("El mensaje fue alterado")
    except:
        print("El mensaje fue alterado.")

########################### AES ######################################

def encriptarAES(Mensaje):
    global nonce
    print("-------------ENCRIPTANDO AES-----------")
    cipher = AES.new(key3, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(Mensaje.encode('ascii'))
    TextoEnBytes = ciphertext
    MensajeDeEntrada=open("mensajeentrada.txt", "ab")
    MensajeDeEntrada.write(TextoEnBytes)
    MensajeDeEntrada.close()
    return nonce, ciphertext

def descifrarAES(Mensaje):
    try:
        global nonce
        texto = open("mensajeentrada.txt", "rb")
        TextoCifrado = texto.readline()
        cipher = AES.new(key3, AES.MODE_EAX, nonce = nonce)
        print("-------------DESCIFRANDO AES----------")
        plaintext = cipher.decrypt(TextoCifrado)
        TextoDescifrado = plaintext.decode('ascii')
        MensajeDeSalida=open("mensajerecibido.txt", "w")
        MensajeDeSalida.write(TextoDescifrado)
        MensajeDeSalida.close()
        if TextoDescifrado == Mensaje:
            print("Es seguro")
                
        else:
            print("El mensaje fue alterado")
    except:
        print("El mensaje fue alterado.")

#############################################################
botoncito = True
while botoncito:
    try:
        if ValorP == 0:
            ValorP = int(input("Ingrese el valor de P: "))
            Comprobante = Primo(ValorP)
            if Comprobante == True:
                pass
            else:
                ValorP = 0
                botoncito = True
        else:
            None
        if VariableNumeroG == 0:
            VariableNumeroG = int((input("Ingrese el valor de G: ")))
            Comprobante2 = MayorMenor(ValorP, VariableNumeroG)
            print(Comprobante2)
            if Comprobante2 == True:
                b = random.randint(0, ValorP - 1)
            else:
                VariableNumeroG = 0
                botoncito == True

        if ValorP == 0 or VariableNumeroG == 0:
            pass

        else:
            print("Piensa en un número que será tu 'a' el cual será secreto para ti (presiona Enter cuando lo tengas)")
            print("El valor de P es: ", ValorP)
            print("El valor de G es: ", VariableNumeroG)
            if A_Usuario == 0:
                A_Usuario = int(input("Ingrese el valor que obtuvo de A: "))
            else:
                None
            B_Server = VariableNumeroG**b%ValorP
            print("El valor de B es: ", B_Server)
            K_Usuario = int(input("Ingrese el valor de K: "))
            K_Servidor = A_Usuario**b%ValorP


            if K_Usuario == K_Servidor:
                print("Llaves sincronizadas")
                Mensaje = input("Ingrese el texto que quiera: ")
                for ix in Mensaje:
                    if ix not in abcdario:
                        print("Ingrese caracteres válidos.")
                        botoncito = True
                    else:
                        botoncito = False
            else:
                print("Las llaves son distintas. No serán sincronizadas.")
                print("-------------------------------------")
                botoncito = True
    except:
        print("Opción no válida.")

key = K_Servidor.to_bytes(8,'big')
key2 = DES3.adjust_key_parity(get_random_bytes(24))
key3 = K_Servidor.to_bytes(16, 'big')

def main():
    boton = True
    while boton:
        Decision = input("¿Qué desea hacer?: \n a) DES \n b) 3DES \n c) AES \n d) Cerrar el programa \n")
        if Decision == "a":
            MensajeEntrada = open("mensajeentrada.txt", "w")
            encriptarDes(Mensaje)
            Descifrar = input("¿Desea descifrar el mensaje? (s/n): ")
            if Descifrar == "s":
                descifrarDES(Mensaje)
                boton == True
            elif Descifrar == "n":
                boton == True
            else:
                print("No válido")
                boton = True
        elif Decision == "b":
            MensajeEntrada = open("mensajeentrada.txt", "w")
            encriptar3Des(Mensaje)
            Descifrar = input("¿Desea descifrar el mensaje? (s/n): ")
            if Descifrar == "s":
                descifrar3DES(Mensaje)
                boton == True
            elif Descifrar == "n":
                boton == True
            else:
                print("No válido")
                boton = True
        elif Decision == "c":
            MensajeEntrada = open("mensajeentrada.txt", "w")
            encriptarAES(Mensaje)
            Descifrar = input("¿Desea descifrar el mensaje? (s/n): ")
            if Descifrar == "s":
                descifrarAES(Mensaje)
                boton == True
            elif Descifrar == "n":
                boton = True
            else:
                print("No válido")
                boton == True
        elif Decision == "d":
            print("adiosito uwu")
            boton = False
        else:
            print("Ingrese una opción válida")
            boton == True

main()