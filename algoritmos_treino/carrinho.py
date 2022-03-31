# Definicao dos estoques
estoque_produto_1 = 10
estoque_produto_2 = 4
estoque_produto_3 = 0


# Criacao de uma lista para guardar os produtos adicionados, simbolizando um carrinho
carrinho = []


# Criacao dos 3 produtos
produto1 = {'id': 1, 'nome':'produto1', 'valor': 150, 'tipo': 'normal'}
produto2 = {'id': 2, 'nome':'produto2', 'valor': 100, 'tipo': 'especial'}
produto3 = {'id': 3, 'nome':'produto3', 'valor': 120, 'tipo': 'normal'}


# DEFINICAO DOS METODOS AUXILIARES:


def estoque_disponivel(numero_produto, quantidade_desejada):
    if numero_produto == 1:
        return quantidade_desejada <= estoque_produto_1
        
    elif numero_produto == 2:
        return quantidade_desejada <= estoque_produto_2

    elif numero_produto == 3:
        return quantidade_desejada <= estoque_produto_3


def adicionar_ao_carrinho(self):
    carrinho.append(self)


def mostrar_carrinho(): 
    if carrinho == []:
        print([])
    else:
        for produto in carrinho:
            print(produto)


def corrigir_preco(produtos_a_corrigir_preco):
    for i in produtos_a_corrigir_preco:
        i['valor'] = i['valor'] + ((i['valor'] / 100) * 7)


def somar_carrinho(): 
    soma_total_carrinho = 0.00

    for i in carrinho:
        soma_total_carrinho = soma_total_carrinho + i['valor']

    return soma_total_carrinho


def calcular_taxa_entrega():
    taxa_de_entrega = 0

    if carrinho != []:
        taxa_de_entrega = 5
    for i in carrinho:
        if i['id'] == 1:
            taxa_de_entrega = 15

    return taxa_de_entrega


def valor_final():
    valor_total = somar_carrinho() + calcular_taxa_entrega()

    # Aplicando desconto, se a compra for de valor maior que 200 reais
    if valor_total > 200:
        valor_total = valor_total - ((valor_total / 100) * 10)
    
    return valor_total


# Definicao das variaveis de controle
continuar = 'S'
contador = 1


# Loop, adiciona quantos produtos o usuario desejar, desde que exista estoque
while continuar == 'S':
    numero_produto = int(input("Digite o numero do produto:\n"))
    quantidade_desejada = int(input("Digite a quantidade desejada:\n"))    

    if numero_produto == 1 and estoque_disponivel(numero_produto, quantidade_desejada):
        while contador <= quantidade_desejada:
            adicionar_ao_carrinho(produto1)
            contador = contador + 1
            print("Produto adicionado!")

    elif numero_produto == 2 and estoque_disponivel(numero_produto, quantidade_desejada):
        while contador <= quantidade_desejada:
            adicionar_ao_carrinho(produto2)
            contador = contador + 1
            print("Produto adicionado!")

    elif numero_produto == 3 and estoque_disponivel(numero_produto, quantidade_desejada):
        while contador <= quantidade_desejada:
            adicionar_ao_carrinho(produto3)
            contador = contador + 1
            print("Produto adicionado!")

    else:
            print("Estoque indisponivel, adicione uma quantidade valida!")

    # Resetando variaveis de controle // Verificando se mais produtos serao adicionados
    contador = 1
    continuar = input("Digite S para contiuar a adicionar itens ao carrinho:\n")


# Aplicando os impostos em itens especiais
produtos_a_corrigir_preco = []
for produto in carrinho:
    if produto in produtos_a_corrigir_preco:
        pass
    elif produto['tipo'] == 'especial':
        produtos_a_corrigir_preco.append(produto)


corrigir_preco(produtos_a_corrigir_preco)


# Exibir carrinho e valor final da compra
mostrar_carrinho()
print(valor_final())
