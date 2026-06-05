import numpy as np
from scipy.stats import shapiro, normaltest, f_oneway, mannwhitneyu
from sklearn.metrics import r2_score, mean_squared_error
from utils import cargar_datos

df_a, df_b = cargar_datos()

res_a    = np.load('res_a.npy')
res_b    = np.load('res_b.npy')
metricas = np.load('metricas.npy')
r2_a, r2_b = metricas[0], metricas[1]

print("=" * 50)
print("FASE III — EVALUACIÓN ESTADÍSTICA")
print("=" * 50)

# Pruebas de normalidad
def normalidad(res, label):
    sw_stat, sw_p = shapiro(res)
    dp_stat, dp_p = normaltest(res)
    print(f"\n{label}")
    print(f"  Shapiro-Wilk      W = {sw_stat:.6f}   p = {sw_p:.6f}   "
          f"→ {'no normalidad' if sw_p < 0.05 else 'normalidad aceptada'}")
    print(f"  D'Agostino-Pearson K² = {dp_stat:.6f}   p = {dp_p:.6f}   "
          f"→ {'no normalidad' if dp_p < 0.05 else 'normalidad aceptada'}")
    return (sw_p >= 0.05) and (dp_p >= 0.05)

norm_a = normalidad(res_a, "Normalidad residuales — Dataset A")
norm_b = normalidad(res_b, "Normalidad residuales — Dataset B")

# Prueba comparativa
np.random.seed(42)
n = min(len(res_a), len(res_b))
s_a = np.random.choice(res_a, size=n, replace=False)
s_b = np.random.choice(res_b, size=n, replace=False)

print("\nPrueba comparativa de rendimiento")
if norm_a and norm_b:
    stat, p = f_oneway(s_a, s_b)
    prueba  = "ANOVA (F)"
else:
    stat, p = mannwhitneyu(s_a, s_b, alternative='two-sided')
    prueba  = "Mann-Whitney U"

print(f"  Prueba aplicada : {prueba}")
print(f"  Estadístico     : {stat:.6f}")
print(f"  p-valor         : {p:.6f}")
print(f"  Decisión        : {'diferencias significativas' if p < 0.05 else 'sin diferencias significativas'}")

# Métricas comparativas
rmse_a = np.sqrt(mean_squared_error(df_a['Esfuerzo'], df_a['Esfuerzo'] - res_a + res_a))
rmse_a = np.sqrt(np.mean(res_a**2))
rmse_b = np.sqrt(np.mean(res_b**2))
mae_a  = np.mean(np.abs(res_a))
mae_b  = np.mean(np.abs(res_b))

print(f"\n{'Métrica':<20} {'Dataset A':>12} {'Dataset B':>12}")
print("-" * 44)
print(f"{'R²':<20} {r2_a:>12.4f} {r2_b:>12.4f}")
print(f"{'RMSE':<20} {rmse_a:>12.4f} {rmse_b:>12.4f}")
print(f"{'MAE':<20} {mae_a:>12.4f} {mae_b:>12.4f}")

# Guardar para la siguiente fase
np.save('norm_flags.npy', np.array([norm_a, norm_b]))
np.save('rmse_mae.npy', np.array([rmse_a, rmse_b, mae_a, mae_b]))
