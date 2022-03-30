
# Faça um programa em Python para encontrar a mediana de três valores inseridos pelo usuário.

print("\t ---- Cálculo da mediana de 3 números ----")
lista =[]

for i in range(3):
    lista.append(int(input(f"Digite o {i+1}º numero: ")))

print("\nMetodo 1")
lista_organizada =sorted(lista)
print(f"A mediana dos 3 valore é: {lista_organizada[1]}")

print("\nMetodo 2")

num0 = lista[0]
num1 = lista[1]
num2 = lista[2]

if num0 < num1 < num2 or num0 > num1 > num2:
    mediana = num1

elif num0 < num2 < num1 or num0 > num2 > num1:
    mediana = num2

elif num1 < num0 < num2 or num1 > num0 > num2:
    mediana = num0

print(f"A mediana dos 3 valore é: {mediana}")

print("\nMetodo 3")
num3 = num2
num2 = num1
num1 = num0



if num1 > num2:
    if num1 < num3:
        mediana = num1
    elif num2 > num3:
        mediana = num2
    else:
        mediana = num3
else:
    if num1 > num3:
        mediana = num1
    elif num2 < num3:
        mediana = num2
    else:
        mediana = num3

print(f"A mediana dos 3 valore é: {mediana}")