#variáveis
wheels = int
weight = int
npeople = int

#código
print("Digite os dados solicitados para avaliar em qual categoria de habilitação você se enquadra:")
wheels=int(input("Quantidade de rodas: "))
weight=int(input("Peso bruto do veículo em Kg: "))
npeople=int(input("Quantidade de pessoas no veículo: "))

if (wheels == 2) or (wheels == 3):
    print("A categoria da sua habilitação é A, a qual inclui veículos com duas ou três rodas.")
elif (wheels == 4) and (npeople <= 8) and (weight <= 3500):
    print("A categoria da sua habilitação é B, a qual inclui veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg.")
elif (wheels >= 4) and(weight >=3500 and weight <= 6000):
    print("A categoria da sua habilitação é C, a qual inclui veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg.")
elif (wheels >= 4) and (npeople > 8) and (weight >=3500 and weight <= 6000):
    print("A categoria da sua habilitação é D, a qual inclui veículos com quatro rodas ou mais e que acomodam mais de oito pessoas.")
elif (wheels >= 4) and (npeople > 8) and (weight > 6000):
    print("A categoria da sua habilitação é E, a qual inclui veículos com quatro rodas ou mais e com mais de 6000 kg.")
else:
    print("O veículo não se enquadra em nenhuma das categorias")