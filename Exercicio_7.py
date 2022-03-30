#
# Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número
# digitado. Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).

print("\t ---- Soma de todos os numeros de 1 até o valor digitado ---- ")

numero_digitado = int(input("Digite um número pra fazermos a soma: "))

soma = 1

while numero_digitado != 1:

    soma = soma + numero_digitado

    if numero_digitado > 0:
        numero_digitado -=1

    else:
        numero_digitado +=1



print(f"A soma dos valores da expressão é igual a {soma}")
