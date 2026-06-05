import numpy as np
import matplotlib.pyplot as plt
import os
from utils import cargar_datos, OUTPUT_DIR

df_a, df_b = cargar_datos()

# Estadísticos descriptivos
def stats(df, label):
    print(f"\n{label}")
    print(f"  Media     — NESMA: {df['NESMA'].mean():.2f}   Esfuerzo: {df['Esfuerzo'].mean():.2f}")
    print(f"  Mediana   — NESMA: {df['NESMA'].median():.2f}   Esfuerzo: {df['Esfuerzo'].median():.2f}")
    print(f"  Desv.Std  — NESMA: {df['NESMA'].std():.2f}   Esfuerzo: {df['Esfuerzo'].std():.2f}")
    print(f"  Mín/Máx   — NESMA: {df['NESMA'].min()} / {df['NESMA'].max()}   "
          f"Esfuerzo: {df['Esfuerzo'].min()} / {df['Esfuerzo'].max()}")
    print(f"  Q1 / Q3   — NESMA: {df['NESMA'].quantile(.25):.2f} / {df['NESMA'].quantile(.75):.2f}   "
          f"Esfuerzo: {df['Esfuerzo'].quantile(.25):.2f} / {df['Esfuerzo'].quantile(.75):.2f}")

print("=" * 50)
print("FASE I — ANÁLISIS EXPLORATORIO DE DATOS")
print("=" * 50)
stats(df_a, "Dataset A (n=45)")
stats(df_b, "Dataset B (n=429)")

# Correlación de Pearson
r_a = df_a['NESMA'].corr(df_a['Esfuerzo'])
r_b = df_b['NESMA'].corr(df_b['Esfuerzo'])
print(f"\nCorrelación de Pearson")
print(f"  Dataset A: r = {r_a:.4f}")
print(f"  Dataset B: r = {r_b:.4f}")

# Figura 1: Histogramas
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Figura 1: Histogramas — Dataset A y B', fontsize=13, fontweight='bold')
axes[0,0].hist(df_a['NESMA'],    bins=10, color='steelblue', edgecolor='black', alpha=0.8)
axes[0,0].set(title='Dataset A — NESMA', xlabel='Puntos de Función', ylabel='Frecuencia')
axes[0,1].hist(df_a['Esfuerzo'], bins=10, color='coral',     edgecolor='black', alpha=0.8)
axes[0,1].set(title='Dataset A — Esfuerzo', xlabel='Horas-Hombre', ylabel='Frecuencia')
axes[1,0].hist(df_b['NESMA'],    bins=20, color='steelblue', edgecolor='black', alpha=0.8)
axes[1,0].set(title='Dataset B — NESMA', xlabel='Puntos de Función', ylabel='Frecuencia')
axes[1,1].hist(df_b['Esfuerzo'], bins=20, color='coral',     edgecolor='black', alpha=0.8)
axes[1,1].set(title='Dataset B — Esfuerzo', xlabel='Horas-Hombre', ylabel='Frecuencia')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'figura_1_histogramas.png'), dpi=150, bbox_inches='tight')
plt.close()

# Figura 2: Boxplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Figura 2: Boxplots — Detección de outliers', fontsize=13, fontweight='bold')
for ax, df, titulo in zip(axes, [df_a, df_b], ['Dataset A (n=45)', 'Dataset B (n=429)']):
    ax.boxplot([df['NESMA'], df['Esfuerzo']], tick_labels=['NESMA', 'Esfuerzo'],
               patch_artist=True, boxprops=dict(facecolor='lightblue'),
               medianprops=dict(color='red', linewidth=2))
    ax.set(title=titulo, ylabel='Valor', xlabel='Variable')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'figura_2_boxplots.png'), dpi=150, bbox_inches='tight')
plt.close()

# Figura 3: Dispersión
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Figura 3: Dispersión NESMA vs. Esfuerzo', fontsize=13, fontweight='bold')
for ax, df, titulo, color in zip(axes, [df_a, df_b],
                                  ['Dataset A (n=45)', 'Dataset B (n=429)'],
                                  ['steelblue', 'darkorange']):
    ax.scatter(df['NESMA'], df['Esfuerzo'], alpha=0.6, color=color,
               edgecolors='black', linewidths=0.3, s=40)
    m, b = np.polyfit(df['NESMA'], df['Esfuerzo'], 1)
    x_line = np.linspace(df['NESMA'].min(), df['NESMA'].max(), 200)
    ax.plot(x_line, m * x_line + b, color='red', linewidth=2,
            label=f'Ŷ = {m:.2f}X + {b:.2f}')
    ax.set(title=titulo, xlabel='NESMA (Puntos de Función)', ylabel='Esfuerzo (Horas-Hombre)')
    ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'figura_3_dispersion.png'), dpi=150, bbox_inches='tight')
plt.close()

print("\nFiguras generadas: figura_1_histogramas, figura_2_boxplots, figura_3_dispersion")