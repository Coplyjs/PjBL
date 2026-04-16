import matplotlib.pyplot as plt
import numpy as np

# == TO-DO LIST ==
# Funções oferta, demanda e ponto de equilíbrio
# Menu
# Comandos
# Plotar funções no gráfico
# ================

# == PASSO A PASSO DO CÓDIGO ==

# O objetivo do nosso código é facilitar o entendimento das curvas de oferta, demanda,
# e ponto de equilíbrio. O programa irá calcular e exibir graficamente duas curvas de
# oferta e duas curvas de demanda, representando diferentes cenários.

# Primeiro, definimos funções matemáticas para representar a oferta e a demanda,
# ambas como funções lineares dependentes do preço.

# Em seguida, criamos uma função que calcula o ponto de equilíbrio, ou seja,
# o ponto onde a quantidade ofertada é igual à quantidade demandada.

# Depois, o programa irá permitir que o usuário insira ou altere os valores
# das variáveis (como interceptos e inclinações das curvas), possibilitando
# simular mudanças no mercado.

# Com base nesses valores, geramos um conjunto de preços e calculamos as
# quantidades ofertadas e demandadas correspondentes para cada curva.

# Em seguida, utilizamos a biblioteca matplotlib para plotar os gráficos das
# curvas de oferta e demanda, permitindo visualizar seus deslocamentos.

# Também destacamos no gráfico os pontos de equilíbrio de cada cenário,
# facilitando a comparação entre eles.

# Por fim, o programa pode incluir um menu interativo que permite ao usuário
# repetir o processo, testar diferentes valores e observar como as mudanças
# afetam o equilíbrio de mercado.

# == Varíaveis Globais ==

antiga = [20,2,2,1]
atual = [5,10,15,20]

# == INICÍO DO CÓDIGO ==

# Função oferta (Função linear, y=ax+b)
# c = Constante onde a função intercepta o eixo Y
# d = Inclinação da curva de oferta (Positiva)
# p = Preço do bem

def oferta(c, d, p):
    return c + d*p

# Função demanda (Função linear, y=ax+b)
# a = Quantidade máxima demandada quando o preço é zero
# b = Inclinação da curva de demanda (Negativa)
# p = Preço do bem

def demanda(a, b, p):
    return a - b*p

# Função Preço de equilíbrio (Função que encontra ponto onde oferta e demanda se encontram)

def pontoDeEquilibrio(a,b,c,d):
    return (a-c)/(b+d)

# == Mudar todos os valores ==

def opcao1():
    print("Abacate")

# == Mudar curva de oferta ==

def opcao2():
    print("Abacate")

# == Mudar curva de demanda ==

def opcao3():
    print("Abacate")

# == Plotar gráfico ==

def plotar():
    p = np.linspace(0, 20, 100)

    a = antiga[0]
    b = antiga[1]
    c = antiga[2]
    d = antiga[3]

    qd = demanda(a, b, p)
    qs = oferta(c, d, p)

    # ponto de equilíbrio
    pe = pontoDeEquilibrio(a, b, c, d)
    qe = oferta(c, d, pe)

    plt.figure(figsize=(8, 5))

    # gráfico no padrão econômico (Quantidade no X, Preço no Y)
    plt.plot(qd, p, label='Demanda', color='blue', linewidth=2)
    plt.plot(qs, p, label='Oferta', color='red', linewidth=2)

    # ponto de equilíbrio
    plt.scatter(qe, pe, color='black')
    plt.text(qe, pe, f' E({qe:.2f}, {pe:.2f})')

    plt.title('Oferta e Demanda')
    plt.xlabel('Quantidade')
    plt.ylabel('Preço')
    plt.legend()

    plt.show()

# == Loop do Menu ==

def loopMenu():

    while(True):
        opcao = input("\n 1 - Mudar todos valores\n 2 - Mudar curva de oferta\n 3 - Mudar curva de demanda\n 4 - Plotar gráfico\n 5 - Sair\n : ")

        if(opcao == "1"):

            opcao1()

        elif(opcao == "2"):

            opcao2()

        elif(opcao == "3"):

            opcao3()

        elif(opcao == "4"):

            plotar()

        elif(opcao == "5"):

            break

        else:
            print("Digite uma opção válida!")

loopMenu()


