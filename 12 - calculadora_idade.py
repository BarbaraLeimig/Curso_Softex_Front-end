name = str(input('Digite o seu nome completo: '))
info = True
while info:
    try:
        birth_year = int(input('Digite o seu ano de nascimento: '))
        if 1922 <= birth_year < 2022:
            age = 2022 - birth_year
            print(f'{name} completou ou completará {age} anos em 2022.')
        else:
            raise Exception('Erro!')
    except Exception:
        print('A informação digitada é inválida!')
else:
    info = False
