#
# Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3 valores a, b e c.
# Se o valor de i é par então calcular e imprimir na tela a média aritmética de a, b e c. Caso contrário,
# se i>10 então calcular e imprimir na tela a média aritmética e ponderada de a, b e c. Os pesos dos valores
# são respectivamente 2, 3 e 4.
import sys
print("\t ---- Comprarações entre números ---- ")

i = float(input("Digite um valor inteiro e positivo para i ou um valor negativo para fechar o programa: "))

if i <= 0:
    print("O programa vai ser terminado! ")
    sys.exit();

print(f"O número 'i' digitado foi {i}")

if i > 0:
    a = float(input("Digite um valor para a: "))
    b = float(input("Digite um valor para b: "))
    c = float(input("Digite um valor para c: "))

if i % 2 == 0 and i >= 0:
    print(f"A média aritmética de {a},{b},{c} é {(a + b + c) / 3}")

if i > 10:
    print(f"A média ponderada de {a},{b},{c} é {(a*2 + b*3 + c*4) / (2+3+4)}")

