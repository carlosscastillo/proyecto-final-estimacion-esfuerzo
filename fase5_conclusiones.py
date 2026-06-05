import numpy as np
from utils import cargar_datos

df_a, df_b = cargar_datos()

metricas  = np.load('metricas.npy')
rmse_mae  = np.load('rmse_mae.npy')
norm_flags = np.load('norm_flags.npy')

r2_a, r2_b   = metricas[0], metricas[1]
b0_a, b1_a   = metricas[2], metricas[3]
b0_b, b1_b   = metricas[4], metricas[5]
rmse_a, rmse_b, mae_a, mae_b = rmse_mae
norm_a, norm_b = bool(norm_flags[0]), bool(norm_flags[1])

r_a = df_a['NESMA'].corr(df_a['Esfuerzo'])
r_b = df_b['NESMA'].corr(df_b['Esfuerzo'])

print("=" * 50)
print("FASE V — RESUMEN DE HALLAZGOS")
print("=" * 50)

print(f"\nDataset A (n=45)")
print(f"  Ecuación  : Ŷ = {b0_a:.4f} + {b1_a:.4f} · X")
print(f"  r Pearson : {r_a:.4f}   R² : {r2_a:.4f}")
print(f"  RMSE      : {rmse_a:.2f}   MAE : {mae_a:.2f}")
print(f"  Normalidad residuales : {'Sí' if norm_a else 'No'}")

print(f"\nDataset B (n=429)")
print(f"  Ecuación  : Ŷ = {b0_b:.4f} + {b1_b:.4f} · X")
print(f"  r Pearson : {r_b:.4f}   R² : {r2_b:.4f}")
print(f"  RMSE      : {rmse_b:.2f}   MAE : {mae_b:.2f}")
print(f"  Normalidad residuales : {'Sí' if norm_b else 'No'}")