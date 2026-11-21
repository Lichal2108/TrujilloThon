# Radar Climático Caja Trujillo — Modelo de solución E2E

> Archivo de contexto reutilizable. Reúne todo lo definido para el reto de Caja Trujillo en la hackathon: problema, solución, arquitectura, procesos, datos, normativa, costos y ROI, plan de implementación y demo.
> Última actualización: 21 de noviembre de 2026 (incluye el Solution Concept con los 8 componentes y los criterios de evaluación).

---

## 0. Ficha del proyecto

| Campo | Valor |
| --- | --- |
| Nombre de la solución | Radar Climático Caja Trujillo |
| Equipo | ZAZA SAC (4 integrantes) |
| Integrantes | Richard Pillaca (coordinador, desarrollo tecnológico) · Piero Huayta (desarrollo tecnológico) · Monica Chilon (innovación y negocio) · Hans Belizario (innovación y negocio) |
| Tiempo de implementación | 2 días de hackathon (sede Trujillo) |
| Tipo de solución | Flujo agéntico de IA (4 agentes) con aprobación humana |
| Documento en Claude | https://claude.ai/artifact/Jjq7ZqaVPCFDCF4k7ojpTy |

---

## 1. El reto

**Pregunta de innovación:** ¿Cómo podríamos anticipar los riesgos que los eventos climáticos representan para los negocios financiados por Caja Trujillo y desarrollar estrategias preventivas que fortalezcan su resiliencia?

**Problemática:**
- Lluvias intensas, inundaciones y sequías afectan la actividad de los microempresarios, sobre todo en zonas vulnerables o en rubros sensibles al clima.
- Causan daños en infraestructura, pérdida de inventarios, dificultad de acceso a mercados e interrupciones, afectando ingresos y capacidad de pago.
- Para la microfinanciera, identificarlo a tiempo permite anticipar el impacto en clientes y en la calidad de cartera.
- Combinar información geográfica, actividad económica, características del negocio y escenarios climáticos permite detectar patrones de vulnerabilidad.

**Resultado esperado:** fortalecer la resiliencia de los clientes y de la cartera mediante identificación anticipada de riesgos climáticos y decisiones preventivas.

**Datos e insumos (referenciales, sin compromiso de entrega):** ubicación geográfica, actividad económica, información climática, mapas de amenazas, escenarios climáticos, exposición crediticia, datos sintéticos.

**Riesgos que pide considerar el reto:** incertidumbre de los escenarios; no asumir que exposición = pérdida o incumplimiento; recomendaciones basadas en evidencia; protección de datos y políticas de riesgo de la Caja.

**Complejidad tecnológica exigida:** IA, agentes, analítica predictiva, optimización o automatización avanzada cuando aporten valor. No basta con chatbots genéricos, dashboards, formularios ni automatizaciones básicas. Hay que demostrar desarrollo funcional, integración tecnológica y valor diferencial.

### Cómo cumple la solución cada restricción

| Restricción | Cómo la cumple Radar Climático |
| --- | --- |
| Incertidumbre de escenarios | Score en 3 escenarios (optimista, base, pesimista) con rango, nunca sí/no |
| Exposición ≠ pérdida | La exposición se pondera por sensibilidad del rubro y capacidad de adaptación |
| Basado en evidencia | Explicación SHAP por cliente + política que justifica el producto |
| Protección de datos y políticas | PII no sale de la Caja; políticas consultadas por RAG |
| No chatbot / dashboard | Ciclo agéntico autónomo: detecta, cruza, decide, crea el evento, aprende |
| Desarrollo funcional e integración | Integración real con SIGRID/SENAMHI, PostGIS y un LLM en la demo |

---

## 2. Resumen ejecutivo

Radar Climático es un flujo de 4 agentes de IA que detecta amenazas climáticas, encuentra qué clientes de Caja Trujillo están expuestos y entrega a cada asesor una cartera priorizada con el producto preventivo que le corresponde. Ningún cliente es contactado sin que antes un humano apruebe el evento.

- **Para quién:** comité de riesgos (decide), asesores de negocio (actúan), clientes microempresarios en zonas vulnerables (reciben la protección).
- **Qué cambia:** la Caja deja de reaccionar cuando la mora ya subió y actúa días antes del evento, con lista concreta de clientes, el porqué de cada uno y qué ofrecerle.
- **Diferencial:** no es dashboard ni chatbot; es un ciclo autónomo que se dispara solo ante un aviso, arma una campaña y aprende de cada resultado.
- **Valor:** inversión inicial S/ 1.24 M, operación S/ 484 mil/año. Punto de equilibrio: evitar que se deterioren S/ 2.4 M de cartera al año (0.08% de una cartera de S/ 3,000 M). Escenario base: ROI +205% a 5 años.

