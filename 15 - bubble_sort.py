import random


def bubble_sort(v):
    end = len(v)
    while end > 0:
        i = 0
        # percorrendo o vetor até o final
        while i < end-1:
            if v[i] > v[i+1]:
                # realizando a troca das posições
                temporary = v[i]
                v[i] = v[i+1]
                v[i+1] = temporary
                print(v)
            i += 1
        end -= 1


vetor = list(range(0, 10))
random.shuffle(vetor)
print(vetor)  # imprimindo o vetor em ordem aleatória

bubble_sort(vetor)  # ordenando o vetor
