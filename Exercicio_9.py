#
# Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado.
# Por exemplo, se o número é 2021 , então a saída deve ser 4

print("\t ---- Contador de Digítos ---- ")

entrada = int(input("Digite um número para saber o número de digito: "))
print("Metodo 1")
numero = entrada
contador = 0
while numero / 10 >= 1:
    numero = numero / 10
    contador += 1
print(f"O número {entrada} possui {contador + 1} digitos")
#################################################################################
print("Metodo 2")
numero = entrada
contador = 0
while numero != 0:
    numero //= 10
    contador += 1
print(f"O número {entrada} possui {contador} digitos")
