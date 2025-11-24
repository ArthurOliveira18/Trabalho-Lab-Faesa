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
    print("-",df_perdas)


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
            matriz_alvo[l][c] = novo_valor # Atualiza diretamente a matriz original
            print("Dado atualizado com sucesso!")
            break
        except ValueError:
            print("Erro: O valor deve ser um número inteiro.")