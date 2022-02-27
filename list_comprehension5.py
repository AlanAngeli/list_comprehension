lista = list(range(100))
print(lista)
print()

ex = [v for v in lista if v % 2 == 0] #nota: mesma coisa que "ex = [v * 2 for v in lista]"
print(ex)
print()

ex2 = [v for v in lista if v % 3 == 0 if v % 8 == 0] #números da lista que são divisíveis por 3 e 8
print(ex2)
print()

ex3 = [v if v % 3 == 0 else "-" for v in lista]
print(ex3)
print()

ex4 = [v if v % 3 == 0 and v % 8 == 0 else "-" for v in lista]
print(ex4)
print()