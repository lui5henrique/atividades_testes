# Identificar turno

turno = input ("Digite o turno que você estuda; M - para matutino, V - para vespertino e N - para noturno: ").upper()

if turno == "M":
    print("Bom dia!")

elif turno == "V":
    print("Boa tarde!")

elif turno == "N":
    print("Boa noite!")

else:
    print("Turno inválido!")