**Frase de pitch:** "El proyecto se paga si evita que se deteriore el 0.08% de la cartera al año. En 2017 las cajas municipales tuvieron que reprogramar el 3.93% de su cartera por el Niño Costero."

---

## 3. Solution Concept (formato de la organización)

Los 8 componentes en el orden que pide la organización. El resto del archivo es el sustento.

### 3.1 Problema abordado

Los microempresarios que financia Caja Trujillo en zonas vulnerables pierden infraestructura, inventario y acceso a mercados con lluvias intensas, inundaciones y sequías, y eso termina en mora. Hoy la Caja no tiene una forma sistemática de saber, antes del evento, qué clientes están expuestos ni qué hacer con cada uno: reacciona cuando la mora ya subió.

El costo de llegar tarde es real: la mora de Caja Trujillo fue 9.45% en 2024 frente a 6.27% del promedio de cajas municipales, y tras el Niño Costero 2017 las cajas reprogramaron el 3.93% de su cartera.

### 3.2 Concepto de solución

Flujo de 4 agentes de IA que se dispara solo cuando llega un aviso climático:

1. **Monitor** detecta la amenaza y delimita la zona afectada.
2. **Exposición** cruza esa zona con la cartera y calcula un score de vulnerabilidad por cliente (3 escenarios, con explicación).
3. **Estratega** segmenta en prevenir / proteger / reactivar y asigna el producto que permite la política de la Caja.
4. **Orquestador** arma un evento de campaña preventiva y lo deja en pausa.

El comité de riesgos aprueba o ajusta el evento. Recién entonces cada asesor recibe en su app su cartera priorizada, con el porqué de cada cliente y un guion; los clientes con consentimiento reciben una alerta. Cada resultado reentrena el modelo.

### 3.3 Impacto esperado

KPI del desafío: resiliencia de los clientes y calidad de la cartera. Metas propuestas para un piloto de 3 meses en 2 agencias de La Libertad (son metas, no resultados; se validan con grupo de control):

| KPI | Situación actual | Meta del piloto |
| --- | --- | --- |
| Cartera expuesta contactada antes del evento | No se mide de forma sistemática | ≥ 70% |
| Tiempo desde el aviso hasta la cartera en manos del asesor | No existe el proceso | < 1 hora |
| Alza de mora a 90 días en clientes contactados | Sin comparación | 20% menor que el grupo de control |
| Contactados con consentimiento que toman un producto preventivo | No aplica | ≥ 10% |

Financiero: se paga si evita el deterioro del 0.08% de la cartera al año (≈ S/ 2.4 M). Escenario base: ROI +205% a 5 años, VAN S/ 4.91 M (ver sección de costos).

### 3.4 Enfoque tecnológico

Flujo agéntico con humano en el ciclo, sobre arquitectura híbrida donde los datos personales no salen de la Caja.

- **Agentes:** LangGraph en la demo; Step Functions + Bedrock AgentCore en producción.
- **Geoespacial:** PostgreSQL + PostGIS para cruzar polígonos de amenaza con la ubicación de cada negocio.
- **Analítica predictiva:** XGBoost con 3 escenarios + SHAP.
- **IA generativa:** LLM (Claude) con RAG sobre políticas y catálogo, seguido de validación con reglas.
- **Interfaz:** PWA del asesor (lista, mapa, ficha) y consola de riesgos.
- **Producción:** AWS sa-east-1 solo con datos seudonimizados y climáticos, conectado por VPN a la nube privada de la Caja. La demo corre completa en Docker Compose.

### 3.5 Tecnología preexistente

Datos públicos, librerías open source y un LLM de terceros; ninguno resuelve el problema por sí solo, lo que los une es desarrollo propio (3.6).

| Componente | Tipo | Licencia o condición | Uso |
| --- | --- | --- | --- |
| Avisos SENAMHI y comunicados ENFEN | Datos públicos | Información pública del Estado | Amenazas de corto plazo y El Niño |
| SIGRID de CENEPRED (ArcGIS REST) | Datos geoespaciales públicos | Información pública del Estado | Polígonos de peligro y escenarios |
| PostgreSQL + PostGIS | Base de datos | Open source (PostgreSQL License / GPLv2) | Cruce geoespacial |
| LangGraph | Framework de agentes | Open source (MIT) | Orquestar los 4 agentes y la pausa de aprobación |
| XGBoost y SHAP | Librerías de ML | Open source (Apache 2.0 / MIT) | Score y explicación |
| Claude (API de Anthropic o Amazon Bedrock) | Servicio de terceros | Pago por uso | Estratega y guiones |
| FastAPI, React, Leaflet + OpenStreetMap | Web y mapas | Open source (MIT / BSD-2); datos OSM bajo ODbL | Backend, app y mapa |
| Docker Compose | Contenedores | Open source | Levantar la demo |
| Servicios de AWS | Nube | Pago por uso | Solo arquitectura de producción |

