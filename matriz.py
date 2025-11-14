# Criando variaveis de controle para o laço de repetição
linha = 3
coluna = 4
mes = ["Janeiro" , "Fevereiro" , "Março" , "Abril"]

# Criando a matriz que será adicionada todos os dados, desde as linhas até as colunas
matriz = []

        
    
        
def matrizMaisSeguidores():
    
    # Esse primeiro FOR é para criação da linha, aqui eu pego a minha variavel de controle e uso ela para fazer a contagem máxima de linhas que terá na minha matriz.
    for l in range (linha):
        print("O laço da linha está em: "  , l)
        
        # Aqui eu crio meu vetor com a minha linha atual onde será adicionado as colunas
        linhaAtual = []

    # Esse segundo FOR é para a coluna, e uso a variavel de controle da coluna pra fazer a contagem máxima de colunas 
        for c in range (coluna):
            print("O laço da coluna está em: "  , c)
            
          
            
            # Aqui toda vez que inicia um novo loop, ele faz a pergunta novamente pro usuário e armazena nesta variavel
            valorAtual = int(input(f"Digite a quantidade de seguidores que você ganhou : "))
            
            print(mes[c])
                
            
            # Aqui eu adiciono o valor que o usuário digitou na linha
            linhaAtual.append(valorAtual)

        # Quando o laço da coluna chegar em 4, ele cai pra esse código, aqui ele pega o vetor todo denominado de linha atual e taca pra outro vetor, que se chama matriz, e a partir disso cria a matriz
        matriz.append(linhaAtual)
        

        
        


    print("Matriz criada:")
    print(matriz)
    
# proximoMes()    
matrizMaisSeguidores()



