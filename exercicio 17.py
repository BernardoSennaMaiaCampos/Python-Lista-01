import math

#entrada
valor_galao = 25 # preço
valor_galao = 80 # preco

cobertura = 6 * 1.1 # 6 metros por litro + 10%

litro_lata = 18 # litros
qtd_galao = 3.6 # litros

#area = float(input("Qual o M2?))

# Processamento

#Letra A - lata
litro necessario = area/cobertura #qtd de litros
resp = area/litro_lata #quantidade de tinta das latas
resp = math.ceil(resp) #arredondamento para uma
preco_pago = resp * valor_lata #preço a ser pago

print("Quantidade de galões", qtd)
print("Preço pago R$", preço_pago)

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
