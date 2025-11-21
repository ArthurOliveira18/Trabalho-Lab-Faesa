import pandas as pd

# --- Variáveis Globais ---
linha = 3
coluna = 4
mes = ["Janeiro", "Fevereiro", "Março", "Abril"]
redesSociais = ["Instagram", "Facebook", "Twitter"]


def matrizMaisSeguidores():
    matrizGanhos = []
    print("\n--- Cadastro de GANHOS de Seguidores ---")

    for l in range(linha):
        linhaAtual = []
        # Nome da rede social atual
        rede_atual = redesSociais[l]

        for c in range(coluna):
            while True:
                try:
                    prompt = f"Seguidores ganhos no {rede_atual} em {mes[c]}: "
                    valor_digitado = input(prompt)
                    valorAtual = int(valor_digitado)
                    linhaAtual.append(valorAtual)
                    break
                except ValueError:
                    print("Valor inválido! Digite apenas números inteiros.")

        matrizGanhos.append(linhaAtual)

    print("Dados de ganhos cadastrados com sucesso!")
    # IMPORTANTE: Retorna a matriz preenchida para quem chamou a função
    return matrizGanhos


def menosSeguidores():
    matrizPerdas = []
    print("\n--- Cadastro de PERDAS de Seguidores ---")

    for l in range(linha):
        linhaAtual = []
        rede_atual = redesSociais[l]

        for c in range(coluna):
            while True:
                try:
                    prompt = f"Seguidores perdidos no {rede_atual} em {mes[c]}: "
                    valor_digitado = input(prompt)
                    valorAtual = int(valor_digitado)
                    linhaAtual.append(valorAtual)
                    break
                except ValueError:
                    print("Valor inválido! Digite apenas números inteiros.")

        matrizPerdas.append(linhaAtual)

    print("Dados de perdas cadastrados com sucesso!")
    # IMPORTANTE: Retorna a matriz preenchida
    return matrizPerdas


# --- FUNÇÃO COM PANDAS ---
def mostrarTabela(dadosGanhos, dadosPerdidos):
    # Verificação de segurança: se as listas estiverem vazias ou None
    if not dadosGanhos or not dadosPerdidos:
        print("\n[ERRO] Não há dados para exibir. Cadastre-os primeiro.")
        return

    print("\n" + "=" * 40)
    print("RELATÓRIO FINAL (FORMATO MATRIZ)")
    print("=" * 40)

    # 1. Criando o DataFrame de GANHOS
    # data = os números (sua matriz)
    # index = os rótulos das linhas (Instagram, Facebook...) - Igual "ALUNOS" na imagem
    # columns = os rótulos das colunas (Jan, Fev...) - Igual "Mes1, Mes2" na imagem
    df_ganhos = pd.DataFrame(data=dadosGanhos, index=redesSociais, columns=mes)

    # 2. Criando o DataFrame de PERDAS
    df_perdas = pd.DataFrame(data=dadosPerdidos, index=redesSociais, columns=mes)

    print("\n--- Tabela de GANHOS de Seguidores ---")
    print(df_ganhos)

    print("\n" + "-" * 40)

    print("\n--- Tabela de PERDAS de Seguidores ---")
    print(df_perdas)
