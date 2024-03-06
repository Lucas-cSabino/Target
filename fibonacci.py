"""2)Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma 
dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de 
Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser 
previamente definido no código;"""

a = 0
b = 1
c = 0
fib_seq = [0,1]
range_max = int(input("Informe o número máximo da sequência de Fibonacci: "))
while c <= range_max:
    c = a + b
    fib_seq.append(c)
    a = b
    b = c
isin_fib = int(input("Informe um número: "))

print(fib_seq)

if isin_fib in fib_seq:
    print(f'O número {isin_fib} pertence a sequência de Fibonacci.')
else:
    print(f'O número {isin_fib} não pertence a sequência de Fibonacci.')
