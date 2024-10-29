# Identificar letras vogais ou consoantes

letra = input("Digite uma letra: ")

vogal = ["a", "e", "i", "o", "u"]
if letra in vogal:
    print("A letra digitada é uma vogal")

else:
    print("A letra digitada é uma consoante")
