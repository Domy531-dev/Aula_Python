from datetime import datetime

def mostrar_data_hora():
    agora = datetime.now()
    print("A data e hora de a é: ")
    print(agora.strftime())