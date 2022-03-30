
# Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o
# resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.

print("\t ---- Quem é o vencedor? ---- ")

gols_time_1 = int(input("Qual o placar do Time 1?"))
gols_time_2 = int(input("Qual o placar do Time 2?"))

if gols_time_1 > gols_time_2:
    print("O vencedor da partida é o Time 1!")

elif gols_time_1 < gols_time_2:
    print("O vencedor da partida é o Time 2!")

else:
    print("O Time 1 e o Time 2 empataram!")