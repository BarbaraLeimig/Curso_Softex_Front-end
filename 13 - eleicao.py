"""
Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0
O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda
a nenhum candidato ou seja branco, ele deve ser tratado como nulo.
Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.
Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também,
a quantidade de votos de cada candidato, os brancos e nulos
"""

from enum import Enum


class Candidates(Enum):
    Candidato_X = 889
    Candidato_Y = 847
    Candidato_Z = 515
    branco = 0


def screen():  # função principal que irá aparecer na tela
    print('***** ELEIÇÕES 2022 *****')
    print()
    print('Candidato_X = 889')
    print('Candidato_Y = 847')
    print('Candidato_Z = 515')
    print('branco = 0')
    print()


def vote(v):  # função que imprime o nome do candidato de acordo com o voto e finaliza ou continua a votação
    if v == Candidates.Candidato_X.value:
        print(f'Você votou no {Candidates.Candidato_X.name}')
        return end_vote()
    elif v == Candidates.Candidato_Y.value:
        print(f'Você votou no {Candidates.Candidato_Y.name}')
        return end_vote()
    elif v == Candidates.Candidato_Z.value:
        print(f'Você votou no {Candidates.Candidato_Z.name}')
        return end_vote()
    elif v == Candidates.branco.value:
        print(f'Você votou em {Candidates.branco.name}')
        return end_vote()
    else:
        print('Você votou nulo')
        return end_vote()


def end_vote():  # função que será repetida em cada opção de candidato
    print('Deseja confirmar seu voto?')
    print('1 - Sim')
    print('2 - Não')
    a = int(input())
    if a != 1:
        return print()
    else:
        print('Deseja encerrar a eleição:')
        print('1 - Sim')
        print('2 - Não')
        b = int(input())
        if b != 1:
            return print()
        else:
            print('ELEIÇÃO 2022 ENCERRADA')
            print()
            if counter_c_x > counter_c_y and counter_c_x > counter_c_z:
                print(f'O vencedor foi o {Candidates.Candidato_X.name}')
            elif counter_c_y > counter_c_z:
                print(f'O vencedor foi o {Candidates.Candidato_Y.name}')
            else:
                print(f'O vencedor foi o {Candidates.Candidato_Z.name}')
            print()
            print(f'{Candidates.Candidato_X.name} recebeu {counter_c_x} votos')
            print(f'{Candidates.Candidato_Y} recebeu {counter_c_y} votos')
            print(f'{Candidates.Candidato_Z} recebeu {counter_c_z} votos')
            print(f'Total de {counter_white + counter_null} votos brancos e nulos')
            exit()


b = 0
counter_c_x = 0
counter_c_y = 0
counter_c_z = 0
counter_white = 0
counter_null = 0
while b != 1:  # loop para poder retornar no final vencedor e quantidade dos votos
    try:
        screen()
        v = int(input('Digite o número do seu candidato: '))

        if v == Candidates.Candidato_X.value:
            counter_c_x += 1
        elif v == Candidates.Candidato_Y.value:
            counter_c_y += 1
        elif v == Candidates.Candidato_Z.value:
            counter_c_z += 1
        elif v == Candidates.branco.value:
            counter_white += 1
        else:
            counter_null += 1

        vote(v)

    except ValueError:
        print('A informação digitada não é um número! Vote novamente.')
        print()