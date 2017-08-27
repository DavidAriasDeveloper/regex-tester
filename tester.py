"""
    Tester de expresiones regulares en Python realizado por:
    - Luis David Arias
    - Nicolas Duque
"""
#Libreria de expresiones regulares
import re

#Se define un diccionario para almacenar expresiones regulares
regex = {}
#Se definen las expresiones regulares
regex[0] = re.compile('^[_a-z0-9\-]+(\.[_a-z0-9]+)*@[a-z0-9\-]+(\.[a-z0-9\-]+)*(\.[a-z]{2,3})$')#ER para correos electronicos
regex[1] = re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$') #ER para direcciones ip
regex[2] = re.compile('^((67\d{2})|(4\d{3})|(5[1-5]\d{2})|(6011))(-?\s?\d{4}){3}|(3[4,7])\ d{2}-?\s?\d{6}-?\s?\d{5}$  ')#ER para tarjetas de credito
regex[3] = re.compile('^[0-1]+[b[0-1]+]')#ER para numeros binarios
regex[4] = re.compile('#([a-fA-F]|[0-9]){3,6}')#ER para numeros hexadecimales
regex[5] = re.compile('^[_a-z0-9\-]+(\.[_a-z0-9\-]+)*@[a-z0-9\-]+(\.[a-z0-9\-]+)*(\.[a-z]{2,3})$ ')#ER para direcciones web
regex[6] = re.compile('(/\*[^*]*[^/]*\*/)|(//.*)')#ER para comentarios

#Funcion para imprimir menu
def print_menu():
    print("Regex - Tester")
    print("Seleccione una ER para evaluar")
    print("0. Correo electronico")
    print("1. Direccion IP")
    print("2. Tarjeta de credito")
    print("3. Numero binario")
    print("4. Numero hexadecimal")
    print("5. Direccion web")
    print("6. Comentarios en C/C++")
    print("7. Salir")

#Funcion para testear un texto en una expresion regular
def testRegex(id,text):
    match = re.search(regex[id],text)#Almacenamos el resultado de la busqueda
    if(match):#Si se obtuvo un resultado diferente de None
        print(text[match.start():match.end()]+" es valido\n")#Imprimimos el resultado
    else:
        print("La cadena ingresada no es valida\n")

#Ejecucion del programa
def main():
    option = ''
    while(option != '7'):#Mientras que la opcion no sea 'Salir'
        print_menu()#Imprimimos el menu
        option = str(input('# '))#Almacenamos la opcion digitada
        print()#Salto de linea
        if(int(option) < 7):
            string = str(input("Ingrese la cadena\n>>> "))#Almacenamos la cadena ingresada
            testRegex(int(option),string)#La testeamos con su respectiva ER
        elif(option == '7'):
            print("Hasta Luego\n")
        else:
            print("Opcion no valida\n")

main()
