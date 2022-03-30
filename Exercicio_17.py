#
# Escreva um programa em Python para encontrar números entre 100 e 400 (ambos inclusos), onde cada dígito de um
# número é um número par. Os números obtidos devem ser impressos em sequência separada por vírgulas.

print("\t ---- Encontrando os Pares ---- ")


lista =[]

for i in range(100,401):
    s = str(i)

    if int(s[0])%2 == 0 and int(s[1])%2 == 0 and int(s[2])%2 == 0:
        lista.append(s)

print(",".join(lista))