#
#  Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.

print("\t ----Verificação de Inteiros Positivos,Negativos ou Neutros ---- ")

numero = int(input("Digite um valor inteiro para verificar ou 'sair' para sair: "))

if numero > 0:
    print(f"o número {numero} é positivo!")

elif numero < 0:
    print(f"o número {numero} é negativo!")

else:
    print(f"o número {numero} é neutro!")