class complexo:

    def __init__(self, num1, num2, num3):
        self.x = num1
        self.y = num2
        self.z = num3
        self.adi = self.x + self.y + self.z
        self.sub = self.x - self.y - self.z
        self.mul = self.x * self.y * self.z
        self.div = self.x / self.y / self.z
        self.op_basicas = ["Adição", "Subtração", "Multiplicação", "Divisão"]
        self.op_valores = [self.adi, self.sub, self.mul, self.div]

    def propiedades(num):
        msg = f"\nParte real = {num.real} \nParte imaginária = {num.imag} \n{60 * '-'}"
        return msg

    def operacoes_basicas(self):
        for i in range(4):
            prop = complexo.propiedades(self.op_valores[i])
            print(f"{self.op_basicas[i]}: {self.op_valores[i]}", prop)


calculadora = complexo(5 + 2j, 7 + 3j, 3 + 1j)
calculadora.operacoes_basicas()
