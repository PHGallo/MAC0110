import random

def main():
    print("Bem vindo ao MASTER BIME!!")
    
    # Solicita ao jogador o valor da semente para o gerador de números aleatórios
    semente = int(input("\nDigite o valor da semente: "))
    
    # Inicializa o gerador de números aleatórios com a semente fornecida
    random.seed(semente)
    
    # Gera um número aleatório entre 0 e 999
    senha = random.randint(0, 999)
    print("Número sorteado:", senha)
    
    # Inicializa o número máximo de tentativas e o contador de tentativas
    max_tentativas = 5
    tentativa = 1
    
    while tentativa <= max_tentativas:
        # Solicita ao jogador um chute
        chute = int(input("\nDigite seu chute: "))
        
        # Verifica se o chute é igual à senha
        if chute == senha:
            print(f"Chute {tentativa} / {max_tentativas} : certo!")
            print("Parabéns, você acertou!")
            break
        else:
            print(f"Chute {tentativa} / {max_tentativas} : errado!")
        
        tentativa += 1
    
    # Se todas as tentativas foram usadas e o jogador não acertou
    if tentativa > max_tentativas:
        print("Ha ha, você perdeu!")
    
    print("Fim do jogo.")

# Chama a função principal
if __name__ == "__main__":
    main()
