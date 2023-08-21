import random
import time

# Função para criar uma lista embaralhada
def cria_lista_embaralhada(n):
    lista = list(range(n))
    random.shuffle(lista)
    return lista

# Função para verificar se há um índice inconveniente
def tem_indice_inconveniente(amigo_de):
    for i, amigo in enumerate(amigo_de):
        if i == amigo:
            return True
    return False

# Função para realizar permutações sem índices inconvenientes
def permuta_sem_inconvenientes(amigo_de):
    num = len(amigo_de)
    for i, amigo in enumerate(amigo_de):
        if i == amigo:
            amigo_de[i] = amigo_de[i - 1]
            amigo_de[i - 1] = i

def novo_experimento(N, T):
    lista = [cria_lista_embaralhada(N) for _ in range(T)]

    inconvenientes = [lista[i] for i in range(T) if tem_indice_inconveniente(lista[i])]
    qn = (T - len(inconvenientes)) / T

    return qn, inconvenientes

def main():
    print("Testes do EP09")

    # Testes da função tem_indice_inconveniente
    print("\nFunção tem_indice_inconveniente()")
    amigos1 = [1, 0, 2]
    amigos2 = [1, 2, 0]
    print(" -- tem_indice_inconveniente(%s) = %s" % (amigos1, tem_indice_inconveniente(amigos1)))
    print(" -- tem_indice_inconveniente(%s) = %s" % (amigos2, tem_indice_inconveniente(amigos2)))

    # Parâmetros para os experimentos
    print("\nFunção novo_experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)
    
    MINN = int(input("\nQual o número mínimo de pessoas: "))
    MAXN = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW = input("Você quer ver as listas com índice inconveniente [s/n]: ")

    for n in range(MINN, MAXN + 1, passo):
        instante_inicial = time.time()
        qn, inconvenientes = novo_experimento(n, T)
        print("q(%d) = %f" % (n, qn))

        if SHOW.lower() == 's':
            print("   permutações com índices inconvenientes para q(%d): " % n)
            if not inconvenientes:
                print("      nenhuma lista com índice inconveniente.")
            else:
                for inconveniente in inconvenientes:
                    print("    -- antes  --", inconveniente)
                    permuta_sem_inconvenientes(inconveniente)
                    print("    ++ depois ++", inconveniente)

        instante_final = time.time()
        print("    tempo decorrido: %7.2f ms" % ((instante_final - instante_inicial) * 1000))

    # Teste permuta_sem_inconvenientes para n grande
    print()
    muito_grande = 1000000
    amigos3 = cria_lista_embaralhada(muito_grande)
    amigos3 += [muito_grande]
    print(" -- tem_indice_inconveniente com lista de %d = %s" % (muito_grande, tem_indice_inconveniente(amigos3)))
    instante_inicial = time.time()
    permuta_sem_inconvenientes(amigos3)
    instante_final = time.time()
    print(" ++ tem_indice_inconveniente com lista de %d = %s" % (muito_grande, tem_indice_inconveniente(amigos3)))
    print("    tempo decorrido: %7.2f ms" % ((instante_final - instante_inicial) * 1000))

if __name__ == '__main__':
    main()

