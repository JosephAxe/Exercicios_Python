
# Escreva um programa Python para verificar se uma letra do Alfabeto(Abecedário) é uma vogal ou consoante.

print("\t ---- Vogal ou Consoante ---- ")

letra = input("Digite uma letra: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"A letra '{letra}' é uma vogal!")

else:
    print(f"A letra '{letra}' é uma consoante!")