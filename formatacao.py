
def formatar_resultado(valor):
    return f"{valor:.2f}".rstrip("0.")

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido!")
           
def itens(entrada, valor, simbolo, nome):
    return entrada == valor or entrada == simbolo or entrada.lower() == nome
