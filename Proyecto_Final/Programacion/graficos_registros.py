import matplotlib.pyplot as plt 

class Graficos:

    @staticmethod
    def calcular_estadisticas_mes(registros, mes):
        precipitaciones_dias = registros[mes - 1]  # Obtiene las precipitaciones del mes seleccionado
        max_precipitacion = max(precipitaciones_dias)
        min_precipitacion = min(precipitaciones_dias)
        promedio_precipitacion = sum(precipitaciones_dias) / len(precipitaciones_dias)

        return max_precipitacion, min_precipitacion, promedio_precipitacion
    
    @staticmethod
    def graficar_lluvias_anuales_barra(registros):
        sumas_mensuales = [sum(mes) for mes in registros]
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        
        plt.bar(meses, sumas_mensuales, color='paleturquoise')
        plt.xlabel('Meses')
        plt.ylabel('Lluvias Totales (mm)')
        plt.title('Lluvias Anuales por Mes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def graficar_dispersion_lluvias_dia_mes(registros):
        dias = []
        meses = []
        lluvias_dia = [] 

        for mes_indice, mes in enumerate(registros, start=1): 
            for dia_indice, lluvia in enumerate(mes, start=1):
                dias.append(dia_indice)
                meses.append(mes_indice)
                lluvias_dia.append(lluvia)

        # Ajuste para corregir la paleta de color
        plt.scatter(meses, dias, c=lluvias_dia, cmap='viridis')  # cmap 'viridis' para mejor legibilidad
        plt.colorbar(label='Lluvia (mm)')
        plt.xlabel('Meses (1-12)')
        plt.ylabel('Días (1-31)')
        plt.title('Lluvias Diarias por Mes')
        plt.show()

    @staticmethod
    def graficar_proporcion_lluvia_mes(registros):
        sumas_mensuales = [sum(mes) for mes in registros]
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        
        # Se ajusta la paleta de colores a un rango de 12 colores
        colores = plt.cm.Paired.colors[:12]
        plt.pie(sumas_mensuales, labels=meses, autopct='%1.1f%%', 
                startangle=90, colors=colores)
        plt.title('Proporción de Lluvias por Mes')
        plt.axis('equal')
        plt.show()

    @staticmethod
    def graficar_precipitaciones_por_dia(registros, mes):
        precipitaciones_dias = registros[mes - 1]  # Usa el mes seleccionado
        dias = [f"Día {i+1}" for i in range(len(precipitaciones_dias))]

        plt.pie(precipitaciones_dias, labels=dias, autopct='%1.1f%%', startangle=90)
        plt.title(f'Precipitaciones Diarias del Mes {mes}')
        plt.axis('equal')
        plt.show()