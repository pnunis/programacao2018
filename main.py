"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.
"""

""" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
            Explicação do cálculo das notas:
1° - Precisamos saber quantas notas podemos usar com determinado valor.
     Para isso precisamos dividir o valor do saque pelo valor da nota. Ex:
        Saque: 256      Nota: 100
        256 / 100 = 2.56
        
    Não podemos utilizar 56% de uma nota de 100, então pegamos apenas a parte 
    inteira da divisão, pois é quantidade de notas de 100 que podemos usar.
    Para isso podemos usar:
        math.floor(256/100) ou int(256/100) ou o mais prático floor division (//)
        
    Então se 256/100=2.56 com floor division fica 256//100=2.
    Agora que sabemos que precisamos de 2 notas de 100 vamos ao próximo passo
    
2° - Subtrair o valor de notas de 100 do valor do saque para que o cálculo das outras
    notas não contem nenhum valor que já foi pago.
    
3º - Repetir para todas as notas.

OBS.: Com esse método não será necessário calcular a quantidade de notas de 1 real,
        pois a quantidade será o que restar do total.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""


# Método simples e didático sem uso de conceitos avançados
def metodo_1(valor):
    valor_total = valor  # não será utilizado nos cálculos, só serve pra dar print depois
    
    notas100 = valor // 100  # calcula quantas notas de R$ 100 são necessárias
    valor -= notas100 * 100  # subtrai valor já pago em notas de 100
    
    notas50 = valor // 50
    valor -= notas50 * 50
    
    notas10 = valor // 10
    valor -= notas10 * 10
    
    notas5 = valor // 5
    valor -= notas5 * 5
    
    # notas de 1 real é o que sobrou na variável "valor"
    # criei print_notas só pra ficar mais legível no console
    print_notas(valor_total, valor, notas5, notas10, notas50, notas100)
    
    
# Métodos com conceitos mais "avançados" (links para leitura nos comentários)
def metodo_2(valor):
    valor_total = valor
    notas = [100, 50, 10, 5, 1]
    qtds = []
    
    # mesma lógica que metodo_1
    for nota in notas:
        qtd = valor//nota
        valor -= nota * qtd
        qtds.append(qtd)

    # inverte a ordem da lista, pois no está em ordem decrescente
    # e na função print_notas os parâmetros passados são do menor para o maior
    qtds = reversed(qtds)
    
    # passa o valor_total e faz o unpacking das quantidades e passa para a função
    # https://docs.python.org/3.6/tutorial/controlflow.html#unpacking-argument-lists
    print_notas(valor_total, *qtds)
    
    

# Ignora essa função, é só pra printar os valores
def print_notas(total, notas1, notas5, notas10, notas50, notas100):
    template = "R$ {:>3}: {:>3} notas"
    print("- Valor do saque: R$ " + str(total))
    print(template.format("100", notas100))
    print(template.format("50", notas50))
    print(template.format("10", notas10))
    print(template.format("5", notas5))
    print(template.format("1", notas1))
    print()
    

# = = = = = = = = = = = = = = = 

valor = int(input('Quanto deseja sacar? '))

print('= = = metodo_1 = = =')
resposta1 = metodo_1(valor)

print('= = = metodo_2 = = =')
resposta2 = metodo_2(valor)

