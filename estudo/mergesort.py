def mergesort(vetor):

  if len(vetor) == 1: # Se o vetor tiver apenas um elemento, já estará "ordenado"
    return vetor

  elif len(vetor) == 2: # Verificação rápida caso o vetor tenha somente dois elementos
    if vetor[0] > vetor[1]:
      return [vetor[1], vetor[0]]

    else:
      return vetor


  meio = len(vetor)//2
  esquerda = mergesort(vetor[:meio])
  direita = mergesort(vetor[meio:])

  vetor_ordenado = []
  while True:
    if len(esquerda) > 0 and len(direita) > 0:
      if esquerda[0] <= direita[0]:
        vetor_ordenado.append(esquerda[0])
        esquerda = esquerda[1:]
      else:
        vetor_ordenado.append(direita[0])
        direita = direita[1:]

    elif len(esquerda) > 0:
      vetor_ordenado += esquerda
      esquerda = []

    elif len(direita) > 0:
      vetor_ordenado += direita
      direita = []

    else:
      break
  return vetor_ordenado


# Define o tamanho do vetor
tamanho_vetor = int(input("Insira o tamanho do vetor a ser ordenado:\n"))

vetor = []

# Preenche vetor
for i in range(tamanho_vetor):
  valor = int(input("Insira um valor a ser ordenado:\n"))
  vetor.append(valor)

# Exibe a sequência inserida
print(vetor)

# Exibe o vetor ordenado
print(mergesort(vetor))
