def quick(lista, inicio, fim):
    pivot = lista[fim]
    menor = inicio
    for maior in range(inicio, fim):
        if lista[maior] <= pivot:
            lista[maior], lista[menor] = lista[menor], lista[maior]
            menor = menor +1
    lista[menor], lista[fim] = lista[fim], lista[menor]
    return menor # pivo


def quickSort(lista, inicio=0, fim=None):
    if fim == None:
        fim = len(lista)-1

    if inicio < fim:
        p = quick(lista, inicio, fim)
        quickSort(lista, inicio, p-1)
        quickSort(lista, p+1, fim)



# Define o tamanho do vetor
tamanho_vetor = int(input("Insira o tamanho do vetor a ser ordenado:\n"))

vetor = []

# Preenche vetor
for i in range(tamanho_vetor):
    valor = int(input("Insira um valor a ser ordenado:\n"))
    vetor.append(valor)


quickSort(vetor)


for j in range(tamanho_vetor):
    print(f'[{vetor[j]}]')
print('\n')