### 3.6 Funcionalidad crítica (desarrollo nuevo en la fase presencial)

1. **Orquestación agéntica:** 4 agentes encadenados con el evento en pausa hasta la aprobación humana.
2. **Motor de exposición:** cruce geoespacial cartera × polígonos de amenaza.
3. **Score climático:** 3 escenarios, rango de incertidumbre y explicación SHAP en lenguaje simple.
4. **Estratega:** segmentación prevenir / proteger / reactivar y asignación de productos sobre políticas, con validación por reglas y filtro de consentimiento.
5. **App del asesor (PWA):** cartera priorizada, mapa, ficha con el porqué, guion y registro del resultado.
6. **Consola de riesgos:** revisión, aprobación o ajuste del evento, y KPIs.

### 3.7 Nivel de desarrollo esperado

MVP funcional de punta a punta con datos sintéticos, no un prototipo de pantallas: un aviso real o realista dispara los agentes, se crea el evento, riesgos lo aprueba, el asesor ve su cartera y registra un contacto que actualiza el KPI.

- **Funciona de verdad:** ingesta de SIGRID o SENAMHI, cruce en PostGIS, score con SHAP, Estratega con LLM y RAG, pausa de aprobación, app del asesor, consola de riesgos.
- **Simulado y explicado en el pitch:** carga desde el core (CSV en vez de DMS), cola de asignación (`asesor_id` en vez de SQS), envío de SMS/push (panel de enviados y excluidos), reentrenamiento automático.

### 3.8 Factibilidad y dependencias

Construible en 2 días porque la demo no depende de entregas de la Caja ni de desplegar en la nube.

| Aspecto | Detalle |
| --- | --- |
| Tiempo | Plan de 2 días; hito al cierre del día 1: motor de punta a punta en consola |
| Equipo | 4 personas: 2 de desarrollo tecnológico, 2 de innovación y negocio |
| Infraestructura | Laptops con Docker; el modelo corre en CPU, sin GPU |
| Integraciones externas | SIGRID y SENAMHI (públicos, con copia local de respaldo) y API del LLM |
| Licencias | Open source de uso libre; LLM y AWS pago por uso |
| Dependencias de la Caja para la demo | Ninguna: datos sintéticos y políticas de ejemplo |
| Dependencias de la Caja para un piloto | Cartera seudonimizada con ubicación, políticas de riesgo, catálogo real, registro de consentimientos |

### 3.9 Cruce con los criterios de evaluación

| Criterio | Peso | Dónde se sustenta |
| --- | --- | --- |
| Alineación al desafío | 25% | Restricciones del reto respondidas punto por punto (sección 1) |
| Impacto potencial | 30% | Metas del piloto sobre el KPI, punto de equilibrio 0.08% y ROI (3.3 y sección de costos) |
| Viabilidad técnica | 25% | Stack probado, equivalencia demo → producción, cumplimiento normativo (arquitectura y normativa) |
| Factibilidad de construcción | 20% | 6 desarrollos nuevos acotados, plan de 2 días con hito, cero dependencias de la Caja para la demo (3.6 a 3.8 y plan) |

**Nota de la organización:** se pueden usar tecnologías preexistentes siempre que se identifiquen y se proponga un desarrollo funcional nuevo o una adaptación sustantiva en la fase presencial (cubierto en 3.5 y 3.6).

---

## 4. Propuesta de solución: los 4 agentes

| Agente | Qué hace | Entrada | Salida | Tecnología |
| --- | --- | --- | --- | --- |
| 1. Monitor | Detecta y clasifica la amenaza: tipo, nivel, zona, ventana de tiempo | Avisos SENAMHI (hasta 96 h), comunicados ENFEN, escenarios CENEPRED | Alerta con polígono afectado | Lambda + EventBridge |
| 2. Exposición | Cruza la zona con la cartera y calcula el score | Alerta + cartera seudonimizada | Clientes expuestos con score, rango y explicación | PostGIS + SageMaker (XGBoost + SHAP) |
| 3. Estratega | Segmenta en prevenir / proteger / reactivar y asigna productos según política | Clientes con score + políticas y catálogo | Producto y guion por cliente | Bedrock AgentCore + Knowledge Base (RAG) |
| 4. Orquestador | Arma el evento de campaña y lo envía a aprobación | Cartera segmentada | Evento: cartera, ventana, productos, prioridad | Step Functions + DynamoDB |

**Reglas que gobiernan a los agentes:**
- Ningún agente aprueba créditos ni promete reprogramaciones. Solo proponen; el comité decide.
- El evento queda en pausa hasta la aprobación humana (Step Functions con task token).
- El Estratega solo ofrece productos a clientes con consentimiento de marketing. Al resto solo le corresponde la acción preventiva (alerta, educación, revisión de condiciones).
- Los agentes trabajan con IDs seudonimizados; nunca ven nombre, DNI ni teléfono.

