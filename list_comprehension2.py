l1 = ["Alan", "Eloisa", "Kate"]
ex1 = [v.replace("a", "@") for v in l1] #substituir a letra a por @
print(ex1)
print()

l2 = ["Alan", "Eloisa", "Kate"]
ex2 = [v.replace("a", "@").upper() for v in l1]
print(ex2)