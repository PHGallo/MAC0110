# constantes
SIM = 's'

#------------------------------------------------------------------
def main():
    nome = input("Digite o nome de um arquivo texto: ")
    opcao = input("Digite '%s' se deseja ver o texto lido: " % (SIM))
    if opcao == SIM:
        mostre_texto = True
    else:
        mostre_texto = False

    # leia texto do arquivo nome
    with open(nome, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

    # deseja que o texto seja exibido?
    if mostre_texto:
        print("\nConteudo do arquivo '%s':" % (nome))
        print(texto)

    palavra = input("Digite uma palavra a ser substituída: ")
    nova_palavra = input("Digite uma palavra substituta: ")

    # encontre as posições onde a palavra ocorre
    ocorrencias = busque(palavra, texto)

    # mostre as posições encontradas
    print("\nAchei '%s' nos seguintes lugares: " % (palavra))
    print(ocorrencias)

    # crie um texto onde as ocorrências de `palavra` foram substituídas por
    # `nova_palavra`
    novo_texto = substitua(palavra, nova_palavra, texto)

    # exiba o texto criado
    print("\nNovo texto:")
    print(novo_texto)

    print("Fim dos testes.")

#------------------------------------------------------------------
def busque(palavra, texto):
    ''' (str, str) -> list

    RECEBE duas strings, `palavra` e `texto`, e RETORNA uma lista
    contendo o início de cada ocorrência de `palavra` em `texto`.

    No caso de haver sobreposições de ocorrências de `palavra`, apenas
    menor índice dentre as ocorrências sobrepostas deverá ser inserido
    na lista.

    Exemplos:

    busque("mana", "ana e mariana compraram bananas") retorna []

    busque("bana", "ana e mariana compraram bananas") retorna [24]

    busque("ana", "ana e mariana compraram bananas") retorna [0, 10, 25]

    busque("AA", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT") retorna [2, 8, 10]
    '''
    # Aqui você deve implementar a função busque
    # e retornar a lista com as posições onde a palavra ocorre.
    # Dica: Utilize o método `find()` para encontrar as ocorrências.
    # Se houver sobreposições, mantenha apenas a primeira ocorrência.
    # Lembre-se que a indexação em Python começa em 0.
    ocorrencias = []
    index = texto.find(palavra)
    while index != -1:
        ocorrencias.append(index)
        index = texto.find(palavra, index + 1)
    return ocorrencias

#------------------------------------------------------------------
def substitua(palavra, nova_palavra, texto):
    ''' (str, str, str) -> str

    RECEBE as strings `palavra`, `nova` e `texto` e
    RETORNA uma string onde todas as ocorrências de `palavra`
    foram substituídas pela `nova_palavra`.

    No caso de haver sobreposições de ocorrências de `palavra`, apenas
    a de menor índice dentre as ocorrências sobrepostas deverá ser
    substituída por `nova_palavra`.

    Exemplos:

    substitua("compraram","venderem","ana e mariana compraram bananas")
    retorna 'ana e mariana venderem bananas'

    substitua("ana","ely","ana e mariana compraram bananas")
    retorna 'ely e mariely compraram belynas'

    substitua("AA", "????", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    retorna 'AC????AGTC????????TTGTGTAGTGTGACGTTTT'

    substitua("TGT", "X", "ACAAAGTCAAAATTGTGTAGTGTGACGTTTT")
    retorna 'ACAAAGTCAAAATXGTAGXGACGTTTT'
    '''
    # Aqui você deve implementar a função substitua
    # e retornar a string onde as ocorrências de `palavra` foram substituídas por `nova_palavra`.
    # Lembre-se de considerar a possibilidade de sobreposições.
    index = texto.find(palavra)
    while index != -1:
        texto = texto[:index] + nova_palavra + texto[index + len(palavra):]
        index = texto.find(palavra, index + len(nova_palavra))
    return texto

# Esse if serve para rodar a main() dentro do Spyder.
if __name__ == '__main__':
    main()