---

## 5. Arquitectura de solución

Arquitectura híbrida: AWS (región sa-east-1, São Paulo) procesa solo datos seudonimizados y climáticos; los datos personales se quedan en la nube privada de Caja Trujillo (on-premise), conectada por Site-to-Site VPN o Direct Connect.

Contexto de la Caja: invirtió en nube privada y tiene 3 centros de datos (2 Tier III en Lima, 1 de respaldo en Trujillo). Su app Caja Trujillo Móvil es el canal alternativo con mayor participación.

### 5.1 Capas y componentes

| Capa | Componentes | Responsabilidad |
| --- | --- | --- |
| Fuentes climáticas | SENAMHI, ENFEN, CENEPRED SIGRID (ArcGIS REST) | Avisos de hasta 96 h, comunicados El Niño, escenarios de riesgo |
| Ingesta climática | EventBridge Scheduler (cada 6 h), Lambda ingestores, S3 raw | Leer fuentes y guardar avisos y capas |
| Orquestación agéntica | EventBridge (nuevo aviso), Step Functions, 4 agentes (Lambda + Bedrock AgentCore), aprobación humana (task token) | Ejecutar el flujo y pausar para aprobación |
| Knowledge Base (RAG) | S3 políticas y catálogo, Bedrock embeddings, OpenSearch (índice vectorial) | Dar al Estratega políticas de riesgo y catálogo |
| Analítica predictiva | SageMaker Training (XGBoost, 3 escenarios), SageMaker Endpoint (score + SHAP) | Score y explicación |
| Datos | DMS (CDC cartera), Glue (ETL + catálogo), Aurora PostgreSQL + PostGIS, DynamoDB (eventos, resultados), S3 curated (histórico, features) | Cartera seudonimizada, cruce geoespacial, eventos, histórico |
| Mensajería | SNS (fan-out), SQS FIFO (asignación a asesores), End User Messaging (push/SMS con consentimiento) | Repartir el evento aprobado |
| API y acceso | Amplify Hosting (PWA offline-first), CloudFront, WAF, Cognito (SSO, roles), API Gateway (REST privado), Lambda backend | App del asesor y consola de riesgos; re-identificación on-premise |
| Seguridad | KMS, Secrets Manager, IAM (mínimo privilegio), Macie (detecta PII), GuardDuty, CloudTrail, Security Hub → SIEM Caja | Cifrado, control de acceso, auditoría |
| Observabilidad | CloudWatch, X-Ray (trazas de agentes), QuickSight (mora contactados vs control) | Métricas, trazas, KPIs |
| Caja Trujillo on-premise | Core bancario, servicio de seudonimización (ID → token), CRM con contacto y consentimientos | Fuente de cartera; único lugar donde vive la PII |

### 5.2 Zonas de datos

| Zona | Qué guarda | Dónde vive |
| --- | --- | --- |
| Pública | Avisos, escenarios, capas de amenaza | AWS (S3) |
| Confidencial | Cartera seudonimizada, scores, eventos | AWS (Aurora PostGIS, DynamoDB), cifrada con KMS |
| Restringida | Nombre, DNI, teléfono, consentimientos | Core y CRM de la Caja, on-premise; nunca se copia |

### 5.3 Flujo E2E (8 pasos, numerados igual en el diagrama)

1. **Ingesta:** cada 6 h se leen avisos SENAMHI, comunicados ENFEN y escenarios SIGRID → S3.
2. **Cartera:** llega seudonimizada desde el core vía VPN + DMS; ningún dato personal sale de la Caja.
3. **Disparo:** un aviso nuevo activa EventBridge y arranca el flujo en Step Functions.
4. **Agentes:** Monitor delimita la zona → Exposición cruza cartera y calcula score → Estratega asigna productos según política → Orquestador crea el evento en DynamoDB.
5. **Aprobación:** SNS avisa al comité de riesgos, que aprueba o ajusta desde su consola (callback con task token). Si ajusta, vuelve al Estratega.
6. **Reparto:** SNS reparte el evento aprobado: SQS asigna la cartera a cada asesor; End User Messaging alerta a clientes con consentimiento.
7. **Acción comercial:** el asesor ve su cartera priorizada en la PWA; nombre y teléfono se traen del CRM on-premise solo para su cartera.
8. **Aprendizaje:** el resultado de cada contacto vuelve a DynamoDB → S3 curated → reentrena el modelo y alimenta los KPIs.

### 5.4 Flujo por actor (carriles BPM)

