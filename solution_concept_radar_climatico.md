# Radar Climático Caja Trujillo — Solution Concept

Reto: Eje 4 · Inteligencia Predictiva de Riesgo Climático y Crediticio para Microfinanzas.

Cada cifra de este documento lleva su origen: **[Caja]** dato oficial entregado por Caja Trujillo, **[Fuente]** fuente pública citada al final, **[Estimación]** cálculo del equipo que debe validarse con datos de la Caja.

---

## 1. Identificación de la propuesta

| Campo | Valor |
| --- | --- |
| Solución | Radar Climático Caja Trujillo |
| Eje | 4 · Inclusión financiera y resiliencia |
| Equipo | ZAZA SAC |
| Integrantes | Richard Pillaca (coordinador), Piero Huayta, Monica Chilon, Hans Belizario. Los cuatro desarrollan. |
| Tipo de solución | Inteligencia predictiva de riesgo climático y crediticio, con un flujo de 4 agentes de IA y aprobación humana |
| Usuarios | Área de Riesgos, jefes de agencia y asesores de negocio de Caja Trujillo |

---

## 2. Concepto de solución

### El problema

Cuando un evento climático golpea a los negocios de los clientes, la Caja se entera cuando el atraso ya aparece en la cartera. Hoy no cuenta con una forma sistemática de saber antes qué clientes, sectores y zonas son los más vulnerables, cuánto saldo está en juego ni qué hacer con cada cliente.

El momento es ahora. El ENFEN mantiene el estado de Alerta de El Niño Costero y prevé que el evento, iniciado en marzo de 2026, continúe con magnitud extraordinaria hasta febrero de 2027, con lluvias por encima de lo normal en la costa norte y la sierra norte occidental (Comunicado Oficial ENFEN N.° 20-2026) **[Fuente 1]**.

### Qué hace Radar Climático

1. **Predice.** Para cada cliente estima la probabilidad de caer en atraso mayor a 30 días tras un evento climático, en tres escenarios (optimista, base, pesimista). El atraso mayor a 30 días es la señal de deterioro que definió la Caja **[Caja]**.
2. **Mide el impacto.** Suma esas probabilidades por zona, sector económico y segmento de portafolio, y las traduce a saldo en riesgo, alza de la mora, provisiones y pérdida esperada.
3. **Alerta y recomienda.** Genera para cada asesor una lista priorizada de clientes, con el motivo de cada alerta y una recomendación preventiva. Ninguna alerta llega al asesor sin que una persona la apruebe.

### Dos horizontes

| Horizonte | Fuente | Para qué sirve |
| --- | --- | --- |
| Aviso (24 a 96 horas) | Avisos del SENAMHI: lluvia, helada, friaje, calor, viento | Avisar al cliente y proteger mercadería, local e inventario |
| Temporada (meses) | Escenarios del ENFEN: El Niño, La Niña, sequía | Decisiones de crédito y de cartera con tiempo: facilidades, provisiones, priorización de zonas |

La Caja confirmó que puede aplicar medidas especiales o facilidades crediticias a clientes afectados por El Niño **[Caja]**. Radar Climático le indica a quién, dónde y con cuánta anticipación.

### Los 4 agentes

Cada agente toma una decisión, no solo ejecuta un paso.

| Agente | Qué decide | Cómo |
| --- | --- | --- |
| 1. Monitor | Si un aviso amerita abrir un evento, según cuántos clientes y cuánto saldo hay en la zona | Lee directamente las capas ya estructuradas y usa un modelo de lenguaje (LLM) para las fuentes que solo publican texto, como los comunicados del ENFEN |
| 2. Exposición | Qué clientes están realmente en riesgo, no solo expuestos | Cruza el aviso, las zonas de peligro y la ubicación del negocio; un modelo predictivo calcula la probabilidad de atraso y explica los factores de cada caso |
| 3. Estratega | Qué recomendación corresponde a cada segmento | Las reglas que define Riesgos asignan la acción; el LLM redacta el guion del asesor y reinterpreta los ajustes que escribe el aprobador |
| 4. Orquestador | A quién contactar primero y por qué canal | Verifica reglas y consentimiento, y optimiza los contactos según la capacidad de los asesores y los canales de la Caja (presencial, telefónico, digital) **[Caja]** |

### Supervisión humana

- **El jefe de agencia aprueba o ajusta cada evento.** Antes ve cómo se reparten las alertas por zona y sector. Si ajusta, el evento vuelve al Estratega.
- **El área de Riesgos define las reglas** y ve el impacto financiero.
- **Ningún agente decide créditos.** La alerta es un insumo para una persona, nunca una decisión crediticia automática.

