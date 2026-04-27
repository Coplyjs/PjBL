import matplotlib.pyplot as plt
import numpy as np

# =========================
# VARIÁVEIS GLOBAIS
# =========================
antiga = [20, 2, 2, 1]
atual = None

# =========================
# MODELO ECONÔMICO
# =========================
def oferta(c, d, p):
    return c + d * p

def demanda(a, b, p):
    return a - b * p

def pontoDeEquilibrio(a, b, c, d):
    if b + d == 0:
        return None

    pe = (a - c) / (b + d)

    if pe < 0:
        return None

    return pe


# =========================
# INPUT SEGURO (BLINDAGEM)
# =========================
def ler_valor(nome, positivo=False):
    while True:
        try:
            v = float(input(f"Digite o valor de {nome}: "))

            if positivo and v <= 0:
                print("❌ Esse valor não pode ser 0 ou negativo.")
                continue

            if not positivo and v < 0:
                print("❌ Esse valor não pode ser negativo.")
                continue

            return v

        except ValueError:
            print("❌ Digite um número válido.")


# =========================
# OPÇÕES
# =========================
def opcao1():
    global antiga, atual

    a = ler_valor("A")
    b = ler_valor("B", positivo=True)  # BLINDADO
    c = ler_valor("C")
    d = ler_valor("D", positivo=True)  # BLINDADO

    if atual is not None:
        antiga = atual.copy()

    atual = [a, b, c, d]


def opcao2():
    global antiga, atual

    if atual is None:
        atual = antiga.copy()

    c = ler_valor("C")
    d = ler_valor("D", positivo=True)  # BLINDADO

    antiga = atual.copy()
    atual[2] = c
    atual[3] = d


def opcao3():
    global antiga, atual

    if atual is None:
        atual = antiga.copy()

    a = ler_valor("A")
    b = ler_valor("B", positivo=True)  # BLINDADO

    antiga = atual.copy()
    atual[0] = a
    atual[1] = b


# =========================
# GRÁFICO
# =========================
def plotar():
    global antiga, atual

    fig, ax = plt.subplots(figsize=(10, 6))

    a1, b1, c1, d1 = antiga

    if atual is not None:
        a2, b2, c2, d2 = atual
    else:
        a2, b2, c2, d2 = a1, b1, c1, d1

    # evita divisão por zero aqui também
    p_max = max(a1 / b1, a2 / b2)
    p = np.linspace(0, p_max, 300)

    # ======================
    # ANTES
    # ======================
    qd1 = demanda(a1, b1, p)
    qs1 = oferta(c1, d1, p)

    mask_d1 = qd1 >= 0

    ax.plot(qd1[mask_d1], p[mask_d1],
            label='Demanda (antes)', color='#F97316', linewidth=3)

    ax.plot(qs1, p,
            label='Oferta (antes)', color='#FF2D95', linewidth=3)

    pe1 = pontoDeEquilibrio(a1, b1, c1, d1)
    if pe1 is not None:
        qe1 = oferta(c1, d1, pe1)
        ax.scatter(qe1, pe1, color='black')
        ax.text(qe1, pe1, f'E₀({qe1:.1f}, {pe1:.1f})')

    # ======================
    # DEPOIS
    # ======================
    if atual is not None:
        qd2 = demanda(a2, b2, p)
        qs2 = oferta(c2, d2, p)

        mask_d2 = qd2 >= 0

        ax.plot(qd2[mask_d2], p[mask_d2],
                '--', label='Demanda (depois)', color='#8172B3', linewidth=3)

        ax.plot(qs2, p,
                '--', label='Oferta (depois)', color='#55A868', linewidth=3)

        pe2 = pontoDeEquilibrio(a2, b2, c2, d2)
        if pe2 is not None:
            qe2 = oferta(c2, d2, pe2)
            ax.scatter(qe2, pe2, color='black')
            ax.text(qe2, pe2, f'E₁({qe2:.1f}, {pe2:.1f})')

    # ======================
    # ESTÉTICA
    # ======================
    ax.set_title('Oferta e Demanda', fontsize=14)
    ax.set_xlabel('Quantidade')
    ax.set_ylabel('Preço')

    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.show()


# =========================
# MENU
# =========================
def loopMenu():
    while True:
        opcao = input(
            "\n1 - Mudar todos valores\n"
            "2 - Mudar curva de oferta\n"
            "3 - Mudar curva de demanda\n"
            "4 - Plotar gráfico\n"
            "5 - Sair\n: "
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
            print("Opção inválida!")


# =========================
# EXECUÇÃO
# =========================
loopMenu()
