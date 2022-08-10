# funções
def data():
    n1 = float(input("Insira o primeiro valor: "))
    n2 = float(input("Insira o segundo valor: "))
    return n1, n2


def calculator(op):
    if op == 1:
        n1, n2 = data()
        return n1 + n2
    elif op == 2:
        n1, n2 = data()
        return n1 - n2
    elif op == 3:
        n1, n2 = data()
        return n1 * n2
    elif op == 4:
        n1, n2 = data()
        return n1 / n2
    elif op == 0:
        print("Encerrando...")
        exit()
    else:
        return "Essa opção não existe!"


# código principal
op = 1
while op != 0:
    print("Escolha o número referente a uma das operações a seguir")
    print("Digite a opção 0 apenas quando desejar encerrar a calculadora")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    print()
    op = int(input("Insira o número referente à operação escolhida: "))
    print(f"Resultado: {calculator(op)}")
    print()