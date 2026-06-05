import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from utils import cargar_datos, OUTPUT_DIR

df_a, df_b = cargar_datos()

print("=" * 50)
print("FASE II — REGRESIÓN LINEAL SIMPLE")
print("=" * 50)

def ajustar(df, label):
    X = df['NESMA'].values.reshape(-1, 1)
    y = df['Esfuerzo'].values
    modelo = LinearRegression().fit(X, y)
    y_pred = modelo.predict(X)
    r2     = r2_score(y, y_pred)
    res    = y - y_pred
    print(f"\n{label}")
    print(f"  Ecuación : Ŷ = {modelo.intercept_:.4f} + {modelo.coef_[0]:.4f} · X")
    print(f"  R²       : {r2:.4f}  ({r2*100:.2f}% varianza explicada)")
    return modelo, y_pred, res, r2, modelo.intercept_, modelo.coef_[0]

modelo_a, y_pred_a, res_a, r2_a, b0_a, b1_a = ajustar(df_a, "Dataset A (n=45)")
modelo_b, y_pred_b, res_b, r2_b, b0_b, b1_b = ajustar(df_b, "Dataset B (n=429)")

np.save('res_a.npy', res_a)
np.save('res_b.npy', res_b)
np.save('y_pred_a.npy', y_pred_a)
np.save('y_pred_b.npy', y_pred_b)
np.save('metricas.npy', np.array([r2_a, r2_b, b0_a, b1_a, b0_b, b1_b]))

# Figura 4: Residuales
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Figura 4: Análisis de Residuales', fontsize=13, fontweight='bold')

axes[0,0].scatter(y_pred_a, res_a, alpha=0.7, color='steelblue', edgecolors='black', linewidths=0.3)
axes[0,0].axhline(0, color='red', linestyle='--', linewidth=1.5)
axes[0,0].set(title='Dataset A — Residuales vs. Predichos',
              xlabel='Valores Predichos (Ŷ)', ylabel='Residuales (e)')

stats.probplot(res_a, plot=axes[0,1])
axes[0,1].set_title('Dataset A — Q-Q Plot')
axes[0,1].get_lines()[1].set_color('red')

axes[1,0].scatter(y_pred_b, res_b, alpha=0.4, color='darkorange', edgecolors='black', linewidths=0.2)
axes[1,0].axhline(0, color='red', linestyle='--', linewidth=1.5)
axes[1,0].set(title='Dataset B — Residuales vs. Predichos',
              xlabel='Valores Predichos (Ŷ)', ylabel='Residuales (e)')

stats.probplot(res_b, plot=axes[1,1])
axes[1,1].set_title('Dataset B — Q-Q Plot')
axes[1,1].get_lines()[1].set_color('red')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'figura_4_residuales.png'), dpi=150, bbox_inches='tight')
plt.close()

print("\nFigura generada: figura_4_residuales")