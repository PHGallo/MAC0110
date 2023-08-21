def main():
    # Solicita ao usuário o número inteiro n
    n = int(input("Digite n: "))

    # Inicializa a variável para armazenar a soma parcial
    soma_parcial = 0.0

    # Loop para ler n números reais
    for i in range(n):
        # Solicita ao usuário um número real
        numero = float(input("Digite um número: "))
        
        # Adiciona o número à soma parcial
        soma_parcial += numero
        
        # Imprime a soma parcial até o momento
        print(f"Soma parcial {i+1} = {soma_parcial} \n")
    
    # Calcula a média dos números lidos
    media = soma_parcial / n
    
    # Imprime a média calculada
    print(f"Média = {media}")

# Chama a função principal
if __name__ == "__main__":
    main()
