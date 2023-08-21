def main():
    maux = [ [1,2,3,4,5],[3,4,5,6,7],[2,4,6,8,1],[5,3,1,7,9],[9,6,3,1,7] ]
    print( 'Matriz maux:')
    print( maux )
    print()
    print( to_string(maux, '> maux' ) )

    nova = crie (5, 5, 10)
    print( to_string( nova, '> nova') )

    dif = subtraia( nova, maux)
    print( to_string( dif , '> dif = nova - maux') )

    clo = clone(dif)
    print( to_string( clo , '> clo') )

    limiarize(clo, 5)
    print( to_string( clo , '> clo apos limiarize') )

    print( to_string( dif , '> dif apos limiarize') )
    
#------------------------------------------------------------------
#
def crie ( nlins, ncols, vini = 0 ):
    ''' (int, int, int) -> list

    RECEBE três inteiros, `nlins`, `ncols` e `vini`. 
    RETORNA uma matriz de dimensão `nlins` x `ncols` em que o valor do elemento
    em cada posição [lin][col] deve ser valor `vini`.
    '''
    matriz = []
    for _ in range(nlins):
        linha = [vini] * ncols
        matriz.append(linha)
    return matriz

#------------------------------------------------------------------
#
def clone ( mat ):
    ''' (list) -> list

    RECEBE uma matriz bidimensional mat e RETORNA um clone de mat.
    '''
    matriz_clone = [linha.copy() for linha in mat]
    return matriz_clone

#------------------------------------------------------------------
#
def subtraia ( mat1, mat2 ):
    ''' (list) -> list

    RECEBE duas matrizes bidimensionais `mat1` e `mat2` de números inteiros 
    e de mesma dimensão.
    RETORNA uma a matriz dif de mesma dimensão das matrizes. O valor 
    de cada posição [lin][col] deve ser dado por
 
        dif[lin][col] = mat1[lin][col] - mat2[lin][col].
    '''
    nlins = len(mat1)
    ncols = len(mat1[0])
    matriz_dif = []
    for lin in range(nlins):
        linha_dif = [mat1[lin][col] - mat2[lin][col] for col in range(ncols)]
        matriz_dif.append(linha_dif)
    return matriz_dif
    
#------------------------------------------------------------------
#
def to_string ( mat , nome = 'matriz' ):
    ''' (list, str) -> str

    RECEBE uma matriz bidimensional `mat` de números inteiros e uma string `nome`.  
    RETORNA uma string utilizada por print() para exibir a matriz, como por exemplo 
    em 

        print(to_string(bla, 'minha matriz bla'))

    que exibe o conteúdo da matriz bla.

    No que segue, por linha da string retornada entenda uma substring seguida 
    do caractere "\n" de mudança de linha.

    A string retornada deve ter o seguinte formato:

      - a primeira linha da string contém a string `nome`;
      - as demais linhas da string contém uma a uma as linhas da matriz
        `mat`.

    Os valores da matriz devem representados na string retornada por substring 
    de mesmo tamanho. O efeito será que ao exibirmos uma matriz bla através de
    print(to_string(bla)) os valores de cada coluna estarão alinhados.

    Reserve ao menos 4 posições para exibir cada número inteiro.
    '''
    str_mat = nome + '\n'
    for linha in mat:
        str_linha = ' '.join([f'{num:4}' for num in linha]) + '\n'
        str_mat += str_linha
    return str_mat 

#------------------------------------------------------------------
#
def limiarize ( mat, limite, alto=255, baixo=0 ):
    ''' (list, int, int, int) -> None
    RECEBE uma matriz bidimensional `mat` de números inteiros e três inteiros
    `limite`, `alto` e baixo.

    A função deve MODIFICAR `mat` da sequinte forma.
 
    Cada posição [lin][col] de `mat` em que mat[lin][col] > `limite`,
    deve receber o valor `alto`. As demais posições devem receber o valor 
    `baixo`.
    '''
    for lin in range(len(mat)):
        for col in range(len(mat[lin])):
            if mat[lin][col] > limite:
                mat[lin][col] = alto
            else:
                mat[lin][col] = baixo

if __name__ == '__main__':
    main()