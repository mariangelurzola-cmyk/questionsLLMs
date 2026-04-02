import numpy as np
import random
from sklearn.preprocessing import LabelEncoder

def generar_caso_de_uso_codificar_etiquetas():
    """
    Genera un array aleatorio de etiquetas y su transformación numérica.
    """
    # 1. Crear datos aleatorios (Categorías de texto)
    categorias = ['rojo', 'azul', 'verde', 'amarillo']
    labels = np.array([random.choice(categorias) for _ in range(12)])

    input_data = {'labels': labels}

    # 2. Calcular la respuesta correcta usando LabelEncoder
    le = LabelEncoder()
    output_data = le.fit_transform(labels)

    return input_data, output_data
