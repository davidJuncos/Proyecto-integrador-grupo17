import inspect
import random
import aritmetica

# Lista de operaciones en módulo aritmetica
operaciones = [aritmetica.multiplicar, aritmetica.sumar_n, aritmetica.promedio_n, 
               aritmetica.suma_numeros, aritmetica.restar_numeros, aritmetica.dividir_numeros]

def generar_captcha():
    operacion_aleatoria = random.choice(operaciones)
    numero_de_argumentos = len(inspect.signature(operacion_aleatoria).parameters)

    if operacion_aleatoria in [aritmetica.promedio_n, aritmetica.sumar_n]:
        numero_de_argumentos = max(3, numero_de_argumentos)

    print(f"Operación aleatoria seleccionada: {operacion_aleatoria.__name__}")
    print(f"Número de argumentos: {numero_de_argumentos}")

    argumentos_aleatorios = [round(random.uniform(1.5, 10.5), 2) for _ in range(numero_de_argumentos)]
    resultado = round(operacion_aleatoria(*argumentos_aleatorios), 2)
    return operacion_aleatoria, argumentos_aleatorios, resultado

def formatear_operacion(operacion, argumentos):
    if operacion == aritmetica.sumar_n or operacion == aritmetica.suma_numeros:
        return " + ".join(f"{arg:.2f}" for arg in argumentos)
    elif operacion == aritmetica.restar_numeros:
        return " - ".join(f"{arg:.2f}" for arg in argumentos)
    elif operacion == aritmetica.dividir_numeros:
        return " / ".join(f"{arg:.2f}" for arg in argumentos)
    elif operacion == aritmetica.multiplicar:
        return " * ".join(f"{arg:.2f}" for arg in argumentos)
    elif operacion == aritmetica.promedio_n:
        suma = " + ".join(f"{arg:.2f}" for arg in argumentos)
        return f"({suma}) / {len(argumentos)}"
    return ""

def main(resultado_usuario = None):
    while True:
        operacion_aleatoria, argumentos_aleatorios, resultado_correcto = generar_captcha()
        operacion_str = formatear_operacion(operacion_aleatoria, argumentos_aleatorios)

        print(f"\nOperación generada: {operacion_str}")
        print(f"Resultado correcto (para verificación): {resultado_correcto}")

        while resultado_usuario is None:
            try:
                resultado_usuario = round(float(input(f"¿Cuál es el resultado de la siguiente operación? \n{operacion_str} = ")), 2)
            except ValueError:
                print("Por favor, ingresa un número válido.")
                resultado_usuario = None 
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
                resultado_usuario = None

        if resultado_usuario == resultado_correcto:
            print("Usuario Registrado")
            break
        else:
            print("Resultado incorrecto. Intenta de nuevo.")
            resultado_usuario = None

if __name__ == "__main__":
    main()