| Carril | Pasos |
| --- | --- |
| Datos | Aviso climático (SENAMHI, SIGRID) · Cartera Caja seudonimizada |
| Agentes IA | Monitor → Exposición → Estratega → Orquestador |
| Comité de riesgos | Aprueba evento (o ajusta → vuelve al Estratega) |
| Asesor | Cartera en app (lista y guion) → Contacta (visita o llamada) → Registra resultado (→ reentrena el modelo) |
| Cliente | Recibe oferta (acepta o no) · Recibe alerta (solo con consentimiento) |

---

## 6. Procesos de negocio

| # | Proceso | Responsable | Disparador | Resultado |
| --- | --- | --- | --- | --- |
| PN1 | Vigilancia climática | Agente Monitor (automático) | Aviso nuevo SENAMHI/ENFEN o escenario CENEPRED | Alerta clasificada por tipo, nivel y zona |
| PN2 | Evaluación de exposición de cartera | Agente Exposición | Alerta en zona con clientes | Clientes expuestos con score y rango |
| PN3 | Definición de estrategia preventiva | Agente Estratega | Cartera expuesta | Segmentos prevenir/proteger/reactivar con productos permitidos |
| PN4 | Aprobación del evento de campaña | Comité de riesgos o jefe de agencia | Evento del Orquestador | Evento aprobado, ajustado o rechazado |
| PN5 | Gestión comercial preventiva | Asesor de negocios | Cartera asignada en su app | Cliente contactado, oferta presentada, resultado registrado |
| PN6 | Comunicación preventiva al cliente | Sistema, solo con consentimiento | Evento aprobado | Alerta o mensaje educativo enviado |
| PN7 | Seguimiento y mejora | Riesgos y analítica | Resultados registrados | KPIs (contactados vs control) y modelo reentrenado |

---

## 7. Procesos funcionales y alcance de la hackathon

| # | Función del sistema | Soporta | Componente de producción | En la hackathon |
| --- | --- | --- | --- | --- |
| PF1 | Ingesta y normalización de avisos | PN1 | Lambda + S3 | **Real:** capa SIGRID o aviso real SENAMHI |
| PF2 | Carga de cartera seudonimizada | PN2 | DMS + VPN | Simulado: CSV sintético seudonimizado |
| PF3 | Cruce geoespacial amenaza × negocio | PN2 | Aurora + PostGIS | **Real** |
| PF4 | Score con escenarios y explicación | PN2 | SageMaker | **Real**, local: XGBoost + SHAP |
| PF5 | Consulta de políticas y asignación de productos | PN3 | Bedrock + Knowledge Base | **Real:** LLM lee PDF de políticas |
| PF6 | Creación del evento y guion | PN3 | Orquestador + DynamoDB | **Real** |
| PF7 | Aprobación humana | PN4 | Step Functions + SNS | **Real**, simplificado: pausa hasta aprobar en pantalla |
| PF8 | Asignación de cartera a asesores | PN5 | SQS FIFO | Simplificado: campo `asesor_id` |
| PF9 | App del asesor: lista, mapa, ficha "por qué", registro | PN5 | Amplify (PWA) | **Real** |
| PF10 | Notificación al cliente con filtro de consentimiento | PN6 | End User Messaging | Simulado: panel de enviados y excluidos |
| PF11 | KPIs y reentrenamiento | PN7 | QuickSight + SageMaker | Vista mínima de KPIs; reentrenamiento explicado |
| PF12 | Seguridad: autenticación, roles, auditoría | Todos | Cognito, IAM, CloudTrail | Login con 2 roles (riesgos, asesor) + tabla de log |

**Stack de la demo:** todo en Docker Compose. PostGIS (geoespacial), backend FastAPI, agentes en LangGraph llamando a Bedrock o a la API de Claude, front React como PWA con mapa Leaflet. No se despliega en AWS durante la hackathon; el diagrama AWS es la versión de producción.

---

## 8. Modelo de datos, score y catálogo

### 8.1 Score de vulnerabilidad

```
Score(i, e) = P(amenaza_e) × S_rubro × E_i × (1 − A_i)
```

- `e`: escenario (optimista, base, pesimista)
- `S_rubro`: sensibilidad climática del rubro (CIIU): agro, pesca, comercio en mercado, transporte son los más sensibles
- `E_i`: exposición crediticia (saldo y cuotas dentro de la ventana del evento)
- `A_i`: capacidad de adaptación (ahorros, ingresos diversificados, historial de pago)

XGBoost aprende los pesos con datos sintéticos calibrados con el Niño Costero 2017 y el ciclón Yaku 2023. SHAP explica cada caso al asesor en lenguaje simple. Salida con rango, no binaria.

### 8.2 Dataset sintético (≈2,000 clientes en La Libertad y Piura)

