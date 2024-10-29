# Calculadora composta

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador: (+, -, *, /, **):")
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = num1 + num2 
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":   
    resultado = num1 * num2
elif operador == "/":   
    resultado = num1 / num2
elif operador == "**":
    resultado = num1 ** num2
else:
    print("Operador inválido") 
          
# Identificar se o número é positivo ou negativo;
if resultado >= 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"
else:
    sinal = "zero"

# Identificar se o número é par ou impar;

if resultado == int(resultado) and resultado % 2 == 0:
    paridade = "par"
elif resultado == int(resultado) and resultado % 2 != 0:
    paridade = "ímpar"
else:
    paridade = "não aplicável"

# Identificar se o número é inteiro ou decimal;

if resultado == int(resultado):
    inteiro = "inteiro"
else:
    inteiro = "decimal"

print(f"O resultado {num1} {operador} {num2} é = {resultado} é {sinal}, {paridade} e {inteiro}.")

