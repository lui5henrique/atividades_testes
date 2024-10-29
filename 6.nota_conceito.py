# Sistema para indentificar aluno APROVADO ou REPROVADO

# Definindo as médias
media_1 = "10 e 9.0" 
media_2 = "8.9 e 7.5" 
media_3 = "7.4 e 6.0"
media_4 = "5.9 e 4.0" 
media_5 = "3.9 e 0.0" 

# Solicitando a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Verificando a faixa de nota e exibindo a mensagem correspondente
if 10 >= nota >= 9.0:
    print(f"O aluno tirou a nota {nota} e ficou com média entre {media_1}. Aprovado")
elif 8.9 >= nota >= 7.5:
    print(f"O aluno tirou a nota {nota} e ficou com média entre {media_2}. Aprovado")
elif 7.4 >= nota >= 6.0:
    print(f"O aluno tirou a nota {nota} e ficou com média entre {media_3}. Aprovado")
elif 5.9 >= nota >= 4.0:
    print(f"O aluno tirou a nota {nota} e ficou com média entre {media_4}. Reprovado")
elif 3.9 >= nota >= 0.0:
    print(f"O aluno tirou a nota {nota} e ficou com média entre {media_5}. Reprovado")
else:
    print("Nota inválida.")