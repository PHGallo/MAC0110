import math

EPSILON = 1e-6

def erro_rel(y, x):
    if x == 0 and y == 0:
        return 0
    elif x == 0 and y != 0:
        return 1
    else:
        return abs((y - x) / x)

def integral_por_retangulos(f, a, b, k):
    delta_x = (b - a) / k
    total_area = 0
    
    for i in range(k):
        x_middle = a + i * delta_x + delta_x / 2
        area = f(x_middle) * delta_x
        total_area += area
    
    return total_area

def aproxima_integral(f, a, b, eps=EPSILON):
    k = 1
    prev_approximation = integral_por_retangulos(f, a, b, k)
    
    while True:
        k *= 2
        approximation = integral_por_retangulos(f, a, b, k)
        
        if erro_rel(approximation, prev_approximation) < eps:
            return approximation, k
        
        prev_approximation = approximation

# Funções exemplo
def funcao_1(x):
    return x

def funcao_2(x):
    return math.sin(x)

def funcao_3(x):
    return math.cos(x)

def main():
    funcao_x = funcao_3
    
    print(f"funcao_x usada nesses testes: {funcao_x.__name__}")
    
    for x in [0.0, 0.5, 1.0]:
        print(f"Valor de {funcao_x.__name__} em {x}: {funcao_x(x)}")
    
    print("\nIntegral por retângulos:")
    for k in [1, 10, 100]:
        result = integral_por_retangulos(funcao_x, 0, 1, k)
        print(f"para {k} retangulos no intervalo [0.000000, 1.000000]:")
        print(f"--> integral: {result}")
    
    print("\nAproxima Integral:")
    for eps in [1e-6, 1e-5, 1e-4, 1e-3]:
        result, k = aproxima_integral(funcao_x, 0, 1, eps)
        print(f"para eps = {eps} e intervalo [0.000000, 1.000000]:")
        print(f"--> integral = {result:.6f}, com {k} retângulos.")
    
    print("Fim dos testes.")

if __name__ == "__main__":
    main()
