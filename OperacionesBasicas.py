

import math

cifra_1 =0;
cifra_2 = 0;

def sqrt():
    cifra = float(input("Dame un número para calcular su raíz cuadrada\n"))
    if cifra < 0:
        print("\nError: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        resultado = math.sqrt(cifra)
        print("\nEl resultado de la raíz cuadrada de", cifra, "es", resultado)

def power():
    base = float(input("Dame la base\n"))
    exponente = float(input("Dame el exponente\n"))
    resultado = base ** exponente
    print("\nEl resultado de", base, "elevado a la potencia", exponente, "es", resultado)


def add ():
    cifra_1 = float (input("Dame el primer numero para sumar\n"))
    cifra_2 = float (input ("Dame el segundo numero para sumar \n"))
    resultado = cifra_1 + cifra_2
    print ("\nEl resultado de la suma de: ", cifra_1, "+", cifra_2, "=", resultado)

def subtract ():
    cifra_1 = float (input("Dame el primer numero para restar\n"))
    cifra_2 = float (input ("Dame el segundo numero para restar \n"))
    resultado = cifra_1 - cifra_2
    print ("\nEl resultado de la resta de: ", cifra_1, "-", cifra_2, "=", resultado)

def mul():
    cifra_1 = float (input("Dame el primer numero para multiplicacion\n"))
    cifra_2 = float (input ("Dame el segundo numero para multiplicacion\n"))
    resultado = cifra_1 * cifra_2
    print ("\nEl resultado de la multiplicacion de: ", cifra_1, " * ", cifra_2, "=", resultado)

    
def div ():
    cifra_1 = float (input("Dame el primer numero para dividir\n"))
    cifra_2 = float (input ("Dame el segundo numero para dividir \n"))
    resultado = cifra_1 / cifra_2
    print ("\nEl resultado de la division de: ", cifra_1, " / ", cifra_2, "=", resultado)
    

def ask_the_user ():
    user_decision = int(input("Que quieres hacer (Ingresa un valor numerico): \n1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Raíz cuadrada \n6. Potencia\n"))
    if (user_decision == 1):
        add ()
    elif (user_decision == 2):
        subtract ()
    elif (user_decision == 3):
        mul ()
    elif(user_decision == 4):
        div ()
    elif(user_decision == 5):
        sqrt()
    elif(user_decision == 6):
        power()



while True:
    ask_the_user()