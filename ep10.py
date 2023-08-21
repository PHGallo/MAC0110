import math        # math.exp(), math.sqrt() e math.pi   
import random      # random.seed(), random.choices()
import numpy as np # np.arange()
import matplotlib.pyplot as plt # plt.subplots(), plt.bar(),  plt.xlabel(),
                                # plt.ylabel(), plt.title(), plt.show()

# Constantes
SEED   = 123456 # para gerador aleatório; garante reproducibilidade dos experimentos
CARA   = 'H'    # possível valor em uma amostra aleatória produzida por random.choices()
COROA  = 'T'    # possível valor em uma amostra aleatória produzida por random.choices()

def main():
    random.seed(SEED)

    while True:
        n = int(input("Digite o número n de lançamentos da moeda: "))
        p = float(input("Digite a probabilidade de obtermos cara: "))
        t = int(input("Digite o número t de amostras: "))
        s = input("Deseja ver a distribuição normal? ('s' para sim): ")
        mostre_normal = (s.lower() == 's')

        caras = caras_em_amostras(n, t, p)
        freq_obs = frequencias_observadas(caras, n)
        Bnp = distribuicao_binomial(n, p)
        freq_esp = frequencias_esperadas(Bnp, t)
        
        print("Frequências observadas (esperadas)")
        for i in range(n + 1):
            print("%8d: %7d (%g)" % (i, freq_obs[i], freq_esp[i]))

        plot(freq_obs, freq_esp, n, t, p, mostre_normal)

        resp = input("Deseja continuar? ('s' para sim): ")
        if resp.lower() != 's':
            break

def caras_em_amostras(n, t, p=0.5):
    return [sum(1 for _ in range(n) if random.choices([CARA, COROA], weights=(p, 1 - p))[0] == CARA) for _ in range(t)]

def frequencias_observadas(no_caras, n):
    freq = [0] * (n + 1)
    for valor in no_caras:
        freq[valor] += 1
    return freq

def distribuicao_binomial(n, p=0.5):
    binomials = [math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)]
    return binomials

def frequencias_esperadas(Bnp, t):
    return [freq * t for freq in Bnp]

def plot(y_obs, y_esp, n, t, p, mostre_normal=False):
    # crie um gráfico
    fig, ax = plt.subplots()
    x = np.arange(n+1)
    
    # desenhe barras para representar com a frequência observada
    plt.bar(x, y_obs)

    # desenhe o gráfico com as frequência esperadas obtidas através da distribuição binomial
    ax.plot(x, y_esp, color='red', marker='^', linestyle='dashed', linewidth=1, markersize=6)

    # devemos desenhar a distribuição normal?
    if mostre_normal:
        
        # média da distribuição binomail
        mu = n*p
        
        # variância de distribuição binomial
        sigma2 = n*p*(1-p)
        
        # domínimo para o cálculo dos valores da função densidade da distribuição (continua) normal
        z = np.arange(0, n+1, 0.1)
        
        # valores da distribuição normal
        N = [0]*len(z) # np.zeros(len(z))
        for i in range(len(z)):
            N[i] = phi(z[i], mu, sigma2) * t
            
        # desenhe os pontos
        ax.plot(z, N, color='green', marker='*', linestyle='solid', linewidth=.5, markersize=2)

    # rotulos
    plt.xlabel('no. de caras')
    plt.ylabel('frequências')
    plt.title('Histograma para n=%d, t=%d e p=%g'%(n,t,p))
    plt.grid(True)

    # desenhe
    plt.show()

def phi(x, mu=0, sigma2=1):
    return math.exp(-(x - mu) ** 2 / (2 * sigma2)) / math.sqrt(2 * math.pi * sigma2)

if __name__ == '__main__':
    main()
