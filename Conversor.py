import Medidas
import Graus

def menuTemperatura():
    print("*CONVERSOR DE TEMPERATURA*")
    print("Que temperaturas deseja converter? ")
    print("(1) - °C -> °F * (2) - °C -> °K"
          "(3) - °F -> °C * (4) - °F -> °K"
          "(5) - °K -> °C * (6) - °K -> °F")

def menuMedidas():
    print("*CONVERSOR DE MEDIDAS*")
    print("Que tipos de medidas deseja converter? ")
    print("(1) - Kilometros -> Metro * (2) - Metros - Kilometros * (3) - Kilometros -> Milhas * (4) - Milhas para "
          "Kilometros")

def menuInicial():
    print("O que deseja converter?")
    print("(1) - Medidas * (2) - Temperatura * (3) - Saindo")

def menuBoasVindas():
    print("******************")
    print("*Conversor Python*")
    print("******************")

    print("Bem vindo ao conversor geral Python")

menuBoasVindas()
menuInicial()

op = int(input("Escolha: "))

while 0 < op < 4:
    if op == 1:
        menuMedidas()
        esc = int(input("Selecione uma das opções: "))
        while 0 < esc < 5:
            if esc == 1:
                Medidas.kilometrosToMetros()
                break

            elif esc == 2:
                Medidas.MetrosToKilometros()
                break

            elif esc == 3:
                Medidas.KilometrosToMilhas()
                break

            elif esc == 4:
                Medidas.MilhasToKilometros()
                break

    elif op == 2:
        menuTemperatura()
        esc = int(input("Selecione uma das opcoes: "))

        while 0 < esc < 7:
            if esc == 1:
                Graus.CtoF()
                break

            elif esc == 2:
                Graus.CtoK()
                break

            elif esc == 3:
                Graus.FtoC()
                break

            elif esc == 4:
                Graus.FtoK()
                break

            elif esc == 5:
                Graus.KtoC()
                break

            elif esc == 6:
                Graus.KtoF()
                break

    elif op == 3:
        print("Saindo...")
        op += 1

    if op != 4:
        repete = input("Deseja continuar? [S/N]: ").upper()

        if repete == "N":
            print("Saindo...")
            op += 1

        else:
            menuInicial()

            op = int(input("Escolha: "))
