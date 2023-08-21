# MODULOS A SEREM UTILIZADOS NO PROGRAMA
import random # para random.choice(lista) na função gere_frase()

#------------------------------------------------------------------
# CONSTANTES

# ponto final, ponto de interrogação, ponto de exclamação
# não consideraremos reticências "..."
PONTUACAO_FINAL = ".?!"

# vírgula, ponto e vírgula, dois pontos, fecha parênteses
# não devem ser precedidos de espaço na frase gerada
PONTUACAO_SEM_ESPACO = ',;:)' + PONTUACAO_FINAL

# travesão, aspas, abre chaves
# devem ser precedidos de espaço na frase gerada
PONTUACAO_COM_ESPACO = '—"('

# todas juntas (reticências foram desconsideradas)
PONTUACAO = PONTUACAO_SEM_ESPACO + PONTUACAO_COM_ESPACO

# usado na função insira espacos
ESPACO = ' '

# semente para o gerador aleatório com o objetivo de reprodutibilidade
SEED = 1234

#------------------------------------------------------------------
#
def main():
    '''(None) -> None

    Para testar as funções juntas. Esta função não será avaliada, entretanto
    ela __não__ deve gerar erro de execução ou sintático. 
    Modifique-a se desejar.
    '''
    # Para efeitos de reprodutibilidade
    random.seed(SEED)

    print('ESCREVENDO "como" MACHADO DE ASSIS!\n')

    # leia nome do arquivo 
    nome = input("Digite o nome do arquivo com o texto: ")

    # leia o corpus
    try:
        with open(nome, "r", encoding="utf-8") as arq:
            texto = arq.read()
    except:
        print("main(): Erro na leitura do arquivo '%s'"%(nome))
        return None
    
    # insira espaços antes de pontuações
    texto = insira_espacos(texto)

    # obtenha lista com itens léxicos
    lst_itens = texto.split()
    
    # construa dicionario de sucessores
    dicio = dicio_sucessores(lst_itens)

    # quantidade de frases que devem ser geradas
    n = int(input("Digite o numero de frases que devem ser geradas: "))

    for i in range(n):
        print("---")
        
        # pegue palavra inicial da frase gerada
        palavra_inicial = input("Digite a palavra inicial da frase %d: "%(i+1))

        # gere uma frase começando com 
        frase = gere_frase(palavra_inicial, dicio)
        print("Frase gerada:", frase)

    print("\nFIM")

#------------------------------------------------------------------
def insira_espacos(texto):
    '''(str) -> str

    RECEBE uma string `texto` e RETORNA a string resultante da
    inserção de um ESPACO antes e depois de __cada sinal__ em
    PONTUACAO que estiver na string `texto`.
    '''
    novo_texto = ""

    for char in texto:
        if char in PONTUACAO:
            novo_texto += f" {char} "
        else:
            novo_texto += char

    return novo_texto
    
#------------------------------------------------------------------
def dicio_sucessores(lst):
    '''(list) -> dict

    RECEBE uma lista `lst` e RETORNA um dicionário em que 

        - as __chaves__ são os itens que ocorrem em `lst` e 
        - o  __valor__ associado a cada chave é a lista dos 
          itens que ocorrem imediatamente após a chave na 
          lista `lst`.

    Por convenção a lista correspondente ao valor do último item 
    na lst (=lst[-1]) deve conter o primeiro item da lista (=lst[0]).

    Se a lista é vazia a função deve retornar o dicionário vazio.
    '''
    dicio = {}

    if not lst:  # Verifica se a lista está vazia
        return dicio

    for i, item in enumerate(lst):
        proximo_item = lst[(i + 1) % len(lst)]  # Para lidar com o último item
        if item not in dicio:
            dicio[item] = []
        dicio[item].append(proximo_item)

    return dicio

#------------------------------------------------------------------
def gere_frase(p_inicial, dicio):
    '''(str, dict) -> str

    RECEBE uma palavra `p_inicial` e um dicionário `dicio`.

    O dicionário foi criado a partir de um texto com uma ou 
    mais frases; como nos textos de Machado de Assis.

    Cada chave do dicionário é um item (str). O valor no dicionário 
    correspondente a cada chave é uma lista (list) de itens (str). 

    RETORNA uma string representando uma frase.

    A frase retornada deve começar com a string p_inicial e ser gerada 
    segundo o __processo aleatório__ descrito no enunciado.
    
    Os itens na frase devem ser precedidos de um ESPACO, exceto:

        - a palavra inicial 
        - e os sinais de pontuação na string PONTUACAO_SEM_ESPACO.

    Se p_inicial não está no dicionário a função deve retornar a string vazia.
    '''
    if p_inicial not in dicio:
        return ""

    frase_gerada = p_inicial
    palavra_atual = p_inicial

    while True:
        proximas_palavras = dicio[palavra_atual]
        proxima_palavra = random.choice(proximas_palavras)

        if proxima_palavra in PONTUACAO_SEM_ESPACO:
            frase_gerada += proxima_palavra
        else:
            frase_gerada += " " + proxima_palavra

        if proxima_palavra in PONTUACAO_FINAL:
            break

        palavra_atual = proxima_palavra

    return frase_gerada

if __name__ == '__main__':
    main()