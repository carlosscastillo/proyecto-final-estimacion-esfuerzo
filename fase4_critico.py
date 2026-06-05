import numpy as np
import matplotlib.pyplot as plt
import os
from utils import cargar_datos, OUTPUT_DIR

df_a, df_b = cargar_datos()

res_a = np.load('res_a.npy')
res_b = np.load('res_b.npy')

print("=" * 50)
print("FASE IV — ANÁLISIS CRÍTICO")
print("=" * 50)

# Sobreestimación / Subestimación
sobre_a = np.sum(res_a < 0) / len(res_a) * 100
sub_a   = np.sum(res_a > 0) / len(res_a) * 100
sobre_b = np.sum(res_b < 0) / len(res_b) * 100
sub_b   = np.sum(res_b > 0) / len(res_b) * 100

print(f"\nSobreestimación (Ŷ > Y) / Subestimación (Ŷ < Y)")
print(f"  Dataset A — Sobre: {sobre_a:.1f}%   Sub: {sub_a:.1f}%")
print(f"  Dataset B — Sobre: {sobre_b:.1f}%   Sub: {sub_b:.1f}%")

# Figura 5: Residuales vs NESMA
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Figura 5: Residuales vs. NESMA — Patrones sistemáticos',
             fontsize=13, fontweight='bold')

axes[0].scatter(df_a['NESMA'], res_a, alpha=0.7, color='steelblue',
                edgecolors='black', linewidths=0.3)
axes[0].axhline(0, color='red', linestyle='--', linewidth=1.5)
axes[0].set(title='Dataset A (n=45)', xlabel='NESMA (X)', ylabel='Residual (e)')

axes[1].scatter(df_b['NESMA'], res_b, alpha=0.4, color='darkorange',
                edgecolors='black', linewidths=0.2)
axes[1].axhline(0, color='red', linestyle='--', linewidth=1.5)
axes[1].set(title='Dataset B (n=429)', xlabel='NESMA (X)', ylabel='Residual (e)')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'figura_5_residuales_vs_nesma.png'), dpi=150, bbox_inches='tight')
plt.close()

print("\nFigura generada: figura_5_residuales_vs_nesma")