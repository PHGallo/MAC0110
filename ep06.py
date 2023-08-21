def acertou_tiro(x, y):
    if (x >= -0.5 and x <= 0.5 and y >= 9.5 and y <= 10.5) or (x >= 0 and x <= 4 and y >= 8 and y <= 12):
        return True
    elif (x >= 2 and x <= 3 and y >= 6 and y <= 7) or (x >= 3 and x <= 4 and y >= 7 and y <= 8):
        return True
    else:
        return False

def main():
    N = int(input("Digite N: "))
    A = int(input("\nDigite dígito para A: "))
    E = int(input("Digite dígito para E: "))
    
    code = ''
    
    for _ in range(N):
        x = float(input("\nDigite x: "))
        y = float(input("Digite y: "))
        
        if acertou_tiro(x, y):
            code += str(A)
            print("Acertou")
        else:
            code += str(E)
            print("Errou")
    
    print("Código:", code)

if __name__ == "__main__":
    main()