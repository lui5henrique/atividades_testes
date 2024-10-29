# Identificar qual o produto mais barato

preco1 = float(input("Digite o valor do primeiro produto:")) 
preco2 = float(input("Digite o valor do segundo produto:"))
preco3 = float(input("Digite o valor do terceiro produto"))

if preco1 < preco2 and preco1 < preco3:
    print("O primeiro produto é o mais barato")

elif preco2 < preco1 and preco2 < preco3:
    print("O segundo produto é o mais barato")

elif preco3 < preco1 and preco3 < preco2:
    print("O terceiro produto é o mais barato")

else:
    print("Todos os produto possuem preços iguais")