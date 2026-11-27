# Radar Climático — secuencia y arquitectura simple

Cómo viaja un aviso climático hasta la lista del asesor, y lo mínimo que hay que levantar para que funcione. Incluye los tres añadidos: Monitor que decide, ciclo de verificación y optimización de visitas.

Los diagramas están en Mermaid: se ven en GitHub y en VS Code (con la extensión Markdown Preview Mermaid Support).

## 1. Diagrama de secuencia

```mermaid
sequenceDiagram
    autonumber
    participant F as Fuentes públicas
    participant M as Monitor
    participant E as Exposición
    participant S as Estratega
    participant O as Orquestador
    participant A as Aprobador
    participant V as Asesor
    Note over M: se activa cada 6 horas
    M->>F: pide avisos nuevos (SENAMHI)
    F-->>M: aviso en texto
    M->>M: el LLM extrae tipo, nivel, zona y ventana
    M->>E: ¿cuántos clientes y saldo hay en la zona?
    E-->>M: clientes y saldo en zona de peligro
    alt exposición bajo el umbral
        M->>M: registra el aviso y termina
    else exposición relevante
        M->>E: abre el evento
        E->>E: cruza aviso, peligro SIGRID y cartera (PostGIS)
        E->>E: score XGBoost en 3 escenarios con explicación
        E->>S: clientes expuestos con score
        S->>S: reglas asignan segmento y producto, filtra consentimiento
        S->>S: el LLM redacta justificación y guion
        S->>O: propuesta de campaña
        loop hasta cumplir las reglas
            O->>O: verifica política y consentimiento
            O-->>S: devuelve si hay una violación
        end
        O->>O: optimiza visitas según capacidad (OR-Tools)
        O->>A: evento pendiente, plazo de 2 horas
        alt pide un ajuste
            A-->>S: ajuste en lenguaje natural
            S->>O: propuesta recalculada
            O->>A: evento actualizado
        end
        A->>O: aprueba
        O->>V: lista priorizada con el porqué y el guion
        V->>V: contacta al cliente
        V-->>E: registra el resultado para reentrenar
    end
```

Nada llega al asesor antes del paso «aprueba».

Las tres decisiones que lo distinguen de una automatización fija:

- **El Monitor decide si abre un evento.** Un aviso que toca pocos clientes o poco saldo se registra y no molesta a nadie.
- **El Orquestador verifica antes de pedir aprobación.** Si la propuesta rompe una regla o ignora el consentimiento, vuelve al Estratega.
- **Una persona aprueba cada evento.** El comité aprueba las reglas una sola vez; el aprobador designado puede ajustar el evento escribiendo en lenguaje natural.

## 2. Arquitectura simple

```mermaid
flowchart LR
    subgraph FUENTES[Fuentes públicas]
        SEN[SENAMHI<br/>avisos: cuándo llueve]
        SIG[SIGRID · CENEPRED<br/>zonas de peligro: dónde]
    end

    CAR[Cartera de la Caja<br/>CSV sin datos personales]

    subgraph SERVIDOR[Un servidor · Docker Compose]
        subgraph BACK[Backend · FastAPI + LangGraph]
            direction LR
            MON[Monitor<br/>LLM] --> EXP[Exposición<br/>XGBoost, SHAP] --> EST[Estratega<br/>reglas + LLM] --> ORQ[Orquestador<br/>OR-Tools]
        end
        DB[(PostgreSQL + PostGIS<br/>cartera, capas de peligro,<br/>eventos, resultados,<br/>estado del flujo)]
        WEB[Web · React + Leaflet<br/>consola de aprobación<br/>lista y mapa del asesor]
    end

    LLM[API del LLM · Claude<br/>único servicio de pago]
    APR([Aprobador])
    ASE([Asesores])

    SEN -- aviso --> BACK
    SIG -- capas --> BACK
    CAR -- carga --> DB
    BACK <-- SQL --> DB
    WEB -- REST --> BACK
    BACK <-- sin datos personales --> LLM
    APR -- aprueba --> WEB
    ASE -- registra --> WEB
```

Tres contenedores en una sola máquina. Lo único que sale del servidor son las llamadas al LLM, sin nombres, documentos, teléfonos ni coordenadas.

El backend corre una tarea programada cada 6 horas; el flujo se pausa hasta la aprobación y guarda su estado en la base. El mismo servidor puede ser una laptop en la demo o una máquina dentro de la nube privada de la Caja en un piloto, sin cambiar el código.

## 3. Cómo escala cada pieza

| Pieza simple                       | Cuándo se queda corta                      | Reemplazo                                      |
| ---------------------------------- | ------------------------------------------- | ---------------------------------------------- |
| PostgreSQL + PostGIS en contenedor | Muchas agencias consultando a la vez        | PostgreSQL administrado (Aurora)               |
| Tarea programada en el backend     | Muchas fuentes o avisos simultáneos        | Programador y colas (EventBridge, SQS)         |
| LangGraph en un proceso            | Flujos largos con auditoría formal         | Step Functions                                 |
| XGBoost dentro del backend         | Reentrenamiento periódico con datos reales | SageMaker                                      |
| Web React                          | Asesores sin señal en campo                | Aplicación con modo sin conexión             |
| Un servidor                        | Se exige alta disponibilidad                | Kubernetes en la nube privada de la Caja o AWS |
