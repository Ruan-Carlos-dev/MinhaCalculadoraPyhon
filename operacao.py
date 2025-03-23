import os

def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2 if num2 != 0 else "Erro: não é possivel dividir por zero"

def multiplicar(num1, num2):
    return num1 * num2

def finalizar():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print("Finalizado\n")
    
