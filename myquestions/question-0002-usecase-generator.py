import pandas as pd
import numpy as np

def generar_caso_de_uso():
    n_filas = 30
    df = pd.DataFrame({
        "radiacion_w_m2": np.random.uniform(0, 1100, n_filas),
        "eficiencia_porcentaje": np.random.uniform(15, 22, n_filas)
def eficiencia_promedio_alta_radiacion(df_solar):
    pass

def generar_caso_de_uso():
    n_filas = 30
    df = pd.DataFrame({
        "radiacion_w_m2": np.random.uniform(0, 1100, n_filas),
        "eficiencia_porcentaje": np.random.uniform(15, 22, n_filas)
    })
    
    filtro = df[df['radiacion_w_m2'] > 800]
    if filtro.empty:
        resultado = 0.0
    else:
        resultado = float(filtro['eficiencia_porcentaje'].mean())
        
    return {"df_solar": df}, resultado
