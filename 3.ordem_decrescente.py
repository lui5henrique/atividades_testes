# Mostrar números digitados em ordem decrescente
"""
    #cria uma lista vazia - será utilizada para armazenar os números digitados
    numeros = [] 

    #inicia um loop "for" / "i" significa o indice de repetições
    for i in range(5): 

    #input captura o número digitado / int converte para nº inteiro
    num = int(input("Digite um número: ")) 

    #append adiciona em "numeros" os númerosdigitados em "num"
    numeros.append(num) 

    #sort(reverse=true) ordena os números em ordem decrescente
    numeros.sort(reverse=True)  

    print(numeros)"""

numeros = []

for i in range(3):
    num = int(input("Digite um número:"))
    numeros.append(num)

numeros.sort(reverse=True)

print(numeros)