| Campo | Tipo | Ejemplo | Uso |
| --- | --- | --- | --- |
| `cliente_token` | texto | CT-00871 | ID seudonimizado de los agentes |
| `lat`, `lon` | número | -8.11, -79.03 | Ubicación del negocio |
| `ciiu` / `rubro` | texto | 0111 / agricultura | Sensibilidad climática |
| `saldo_soles` | número | 12500 | Exposición crediticia |
| `cuotas_ventana` | número | 2 | Cuotas que vencen durante el evento |
| `dias_atraso_max_12m` | número | 8 | Historial de pago |
| `ahorro_soles` | número | 1800 | Capacidad de adaptación |
| `consentimiento_marketing` | bool | true | Filtro para ofrecer productos |
| `asesor_id` | texto | AS-014 | Asignación de cartera |
| `nombre`, `telefono` | texto | ficticios | Solo visibles en la app del asesor |

### 8.3 Catálogo por segmento (hipótesis a validar con el catálogo real)

| Segmento | Momento | Productos y acciones |
| --- | --- | --- |
| Prevenir | Antes del evento | Microseguro multirriesgo, crédito para reforzar el local o adelantar inventario, ahorro de emergencia |
| Proteger | Durante | Revisión de condiciones o periodo de gracia (solo si política y SBS lo habilitan); alertas y guía práctica |
| Reactivar | Después | Crédito de reactivación o adaptación, financiable con la línea climática de la AFD (US$15 M, 7 años, 3 de gracia) |

---

## 9. Seguridad y cumplimiento normativo

El diseño puede cumplir si se mantienen los controles. Lo principal: la PII nunca sale de la Caja y no se ofrece nada sin consentimiento de marketing. Es un análisis técnico; la validación final corresponde a Cumplimiento y al Oficial de Datos de la Caja.

| Norma | Qué exige | Control en Radar Climático |
| --- | --- | --- |
| Ley 29733 + D.S. 016-2024-JUS (vigente desde 31/03/2025) | Consentimiento por finalidad (incl. llamadas publicitarias), informar decisiones automatizadas y perfiles, notificar incidentes a la ANPDP en 48 h, oposición en 10 días, Oficial de Datos Personales | Agentes con IDs seudonimizados; PII on-premise; filtro de consentimiento; botón "no contactar"; logs al SIEM |
| Ley 31814 + D.S. 115-2025-PCM (IA) | Evaluación crediticia = riesgo alto; supervisión humana capaz de detener o corregir; transparencia. Primer plazo de adecuación para finanzas: 10/09/2026 | Aprobación humana obligatoria por evento; SHAP por cliente; tratar el sistema como riesgo alto |
| Res. SBS 053-2023 (riesgo de modelo) | Inventario de modelos; directorio y comités responsables | Score en inventario con ficha técnica, validación independiente, backtesting 2017/2023 |
| Res. SBS 504-2021 (seguridad de la información y ciberseguridad) | Requisitos para terceros incluida la nube; autorización SBS si no se cumplen; estrategia de salida | Solo data seudonimizada y climática en AWS; cifrado KMS; contenedores portables |
| Normativa SBS de reprogramaciones | Solo cuando la SBS lo habilita (lo hizo en 2017 y 2023) | El agente sugiere revisar condiciones; nunca promete reprogramación |

---

## 10. Costos y retorno de inversión

### 10.1 Inversión inicial (8 meses: 3 de piloto en 2 agencias de La Libertad + 5 de escalamiento)

Costo empresa mensual por rol (S/, ≈1.45 × sueldo bruto): tech lead/arquitecto 17,000 · data scientist ×2 26,000 · ing. de datos/geo 12,000 · dev IA/agentes 12,000 · dev frontend PWA 9,500 · DevSecOps/QA 11,500 · PO Caja 50% 8,500 · especialista riesgos/cumplimiento 30% 4,000. Piloto ≈ S/ 89.3 mil/mes (front y DevSecOps al 50%), escalamiento ≈ S/ 100.5 mil/mes.

| Concepto | S/ |
| --- | --- |
| Equipo (3 meses piloto + 5 escalamiento) | 772,500 |
| Infraestructura on-premise adicional (nodos K8s, storage) | 120,000 |
| Validación independiente del modelo (SBS 053-2023) | 45,000 |
| Capacitación de asesores y gestión del cambio | 40,000 |
| Pentest | 35,000 |
| API LLM + infraestructura durante construcción | 32,000 |
| Evaluación de impacto de privacidad + revisión legal | 30,000 |
| Contingencia 15% | 161,175 |
| **Total** | **≈ 1,236,000** |

### 10.2 Operación anual ≈ S/ 484 mil

Equipo (1 DS + 1 MLOps + PO 30%) 330,000 · infraestructura y soporte 72,000 · revalidación del modelo + pentest anual 40,000 · API LLM 30,000 · SMS/push 12,000.

Costo total a 5 años: **S/ 3.33 M**.

