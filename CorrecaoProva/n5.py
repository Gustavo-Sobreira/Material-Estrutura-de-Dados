
#Questão 5
"""Pilhas e filas possuem bastantes usos em sistemas
computacionais. Por exemplo: as operações de desfazer e refazer de editores de texto e de voltar e avançar em navegadores são comumente implementadas usando duas pilhas. Implemente um simulador de editor de texto usando a função input de Python.

O script irá registrar a string digitada pelo usuário e imprimir as últimas strings fornecidas. O usuário poderá fornecer três "strings especiais" que funcionarão como comandos: 'ctrl+z' fará o script descartar a última string digitada (operação pop), 'ctrl+y' fará o script recuperar a última string descartada e, 'stop' irá parar o scripts. Veja abaixo um exemplo de execução script:"""

from pythonds.basic.stack import Stack

pilha = Stack()
apagados = Stack()

comandos = ["a","b","c","ctrl+z","ctrl+z","ctrl+y","d","ctrl+z","ctrl+y","stop","parou?"]

for i in range(0, len(comandos)):

    if comandos[i] == "ctrl+y":
        pilha.push(apagados.pop())

    else:
        if comandos[i] == "ctrl+z":
            apagados.push(pilha.pop())

        else:
            if comandos[i] == "stop":
                break

            else:
                pilha.push(comandos[i])

a = pilha.size()
while a != 0:
    print( "Posição -> ", pilha.size() - 1," = ",pilha.peek())
    pilha.pop()
    a -= 1