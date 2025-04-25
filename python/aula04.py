def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media = (nota1 + nota2 + nota3+ nota4) / 4

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

calcular_media()
calcular_media()         





def media_notas():
    soma = 0
    for i in range(4):
        nota = float(input(f"Digite a  nota "))
        soma += nota     
        