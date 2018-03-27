#Faça um programa que leia um número n inteiro qualquer (n é um valor inteiro positivo passado como parâmetro
#na linha de comando, se o valor de n não for informado ele deve ser solicitado no início do programa) e mostre
#na tela a sua tabuada de multiplicação

n = int(input("Tabuada de:"))
x = 1
while x <= 10:
     print(n+x)
     x = x + 1
