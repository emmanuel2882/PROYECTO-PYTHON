import pandas as pd
from api.api_module import consultar_api
from ui.ui_module import solicitar_datos

def calcular_mediana(df):
    # Nombres de las columnas de interés
    columnas_interes = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']
    
    # Convertir las columnas a valores numéricos
    df[columnas_interes] = df[columnas_interes].apply(pd.to_numeric, errors='coerce')
    
    # Calcular las medianas
    medianas = df[columnas_interes].median()
    
    return medianas

def mostrar_tabla(departamento, municipio, cultivo, topografia, medianas):
    # Crear un DataFrame con los datos para la tabla
    tabla = pd.DataFrame({
        'Departamento': [departamento],
        'Municipio': [municipio],
        'Cultivo': [cultivo],
        'Topografia': [topografia],
        'Mediana pH': [medianas['ph_agua_suelo_2_5_1_0']],
        'Mediana Fósforo (P)': [medianas['f_sforo_p_bray_ii_mg_kg']],
        'Mediana Potasio (K)': [medianas['potasio_k_intercambiable_cmol_kg']]
    })
    
    # Mostrar la tabla
    print(tabla)

def calcular_mediana(df):
    # Nombres de las columnas de interés
    columnas_interes = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']
    
    # Convertir las columnas a valores numéricos
    df[columnas_interes] = df[columnas_interes].apply(pd.to_numeric, errors='coerce')
    
    # Calcular las medianas
    medianas = df[columnas_interes].median()
    
    return medianas

def mostrar_tabla(departamento, municipio, cultivo, topografia, medianas):
    # Crear un DataFrame con los datos para la tabla
    tabla = pd.DataFrame({
        'Departamento': [departamento],
        'Municipio': [municipio],
        'Cultivo': [cultivo],
        'Topografia': [topografia],
        'Mediana pH': [medianas['ph_agua_suelo_2_5_1_0']],
        'Mediana Fósforo (P)': [medianas['f_sforo_p_bray_ii_mg_kg']],
        'Mediana Potasio (K)': [medianas['potasio_k_intercambiable_cmol_kg']]
    })
    
    # Mostrar la tabla
    print(tabla)

import pandas as pd
from api.api_module import consultar_api
from ui.ui_module import solicitar_datos

def main():
    # Solicitar datos al usuario
    departamento, municipio, cultivo, limit = solicitar_datos()
    
    df = consultar_api(departamento, municipio, cultivo, limit)

    # Calcular la mediana
    medianas = calcular_mediana(df)

    # Obtener una topografía representativa (por ejemplo, la primera topografía)
    topografia = df['topografia'].iloc[0] if 'topografia' in df.columns and not df['topografia'].empty else 'Desconocida'

    # Mostrar la tabla con los resultados
    mostrar_tabla(departamento, municipio, cultivo, topografia, medianas)

if __name__ == "__main__":
    main()