### Quién la usa y quién se beneficia

La usa y la opera la Caja. El microempresario no instala nada: recibe una visita, una llamada o un mensaje. Todo cliente expuesto recibe la alerta preventiva; las ofertas de productos solo van a quien dio su consentimiento.

---

## 3. Impacto esperado

### Indicadores del piloto

Son metas, no resultados. Se miden contra un grupo de control en un piloto de 3 meses en 2 agencias.

| Indicador | Hoy | Meta del piloto |
| --- | --- | --- |
| Clientes expuestos contactados antes del evento | No se mide | 70% o más |
| Tiempo desde el aviso hasta la lista aprobada en manos del asesor | No existe el proceso | Menos de 4 horas, incluida la aprobación |
| Atraso mayor a 30 días en clientes contactados frente al grupo de control | Sin comparación | Menor que en el grupo de control; el piloto mide cuánto |
| Diferencia entre el impacto estimado y el observado por agencia | No existe la estimación | Se mide y se usa para recalibrar |

### Pérdida de referencia

| Dato | Valor | Origen |
| --- | --- | --- |
| Pérdida de las operaciones especiales del Niño 2017 | Cerca del 10% de su saldo de capital | **[Caja]** |
| Créditos reprogramados por las cajas municipales en 2017 | S/ 698.8 millones, 3.93% de su cartera directa | **[Fuente 2]** |
| Pérdida de un evento similar con la cartera actual | S/ 3,000 M × 3.93% × 10% ≈ S/ 11.8 millones | **[Estimación]** |

La última fila aplica a Caja Trujillo el promedio de todas las cajas en 2017 y una cartera de S/ 3,000 millones. El valor real se obtiene con el saldo de operaciones especiales de 2017 y 2023 de la propia Caja.

### Propuesta por etapas

No pedimos financiar un proyecto completo sobre un supuesto. Pedimos medir primero.

| Etapa | Qué se hace | Inversión | Condición para pasar a la siguiente |
| --- | --- | --- | --- |
| 1. Piloto (3 meses, 2 agencias) | Calibrar el modelo con el histórico de la Caja y medir, con grupo de control, qué parte de la pérdida climática se evita | Entre S/ 175 mil y S/ 320 mil **[Estimación]** | Que se evite al menos el 13% de la pérdida climática |
| 2. Escala a toda la red | Integración con los sistemas de la Caja, validación independiente del modelo, capacitación | Cerca de S/ 0.66 millones, más S/ 0.34 millones al año de operación **[Estimación]** | Resultados sostenidos por agencia |

El 13% es el punto en que el sistema se paga en 5 años con ese tamaño de equipo **[Estimación]**. Si el piloto queda por debajo, la Caja lo sabe con una inversión acotada.

El costo depende casi por completo del equipo humano. La arquitectura propuesta usa software libre y un único servicio de pago por uso, por lo que infraestructura y licencias pesan poco.

---

## 4. Enfoque tecnológico

Un solo servidor con contenedores (Docker Compose). Corre en una laptop en la demo y puede instalarse en la infraestructura de la Caja en el piloto, sin sacar datos de clientes. El detalle está en `Diagrama_Otras_Tecnologias.html`.

### Tecnologías por función

| Lo que pide el reto | Función | Tecnología |
| --- | --- | --- |
| Georreferenciación | Cruce de avisos y zonas de peligro con la ubicación de cada negocio | PostgreSQL + PostGIS |
| Modelos predictivos | Probabilidad de atraso mayor a 30 días en 3 escenarios, con explicación por cliente | XGBoost + SHAP |
| Analítica avanzada | Impacto financiero por zona, sector y segmento; simulador de temporada | Python (pandas) |
| Inteligencia artificial y agentes | Flujo de 4 agentes con pausa de aprobación; lectura de comunicados y redacción de guiones | LangGraph + API de un LLM (Claude) |
| Optimización | Reparto de contactos por canal según la capacidad de los asesores | OR-Tools |
| Mecanismos de alerta | Lista priorizada, consola de aprobación y mapa | FastAPI + React + Leaflet |
| Control de sesgos | Medición por zona, sector y segmento en la validación del modelo | Fairlearn |

### Tecnología preexistente

| Componente | Tipo | Condición de uso |
| --- | --- | --- |
| Avisos del SENAMHI, comunicados del ENFEN | Datos públicos | Información pública del Estado |
| SIGRID de CENEPRED | Datos geoespaciales | Cuenta de usuario registrado; el equipo ya la tiene |
| PostgreSQL, PostGIS, LangGraph, FastAPI, XGBoost, SHAP, Fairlearn, OR-Tools, React, Leaflet, Docker | Software libre | Licencias abiertas |
| API de Claude | Servicio de terceros | Pago por uso; no recibe datos que identifiquen a un cliente |

