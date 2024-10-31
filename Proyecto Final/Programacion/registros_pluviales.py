# registros_pluviales.py
import os
import random
import csv

class RegistrosPluviales:
    @staticmethod
    def obtener_ruta_archivo_csv(anio):
        directorio = os.path.dirname(__file__)
        ruta_completa = os.path.join(directorio, "datosAnalizados", f"registroPluvial{anio}.csv")
        ruta_completa = os.path.abspath(ruta_completa)
        return ruta_completa

    @staticmethod
    def cargar_o_generar_registros(anio):
        nombre_archivo = RegistrosPluviales.obtener_ruta_archivo_csv(anio)
        if os.path.exists(nombre_archivo):
            try:
                return RegistrosPluviales.cargar_registros_csv(nombre_archivo)
            except Exception:
                registros = RegistrosPluviales.generar_registros_aleatorios()
                RegistrosPluviales.guardar_registros_csv(nombre_archivo, registros)
                return registros
        else:
            registros = RegistrosPluviales.generar_registros_aleatorios()
            RegistrosPluviales.guardar_registros_csv(nombre_archivo, registros)
            return registros

    @staticmethod
    def cargar_registros_csv(nombre_archivo):
        registros = []
        with open(nombre_archivo, mode='r') as file:
            csv_reader = csv.reader(file)
            for fila in csv_reader:
                registros.append([int(dia) for dia in fila])
        return registros

    @staticmethod
    def guardar_registros_csv(nombre_archivo, registros):
        with open(nombre_archivo, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(registros)
        print(f"Registros guardados en {nombre_archivo}.")

    @staticmethod
    def generar_registros_aleatorios():
        registros = []
        # 12 meses: 31 días (excepto febrero que tiene 28, pero simplificamos aquí)
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for dias in dias_por_mes:
            mes = [random.randint(0, 100) for _ in range(dias)]  # Generar lluvias aleatorias (0 a 100 mm)
            registros.append(mes)
        return registros

    @staticmethod
    def mostrar_registros_por_mes(registros, mes):
        # Mes: Enero=1, Febrero=2, etc.
        if 1 <= mes <= 12:
            print(f"Registros de lluvia para el mes {mes}:")
            for dia, lluvia in enumerate(registros[mes - 1], start=1):
                print(f"Día {dia}: {lluvia} mm")
        else:
            print("Mes inválido. Debes ingresar un número entre 1 y 12.")

    @staticmethod
    def calcular_estadisticas_mes(registros, mes):
        precipitaciones_dias = registros[mes - 1]  
        max_precipitacion = max(precipitaciones_dias)
        min_precipitacion = min(precipitaciones_dias)
        promedio_precipitacion = sum(precipitaciones_dias) / len(precipitaciones_dias)

        return max_precipitacion, min_precipitacion, promedio_precipitacion
