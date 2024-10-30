# Um sistema que aceite números inteiros e informe se é ou não um número primo.

def eh_primo(n):
    #Verifica se um número é primo.
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 é o único número primo par
    if n % 2 == 0:
        return False  # elimina números pares maiores que 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    # Solicitar um número do usuário
    numero = int(input("Digite um número inteiro: "))

    # Verificar se o número é primo
    if eh_primo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

# Executar o programa principal
if __name__ == "__main__":
    main()