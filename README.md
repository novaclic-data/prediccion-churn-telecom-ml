### 📊  Prediccion de Churn en Telecomunicaciones mediante Machine Learning 

### 📌 Contexto general 

Este repositorio contiene un proyecto práctico enfocado en la toma de decisiones basada en datos , desarrollado en escenarios reales de negocio. 
Donde una importante compañía de telecomunicaciones detectó una caída masiva en el consumo de datos de sus clientes. El objetivo fue identificar patrones de abandono y predecir qué usuarios están en riesgo de fuga antes de que cancelen su servicio. 

### 🛠️  Metologia aplicada 

#### 1. Ingeniería de Datos: Extracción y limpieza de registros reales (7,043 usuarios), gestionando valores nulos y estandarizando tipos de datos numéricos. 

#### 2. Análisis de Tendencias (Feature Engineering): Creación de la métrica "Diferencia de Consumo" para analizar las razones de cancelación, extraer patrones cualitativos que expliquen el por qué detrás del churn y validar o descartar hipótesis. 

#### 3. Modelado Predictivo: Implementación de un algoritmo de Random Forest (Bosque Aleatorio) para clasificar el riesgo de fuga basándose en el comportamiento histórico de consumo. 

#### 4. Decisión final basada en valor real , no en complejidad técnica. 

          ###🏆 Resultados e Impacto: 

*Capacidad de Detección (Recall): 98%. El modelo identifica casi la totalidad de los clientes en riesgo de abandono. 

*Patrón Crítico: Se detectó que el 60% del riesgo está concentrado en el comportamiento del mes de Agosto, permitiendo una ventana de intervención de 30 días antes de la fuga definitiva. 

### 📊 Visualización de Hallazgos Estratégicos 
 
#### 1. La "Huella" del Abandono (Tendencia de Consumo) 
Analizamos el histograma de caída de consumo, donde la línea roja marca el punto crítico de riesgo. 
![Histograma de Caída](grafico_caida_consumo.png) 
*Hallazgo: Identificamos un volumen masivo de clientes con una reducción drástica en el uso de datos 30 días antes de la cancelación.* 
 
#### 2. Lectura de Mente de la IA (Importancia de Variables) 
¿Qué mira nuestro Bosque Aleatorio para decidir quién se va? 
![Importancia de Meses](grafico_importancia.png) 
*Conclusión Técnica: El comportamiento de Agosto es el predictor más fuerte (60% de peso), validando la hipótesis de que la fuga es un proceso progresivo y no un evento aleatorio.* 
 
--- 
 
### 💡 Recomendación Ejecutiva de Negocio 
** Recomiendo estabilizar ingresos identificando los puntos críticos donde se está generando churn. Para luego atacar primero al segmento con más reclamos en soporte, aplicando una mitigación inmediata mientras se mide el impacto.** 

 

 