Ninguna de estas piezas resuelve el reto por sí sola. El desarrollo nuevo es todo lo que las une: el generador de datos, el modelo, las reglas, los agentes, el cálculo de impacto y la aplicación (sección 5).

### Camino de escala

Si la Caja decide llevarlo a nube pública, cada pieza tiene un equivalente administrado en AWS (`arquitectura_radar_climatico_v2.html`): Step Functions para el flujo, Bedrock para el LLM, SageMaker para el modelo y Aurora para la base. La carga de trabajo no lo exige: el cruce y la puntuación de toda la cartera caben en un servidor.

### Protección de datos

- La cartera llega seudonimizada, con un indicador de consentimiento.
- Nombre y teléfono se quedan en los sistemas de la Caja y se consultan en el servidor solo para la cartera de cada asesor.
- Al LLM solo salen textos de avisos, reglas y perfiles por segmento.
- En el piloto se agregan el acceso con el directorio de la Caja, la bitácora hacia su sistema de seguridad, el respaldo y un modo de operación sin LLM.

---

## 5. Alcance del prototipo

Al cierre de los 2 días se muestra un flujo que funciona de punta a punta con datos sintéticos, no un conjunto de pantallas.

### Qué funciona de verdad y qué se simula

| Función | En el prototipo |
| --- | --- |
| Carga de avisos y zonas de peligro, con copia local | Real |
| Cruce geoespacial de avisos, zonas y clientes | Real |
| Modelo predictivo en 3 escenarios, con explicación por cliente | Real, entrenado con datos sintéticos |
| Impacto financiero por zona, sector y segmento | Real |
| Simulador de temporada con el comunicado del ENFEN | Real |
| Reglas, guion del asesor y ajustes en lenguaje natural | Real |
| Optimización de contactos por canal | Real |
| Tabla de sesgo por zona, sector y segmento | Real |
| Pausa de aprobación y consola del jefe de agencia | Real |
| Lista y mapa del asesor, registro del resultado | Real |
| Carga de la cartera desde los sistemas de la Caja | Simulado: archivo sintético |
| Envío de mensajes al cliente | Simulado: panel de mensajes |
| Acceso con el directorio de la Caja, bitácora externa, respaldo | Fase de piloto |
| Recalibración trimestral del modelo | Se explica; no hay historia que recalibrar |

### Plan de 2 días

Los cuatro integrantes desarrollan, con asistencia de IA para programar.

| Integrante | Frente |
| --- | --- |
| Richard Pillaca | Flujo de agentes, Monitor, pausa de aprobación y API |
| Piero Huayta | Datos sintéticos, base geoespacial, capas, modelo predictivo y tabla de sesgo |
| Monica Chilon | Estratega (reglas, guiones, ajustes), impacto financiero y simulador de temporada |
| Hans Belizario | Aplicación web (Riesgos, aprobación, asesor) y optimización de contactos |

- **Hito del día 1:** el flujo corre completo en consola, desde el aviso hasta el evento pendiente de aprobación.
- **Cierre del día 2:** código congelado y demo ensayada, con video de respaldo.
- **Si falta tiempo, se recorta en este orden:** optimización (se reemplaza por orden de prioridad con tope por asesor), ajustes en lenguaje natural, tabla de sesgo como librería. El impacto financiero, el simulador y la aprobación no se recortan.

### Demostración (3 minutos)

1. **La temporada.** Riesgos abre el simulador con el escenario vigente del ENFEN y ve el impacto estimado por zona, sector y segmento.
2. **Llega un aviso.** El Monitor lo lee y abre un evento; el mapa muestra la zona y los clientes en riesgo.
3. **El jefe de agencia aprueba.** Revisa el reparto de alertas, pide un ajuste por escrito y el evento se recalcula.
4. **El asesor actúa.** Ve su lista priorizada con el motivo de cada alerta y el guion, y registra un contacto.
5. **Se cierra el ciclo.** El indicador de clientes contactados se actualiza y se ve quién quedó sin oferta por no haber dado consentimiento.

---

## 6. Datos e insumos

### Cartera sintética

La Caja no entregará bases de datos **[Caja]** y las bases de la hackathon establecen el uso de datos sintéticos. El equipo genera una cartera ficticia con estos campos:

