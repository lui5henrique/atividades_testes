# Saldo médio e valor de crédito

def calcular_credito(saldo_medio):
    if saldo_medio >= 0 and saldo_medio <= 200:
        credito = 0
    elif saldo_medio >= 201 and saldo_medio <= 400:
        credito = saldo_medio * 0.20
    elif saldo_medio >= 401 and saldo_medio <= 600:
        credito = saldo_medio * 0.30
    elif saldo_medio >= 601:
        credito = saldo_medio * 0.40
    else:
        credito = 0  # Caso saldo médio seja um valor negativo, o que não é esperado conforme a tabela
    return credito

def main():
    # Solicitar o saldo médio do cliente
    saldo_medio = float(input("Digite o saldo médio do cliente: "))

    # Calcular o crédito baseado no saldo médio
    credito = calcular_credito(saldo_medio)

    # Mostrar a mensagem informando o saldo médio e o valor do crédito
    print(f"Saldo médio: R${saldo_medio:.2f}")
    print(f"Valor do crédito: R${credito:.2f}")

# Executar o programa principal
if __name__ == "__main__":
    main()