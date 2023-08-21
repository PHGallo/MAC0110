# Constantes
DNA = 'ATCG'
GAP = '_'

#------------------------------------------------------------------
def main():
    '''
    Modifique essa função, escrevendo os seus testes.
    '''
    dna_a = input("Digite sua sequência:")
    dna_b = input("Digite sua sequência:")
    
    # Testes para a função gera_gaps
    lista_dna_a = gera_gaps(dna_a)
    lista_dna_b = gera_gaps(dna_b)
    
    # Testes para a função pontuação
    m = int(input("Digite a pontuação para correspondência de letras: "))
    d = int(input("Digite a pontuação para letras diferentes: "))
    g = int(input("Digite a pontuação para gaps: "))
    
    s = lista_dna_a[0]
    t = lista_dna_b[0]
    
    print("Pontuação do alinhamento:", pontuacao(m, d, g, s, t))
    print("Fim dos meus testes.")

#------------------------------------------------------------------
def gera_gaps(dna):
    ''' ( str ) -> list
    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (um gap).
    RETORNA uma lista com todas as variações de dna com um gap a 
    mais e sem repetição.

    exemplos: 
    In  [1]: gera_gaps( 'T' )
    Out [1]: ['_T', 'T_']
    
    In  [2]: gera_gaps( 'CA' )
    Out [2]: ['_CA', 'C_A', 'CA_']
    
    In  [3]: gera_gaps( 'AT_G')
    Out [3]: ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_'] 
    '''
    n = len(dna)
    lista = []
    for i in range(n + 1):
        DNA = dna[:i] + GAP + dna[i:]
        if DNA not in lista:
            lista.append(DNA)
    return lista

#------------------------------------------------------------------
def pontuacao(m, d, g, s, t):
    ''' (int, int, int str, str) -> int
    RECEBE 3 inteiros não negativos `m`, `d`, e `g` e duas strings `s` e `t` 
    de mesmo tamanho com zero ou mais gaps representando fitas de DNA.
 
    RETORNA a pontuação do alinhamento entre `s` e `t` calculada da seguinte 
    forma:
 
       * duas letras iguais alinhadas contam m pontos, 
       * duas letras diferentes alinhadas contam −d pontos (subtrai d pontos) e 
       * uma letra alinhada com um gap ou dois gaps alinhados contam −g pontos.

    Exemplos:
    In  [1]: pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___')
    Out [1]: -7 
    
    In  [2]: pontuacao(1, 5, 3, 'T_CGTAC', 'ATCG___')
    Out [2]: -15
    
    In  [3]: pontuacao(5, 5, 3, 'T_CGTA', 'ATCG__')
    Out [3]: -4
    '''
    n = len(s)
    pontos = 0
     
    for i in range(n):
        if s[i] == t[i] and s[i] != GAP and t[i] != GAP:
            pontos += m
        elif s[i] != t[i] and s[i] != GAP and t[i] != GAP:
            pontos -= d
        else:
            pontos -= g
    
    return pontos

if __name__ == '__main__':
    main()
