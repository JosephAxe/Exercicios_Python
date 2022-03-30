#
# Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5.
# Os números obtidos devem ser impressos em sequência.

print("\t ---- Teste divisivel por 7 sem ser multiplo de 5 ----")

print("Testando números entre 5 e 100 . . .")

for numero in range(5,100,1):

    if numero % 7 == 0 and numero % 5 != 0:
        print(f"O número {numero} é divisível por 7 ({numero/7}) mas não é multiplo de 5!")

print("\nTodos os números de 5 a 100 foram verificados!")
