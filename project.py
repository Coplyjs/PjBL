import matplotlib.pyplot as plt
import numpy as np

# == VARIÁVEIS GLOBAIS ==

antiga = [20, 2, 2, 1]
atual = None

# == FUNÇÕES ==

def oferta(c, d, p):
    return c + d * p

def demanda(a, b, p):
    return a - b * p

def pontoDeEquilibrio(a, b, c, d):
    return (a - c) / (b + d)

# == OPÇÕES ==

def opcao1():
    global antiga, atual

    while True:
        try:
            a = float(input("Digite o valor de A: "))
            if a < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    while True:
        try:
            b = float(input("Digite o valor de B: "))
            if b < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    while True:
        try:
            c = float(input("Digite o valor de C: "))
            if c < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    while True:
        try:
            d = float(input("Digite o valor de D: "))
            if d < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    if atual is not None:
        antiga = atual.copy()

    atual = [a, b, c, d]


def opcao2():
    global antiga, atual

    if atual is None:
        atual = antiga.copy()

    while True:
        try:
            c = float(input("Digite o valor de C: "))
            if c < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    while True:
        try:
            d = float(input("Digite o valor de D: "))
            if d < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    antiga = atual.copy()

    atual[2] = c
    atual[3] = d


def opcao3():
    global antiga, atual

    if atual is None:
        atual = antiga.copy()

    while True:
        try:
            a = float(input("Digite o valor de A: "))
            if a < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    while True:
        try:
            b = float(input("Digite o valor de B: "))
            if b < 0: raise ValueError
            break
        except ValueError:
            print("Digite um número não negativo.")

    antiga = atual.copy()

    atual[0] = a
    atual[1] = b


# == GRÁFICO ==

def plotar():
    global antiga, atual

    p = np.linspace(0, 20, 100)

    fig, ax = plt.subplots(figsize=(10, 6))

    fig.patch.set_facecolor('#F9FAFB')
    ax.set_facecolor('#F9FAFB')

    a, b, c, d = antiga

    qd = demanda(a, b, p)
    qs = oferta(c, d, p)

    pe = pontoDeEquilibrio(a, b, c, d)
    qe = oferta(c, d, pe)

    ax.plot(qd, p, label='Demanda (antes)', color='#F97316', linewidth=3)
    ax.plot(qs, p, label='Oferta (antes)', color='#FF2D95', linewidth=3)

    ax.scatter(qe, pe, color='#111827', s=40, zorder=5)
    ax.text(qe, pe, f' E₀({qe:.1f}, {pe:.1f})', color='#111827')

    if atual is not None:
        a, b, c, d = atual

        qd = demanda(a, b, p)
        qs = oferta(c, d, p)

        pe = pontoDeEquilibrio(a, b, c, d)
        qe = oferta(c, d, pe)

        ax.plot(qd, p, '--', label='Demanda (depois)', color='#8172B3', linewidth=3)
        ax.plot(qs, p, '--', label='Oferta (depois)', color='#55A868', linewidth=3)

        ax.scatter(qe, pe, color='#111827', s=40, zorder=5)
        ax.text(qe, pe, f' E₁({qe:.1f}, {pe:.1f})', color='#111827')

    ax.set_title('Oferta e Demanda', fontsize=16, weight='bold', color='#111827')
    ax.set_xlabel('Quantidade', color='#111827')
    ax.set_ylabel('Preço', color='#111827')

    ax.grid(True, color='#E5E7EB', linewidth=0.8)

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    ax.spines['left'].set_color('#D1D5DB')
    ax.spines['bottom'].set_color('#D1D5DB')

    ax.legend(frameon=False)

    plt.tight_layout()
    plt.show()


# == MENU ==

def loopMenu():
    while True:
        opcao = input(
            "\n 1 - Mudar todos valores\n"
            " 2 - Mudar curva de oferta\n"
            " 3 - Mudar curva de demanda\n"
            " 4 - Plotar gráfico\n"
            " 5 - Sair\n : "
        )

        if opcao == "1":
            opcao1()

        elif opcao == "2":
            opcao2()

        elif opcao == "3":
            opcao3()

        elif opcao == "4":
            plotar()

        elif opcao == "5":
            break

        else:
            print("Digite uma opção válida!")


# == EXECUÇÃO ==
loopMenu()
