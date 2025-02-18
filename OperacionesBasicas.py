#Integrantes de equipo
#Cerrillo Cano Hugo Emmanuel (Lider de equipo)
#Martinez Cortes Joseph Alexander

#Objetivo del programa
#Generar un programa que realice operaciones basicas simples de dos numeros (Sumas, restas, multiplicacion y division)

cifra_1 =0;
cifra_2 = 0;

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

def ask_the_user ():
    user_decision = int (input ("Que quieres hacer (Ingresa un valor numerico): \n1.Sumar \n2.Restar \n3.Multiplicar \n4.Dividr\n"))
    if (user_decision == 1):
        add ()
    elif (user_decision == 2):
        subtract ()

while True:
    ask_the_user()