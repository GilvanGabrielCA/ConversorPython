def CtoF():
    c = float(input("Informe a temperatura em celsius: "))
    f = (c * 9 / 5) + 32
    print("{}°C = {}°F".format(c, f))

def CtoK():
    c = float(input("Informe a temperatura em celsius: "))
    k = c + 273.15
    print("{}°C = {}°K".format(c, k))

def FtoC():
    f = float(input("Informe a temperatura em fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("{}°F = {}°C".format(f, c))

def FtoK():
    f = float(input("Informe a temperatura em fahrenheit: "))
    k = (f - 32) * 5 / 9 + 273.15
    print("{}°F = {}°K".format(f, k))

def KtoC():
    k = float(input("Informe a temperatura em Kelvin: "))
    c = k - 273.15
    print("{}°K = {}°C".format(k, c))

def KtoF():
    k = float(input("Informe a temperatura em Kelvin: "))
    f = (k - 273.15) * 9 / 5 + 32
    print("{}°K = {}°C".format(k, f))