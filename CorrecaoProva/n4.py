
#Questão 4
"""Um número diferente de 0 (zero), significa inserir esse número na fila e, o número 0,
significa remover o elemento da fila que está na frente (dequeue).

Dar a sequência de valores devolvidos pelas operações dequeue, remoção da fila, quando esta sequência de operações é realizada em uma fila inicialmente vazia, após a leitura da seguinte sequência de números:

123040556000078 """

import queue #Importa a biblioteca queue

fila = queue.Queue() #Fila vazia
dequeue = [] #Lista do que foi excluido

adicionar = int(input(" Quantos números passará? ")) #Prova = 15
contador = adicionar

while contador != 0:
    contador -= 1
    passarNum = int(input("Diga o número para ser adicionado na Fila: "))

    if passarNum == 0: #Verificação se é remoção de valor
        dequeue.append(fila.get())  #dequeue. append joga o valor na lista de excluidos e   fila.get()remove o 1° valor adicionado na fila
    else:
        fila.put(passarNum) #Fila.put() adiciona o número que foi passado

print(f"\nDequeue = {dequeue}")