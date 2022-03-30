
#  Escreva um programa em Python para calcular o fatorial de qualquer número inteiro.

print("\t ---- Cálculo do Fatoria! ----")

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

if numero < 0:
    print("Não existe fatorial para número negativo")

elif numero == 0:
    print("O fatorial de 0 é 1")

else:
    for i in range(1,numero+1):
        fatorial = fatorial*i

print(f"O fatorial de {numero} é igual a {fatorial}")

