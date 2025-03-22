import os

#user:str =  input("Insira seu nome:")
#esteja preparado {user}''')


num1= input("insira um número:")
num2= input("segundo número:") 

def somar():
  num3 = num1 + num2 
  return num3

def subtrair():
    num3 = num1 - num2
    return num3

def dividir():
    num3 = num1 / num2
    return num3

def multiplicar(): 
    num3 = num1 * num2
    return num3
def finalizar():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix': 
        os.system('clear')

    print("Finalizado\n")


print("1-somar(+)", "2-subtrair(-) ", "3-dividir(/)", "4-multiplicar(*)", "0-sair", sep="\n")
action:str =(input("Escolha sua ação"))

if action == "1" or "+" or "somar": 
    print("")

elif action == "2" or "-" or "subtrair":
    print("")

elif action == "3" or "/" or "dividir": 
    print ("")

elif action == "4" or "*" or "multiplicar":
    print("")

elif action == "0" or "sair": 
    finalizar()
else:
    print("Ação não reconhecida, tente novamente!")

