#var
n1 = float
n2 = float
op = int

#code
print("------ Calculadora de 2 números ------")
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
print()
print("Operações:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print()
op = int(input("Insira o número referente à operação escolhida: "))

def calculator(n1, n2, op):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    elif op == 4: 
        return n1 / n2
    else:
        return 0
print(calculator(n1, n2, op))