
def suma_numeros(a,b) ->float:
 suma= a + b
 return suma


def restar_numeros(a,b) ->float:
 resta= a - b
 return resta 

def dividir_numeros(a,b) -> float:
   
    try:
        dividir = a / b
        
        return dividir 
   
    except ZeroDivisionError:
      raise ValueError(" Error en la Division ")
      return None

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