| Insumo del reto | Campos |
| --- | --- |
| Actividad económica y sector | Código y nombre del rubro, registrado en la evaluación crediticia **[Caja]** |
| Cartera y exposición crediticia | Saldo, cuotas que vencen en la ventana del evento |
| Comportamiento de pago | Días de atraso máximo en 12 meses, atraso actual |
| Sobreendeudamiento | Número de entidades acreedoras, relación cuota a ingreso |
| Portafolios por segmento | Consumo, micro, pequeña, hipotecario, mediana empresa |
| Georreferenciación | Latitud y longitud del negocio, distrito |
| Gestión | Asesor, agencia, indicador de consentimiento |

### Qué se puede afirmar con datos sintéticos

- **Sí:** que el flujo funciona de punta a punta, que el cruce geoespacial es correcto y que el modelo, el impacto financiero y las alertas se calculan y se explican.
- **No:** que el modelo ya predice el atraso real. Sus etiquetas salen de reglas declaradas por el equipo.
- **Por eso** el generador y sus supuestos se publican, y la primera tarea del piloto es recalibrar el modelo con el histórico de la Caja de 2017 y 2023.

### Fuentes externas

| Fuente | Qué aporta | Estado |
| --- | --- | --- |
| SENAMHI | Avisos meteorológicos por zona y nivel | Público |
| ENFEN | Estado y escenarios de El Niño y La Niña | Público, en documentos de texto |
| SIGRID de CENEPRED | Zonas de peligro por inundación y huaico | El equipo tiene cuenta; la descarga de capas está en verificación |
| OpenStreetMap, modelo de elevación, histórico de emergencias de 2017 | Capa de peligro propia si SIGRID no permite la descarga | Alternativa abierta |

Todas las capas se guardan en copia local para que la demo no dependa de la conexión.

### Datos que se pedirían en un piloto

- Cartera seudonimizada con ubicación o distrito del negocio, actualizada al menos una vez al mes.
- Saldos y resultados de las operaciones especiales de 2017 y 2023.
- Serie de atraso mayor a 30 días por agencia.
- Reglas de riesgo y catálogo de facilidades vigentes.
- Tasas de provisión que el área de Riesgos quiere aplicar en el cálculo.

---

## Cómo se cubre cada exigencia del reto

| Exigencia o riesgo | Cómo se cubre |
| --- | --- |
| Identificar clientes, sectores y zonas vulnerables | Probabilidad de atraso por cliente, agregada por zona, sector y segmento |
| Estimar el impacto en la cartera y los estados financieros | Módulo de impacto financiero: saldo en riesgo, mora, provisiones y pérdida esperada |
| Alertas tempranas con recomendaciones | Lista priorizada con motivo y guion, en dos horizontes |
| La exposición no implica pérdida | El modelo pondera la exposición con rubro, comportamiento de pago y capacidad de adaptación, en 3 escenarios |
| Calidad y actualización mensual de la información | Carga mensual de la cartera; cada alerta muestra la fecha del dato |
| Evitar sesgos en clientes y zonas | Medición de sesgo en la validación del modelo y reparto de alertas visible antes de aprobar |
| Confidencialidad | Cartera seudonimizada; datos de contacto dentro de la Caja; el LLM no recibe datos que identifiquen clientes |
| La alerta no es una decisión crediticia automática | Aprobación humana obligatoria; ningún agente decide créditos |
| Fenómenos del reto | Lluvia, inundación, huaico, helada, friaje y calor por aviso; El Niño y sequía por temporada |
| No basta un chatbot o un dashboard | Agentes que deciden, modelo predictivo, optimización y un ciclo que termina en una acción registrada |

---

## 7. Revisión y envío

Lista de comprobación antes de subir el documento:

- [ ] Adjuntar una captura de `Diagrama_Otras_Tecnologias.html`.
- [ ] Abrir el Comunicado Oficial ENFEN N.° 20-2026 y confirmar el texto citado en la sección 2; hay una actualización prevista para el 30 de noviembre de 2026.
- [ ] Confirmar nombres y roles del equipo.
- [ ] Confirmar las licencias de las librerías si el formulario las pide una por una.
- [ ] Confirmar si las capas de peligro de SIGRID se pueden descargar con la cuenta del equipo.
- [ ] Revisar que el reparto del plan de 2 días coincide con lo que cada integrante hará.

## Fuentes

1. ENFEN, Comunicado Oficial N.° 20-2026 (13 de noviembre de 2026): https://enfen.imarpe.gob.pe/comunicados/ · Cobertura: https://andina.pe/agencia/noticia-enfen-nino-costero-extraordinario-continuaria-hasta-inicios-invierno-2027-1099939.aspx
2. Andina, "SBS: Reprogramación de deudas de mypes por Niño suman S/ 2,491 millones" (junio de 2017): https://andina.pe/ingles/noticia-sbs-reprogramacion-deudas-mypes-nino-suman-s-2491-millones-671184.aspx
