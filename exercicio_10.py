#
# Faça um programa em linguagem Python, que lê um número n e imprime os n primeiros números da sequência de Fibonacci.

print("\t ---- Fazendo uma sequência de Fibonacci ---- ")

termos = int(input("Digite um número de termos para criar uma sequência de Fibonacci: "))
fibonacci_1 = 0
fibonacci_2 = 1


print("Metodo 1")
for i in range(termos):
    print(fibonacci_1)
    fibonacci_3 = fibonacci_1 + fibonacci_2
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_3

print("Metodo 2")
fibonacci_1 = 0
fibonacci_2 = 1
contador = 0
while contador < termos:
    print(fibonacci_1)
    fibonacci_3 = fibonacci_1 + fibonacci_2
    fibonacci_1 = fibonacci_2
    fibonacci_2 = fibonacci_3
    contador +=1
    




