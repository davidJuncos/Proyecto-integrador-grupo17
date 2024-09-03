#Iniciando el punto 3
#suma
def suma_numeros(a,b) ->float:
 suma= a + b
 return suma

#resta
def restar_numeros(a,b) ->float:
 resta= a - b
 return resta 
 #dividir
#parametrisar
# Manejando errores:Para manejar (capturar) las excepciones podemos usar 
#un bloque de código con las palabras reservada try and except
#Aquel código que se encuentre dentro del bloque try se ejecutará normalmente siempre y cuando haya un error
#Si se produce una excepción, ésta será capturada por el bloque except, ejecutandose el código que contiene.
def dividir_numeros(a,b) -> float:
   
    try:
        dividir = a / b
        
        return dividir 
   
    except ZeroDivisionError:
      raise ValueError(" Error en la Division ")
      return None
