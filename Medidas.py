def kilometrosToMetros():
    km = float(input("Informe a kilometragem: "))
    m = km * 1000
    print("{} kilometros correspondem a {} metros".format(km, m))

def MetrosToKilometros():
    m = float(input("Informe a metragem: "))
    km = m / 1000
    print("{} Metros correspondem a {} kilometros".format(m, km))

def KilometrosToMilhas():
    km = float(input("Informe a kilometragem: "))
    milhas = km / 1.609  # para um resultado aproximado, o valor é divido por 1,609
    print("{} kilometros correspondem a {} milhas".format(km, milhas))

def MilhasToKilometros():
    milhas = float(input("Informe a milhas: "))
    km = milhas * 1.609  # para um resultado aproximado, multiplique o valor de comprimento por 1,609
    print("{} milhas correspondem a {} kilometros".format(milhas, km))