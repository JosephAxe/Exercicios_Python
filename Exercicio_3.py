# Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

print("\t ---- Tabuada do Zé ---- ")

numero =int(input("Digite um número para saber a sua tabuada: "))

print("\n Tabuada de", numero, ":")

for i in range(1,11,1):
    produto = i * numero
    print("{} x {} = {}".format(numero,i,produto))