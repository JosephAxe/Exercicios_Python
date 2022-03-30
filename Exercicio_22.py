
# Faça um programa em Python para calcular a soma e a média de n números inteiros inseridos pelo usuário.
# Digite 0 para terminar.

print("\t ---- Somas e Médias ---- ")
print("Digite os números para calcular a soma e as médias.Pressione 0 para iniciar o cálculo:")
sair = False
lista =[]
contador = 0
soma = 0

while sair == False:
    num = int(input("  "))
    contador +=1

    if num == 0:
        sair == True
        break
    else:
        lista.append(num)


for i in range(contador):
    soma = sum(lista)

media = soma/len(lista)

print(lista)
print(soma,media )
