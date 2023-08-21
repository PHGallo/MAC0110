def main():
    # Solicitar que o usuário insira uma string p, um número inteiro i
    # e um número real r
    p = input("Digite uma palavra p: ")
    i = int(input("Digite um inteiro i: "))
    r = float(input("Digite um real r: "))
    
    # Realizar as operações especificadas e imprimir os resultados formatados
    print(f"Resultado de p + p: {p + p}")
    print(f"Resultado de i + i: {i + i}")
    print(f"Resultado de r + r: {r + r}")
    print(f"Resultado de i * p: {i * p}")
    print(f"Resultado de i * i: {i * i}")
    print(f"Resultado de i * r: {i * r}")
    print(f"Resultado de r / i: {r / i}")
    print(f"Resultado de 2 * i / i: {2 * i / i}")
    print(f"Resultado de i / i * 2: {i / i * 2}")

if __name__ == "__main__":
    main()
