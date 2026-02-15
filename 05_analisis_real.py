import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import warnings

# 1. CONFIGURACIÓN INICIAL
warnings.filterwarnings('ignore')

# 2. CARGA DE DATOS (Ruta Blindada)
df = pd.read_csv(r"C:\Users\PC\OneDrive\Documentos\ia_ml\datos\telecom_churn_data.csv")

# 3. LIMPIEZA Y CREACIÓN DE VARIABLES
# Llenamos nulos con 0 para que la IA no se trabe
df['sep_vbc_3g'] = df['sep_vbc_3g'].fillna(0)
df['aug_vbc_3g'] = df['aug_vbc_3g'].fillna(0)
df['jul_vbc_3g'] = df['jul_vbc_3g'].fillna(0)

# Creamos nuestra columna objetivo 'churn' (1=Fuga, 0=Sigue)
df['churn'] = (df['sep_vbc_3g'] == 0).astype(int)

# 4. ARQUITECTURA DE IA
X = df[['aug_vbc_3g', 'jul_vbc_3g']] 
y = df['churn']

# Dividimos 80% estudio / 20% examen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. ENTRENAMIENTO DEL BOSQUE (100 Árboles)
modelo_fuga = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_fuga.fit(X_train, y_train)

# 6. REPORTE DE CALIDAD (Texto en terminal)
predicciones = modelo_fuga.predict(X_test)
print("\n--- REPORTE DE CALIDAD ---")
print(classification_report(y_test, predicciones))

# 7. IMPORTANCIA DE VARIABLES (Sin abrir ventanas pesadas)
plt.figure(figsize=(8, 5))
importancia = pd.Series(modelo_fuga.feature_importances_, index=X.columns)
importancia.sort_values().plot(kind='barh', color='skyblue')
plt.title('¿Qué mes influye más en la fuga?')

# GUARDAMOS LA IMAGEN (Busca el archivo en tu carpeta de Windows)
plt.savefig("grafico_importancia.png") 
plt.close() # Cerramos el gráfico internamente para liberar RAM

# 8. CONGELAR EL MODELO
joblib.dump(modelo_fuga, 'modelo_churn_vbc.pkl')

print("\n✅ ¡PROCESO COMPLETADO!")
print("👉 Mira en tu carpeta: 'grafico_importancia.png' ha sido creado.")
print("👉 El modelo 'modelo_churn_vbc.pkl' está listo.")