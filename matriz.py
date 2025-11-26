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
    # IMPORTANTE: Retorna a matriz preenchida, e com esse retorno da matriz preenchida, eu crio uma variavel no arquivo principal e armazeno esse return, ou seja, o resultado essa matriz na variavel.
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
    # IMPORTANTE: Retorna a matriz preenchida, e com esse retorno da matriz preenchida, eu crio uma variavel no arquivo principal e armazeno esse return, ou seja, o resultado essa matriz na variavel.
    return matrizPerdas


# --- FUNÇÃO COM PANDAS ---
def mostrarTabela(dadosGanhos, dadosPerdidos):
    # Verificação de segurança
    if not dadosGanhos or not dadosPerdidos:
        print("\n[ERRO] Não há dados para exibir. Cadastre-os primeiro.")
        return

    print("\n" + "=" * 40)
    print("RELATÓRIO FINAL (FORMATO MATRIZ)")
    print("=" * 40)

    # 1. Criando o DataFrame de GANHOS (Normal)
    df_ganhos = pd.DataFrame(data=dadosGanhos, index=redesSociais, columns=mes)

    # 2. Criando o DataFrame de PERDAS
    # Criamos o DataFrame com os dados originais
    df_perdas = pd.DataFrame(data=dadosPerdidos, index=redesSociais, columns=mes)

    # TRUQUE: Multiplicamos o DataFrame inteiro por -1 apenas para exibição
    # Assim, visualmente fica negativo, mas sua lista original continua intacta para os cálculos
    df_perdas_visual = df_perdas * -1

    print("\n--- Tabela de GANHOS de Seguidores ---")
    print(df_ganhos)

    print("\n" + "-" * 40)

    print("\n--- Tabela de PERDAS de Seguidores ---")
    # Agora imprimimos a tabela visual com o sinal de menos
    print(df_perdas_visual)


def atualizarDados(dadosGanhos, dadosPerdidos):
    # Validação: Se as listas estiverem vazias ou não existirem
    if not dadosGanhos or not dadosPerdidos:
        print("\n[ERRO] As matrizes estão vazias. Execute a opção 1 primeiro.")
        return

    print("\n--- ATUALIZAÇÃO DE DADOS ---")

    # 1. Escolher qual matriz editar
    while True:
        print("\nQual tabela deseja alterar?")
        print("1 - Tabela de Ganhos")
        print("2 - Tabela de Perdas")
        op = input("Opção: ")

        if op == "1":
            matriz_alvo = dadosGanhos
            nome_tabela = "GANHOS"
            break
        elif op == "2":
            matriz_alvo = dadosPerdidos
            nome_tabela = "PERDAS"
            break
        else:
            print("Opção inválida. Digite 1 ou 2.")

    # 2. Escolher LINHA (Rede Social) pelo índice
    print(f"\nSelecione a Rede Social em {nome_tabela}:")
    for i, rede in enumerate(redesSociais):
        print(f"{i} - {rede}")

    while True:
        try:
            l = int(input("Digite o número da linha: "))
            if 0 <= l < linha:
                break
            print(f"Erro: Digite um valor entre 0 e {linha-1}")
        except ValueError:
            print("Erro: Digite um número inteiro.")

    # 3. Escolher COLUNA (Mês) pelo índice
    print(f"\nSelecione o Mês em {nome_tabela}:")
    for i, m in enumerate(mes):
        print(f"{i} - {m}")

    while True:
        try:
            c = int(input("Digite o número da coluna: "))
            if 0 <= c < coluna:
                break
            print(f"Erro: Digite um valor entre 0 e {coluna-1}")
        except ValueError:
            print("Erro: Digite um número inteiro.")

    # 4. Atualizar o valor
    valor_antigo = matriz_alvo[l][c]
    print(f"\nValor atual de {redesSociais[l]} em {mes[c]}: {valor_antigo}")

    while True:
        try:
            novo_valor = int(input("Digite o NOVO valor: "))
            matriz_alvo[l][c] = novo_valor  # Atualiza diretamente a matriz original
            print("Dado atualizado com sucesso!")
            break
        except ValueError:
            print("Erro: O valor deve ser um número inteiro.")


def gerarRelatorio(dadosGanhos, dadosPerdidos):
    # 1. Verificação: Se os dados não existem (Requisito: Exibir mensagem caso dados não sejam encontrados)
    if not dadosGanhos or not dadosPerdidos:
        print(
            "\n[AVISO] Dados não encontrados. Por favor, realize o cadastro (Opção 1) primeiro."
        )
        return

    print("\n" + "=" * 40)
    print("RELATÓRIO DE DESEMPENHO (FILTRO POR REDE)")
    print("=" * 40)

    # 2. Filtro: Usuário escolhe qual Rede Social quer analisar
    print("Selecione a Rede Social para filtrar os dados:")
    for i, rede in enumerate(redesSociais):
        print(f"{i} - {rede}")

    indice_filtro = -1
    while True:
        try:
            op = int(input("Digite o número da rede social: "))
            if 0 <= op < linha:
                indice_filtro = op
                break
            else:
                print(f"Erro: Digite um valor entre 0 e {linha-1}")
        except ValueError:
            print("Erro: Digite um número inteiro.")

    nome_rede = redesSociais[indice_filtro]

    # 3. Processamento: Buscar Maior Ganho e Maior Perda
    # Pegamos a linha específica da rede escolhida
    linha_ganhos = dadosGanhos[indice_filtro]
    linha_perdas = dadosPerdidos[indice_filtro]

    # Acha o maior valor e o índice (mês) onde ele ocorreu
    maior_ganho = max(linha_ganhos)
    mes_maior_ganho_index = linha_ganhos.index(maior_ganho)
    mes_maior_ganho_nome = mes[mes_maior_ganho_index]

    maior_perda = max(linha_perdas)
    mes_maior_perda_index = linha_perdas.index(maior_perda)
    mes_maior_perda_nome = mes[mes_maior_perda_index]

    # 4. Exibição dos Resultados
    print(f"\n--- Análise: {nome_rede.upper()} ---")

    # Resultado de Ganhos
    print(f"Maior crescimento: {maior_ganho} seguidores.")
    print(f"Mês do recorde: {mes_maior_ganho_nome}")

    print("-" * 20)

    # Resultado de Perdas
    print(f"Maior queda: {maior_perda} seguidores.")
    print(f"Mês da maior perda: {mes_maior_perda_nome}")
    print("=" * 40)
