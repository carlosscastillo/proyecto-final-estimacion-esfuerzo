# Proyecto Final — Estimación de Esfuerzo de Software

**Asignatura:** Estadística para la Calidad de Software  
**Institución:** Universidad Veracruzana — Facultad de Estadística e Informática  
**Técnicas aplicadas:** Modelado Predictivo y Evaluación Estadística  

---

## Descripción

Este proyecto aplica técnicas de análisis exploratorio, regresión lineal simple y evaluación estadística para modelar la relación entre el tamaño funcional de un software (medido en puntos de función NESMA) y el esfuerzo de desarrollo requerido (expresado en horas-hombre).

Se trabajó con dos conjuntos de datos independientes:

| Dataset | Archivo      | Registros |
|---------|--------------|-----------|
| A       | `datos/45.csv`  | 45        |
| B       | `datos/429.csv` | 429       |

Ambos datasets contienen las columnas:
- `FSM` → Tamaño funcional NESMA (variable independiente X)
- `Effort` → Esfuerzo de desarrollo en horas-hombre (variable dependiente Y)

---

## Estructura del repositorio

```
proyecto-final-estimacion-esfuerzo/
├── datos/
│   ├── 45.csv
│   └── 429.csv
├── figuras/               ← se genera automáticamente al ejecutar
├── utils.py               ← carga de datos y configuración compartida
├── fase1_aed.py           ← Fase I:   Análisis Exploratorio de Datos
├── fase2_regresion.py     ← Fase II:  Regresión Lineal Simple
├── fase3_estadistica.py   ← Fase III: Evaluación Estadística
├── fase4_critico.py       ← Fase IV:  Análisis Crítico
├── fase5_conclusiones.py  ← Fase V:   Resumen de Hallazgos
├── .gitignore
└── README.md
```

---

## Requisitos

- Python 3.8 o superior
- Las siguientes librerías:

```
pandas
numpy
matplotlib
scipy
scikit-learn
```

Instalar con:

```bash
pip install pandas numpy matplotlib scipy scikit-learn
```

---

## Ejecución

Los scripts deben ejecutarse **en orden**, ya que cada fase genera archivos intermedios (`.npy`) que la siguiente necesita:

```bash
python fase1_aed.py
python fase2_regresion.py
python fase3_estadistica.py
python fase4_critico.py
python fase5_conclusiones.py
```

Al finalizar, la carpeta `figuras/` contendrá las 5 gráficas del proyecto:

| Archivo                          | Contenido                                      |
|----------------------------------|------------------------------------------------|
| `figura_1_histogramas.png`       | Distribución de NESMA y Esfuerzo               |
| `figura_2_boxplots.png`          | Detección de outliers por variable             |
| `figura_3_dispersion.png`        | Dispersión NESMA vs. Esfuerzo + tendencia      |
| `figura_4_residuales.png`        | Residuales vs. predichos y Q-Q plots           |
| `figura_5_residuales_vs_nesma.png` | Patrones sistemáticos en los errores         |

---

## Resultados obtenidos

### Fase I — Análisis Exploratorio de Datos
| Variable    | Dataset A media | Dataset A r | Dataset B media | Dataset B r |
|-------------|-----------------|-------------|-----------------|-------------|
| NESMA (X)   | 1,339.67        | —           | 977.22          | —           |
| Esfuerzo (Y)| 812.24          | —           | 2,834.26        | —           |

Correlación de Pearson: Dataset A **r = 0.9299** (muy fuerte positiva) · Dataset B **r = 0.8994** (fuerte positiva)

### Fase II — Modelos de Regresión Lineal
| Dataset | Ecuación                   | R²     |
|---------|----------------------------|--------|
| A       | Ŷ = 13.9527 + 0.5959 · X  | 0.8648 |
| B       | Ŷ = 415.1543 + 2.4755 · X | 0.8090 |

### Fase III — Pruebas de normalidad (α = 0.05)
| Dataset | Shapiro-Wilk p | D'Agostino p | Conclusión      |
|---------|----------------|--------------|-----------------|
| A       | 0.3827         | 0.4891       | Normalidad ✓    |
| B       | 0.000011       | 0.0037       | No normalidad ✗ |

Prueba comparativa aplicada: **Mann-Whitney U** (p = 0.1857) → sin diferencias significativas entre modelos.

### Fase III — Métricas comparativas
| Métrica | Dataset A | Dataset B |
|---------|-----------|-----------|
| R²      | 0.8648    | 0.8090    |
| RMSE    | 194.59    | 902.68    |
| MAE     | 154.10    | 695.73    |

### Fase IV — Sobreestimación / Subestimación
| Dataset | Sobreestimación (Ŷ > Y) | Subestimación (Ŷ < Y) |
|---------|-------------------------|------------------------|
| A       | 48.9%                   | 51.1%                  |
| B       | 56.4%                   | 43.6%                  |

Dataset A sin sesgo sistemático. Dataset B tiende a sobreestimar en proyectos pequeños y subestimar en proyectos grandes (heterocedasticidad leve).

### Fase V — Conclusiones
- Relación lineal fuerte confirmada en ambos datasets (r > 0.89)
- Ambos modelos explican más del 80% de la variabilidad del esfuerzo
- Dataset A cumple normalidad; Dataset B no (outliers de alto esfuerzo)
- Rendimiento estadísticamente equivalente entre modelos (Mann-Whitney U p = 0.1857)
- La regresión lineal simple es el enfoque adecuado para ambos datasets