import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Configuración global de gráficos
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor']   = 'white'
plt.rcParams['axes.grid']        = True
plt.rcParams['grid.alpha']       = 0.3
plt.rcParams['font.size']        = 11

OUTPUT_DIR = "figuras"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def cargar_datos():
    df_a = pd.read_csv('datos/45.csv')
    df_b = pd.read_csv('datos/429.csv')
    df_a.columns = ['NESMA', 'Esfuerzo']
    df_b.columns = ['NESMA', 'Esfuerzo']
    return df_a, df_b