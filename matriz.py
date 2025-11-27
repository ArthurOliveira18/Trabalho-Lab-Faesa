import pandas as pd

meses = ["Janeiro", "Fevereiro", "Março", "Abril"]
redes = ["Instagram", "Facebook", "Twitter"]

qtd_redes = len(redes)
qtd_meses = len(meses)


def matrizMaisSeguidores():
    print("\n--- Cadastro de GANHOS de Seguidores ---")
    matriz_temporaria = []

    for i in range(qtd_redes):
        linha_atual = []
        nome_rede = redes[i]

        for j in range(qtd_meses):
            nome_mes = meses[j]

            while True:
                try:
                    print(f"Quantos seguidores o {nome_rede} ganhou em {nome_mes}?")
                    valor = int(input("Digite o valor: "))
                    linha_atual.append(valor)
                    break
                except ValueError:
                    print("Erro: Digite apenas números inteiros!")

        matriz_temporaria.append(linha_atual)

    print("Dados de ganhos salvos com sucesso!")
    return matriz_temporaria


def menosSeguidores():
    print("\n--- Cadastro de PERDAS de Seguidores ---")
    matriz_temporaria = []

    for i in range(qtd_redes):
        linha_atual = []
        nome_rede = redes[i]

        for j in range(qtd_meses):
            nome_mes = meses[j]

            while True:
                try:
                    print(f"Quantos seguidores o {nome_rede} perdeu em {nome_mes}?")
                    valor = int(input("Digite o valor: "))
                    linha_atual.append(valor)
                    break
                except ValueError:
                    print("Erro: Digite apenas números inteiros!")

        matriz_temporaria.append(linha_atual)

    print("Dados de perdas salvos com sucesso!")
    return matriz_temporaria


def mostrarTabela(dadosGanhos, dadosPerdidos):
    if not dadosGanhos or not dadosPerdidos:
        print("\n[ERRO] Você precisa cadastrar os dados primeiro!")
        return

    print("\n" + "=" * 40)
    print("RELATÓRIO GERAL")
    print("=" * 40)

    tabela_ganhos = pd.DataFrame(dadosGanhos, index=redes, columns=meses)
    tabela_perdas = pd.DataFrame(dadosPerdidos, index=redes, columns=meses)

    tabela_perdas_visual = tabela_perdas * -1

    print("\n--- Tabela de GANHOS ---")
    print(tabela_ganhos)

    print("\n--- Tabela de PERDAS ---")
    print(tabela_perdas_visual)


def atualizarDados(dadosGanhos, dadosPerdidos):
    if not dadosGanhos or not dadosPerdidos:
        print("\n[ERRO] Cadastre os dados primeiro!")
        return

    print("\n--- ATUALIZAR UM VALOR ---")
    print("1 - Corrigir Ganhos")
    print("2 - Corrigir Perdas")
    opcao = input("Escolha a opção (1 ou 2): ")

    if opcao == "1":
        matriz_alvo = dadosGanhos
        tipo = "GANHOS"
    elif opcao == "2":
        matriz_alvo = dadosPerdidos
        tipo = "PERDAS"
    else:
        print("Opção inválida.")
        return

    print(f"\nEscolha a Rede Social para alterar em {tipo}:")
    for i in range(qtd_redes):
        print(f"{i} - {redes[i]}")

    try:
        indice_linha = int(input("Digite o número da rede: "))
        if indice_linha < 0 or indice_linha >= qtd_redes:
            print("Número da rede inválido.")
            return
    except ValueError:
        print("Erro: Digite um número.")
        return

    print("\nEscolha o Mês:")
    for j in range(qtd_meses):
        print(f"{j} - {meses[j]}")

    try:
        indice_coluna = int(input("Digite o número do mês: "))
        if indice_coluna < 0 or indice_coluna >= qtd_meses:
            print("Número do mês inválido.")
            return
    except ValueError:
        print("Erro: Digite um número.")
        return

    valor_antigo = matriz_alvo[indice_linha][indice_coluna]
    print(f"Valor atual: {valor_antigo}")

    try:
        novo_valor = int(input("Digite o NOVO valor: "))
        matriz_alvo[indice_linha][indice_coluna] = novo_valor
        print("Atualizado com sucesso!")
    except ValueError:
        print("Erro: O valor deve ser um número inteiro.")


def gerarRelatorio(dadosGanhos, dadosPerdidos):
    if not dadosGanhos or not dadosPerdidos:
        print("\n[ERRO] Cadastre os dados primeiro!")
        return

    print("\n--- ANÁLISE DETALHADA ---")
    print("Escolha qual rede você quer analisar:")

    for i in range(qtd_redes):
        print(f"{i} - {redes[i]}")

    try:
        escolha = int(input("Digite o número da rede: "))

        if escolha < 0 or escolha >= qtd_redes:
            print("Opção inválida.")
            return

        rede_escolhida = redes[escolha]

        lista_de_ganhos = dadosGanhos[escolha]
        lista_de_perdas = dadosPerdidos[escolha]

        maior_ganho = max(lista_de_ganhos)
        maior_perda = max(lista_de_perdas)

        indice_ganho = lista_de_ganhos.index(maior_ganho)
        indice_perda = lista_de_perdas.index(maior_perda)

        mes_ganho = meses[indice_ganho]
        mes_perda = meses[indice_perda]

        print(f"\nResumo para: {rede_escolhida.upper()}")
        print(f"-> Melhor momento: Ganhou {maior_ganho} seguidores em {mes_ganho}.")
        print(f"-> Pior momento: Perdeu {maior_perda} seguidores em {mes_perda}.")

    except ValueError:
        print("Erro: Digite apenas números.")
