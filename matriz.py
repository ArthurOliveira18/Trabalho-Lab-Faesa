import pandas as pd

# Criando variaveis de controle para o laço de repetição
linha = 3
coluna = 4
mes = ["Janeiro", "Fevereiro", "Março", "Abril"]
redesSociais = ["Instagram", "Facebook", "Twiter"]


def matrizMaisSeguidores():

    # Criando a matriz que será adicionada todos os dados, desde as linhas até as colunas
    matrizGanhos = []

    for l in range(linha):

        # Aqui eu crio meu vetor com a minha linha atual onde será adicionado as colunas
        linhaAtual = []

        # O loop externo (l) itera pelas linhas, onde cada linha representa uma rede social. Ele 'pausa' em uma rede social (ex: linha 1) e, enquanto está pausado nela, o loop interno (c) executa completamente para preencher todas as colunas (os meses) daquela rede social. Só depois de passar por todos os meses é que o loop externo avança para a próxima rede social (linha 2).
        redesSociais[l]

        # Esse segundo FOR é para a coluna, e uso a variavel de controle da coluna pra fazer a contagem máxima de colunas
        for c in range(coluna):

            while True:
                try:
                    prompt = f"Digite a quantidade de seguidores que você recebeu no {redesSociais[l]} no mês de {mes[c]}: "

                    # 3. Pegamos a entrada do usuário
                    valor_digitado = input(prompt)

                    # 4. TENTAMOS converter para inteiro.
                    #    Se o usuário digitar "" (vazio) ou "abc",
                    #    a linha abaixo vai falhar e pular para o 'except'.
                    # Aqui toda vez que inicia um novo loop, ele faz a pergunta novamente pro usuário e armazena nesta variavel
                    valorAtual = int(valor_digitado)

                    # Aqui eu adiciono o valor que o usuário digitou na linha
                    linhaAtual.append(valorAtual)
                    break

                except:
                    print("Valor inválido, digite novamente apenas números.")
                # Quando o laço da coluna chegar em 4, ele cai pra esse código, aqui ele pega o vetor todo denominado de linha atual e taca pra outro vetor, que se chama matriz, e a partir disso cria a matriz

        matrizGanhos.append(linhaAtual)

    print("Dados cadastrados!! ")


def menosSeguidores():

    matrizPerdas = []

    print(
        "Iniciando uma nova matriz, essa daqui é de quantidade de seguidores perdido em cada rede social "
    )

    for l in range(linha):
        print("O laço da linha está em: ", l)

        # Aqui eu crio meu vetor com a minha linha atual onde será adicionado as colunas
        linhaAtual = []

        # O loop externo (l) itera pelas linhas, onde cada linha representa uma rede social. Ele 'pausa' em uma rede social (ex: linha 1) e, enquanto está pausado nela, o loop interno (c) executa completamente para preencher todas as colunas (os meses) daquela rede social. Só depois de passar por todos os meses é que o loop externo avança para a próxima rede social (linha 2).
        redesSociais[l]

        # Esse segundo FOR é para a coluna, e uso a variavel de controle da coluna pra fazer a contagem máxima de colunas
        for c in range(coluna):
            print("O laço da coluna está em: ", c)

            while True:
                try:
                    prompt = f"Digite a quantidade de seguidores que você perdeu no {redesSociais[l]} no mês de {mes[c]}: "

                    # 3. Pegamos a entrada do usuário
                    valor_digitado = input(prompt)

                    # 4. TENTAMOS converter para inteiro.
                    #    Se o usuário digitar "" (vazio) ou "abc",
                    #    a linha abaixo vai falhar e pular para o 'except'.
                    # Aqui toda vez que inicia um novo loop, ele faz a pergunta novamente pro usuário e armazena nesta variavel
                    valorAtual = int(valor_digitado)

                    # Aqui eu adiciono o valor que o usuário digitou na linha
                    linhaAtual.append(valorAtual)
                    break

                except:
                    print("Valor inválido, digite novamente apenas números.")
                # Quando o laço da coluna chegar em 4, ele cai pra esse código, aqui ele pega o vetor todo denominado de linha atual e taca pra outro vetor, que se chama matriz, e a partir disso cria a matriz

        matrizPerdas.append(linhaAtual)

    print("Dados cadastrados!! ")


# --- AQUI É ONDE VOCÊ USA O PANDAS ---
def mostrarTabela(dadosGanhos, dadosPerdidos):
    if(not dadosGanhos or not dadosPerdidos):
        print("\n[ERRO] Não há dados para exibir. Cadastre-os primeiro (Opção 1).")
        
    else:
        
        return
    