
#Questão 1
"""Em Python, para obtermos o resto da divisão inteira de um número por 10, fazemos da seguinte forma:

                                        n % 10 -> o resultado  SEMPRE será a UNIDADE

Por exemplo: 15 % 10 resultará 5.
-----------------------------------------------------------------------------------------------------

Para obtermos o quociente da divisão inteira de um número por 10, fazemos da seguinte forma:

                                        n // 10 -> o resultado SEMPRE EXCLUIRÁ a UNIDADE

Por exemplo: 15 // 10 resultará em 1, e 325 // 10 resultará 32
-----------------------------------------------------------------------------------------------------

A função a seguir, retornará qual valor se executarmos o comando Mystery(432)?"""


# ---------- Modelo Usual ---------- #
"""
def mistery(n):

    if n == 0:
        return 0

    else:
        d = n % 10# 4
        return d * mistery(n // 10)

print(mistery(432))"""


# ---------- Modelo Visual ---------- #


def mistery(n):
    retornar = 5 #Mude aqui para mudar a equação

    if n == 0:
        print(f"mistery(\033[1;32m{retornar}\033[m) = {retornar}\n"
              f"Depois de receber o valor {retornar} é só multiplicar!")
        return retornar

    else:

        if n // 10 != 0:
            print(f"Dado ->  n = {n}\n"
                  f"         d = {n // 10}\033[1;31m{n%10}\033[m  % 10\n"
                  f"Temos -> d = \033[1;31m{n % 10}\033[m\n")
        else:
            print(f"Dado ->  n = {n}\n"
                  f"         d = \033[1;31m{n}\033[m  % 10\n"
                  f"Temos -> d = \033[1;31m{n % 10}\033[m\n")

        d = n % 10

        print(f"Retorna {d} x mistery(\033[1;32m{n // 10}\033[m{n % 10} // 10)\n"
              f"Ou seja:\n"
              f"Retorna {d} x mistery(\033[1;32m{n // 10}\033[m)\n")

        func = d * mistery(n // 10)
        return func

print(mistery(432))