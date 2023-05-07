#Escreva um programa que imprima os números de 1 a 100. Mas, para múltiplos de três, imprima "Fizz" em vez do número e, para múltiplos de cinco, imprima "Buzz". Para números que são múltiplos de três e cinco, imprima "FizzBuzz".
for i in range (1,100):
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else: 
        print(i)