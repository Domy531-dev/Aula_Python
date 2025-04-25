# Exercício 09

def jogo_adivinhacao():
    numero_secreto = 7
    tentativas = 3

    print("Tentativas adivinhar o número entre 1 a 10!")

    for i in range(tentativas):
        palpite = int(input("Digite o seu palpite: "))
        
        if palpite == numero_secreto:
            print("Você acertou! Parabéns!")
            return
        elif palpite < numero_secreto:
            print("O número é maior. Tente fornecer valores mais altos")
        else:
            print("O número é maior. Tente fornecer valores mais baixo")
print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}")



