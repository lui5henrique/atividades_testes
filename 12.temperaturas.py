# Solicitar 5 temperaturas e informar qual a menor e maior temperatura.

def main():
    # Inicializar uma lista para armazenar as temperaturas
    temperaturas = []

    # Solicitar ao usuário que insira 5 temperaturas
    for i in range(5):
        temp = float(input(f"Digite a temperatura {i+1}: "))
        temperaturas.append(temp)

    # Encontrar a maior e a menor temperatura
    maior_temp = max(temperaturas)
    menor_temp = min(temperaturas)

    # Exibir os resultados
    print(f"A maior temperatura é: {maior_temp}")
    print(f"A menor temperatura é: {menor_temp}")

# Executar o programa principal
if __name__ == "__main__":
    main()