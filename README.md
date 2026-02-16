## 📊 CAPITULO 1: Prediccion de Churn en Telecomunicaciones mediante Machine Learning 

### 📌 Contexto general 

Este repositorio contiene un conjunto de proyectos prácticos enfocados en la toma de decisiones basada en datos , desarrollados en escenarios reales de negocio. 
Donde una importante compañía de telecomunicaciones detectó una caída masiva en el consumo de datos de sus clientes. El objetivo fue identificar patrones de abandono y predecir qué usuarios están en riesgo de fuga antes de que cancelen su servicio. 

### 🛠️  Metologia aplicada 

#### 1. Ingeniería de Datos: Extracción y limpieza de registros reales (7,043 usuarios), gestionando valores nulos y estandarizando tipos de datos numéricos. 

#### 2. Análisis de Tendencias (Feature Engineering): Creación de la métrica "Diferencia de Consumo" para analizar las razones de cancelación, extraer patrones cualitativos que expliquen el por qué detrás del churn y validar o descartar hipótesis. 

#### 3. Modelado Predictivo: Implementación de un algoritmo de Random Forest (Bosque Aleatorio) para clasificar el riesgo de fuga basándose en el comportamiento histórico de consumo. 

#### 4. Decisión final basada en valor real , no en complejidad técnica. 

### 🏆 Resultados e impacto

**Capacidad de Detección (Recall): 98%. El modelo identifica casi la totalidad de los clientes en riesgo de abandono.** 

**Patrón Crítico: Se detectó que el 60% del riesgo está concentrado en el comportamiento del mes de Agosto, permitiendo una ventana de intervención de 30 días antes de la fuga definitiva.** 


### 📊 Visualización de Hallazgos Estratégicos 
 
#### 1. La "Huella" del Abandono (Tendencia de Consumo) 
Analizamos el histograma de caída de consumo, donde la línea roja marca el punto crítico de riesgo. 
![Histograma de Caída](grafico_caida_consumo.png) 

**Hallazgo: Identificamos un volumen masivo de clientes con una reducción drástica en el uso de datos 30 días antes de la cancelación.** 

<img width="1000" height="500" alt="grafico_caida_consumo" src="https://github.com/user-attachments/assets/fd68e61b-b8ba-4978-9053-8d1d6743b715" />


---
 
#### 2. Lectura de Mente de la IA (Importancia de Variables) 
**¿Qué mira nuestro Bosque Aleatorio para decidir quién se va?** 
![Importancia de Meses](grafico_importancia.png) 


<img width="800" height="500" alt="grafico_importancia" src="https://github.com/user-attachments/assets/8d3d5e3a-81ba-4307-a9b9-741fedd255c0" />


### 💡 ConclusionTécnica 
**El comportamiento de Agosto es el predictor más fuerte (60% de peso), validando la hipótesis de que la fuga es un proceso progresivo y no un evento aleatorio.**
 
### 💰 Recomendación Ejecutiva de Negocio 
**Recomiendo estabilizar ingresos identificando los puntos críticos donde se está generando churn. Para luego atacar primero al segmento con más reclamos en soporte, aplicando una mitigación inmediata mientras se mide el impacto.** 




-----



## 💎 CAPITULO 2: Analisis de Rentabilidad y Segmentacion (ARPU)  

### 🎯 El Desafio de negocio 
No basta con saber **quién se va, sino cuánto** le cuesta a la empresa. En esta fase, analizamos el **ARPU (Average Revenue Per User)** para identificar si estamos perdiendo a nuestros clientes más valiosos (VIP) o a usuarios de bajo consumo. 
 
#### 📊 Hallazgos Criticos de Valor del Cliente (ARPU) 

**Al cruzar los datos de facturación con la fuga, obtuvimos una radiografía financiera reveladora:** 
No todas las fugas impactan igual al negocio. Tras segmentar el ARPU (Average Revenue Per User), descubrimos un hallazgo crítico: 
*   **Clientes Fieles (Churn 0): Tienen un gasto promedio de $468.1.** 
*   **Clientes Fugados (Churn 1): Tienen un gasto promedio de $268.4.**
![Diferencia de valor](grafico_arpu_valor.png)

<img width="800" height="500" alt="grafico_arpu_valor" src="https://github.com/user-attachments/assets/a0937c79-5384-44d9-8dea-e6d4dee187fc" />

 
#### 🔍  Segmentacion Por Uso de Datos (Heavy Users) 

Clasificamos a los usuarios según su intensidad de uso en la red 3G: 
*   **Usuarios Normales:** Registran una tasa de fuga crítica del **97.5%**. 
*   **Usuarios Pesados (>100MB):** Muestran una mayor retención, con una fuga del **72.3%**. 
 
### 💡 Conclusion 

Los clientes de mayor valor (VIP) muestran una lealtad un 74% superior a los clientes básicos. La "hemorragia" de clientes está concentrada en los segmentos de menor rentabilidad, lo que permite priorizar esfuerzos de retención en la base de clientes de alto valor para blindar los ingresos principales. 

### 💰 Estrategia de Salvamento 
*   **Recomiendo una 'Retención Selectiva': blindar al segmento VIP ($468) con ofertas de fidelización, mientras se optimiza el costo de adquisición en el segmento básico, donde la lealtad es mínima.** 

##### ✨  > **Nota técnica:** 
##### **El modelo entrenado (.pkl) no se incluye en el repositorio debido a restricciones de tamaño de GitHub, pero está disponible para su implementación local.** 

 

 
 

 