### 10.3 Beneficio anual por escenario

Fórmula: pérdida evitada = cartera × % expuesta × alza de mora × % evitable × severidad (40%). Más margen de microseguros (S/ 60/año por póliza) y créditos de reactivación (ticket S/ 8,000, margen 12%) sobre el 20% de clientes de mayor riesgo (ticket promedio de cartera S/ 12,000).

| | Conservador | Base | Alto (Niño moderado) |
| --- | --- | --- | --- |
| Cartera expuesta | S/ 450 M (15%) | S/ 750 M (25%) | S/ 1,050 M (35%) |
| Alza de mora / % evitable | +2 pp / 10% | +3 pp / 20% | +4 pp / 30% |
| Conversión seguro / crédito | 5% / 2% | 10% / 5% | 15% / 8% |
| Clientes contactados | 7,500 | 12,500 | 17,500 |
| Pérdida evitada/año | S/ 0.36 M | S/ 1.80 M | S/ 5.04 M |
| Seguros + créditos/año | S/ 0.16 M | S/ 0.67 M | S/ 1.50 M |
| **Beneficio/año** | **S/ 0.53 M** | **S/ 2.48 M** | **S/ 6.54 M** |

### 10.4 Retorno a 5 años (VAN al 12%; año 1 = construcción con 10% del beneficio)

| Escenario | Beneficio total | VAN | ROI | Recuperación |
| --- | --- | --- | --- | --- |
| Pesimista: solo años normales | S/ 2.17 M | −S/ 1.20 M | −35% | No se recupera |
| Base: temporada de lluvias cada año | S/ 10.17 M | S/ 4.91 M | +205% | Mes 19 |
| Con un Niño moderado en el año 5 | S/ 14.23 M | S/ 7.49 M | +327% | Mes 19 |

**Punto de equilibrio:** ≈ S/ 0.94 M de beneficio al año ≈ evitar el deterioro de S/ 2.4 M de cartera ≈ 0.08% de la cartera.

**Advertencias honestas:**
- El supuesto más sensible es el % evitable (10–30%): el piloto lo mide con grupo de control.
- No hay ahorro de personal: el valor está en llegar a tiempo.
- Si la Caja tiene capacidad libre en su nube privada, bajan los S/ 120 mil de infraestructura.
- Venderlo como "seguro barato para la cartera": un solo evento moderado paga varios años de operación.

**Datos de referencia usados:** cartera de Caja Trujillo > S/ 3,000 M; mora de Caja Trujillo 9.45% vs 6.27% del promedio de cajas municipales (2024); en 2017 las cajas reprogramaron S/ 698.8 M (3.93% de su cartera directa) y su mora superó 8% en agro, pesca, minería y construcción; perfiles DS/DE en Perú: promedio US$ 3,225/mes (mid), hasta US$ 5,000 (senior).

---

## 11. Plan de implementación en 2 días

Hito del día 1: **el motor agéntico corre de punta a punta en consola.** Si no, el día 2 empieza arreglándolo antes de tocar la interfaz. Cierre del día 2: código congelado y demo ensayada (mínimo 3 veces).

| Integrante | Día 1 · mañana | Día 1 · tarde | Día 2 · mañana | Día 2 · tarde |
| --- | --- | --- | --- | --- |
| Richard Pillaca (coordinador, tech) | Repo y Docker, esqueleto de agentes | Agentes 1 a 4 en LangGraph + LLM | API de aprobación y API del asesor | Integración final y ensayo de demo |
| Piero Huayta (tech) | Datos sintéticos, carga en PostGIS | Ingesta SIGRID, score XGBoost + SHAP | PWA del asesor: lista, mapa, ficha | Consola de riesgos, KPIs y alertas |
| Monica Chilon (negocio) | Políticas y catálogo (PDF) | Reglas de negocio por segmento | Guion del asesor y textos de la app | QA funcional de punta a punta |
| Hans Belizario (negocio) | Propuesta de valor y storyline | Costos y ROI con supuestos | Deck: arquitectura, ROI y normativa | Pitch y ensayo (demo de 3 min) |

El reparto es una propuesta; ajustar según disponibilidad.

---

## 12. Guion de demo (3 minutos) y KPIs

1. **0:00–0:30 · El aviso llega:** se ingesta un aviso naranja de lluvias del SENAMHI para la costa de La Libertad; aparece el polígono en el mapa.
2. **0:30–1:15 · Los agentes trabajan:** se ve el paso por Monitor, Exposición, Estratega y Orquestador, y el evento con su cartera.
3. **1:15–1:45 · Riesgos aprueba:** el comité revisa el evento y el porqué de cada segmento, y aprueba.
4. **1:45–2:30 · El asesor actúa:** abre su app, ve su cartera priorizada en lista y mapa, abre un cliente con explicación y guion, registra el contacto.
5. **2:30–3:00 · Se cierra el ciclo:** el panel muestra el KPI actualizado y los clientes excluidos por falta de consentimiento.

