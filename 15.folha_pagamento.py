# Sistema folha de pagamento

def calcular_ir(salario_bruto):
    """Calcula o desconto do imposto de renda."""
    if salario_bruto <= 2112.00:
        return 0
    elif salario_bruto <= 2826.65:
        return salario_bruto * 0.075
    elif salario_bruto <= 3751.05:
        return salario_bruto * 0.15
    elif salario_bruto <= 4664.68:
        return salario_bruto * 0.225
    else:
        return salario_bruto * 0.275

def main():
    # Solicitar o valor da hora de trabalho e a quantidade de horas trabalhadas no mês
    valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

    # Calcular o salário bruto
    salario_bruto = valor_hora * horas_trabalhadas

    # Calcular os descontos
    desconto_ir = calcular_ir(salario_bruto)
    desconto_sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11  # FGTS não é descontado, apenas informado

    # Calcular o salário líquido
    salario_liquido = salario_bruto - desconto_ir - desconto_sindicato

    # Exibir os resultados
    print(f"Salário Bruto: R${salario_bruto:.2f}")
    print(f"Desconto IR: R${desconto_ir:.2f}")
    print(f"Desconto Sindicato: R${desconto_sindicato:.2f}")
    print(f"FGTS (não descontado): R${fgts:.2f}")
    print(f"Salário Líquido: R${salario_liquido:.2f}")

# Executar o programa principal
if __name__ == "__main__":
    main()