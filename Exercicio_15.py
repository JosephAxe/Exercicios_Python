#
# Escrever um programa em Python para ler um número inteiro e informar se ele é divisível por 5.

print("\t ---- É divisivel por 5? ----")

numero = int(input("Digite um número para saber se ele é divisível por 5: "))

if numero % 5 == 0:
    print(f"O número {numero} é divisivel por 5!")

else:
    print(f"O número {numero} não é divisivel por 5!")