import random

def main():
    print("Bem vindo ao MASTER BIME!!")
    
    # Solicita ao jogador o valor da semente para o gerador de números aleatórios
    semente = int(input("\nDigite o valor da semente: "))
    
    # Inicializa o gerador de números aleatórios com a semente fornecida
    random.seed(semente)
    
    # Gera um número aleatório entre 0 e 9999
    senha = random.randint(0, 9999)
    
    # Converte a senha em uma string de 4 dígitos com zeros à esquerda
    senha_str = str(senha).zfill(4)
    print("Número sorteado:", senha_str)
    
    # Inicializa o número máximo de tentativas e o contador de tentativas
    max_tentativas = 7
    tentativa = 1
    
    while tentativa <= max_tentativas:
        # Solicita ao jogador um chute
        chute = int(input("\nDigite seu chute: "))
        
        # Converte o chute em uma string de 4 dígitos com zeros à esquerda
        chute_str = str(chute).zfill(4)
        
        # Inicializa o contador de dígitos em posições certas
        contagem_certos = 0
        
        # Verifica quantos dígitos estão na posição certa
        for i in range(len(senha_str)):
            if senha_str[i] == chute_str[i]:
                contagem_certos += 1
        
        print(f"Dígitos em posições certas do chute {tentativa} / {max_tentativas} : {contagem_certos}")
        
        # Se acertou todos os dígitos, encerra o jogo
        if contagem_certos == len(senha_str):
            print("Parabéns, você acertou!")
            break
        
        tentativa += 1
    
    # Se todas as tentativas foram usadas e o jogador não acertou
    if tentativa > max_tentativas:
        print("Ha ha, você perdeu!")
    
    print("Fim do jogo.")

# Chama a função principal
if __name__ == "__main__":
    main()
