# Um programa para solicitar a idade, depois identificar se é aceitável ou não.

idade = int(input("Digite aqui a sua idade, por favor:"))
print(idade)

if idade <= 150:
    print("Idade aceitável")
else:
    print("Idade não aceitável")