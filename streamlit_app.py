import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title("ManageEngine Test Deploy")

# Menú desplegable
option = st.selectbox(
    'Selecciona una opción:',
    ['Opción 1', 'Opción 2', 'Opción 3']
)
st.write('Has seleccionado:', option)

# Deslizador para seleccionar un rango de valores
slider_range = st.slider(
    'Selecciona un rango de valores:',
    0, 100, (25, 75)
)
st.write('El rango seleccionado es:', slider_range)

# Botón de acción
if st.button('Hacer clic'):
    st.write('¡Has hecho clic en el botón!')

# Generar datos de ejemplo
data = {
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valores': np.random.randint(1, 100, 4)
}
df = pd.DataFrame(data)

# Mostrar la tabla de datos
st.write('Tabla de datos de ejemplo:')
st.dataframe(df)

# Gráfico interactivo
st.write('Gráfico de barras de los datos:')
st.bar_chart(df.set_index('Categoría'))

# Otra sección con un gráfico interactivo
st.write('Gráfico de líneas con datos aleatorios:')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Serie A', 'Serie B', 'Serie C']
)
st.line_chart(chart_data)

# Checkbox para mostrar/ocultar elementos
if st.checkbox('Mostrar más detalles'):
    st.write('Aquí hay más detalles sobre la aplicación...')

# Input de texto
user_input = st.text_input('Introduce tu nombre:')
if user_input:
    st.write(f'Hola, {user_input}!')

# Archivo de carga
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('Contenido del archivo:')
    st.dataframe(data)
