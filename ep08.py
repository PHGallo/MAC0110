import random

def cria_lista_embaralhada(n):
    lista = list(range(n))
    random.shuffle(lista)
    return lista

def tem_um_ciclo(amigo_de):
    num = len(amigo_de)
    for x in range(num):
        if amigo_de[x] == x:
            return False

    amigo_atual = amigo_de[0]
    ciclo_len = 1
    while amigo_atual != 0:
        if ciclo_len == num - 1:
            return True
        amigo_atual = amigo_de[amigo_atual]
        ciclo_len += 1

    return ciclo_len == num - 1

def experimento(N, T, debug=False):
    lista = [cria_lista_embaralhada(N) for _ in range(T)]
    ciclos = [lista[i] for i in range(T) if tem_um_ciclo(lista[i])]
    prob = len(ciclos) / T

    if debug:
        for ciclo in ciclos:
            print(ciclo)

    return prob

def main():
    print("Testes do EP08")

    print("\nFunção tem_um_ciclo()")
    amigos1 = [1, 0]
    amigos2 = [0, 1]
    print("tem_um_ciclo(%s) = %s" % (amigos1, tem_um_ciclo(amigos1)))
    print("tem_um_ciclo(%s) = %s" % (amigos2, tem_um_ciclo(amigos2)))

    print("\nFunção experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)

    MINN = int(input("\nQual o número mínimo de pessoas: "))
    MAXN = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW = input("Você quer ver as listas com um ciclo [s/n]: ")

    debug = SHOW.lower() == 's'

    n = MINN
    while n <= MAXN:
        pn = experimento(n, T, debug)
        print("p(%d) = %f" % (n, pn))
        n += passo

if __name__ == '__main__':
    main()


