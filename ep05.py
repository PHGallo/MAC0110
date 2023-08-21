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
    max_tentativas = 10
    tentativa = 1
    
    while tentativa <= max_tentativas:
        # Solicita ao jogador um chute
        chute = int(input("\nDigite seu chute: "))
        
        # Converte o chute em uma string de 4 dígitos com zeros à esquerda
        chute_str = str(chute).zfill(4)
        
        # Calcula os dígitos em posições corretas e os dígitos certos
        em_posicoes_corretas = calc_em_posicoes_corretas(senha_str, chute_str, 4)
        digitos_certos = calc_digitos_certos(senha_str, chute_str)
        
        print(f"Dígitos em posições corretas do chute {tentativa} / {max_tentativas} : {em_posicoes_corretas}")
        print(f"Dígitos certos do chute {tentativa} / {max_tentativas} : {digitos_certos}")
        
        # Se acertou todos os dígitos, encerra o jogo
        if em_posicoes_corretas == 4:
            print("Parabéns, você acertou!")
            break
        
        tentativa += 1
    
    # Se todas as tentativas foram usadas e o jogador não acertou
    if tentativa > max_tentativas:
        print("Ha ha, você perdeu!")
    
    print("Fim do jogo.")

def calc_em_posicoes_corretas(senha, chute, max):
    # Retorna o número de dígitos em posições corretas entre a senha e o chute
    count = 0
    for i in range(max):
        if senha[i] == chute[i]:
            count += 1
    return count

def calc_digitos_certos(senha, chute):
    # Retorna o número de dígitos certos entre a senha e o chute
    count = 0
    for d in chute:
        if d in senha:
            count += 1
            senha = senha.replace(d, '', 1)  # Remove o dígito da senha para não contar novamente
    return count

# Chama a função principal
if __name__ == "__main__":
    main()
