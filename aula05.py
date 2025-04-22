def solicitar_idade():
    while True:
        idade = int(input("Digite sua idade"))

        if idade >= 0 and idade <= 120:
            print("Idade registrada: " , idade)
            break
        else:
            print("Idade Invalida. Tente novamente!")
solicitar_idade()









def menu_simples():
    opcao = ""

    while opcao !=3:
        print(" Ver mensagem ")
        print(" 2- Repetir Menu ")
        print(" Sair ")
        opcao = input("Escolha uma opção")

        if opcao == "1":
            print("Você escolheu ver a primeira mensagem!")
        elif opcao == "2":
            print("Você escolheu ver a segunda mensagem!")
        elif opcao != "3":
            print("Opção inválida!")
    print("Programa encerrado. Até a próxima xD")

menu_simples()