tupla = (
    ("chave", "valor"),
    ("chave2","valor2"),

)


exemplo = [(y,x) for x,y in tupla]
exemplo = dict(exemplo) #convertendo para dicionário
print(tupla)
print()
print(exemplo)