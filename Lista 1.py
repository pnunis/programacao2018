#Faça um programa que leia um número n inteiro qualquer (n é um valor inteiro positivo passado como parâmetro
#na linha de comando, se o valor de n não for informado ele deve ser solicitado no início do programa) e mostre
#na tela a sua tabuada de multiplicação

n = int(input("Digite um numero:"))
a = 1
while a <= 10:
     print(n*a)
     a = a + 1
