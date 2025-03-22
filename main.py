import  os

#user:str =  input("Insira seu nome:")
#esteja preparado {user}''')

def soma():
  resultado = num1 + num2 
  return resultado

def subtrair():
    resultado = num1 - num2
    return resultado

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
def formatar_resultado(valor):
    return f"Resultado: {valor:.2f}".rstrip("0.")

def actions():
    print("1-somar(+)", "2-subtrair(-) ", "3-dividir(/)", "4-multiplicar(*)", "0-sair", sep="\n")
    action:str= (input("Escolha sua ação: "))
    return action

def itens(repost,action,action_symblo,descricao):
            return repost == action or repost == action_symblo or repost.lower == descricao
def calculos(): 
    escolha= actions()
    if itens(escolha,"1","+","somar"):
        num3= soma()
        print(formatar_resultado(num3))

    elif itens(escolha,"2","-","subtrair"):
        num3= subtrair()
        print(formatar_resultado(num3))

    elif itens(escolha,"3","*","multiplicar"):
        num3= multiplicar()
        print(formatar_resultado(num3))

    elif itens(escolha,"4","/","dividir"):
        num3= dividir()
        print(formatar_resultado(num3))

    elif actions() == "0" or escolha == "sair": 
        finalizar()

    else:
        print("Ação não reconhecida, tente novamente!")
    
num1= float(input("insira um número:"))
num2= float(input("segundo número:"))
calculos() 
