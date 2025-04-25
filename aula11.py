# Exercício 10

def analisador_palavras():
    palavra = input("Digite a palavra para ser analisada: ")
    vogais = 0 
    consoantes = 0
    espacos = 0

    for letra in palavra.lower():
        if letra in "aeiou":
            vogais += 1
        elif letra == " ":
            espacos += 1
        elif letra.isalpha():
            concoantes += 1

    print(f"O resultado da {palavra} é : ")
    print("Vogais: ", vogais)
    print("Espaços: ", espacos)
    print("Consoantes:", consoantes)