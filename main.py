import os

def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2 if num2 != 0 else "Erro: divisão por zero"

def multiplicar(num1, num2):
    return num1 * num2

def finalizar():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print("Finalizado\n")

def formatar_resultado(valor):
    return f"Resultado: {valor:.2f}".rstrip("0.")

def actions():
    print("Escolha a operação que deseja realizar:")
    print("1 - Somar (+)")
    print("2 - Subtrair (-)")
    print("3 - Dividir (/)")
    print("4 - Multiplicar (*)")
    print("0 - Sair")
    action = input("Escolha sua ação: ")
    return action

def itens(repost, action, action_symbol, descricao):
    return repost == action or repost == action_symbol or repost.lower() == descricao

def calculos():
    resultado = None

    while True:
        if resultado is None:
            print("꧁༒༻☬ད ░C░a░l░c░u░l░a░d░o░r░a░ ཌ☬༺༒꧂")
            num1 = float(input("Insira o primeiro número: "))
            escolha = actions()

            if itens(escolha, "1", "+", "somar"):
                num2 = float(input("Insira o segundo número: "))
                resultado = soma(num1, num2)
                print(formatar_resultado(resultado))

            elif itens(escolha, "2", "-", "subtrair"):
                num2 = float(input("Insira o segundo número: "))
                resultado = subtrair(num1, num2)
                print(formatar_resultado(resultado))

            elif itens(escolha, "3", "/", "dividir"):
                num2 = float(input("Insira o segundo número: "))
                resultado = dividir(num1, num2)
                print(formatar_resultado(resultado))

            elif itens(escolha, "4", "*", "multiplicar"):
                num2 = float(input("Insira o segundo número: "))
                resultado = multiplicar(num1, num2)
                print(formatar_resultado(resultado))

            elif escolha == "0" or escolha == "sair":
                finalizar()
                break

            else:
                print("Ação não reconhecida, tente novamente!")

        else:
            print("\nEscolha uma opção:")
            print("1 - Limpar (iniciar novo cálculo)")
            print("2 - Continuar (usar o último resultado)")
            print("3 - Sair")

            opcao = input("Escolha sua ação: ")

            if opcao == "1":
                resultado = None
                print("\nCalculadora reiniciada. Comece um novo cálculo.")
            elif opcao == "2":
                escolha = actions()

                if itens(escolha, "1", "+", "somar"):
                    num2 = float(input("Insira o segundo número: "))
                    resultado = soma(resultado, num2)
                    print(formatar_resultado(resultado))

                elif itens(escolha, "2", "-", "subtrair"):
                    num2 = float(input("Insira o segundo número: "))
                    resultado = subtrair(resultado, num2)
                    print(formatar_resultado(resultado))

                elif itens(escolha, "3", "/", "dividir"):
                    num2 = float(input("Insira o segundo número: "))
                    resultado = dividir(resultado, num2)
                    print(formatar_resultado(resultado))

                elif itens(escolha, "4", "*", "multiplicar"):
                    num2 = float(input("Insira o segundo número: "))
                    resultado = multiplicar(resultado, num2)
                    print(formatar_resultado(resultado))

                elif escolha == "0" or escolha == "sair":
                    finalizar()
                    break

                else:
                    print("Ação não reconhecida, tente novamente!")

            elif opcao == "3":
                finalizar()
                break

            else:
                print("Opção inválida. Tente novamente.")

def main():
    calculos()

main()
