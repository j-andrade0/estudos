import sys
import time

# Cria um nó na árvore
class NoArvore(object):
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL(object):

    # Funcao para inserir um nó
    def inserir_no(self, raiz, chave):

        # Encontra a posição correta e insere o nó
        if not raiz:
            return NoArvore(chave)

        elif chave < raiz.chave:
            raiz.esquerda = self.inserir_no(raiz.esquerda, chave)

        else:
            raiz.direita = self.inserir_no(raiz.direita, chave)

        raiz.altura = 1 + max(self.getAltura(raiz.esquerda), self.getAltura(raiz.direita))


        # Atualizar o fator de balanceamento, e balancear a árvore
        fatorBalanceamento = self.getBalanceamento(raiz)

        if fatorBalanceamento > 1:
            if chave < raiz.esquerda.chave:
                return self.rotacionarDireita(raiz)

            else:
                raiz.esquerda = self.rotacionarEsquerda(raiz.esquerda)
                return self.rotacionarDireita(raiz)

        if fatorBalanceamento < -1:
            if chave > raiz.direita.chave:
                return self.rotacionarEsquerda(raiz)
            else:
                raiz.direita = self.rotacionarDireita(raiz.direita)
                return self.rotacionarEsquerda(raiz)

        return raiz

    # Função para deletar um nó
    def deletar_no(self, raiz, chave):

        # Encontrar o nó para ser deletado e o remover
        if not raiz:
            return raiz

        elif chave < raiz.chave:
            raiz.esquerda = self.deletar_no(raiz.esquerda, chave)

        elif chave > raiz.chave:
            raiz.direita = self.deletar_no(raiz.direita, chave)

        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp
            temp = self.getValorMinNo(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = self.deletar_no(raiz.direita, temp.chave)

        if raiz is None:
            return raiz

        # Atualiza o fator de balanceamento dos nós
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda), self.getAltura(raiz.direita))

        fatorBalanceamento = self.getBalanceamento(raiz)

        # Faz o balanceamento da árvore
        if fatorBalanceamento > 1:
            if self.getBalanceamento(raiz.esquerda) >= 0:
                return self.rotacionarDireita(raiz)
            else:
                raiz.esquerda = self.rotacionarEsquerda(raiz.esquerda)
                return self.rotacionarDireita(raiz)
        if fatorBalanceamento < -1:
            if self.getBalanceamento(raiz.direita) <= 0:
                return self.rotacionarEsquerda(raiz)
            else:
                raiz.direita = self.rotacionarDireita(raiz.direita)
                return self.rotacionarEsquerda(raiz)
        return raiz

    # Função para rotacionar a esquerda
    def rotacionarEsquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        return y

        # Função para rotacionar a direita
    def rotacionarDireita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        return y

    # Método get para altura do nó
    def getAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    # Método get para Fator de balanceamento do nó
    def getBalanceamento(self, raiz):
        if not raiz:
            return 0
        return self.getAltura(raiz.esquerda) - self.getAltura(raiz.direita)

    # Método get para valor mínimo do nó
    def getValorMinNo(self, raiz):
        if raiz is None or raiz.esquerda is None:
            return raiz
        return self.getValorMinNo(raiz.esquerda)

    def preOrder(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.chave), end="")
        self.preOrder(raiz.esquerda)
        self.preOrder(raiz.direita)

    # Exibir a árvore
    def exibirArvore(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.chave)
            self.exibirArvore(currPtr.esquerda, indent, False)
            self.exibirArvore(currPtr.direita, indent, True)


minhaArvore = ArvoreAVL()
raiz = None
numeros = [13, 90, 45, 34, 23]

for numero in numeros:
    raiz = minhaArvore.inserir_no(raiz, numero)

print('Árvore AVL: ')
minhaArvore.exibirArvore(raiz, "", True)

print('Escolha uma das opções abaixo:\n')
opcao = int(input('1 - Inserir um novo elemento na árvore AVL\n0 - Encerrrar programa\n'))

while opcao != 0:
    if opcao == 1:

        inserir_mais_numeros = 1
        while inserir_mais_numeros == 1:
            inserirNumero = int(input('Insira um número para ser adicionado a árvore AVL: '))
            numeros.append(inserirNumero)

            inserir_mais_numeros = int(input('Digite 1 para inserir mais números:\n'))

        for numero in numeros:
            raiz = minhaArvore.inserir_no(raiz, numero)

        minhaArvore.exibirArvore(raiz, "", True)
        time.sleep(3)

    else:
        print('Opção inválida!\n')
        time.sleep(2)

    opcao = int(input('1 - Inserir um novo elemento na árvore AVL\n0 - Encerrrar programa\n'))

print('Programa encerrado!')