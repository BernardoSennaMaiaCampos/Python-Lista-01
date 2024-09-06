# temperatura da sala : temp
temp = float(input("Digite a temperatura: "))
ar_condicionado_status = False


# Condição => SE...ENTÃO...SENÃO

if temp >= 24:
    ar_condicionado_status = True
    print("Ligando o ar")
else:
    print("Não preciso ligar o ar")

