def multiplicar (a,b):
    return round(float(a * b),2)

def sumar_n (*numeros):
        total = 0
        for i in numeros:
            total += i
        return round(float(total), 2)

def promedio_n (*numeros):
    if len(numeros) == 0:
        return 0
    suma = 0
    for i in numeros:
        suma += i
    return round(float(suma / len(numeros)),2)