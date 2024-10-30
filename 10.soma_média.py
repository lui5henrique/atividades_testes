# Sistema de repetição de 5 números e informar a soma e a média dos números digitados.

numeros = []

for i in range(5):
    num=int(input("Digite um número:"))
    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)

print(f"A soma dos números digitados é {soma} e a média dos números digitados é {media}")