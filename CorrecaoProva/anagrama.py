#Nome: Gustavo Sobreira Pinto
#Data: 17/05/22
#Curso: Sistemas de Informações
#Perído: 3°

#Solução sem uso da BST

"""txt = "A alegria é uma galeria de estímulos.Na catinga uma cantiga muito escutada é o silêncio do deserto".upper().split()
unicas = []
for termo in range(len(txt)):
    if (txt[termo] not in unicas):
        unicas.append(txt[termo])
        for analizada in range(len(unicas)):
            if (sorted(unicas[analizada]) == sorted(txt[termo]) and ((unicas[analizada]) != txt[termo])):
                print(unicas[analizada]," -> ", txt[termo])
"""

#Solução com uso da BST

class Node: #Nó da árvore
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self): #Transforma a chave em Str
        return str(self.key)


class BianryTree: #Árvore
    def __init__(self,key=None):
        if key is None:
            self.root = None
        else:
            node = Node(key)
            self.root = node

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_traversal(node.left)
        print(node, end=" ")
        if node.right:
            self.simetric_traversal(node.right)


txt = "A alegria é uma galeria de estímulos.Na catinga uma cantiga muito escutada é o silêncio do deserto".upper().split()
unicas = []
for termo in range(len(txt)):
    if (txt[termo] not in unicas):
        unicas.append(txt[termo])
        for analizada in range(len(unicas)):
            if (sorted(unicas[analizada]) == sorted(txt[termo]) and ((unicas[analizada]) != txt[termo]) and (__name__ == '__main__')):
                tree = BianryTree('|->')
                tree.root.left = Node(unicas[analizada])
                tree.root.right = Node(txt[termo])
                tree.simetric_traversal()
                print('')





