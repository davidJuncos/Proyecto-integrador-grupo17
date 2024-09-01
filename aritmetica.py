#Iniciando el punto 3
#suma
def suma_numeros() ->float:
    print("Sumar")
    a = float(input("numero:  "))
    b = float(input("numero:  "))
    suma= a + b
    print(f"Resultado: {suma}") 
    return suma

   #llamar a la funcion
suma_numeros()

#resta
def restar_numeros() ->float:
    print("Restar")
    a = float(input("número: "))
    b = float(input("número: "))
    resta= a - b
    print(f"Resultado: {resta}") 
    return resta
#llamar resta
restar_numeros()

#dividir
# Manejando errores:Para manejar (capturar) las excepciones podemos usar 
#un bloque de código con las palabras reservada try and except
#Aquel código que se encuentre dentro del bloque try se ejecutará normalmente siempre y cuando haya un error
#Si se produce una excepción, ésta será capturada por el bloque except, ejecutandose el código que contiene.
def dividir_numeros() -> float:
    print("Division")
    a = float(input("número: "))
    b = float(input("número: "))
    
    try:
        dividir = a / b
        print(f"Resultado: {dividir}")
        return dividir
    except ZeroDivisionError:
        print(" Error en la Division ")
        return None
#LLamar a dividir
dividir_numeros()