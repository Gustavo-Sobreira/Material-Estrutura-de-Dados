
#Questão 3
"""Considere as funções a seguir.
Qual é o valor de X(3) e X(4)?"""

#X(3) = F
#X(4) = T

#x = 0
def x(n):

    if n == 0:
        print("--X--")
        return True

    else:
        if n > 0:
            print(" ",n)
            return y(n - 1)

#1
def y(n):

    if n == 0:
        print("--X--")
        return False

    else:
        if n > 0:
            print(" ",n)
            return x(n - 1)

print("\n"
      "X(3) = ",x(3) ,"\nX(4) = ",x(4))