| KPI | Qué mide |
| --- | --- |
| Mora a 90 días: contactados vs grupo de control | Impacto real de la acción preventiva |
| % de cartera expuesta contactada antes del evento | Oportunidad de la reacción |
| Tiempo desde el aviso hasta la cartera en manos del asesor | Velocidad del ciclo agéntico |
| Tasa de aceptación de productos por segmento | Pertinencia de lo que ofrece el Estratega |
| % de eventos aprobados sin ajustes | Calidad de las propuestas de los agentes |

---

## 13. Riesgos y supuestos

| Riesgo | Impacto | Mitigación |
| --- | --- | --- |
| API de SIGRID o SENAMHI no responde en la demo | No se ve la integración real | Copia local de la capa y del aviso; llamada real grabada |
| Desplegar en AWS consume el día 1 | No llega el motor agéntico | Todo en Docker Compose; AWS solo en el diagrama |
| El LLM asigna un producto no permitido | Pérdida de credibilidad | Validación con reglas después del LLM; aprobación humana |
| % evitable real < 10% | El ROI no se sostiene | Piloto con grupo de control antes de escalar |
| Datos sintéticos poco realistas | Jurado duda del score | Calibrar rubros y zonas con SIGRID y datos de 2017 |
| Cliente sin consentimiento recibe oferta | Incumplimiento Ley 29733 | Filtro de consentimiento antes del Estratega, visible en la demo |

**Preguntas abiertas para Caja Trujillo durante la hackathon:**
- ¿Tienen capacidad libre en su nube privada?
- ¿La ubicación del negocio está georreferenciada en el core o solo la dirección?
- ¿Qué microseguros y créditos de reactivación tienen hoy en su catálogo?
- ¿Cómo registran hoy el consentimiento de marketing?

---

## 14. Artefactos generados

| Artefacto | Descripción |
| --- | --- |
| Documento Claude Docs | https://claude.ai/artifact/Jjq7ZqaVPCFDCF4k7ojpTy — versión editable con diagramas (flujo por actor, plan de 2 días) e imagen de arquitectura |
| `arquitectura_radar_climatico.png` | Diagrama AWS con íconos oficiales, 8 pasos numerados y leyenda (5200 × 3020 px) |
| `arquitectura_radar_climatico.html` | Fuente editable del diagrama (HTML + SVG) |
| `build.py` | Script que genera el HTML del diagrama (posiciones, componentes, flechas); se renderiza a PNG con Chrome headless (Playwright) |

---

## 15. Fuentes

- SBS — Res. 504-2021, Reglamento de gestión de seguridad de la información y ciberseguridad: https://www.sbs.gob.pe/boletin/detalleboletin/idbulletin/1147
- EY — Nuevo reglamento de la Ley 29733 (D.S. 016-2024-JUS): https://www.ey.com/es_pe/insights/law/proteccion-datos-personales-peru-nuevo-reglamento
- CMS — Nuevo reglamento de protección de datos personales: https://cms.law/en/per/publication/nuevo-reglamento-de-proteccion-de-datos-personales
- El Peruano — Vigencia del nuevo reglamento (consentimiento para llamadas publicitarias): https://www.elperuano.pe/noticia/266995-minjusdh-el-lunes-31-regira-nuevo-reglamento-de-ley
- CENEPRED — Escenarios de riesgo y SIGRID: https://www.gob.pe/institucion/cenepred/noticias/1443077-cenepred-expone-ante-el-congreso-las-acciones-frente-al-fenomeno-el-nino-2027
- gob.pe — Avisos meteorológicos del SENAMHI: https://www.gob.pe/9323-consultar-los-avisos-meteorologicos-mas-recientes-en-peru
- AFD — Acuerdo de financiamiento climático con Caja Trujillo: https://www.afd.fr/fr/commmuniques-de-presse/afd-y-caja-trujillo-firman-acuerdo-para-impulsar-el-financiamiento-climatico
- DCD — Nube privada y centros de datos de Caja Trujillo: https://www.datacenterdynamics.com/es/noticias/caja-trujillo-inicia-su-transformaci%C3%B3n-digital/
- Revista Economía — Canales digitales de Caja Trujillo: https://www.revistaeconomia.com/?p=122822
- AWS — Cumplimiento SBS 504-2021 en la nube: https://aws.amazon.com/financial-services/security-compliance/compliance-center/pe
- Otras cifras (mora 9.45% vs 6.27%, reprogramaciones 2017, Ley 31814 y D.S. 115-2025-PCM, Res. SBS 053-2023, sueldos de mercado) vienen de búsquedas hechas durante la sesión; verificar antes de citarlas en el pitch.
