import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_normalizar_min_max():
    """
    Genera un caso de prueba aleatorio para la función normalizar_min_max.
    Crea un DataFrame con valores numéricos y calcula el resultado esperado.
    """
    # 1. Crear datos aleatorios
    n_filas = 10
    df = pd.DataFrame({
        'A': np.random.uniform(0, 100, n_filas),
        'B': np.random.uniform(10, 20, n_filas),
        'C': np.random.uniform(50, 60, n_filas)
    })
    
    # Seleccionamos una columna al azar para normalizar
    columnas_a_procesar = [random.choice(['A', 'B', 'C'])]
    
    # 2. Guardar el input
    input_data = {
        'df': df.copy(),
        'columnas': columnas_a_procesar
    }
    
    # 3. Calcular la respuesta correcta (Ground Truth)
    df_res = df.copy()
    for col in columnas_a_procesar:
        valor_min = df_res[col].min()
        valor_max = df_res[col].max()
        # Aplicamos la fórmula (x - min) / (max - min)
        df_res[col] = (df_res[col] - valor_min) / (valor_max - valor_min)
    
    output_data = df_res
    
    return input_data, output_data
