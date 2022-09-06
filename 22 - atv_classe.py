class DeciduousTeeth:
    quantity_patients = 0

    def __init__(self, age, teeth, caries):
        DeciduousTeeth.quantity_patients += 1
        self.age = age  #idade do paciente
        self.teeth = teeth  #quantiade de dentes decíduos em boca
        self.caries = caries  #quantidade de dentes decíduos cariados


p1 = DeciduousTeeth(1, 12, 2)
p2 = DeciduousTeeth(2, 16, 1)
p3 = DeciduousTeeth(15, 0, 0)
print(f'Número total de pacientes: {DeciduousTeeth.quantity_patients}')
print()
print(f'Idade do paciente p1: {p1.age} ano')
print(f'Quantidade de dentes decíduos presentes em boca: {p1.teeth}')
print(f'Quantidade de dentes decíduos cariados: {p1.caries}')
print()
print(f'Idade do paciente p2: {p2.age} anos')
print(f'Quantidade de dentes decíduos presentes em boca: {p2.teeth}')
print(f'Quantidade de dentes decíduos cariados: {p2.caries}')
print()
print(f'Idade do paciente p3: {p3.age} anos')
print(f'Quantidade de dentes decíduos presentes em boca: {p3.teeth}')
print(f'Quantidade de dentes decíduos cariados: {p3.caries}')
