
#Questão 2
"""Considere a função à seguir em Python.
Determine o resultado de F(3) + F(7)"""

# ---------- Modelo Usual ---------- #

# f(3) = 9
# f(7) = 23
#23 + 9 = 32
def f(n):

    if n < 4:
        return 3 * n

    else:
        return 2 * f(n - 4) + 5 # 18 + 5 = 23

print(f(3) + f(7))

# ---------- Modelo Visual ---------- #

def f(n):

    if n < 4:
        ab = 3 * n
        print(f" f({n}) -> 3 * {n} = {ab}")
        return ab

    else:
        print("\n----------------------")
        print(f" 2 * f({n} - 4) + 5 = ?")
        print(f" 2 * f({n - 4}) + 5 = ?")
        a = f(n- 4)
        print(f" 2 * {a} + 5 = ?")
        ret = 2 * a + 5
        print(f" 2 * f({a}) + 5 = {ret}")
        print("----------------------")
        return ret


print(f"\n"
      f"----------------\n"
      f"F(3) + F(7) = {f(3) + f(7)}")