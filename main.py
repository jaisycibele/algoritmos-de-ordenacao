import time

# Abra o arquivo de texto em modo de leitura
with open('numeros_10000.txt', 'r') as arquivo:
    # Leia o conteúdo do arquivo e divida-o em uma lista de números
    lista = [int(numero) for numero in arquivo.read().split(',')]

def troca(s, i, j):
    s[i], s[j] = s[j], s[i]
    return s

def empurra(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            troca(lista, i, i+1)

def bubble_sort(lista):
    n = len(lista)
    while n > 1:
        empurra(lista)
        n -= 1

# Principal
bubble_sort(lista)

inicio = time.time()
for i in lista:
    print(f'i:{i}')
fim = time.time()

print(f'Tempo: {(fim-inicio):.3f}')
