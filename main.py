from    operacao   import soma,subtrair,dividir,multiplicar,finalizar
from    formatacao  import itens,formatar_resultado,ler_numero
from    interface   import exibir_menu,exibir_menu2
 
def calculos():
    resultado = None

    while True:
        if resultado is None:
            print("❚█══CALCULADORA══█❚")
            num1 = ler_numero("Insira um número: ")
            escolha = exibir_menu()

            if itens(escolha, "1", "+", "somar"):
                num2 = ler_numero ("Insira o segundo número: ")
                resultado = soma(num1, num2)
                print(f" {formatar_resultado(num1)} + {formatar_resultado(num2)} = {formatar_resultado(resultado)}")

            elif itens(escolha, "2", "-", "subtrair"):
                num2 = ler_numero ("Insira o segundo número: ")
                resultado = subtrair(num1, num2)
                print(f" {formatar_resultado(num1)} - {formatar_resultado(num2)} = {formatar_resultado(resultado)}")

            elif itens(escolha, "3", "/", "dividir"):
                num2 = ler_numero ("Insira o segundo númer: ")
                resultado = dividir(num1, num2)
                print(f" {formatar_resultado(num1)} / {formatar_resultado(num2)} = {formatar_resultado(resultado)}")

            elif itens(escolha, "4", "*", "multiplicar"):
                num2 = ler_numero ("Insira o segundo número: ")
                resultado = multiplicar(num1, num2)
                print(f" {formatar_resultado(num1)} * {formatar_resultado(num2)} = {formatar_resultado(resultado)}")

            elif escolha == "0" or escolha.lower() == "sair":
                finalizar()
                break                
            else:
                print("Ação não reconhecida, tente novamente!")

        elif resultado != None:
            escolha = exibir_menu2()

            if escolha == "1" or escolha.lower()== "limpar":
                resultado = None
                print("\nCalculadora reiniciada. Comece um novo cálculo.")
            elif escolha == "2" or escolha.lower() == "continuar":
                escolha = exibir_menu()
                if itens(escolha, "1", "+", "somar"):
                    num2 = ler_numero ("Insira o segundo número: ")
                    resultado2 = soma(resultado, num2)
                    print(f" {formatar_resultado(resultado)} + {formatar_resultado(num2)} = {formatar_resultado(resultado2)}")

                elif itens(escolha, "2", "-", "subtrair"):
                    num2 = ler_numero ("Insira o segundo número: ")
                    resultado2 = subtrair(resultado, num2)
                    print(f" {formatar_resultado(resultado)} - {formatar_resultado(num2)} = {formatar_resultado(resultado2)}")

                elif itens(escolha, "3", "/", "dividir"):
                    num2 = ler_numero ("Insira o segundo número: ")
                    resultado2 = dividir(resultado, num2)
                    print(f" {formatar_resultado(resultado)} / {formatar_resultado(num2)} = {formatar_resultado(resultado2)}")

                elif itens(escolha, "4", "*", "multiplicar"):
                    num2 = ler_numero ("Insira o segundo número: ")
                    resultado2 = multiplicar(resultado, num2)
                    print(f" {formatar_resultado(resultado)} * {formatar_resultado(num2)} = {formatar_resultado(resultado2)}")

            elif escolha == "0" or escolha.lower() == "sair":
                finalizar()
                break
            else:
                print("Opção inválida. Tente novamente.")


def main():
    calculos()

main()
