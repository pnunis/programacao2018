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
