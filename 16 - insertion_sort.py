import random


def insertion_sort(v):
    i = 1
    while i < len(v):
        temporary = v[i]
        switch = False
        j = i - 1
        while j >= 0 and v[j] > temporary:
            v[j + 1] = v[j]
            switch = True
            j -= 1
        if switch:
            v[j + 1] = temporary
        i += 1


vector = list(range(1, 60, 2))
random.shuffle(vector)
print('Lista de números ímpares desordenados: ', vector)

insertion_sort(vector)
print('Lista de números ímpares ordenados: ', vector)
