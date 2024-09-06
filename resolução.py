import math

# Entrada
valor_galao = 25  # preço
valor_lata = 80  # preço

cobertura = 6  # 6 metros por litro

litro_lata = 18  # litros
litro_galao = 3.6  # litros

# area informada
area = float(input("Qual o M2? "))

# PROCESSAMENTO
# Letra A - Lata
print("#############################")
print("Letra A")
litro_necessario = (area / cobertura) * 1.1  # qtd de litros + 10%
qtd = litro_necessario / litro_lata  # quantidade de latas
qtd = math.ceil(qtd)  # piso superior
preco_pago = qtd * valor_lata  # preço a ser pago

print("Quantidade de latas ", qtd)
print("Preço pago R$", preco_pago)

# Letra B - GALAO
print("#############################")
print('Letra B')
litro_necessario = (area / cobertura) * 1.1  # qtd de litros + 10%
qtd = litro_necessario / litro_galao  # quantidade de galõesn
qtd = math.ceil(qtd)  # piso superior
preco_pago = qtd * valor_galao  # preço a ser pago

print("Quantidade de galões ", qtd)
print("Preço pago R$", preco_pago)

# LETRA C
print("#############################")
print("Letra C")
litro_necessario = (area / cobertura) * 1.1  # qtd de litros + 10%
if litro_necessario > (litro_galao * 3):
    qtd_lata = litro_necessario / litro_lata  # quantidade de latas
    qtd_lata = math.floor(qtd_lata)  # piso inferior
    litro_resto = litro_necessario % litro_lata

    qtd_galao_resto = litro_resto / litro_galao
    qtd_galao_resto = math.ceil(qtd_galao_resto)
    if qtd_galao_resto <= 3:
        preco_pago = (qtd_lata * valor_lata) + (qtd_galao_resto * valor_galao)   # preço a ser pago

        print("Quantidade de latas ", qtd_lata)
        print("Quantidade de galões ", qtd_galao_resto)
        print("Preço pago R$", preco_pago)

    else:
        qtd_lata = qtd_lata + 1
        preco_pago = (qtd_lata * valor_lata)
        print("Quantidade de latas ", qtd)
        print("Preço pago R$", preco_pago)
