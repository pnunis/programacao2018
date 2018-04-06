#Faça um programa que leia um número n inteiro qualquer (n é um valor inteiro positivo passado como parâmetro
#na linha de comando, se o valor de n não for informado ele deve ser solicitado no início do programa) e mostre
#na tela a sua tabuada de multiplicação

n = int(input("Digite um numero:"))
a = 1
while a <= 10:
     print(n*a)
     a = a + 1
    #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. 
"""
km = int(input("Digite a qtde de km rodado: "))
dias = int(input("Digite a qtde de dias: "))

print ('Valor do aluguel: R$ %.2f' %(km*0.15 + dias*60) )
#3
"""
Faça um Programa que leia três números e mostre o maior deles.
"""
n1 = int(input('digite primeiro número: '))

n2 = int(input('digite segundo número: '))

n3 = int(input('digite segundo número: '))

media = (n1+n2+n3)/ int(3)

maior = n1
menor = n1

if maior < n2:
	maior = n2

if maior < n3: 
	maior = n3

if menor > n2:
	menor = n2

if menor > n3:
	menor = n3
print('media de n: %d' %media)
print ('Maior:  %d ' %maior)
print ('Menor:  %d ' %menor)

#4
"""
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de 
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número 
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc. 
"""
fibo = [1,1]
i = 0
num = int(input("Entre com um número: "))

while num > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i+=1

print ('Fibonacci(%d): %d' %(num,fibo[num-1]))
#ou
"""
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
o algoritmo de Euclides. 
"""
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 < n2:
	n1, n2 = n2, n1

r1, mdc = n1%n2, n2
while r1 != 0:
	r1, mdc = mdc%r1, r1
	
print ('O mdc de (%d,%d) é: %d'%(n1,n2,mdc))
