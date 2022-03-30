
# Dada a atual crise hídrica do país, as pessoas começaram a construir reservatórios para armazenar água em suas
# propriedades. Faça um programa em linguagem Python que auxilie os utilizadores do reservatório a controlarem seu
# consumo. Obtenha do teclado as dimensões de um reservatório (altura, largura e comprimento, em centímetros) e o
# consumo médio diário dos utilizadores do reservatório (em litros/dia).
# Assuma que o reservatório esteja cheio, tenha formato cúbico e informe:
# (a) A capacidade total do reservatório, em litros;
# (b) A autonomia do reservatório, em dias;
# (c) A classificação do consumo, de acordo com a quantidade de dias de autonomia: Consumo elevado, se a autonomia for
# menor que 2 dias; Consumo moderado, se a autonomia estiver entre 2 e 7 dias; Consumo reduzido, se a autonomia maior
# que 7 dias.
# Observação: Considere que cada litro equivale a 1000 cm3 ou 1 dm3 .

print("\t ---- Cálculo do Reservatóri e Autonômia ---- ")

largura = float(input("Qual a largura do reservatório em centimetros: "))
comprimento = float(input("Qual o comprimento do reservatório em centimetros: "))
altura = float(input("Qual a altura do reservatório em centimetros: "))
consumo = float(input("Qual o consumo diario em litros: "))

volume_em_metros = largura * comprimento * altura

volume_em_litros = volume_em_metros/1000

print(f"O reservátorio tem um volume de {volume_em_litros} litros.")

autonomia = volume_em_litros/consumo

print("A autonomia do reservatório é de {:.2f} dias.".format(autonomia))

if autonomia < 2:
    print("Consumo elevado!")

elif autonomia > 7:
    print("Consumo reduzido!")

else:
    print("Consumo moderado!")



