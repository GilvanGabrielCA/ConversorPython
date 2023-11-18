print("******************")
print("*Conversor Python*")
print("******************")

print("Bem vindo ao conversor geral Python")

print("O que deseja converter?")
print("(1) - Medidas * (2) - Temperatura * (3) - Moedas")

op = int(input("Escolha: "))

while 0 < op < 4:
    if op == 1:
        print("*CONVERSOR DE MEDIDAS*")
        print("Que tipos de medidas deseja converter? ")
        print("(1) - Kilometros -> Metro * (2) - Metros - Kilometros * (3) - Kilometros -> Milhas * (4) - Milhas para "
              "Kilometros")

        tp = int(input("Selecione uma das opções: "))

        while 0 < tp < 5:
            if tp == 1:
                km = float(input("Informe a kilometragem: "))
                m = km * 1000

                print("{} kilometros correspondem a {} metros".format(km, m))

            elif tp == 2:
                m = float(input("Informe a metragem: "))
                km = m / 1000

                print("{} Metros correspondem a {} kilometros".format(m, km))

            elif tp == 3:
                km = float(input("Informe a kilometragem: "))
                milhas = km / 1.609 #para um resultado aproximado, o valor é divido por 1,609

                print("{} kilometros correspondem a {} milhas".format(km, milhas))

            elif tp == 4:
                milhas = float(input("Informe a milhas: "))
                km = milhas * 1.609 #para um resultado aproximado, multiplique o valor de comprimento por 1,609

    elif op == 2:
        print("*CONVERSOR DE TEMPERATURA*")
        print("Que temperaturas deseja converter? ")
        print("(1) - °C -> °F * (2) - °C -> °K"
              "(3) - °F -> °C * (4) - °F -> °K"
              "(5) - °K -> °C * (6) - °K -> °F")

        esc = int(input("Selecione uma das opcoes: "))

        while 0 < esc < 7:
            if esc == 1:
                c = float(input("Informe a temperatura em celsius: "))
                f = (c * 9 / 5) + 32

                print("{}°C = {}°F".format(c, f))

            elif esc == 2:
                c = float(input("Informe a temperatura em celsius: "))
                k = c + 273,15

                print("{}°C = {}°K".format(c, k))

            elif esc == 3:
                f = float(input("Informe a temperatura em fahrenheit: "))
                c = (f - 32) * 5 / 9

                print("{}°F = {}°C".format(f, c))

            elif esc == 4:
                f = float(input("Informe a temperatura em fahrenheit: "))
                k = (f - 32) * 5 / 9 + 273.15

                print("{}°F = {}°K".format(f, k))

            elif esc == 5:
                k = float(input("Informe a temperatura em Kelvin: "))
                c = k - 273.15

                print("{}°K = {}°C".format(k, c))

            elif esc == 6:
                k = float(input("Informe a temperatura em Kelvin: "))
                f = (k - 273.15) * 9/5 + 32

                print("{}°K = {}°C".format(k, f))
