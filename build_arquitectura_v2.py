"""Genera arquitectura_radar_climatico_v2.html.

Reutiliza los iconos oficiales incrustados en el diagrama original
(arquitectura_radar_climatico (1).html) y su mismo estilo visual.
Uso: python build_arquitectura_v2.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "arquitectura_radar_climatico (1).html"
OUT = HERE / "arquitectura_radar_climatico_v2.html"

W, H = 2600, 1700

# ---------------------------------------------------------------- iconos
src_html = SRC.read_text(encoding="utf-8")
ICONS = {}
for m in re.finditer(r'<div class="n" style="[^"]*">\s*<img src="([^"]+)">\s*([^<]+)', src_html):
    ICONS[m.group(2).strip()] = m.group(1)
for m in re.finditer(r'<div class="card" style="[^"]*">\s*<img src="([^"]+)">\s*<b>([^<]+)</b>', src_html):
    ICONS["card:" + m.group(2).strip()] = m.group(1)


def icon(key):
    if key not in ICONS:
        raise SystemExit(f"Icono no encontrado: {key!r}. Disponibles: {sorted(ICONS)}")
    return ICONS[key]


# ---------------------------------------------------------------- grupos
# (left, top, width, height, color borde, fondo, titulo)
GROUPS = [
    (20, 80, 280, 500, "#7D8998", "#F7F8F9", "Fuentes climáticas públicas"),
    (20, 620, 280, 820, "#D86613", "#FFF6EC", "Caja Trujillo · on-premise"),
    (2300, 620, 280, 820, "#7D8998", "#F7F8F9", "Usuarios"),
    (330, 90, 250, 490, "#147EBA", "#EEF6FC", "Ingesta climática"),
    (620, 90, 1090, 490, "#C7131F", "#FDF0F0", "Orquestación agéntica · AWS Step Functions"),
    (1740, 90, 520, 210, "#8C4FFF", "#F5F0FF", "IA generativa"),
    (1740, 330, 520, 250, "#01A88D", "#EDFAF7", "Analítica predictiva y control de sesgos"),
    (330, 630, 1130, 310, "#3F8624", "#F1F8EE", "Datos e impacto en cartera"),
    (1490, 630, 770, 310, "#E7157B", "#FDF0F6", "Notificación"),
    (330, 980, 1930, 220, "#8C4FFF", "#F7F3FF", "API, backend y acceso"),
    (330, 1240, 1170, 200, "#DD344C", "#FDF1F2", "Seguridad y cumplimiento"),
    (1530, 1240, 730, 200, "#7D8998", "#F7F8F9", "Observabilidad e impacto"),
]

# ---------------------------------------------------------------- tarjetas de agentes
# (left, icono, titulo, texto, color borde)
CARDS = [
    (640, "card:3. Agente Estratega", "1. Agente Monitor",
     "Lee el aviso con el LLM y decide si abre un evento", "#C7131F"),
    (846, "card:1. Agente Monitor", "2. Agente Exposición",
     "Cruce geoespacial y probabilidad de atraso mayor a 30 días", "#C7131F"),
    (1052, "card:3. Agente Estratega", "3. Agente Estratega",
     "Reglas asignan producto; el LLM redacta y reinterpreta ajustes", "#C7131F"),
    (1258, "card:1. Agente Monitor", "4. Agente Orquestador",
     "Verifica reglas y sesgos; optimiza contactos por canal", "#C7131F"),
    (1464, "card:Aprobación humana", "Aprobación humana",
     "Pausa hasta que el jefe de agencia aprueba o ajusta", "#232F3E"),
]
CARD_TOP, CARD_W, CARD_H = 295, 190, 175

# ---------------------------------------------------------------- nodos
# (cx, cy, icono, etiqueta html)  -> el icono queda centrado en (cx, cy)
NODES = [
    # fuentes
    (160, 175, "SENAMHI", "SENAMHI<br>avisos: lluvia, helada, friaje, calor"),
    (160, 315, "ENFEN", "ENFEN<br>escenarios El Niño"),
    (160, 455, "CENEPRED SIGRID", "CENEPRED SIGRID<br>zonas de peligro (ArcGIS REST)"),
    # caja on-premise
    (95, 720, "Core bancario", "Core bancario<br>cartera y pagos"),
    (95, 900, "Seudonimización", "Seudonimización<br>ID → token"),
    (230, 1090, "Site-to-Site VPN /", "Site-to-Site VPN"),
    (230, 1300, "CRM: contacto", "CRM: contacto<br>+ consentimientos"),
    # usuarios
    (2440, 700, "Comité de riesgos", "Jefe de agencia<br>aprueba cada evento"),
    (2440, 900, "Asesores de negocio", "Asesores de negocio"),
    (2440, 1110, "Clientes", "Clientes<br>presencial, teléfono, digital"),
    (2440, 1330, "Comité de riesgos", "Área de Riesgos<br>reglas y vista de cartera"),
    # ingesta
    (455, 175, "EventBridge Scheduler", "EventBridge Scheduler<br>(clima cada 6 h)"),
    (455, 315, "Lambda", "Lambda<br>(ingestores)"),
    (455, 455, "S3 raw", "S3 raw<br>(avisos, capas)"),
    # orquestacion
    (720, 165, "EventBridge", "EventBridge<br>(aviso nuevo)"),
    (900, 165, "Step Functions", "Step Functions<br>(flujo agéntico)"),
    # IA generativa
    (1860, 165, "S3 políticas", "S3 políticas<br>y catálogo"),
    (2130, 165, "Bedrock", "Bedrock (Claude)<br>lee, redacta y ajusta"),
    # analitica
    (1830, 440, "SageMaker Training", "SageMaker Training<br>(XGBoost · atraso > 30 días)"),
    (2000, 440, "SageMaker Endpoint", "SageMaker Serverless<br>(score en 3 escenarios)"),
    (2170, 440, "SageMaker Endpoint", "SageMaker Clarify<br>(sesgos por zona y sector)"),
    # datos
    (410, 790, "S3 raw", "S3 carga mensual<br>(cartera seudonimizada)"),
    (600, 790, "Lambda", "Lambda<br>(valida y carga)"),
    (941, 790, "Aurora PostgreSQL", "Aurora PostgreSQL<br>PostGIS + pgvector"),
    (1150, 790, "Lambda backend", "Lambda impacto en cartera<br>(pérdida esperada)"),
    (1353, 790, "S3 curated", "S3 histórico<br>(resultados, features)"),
    # notificacion
    (1600, 790, "SNS", "SNS<br>(avisa y reparte)"),
    (2100, 790, "End User Messaging", "End User Messaging<br>(SMS / push)"),
    # API
    (941, 1080, "Lambda backend", "Lambda backend<br>(lista, aprobación, resultados)"),
    (1478, 1080, "API Gateway", "API Gateway<br>(REST privado)"),
    (1715, 1080, "Cognito", "Cognito<br>(roles por usuario)"),
    (1950, 1080, "AWS WAF", "AWS WAF"),
    (2190, 1080, "Amplify Hosting", "Amplify Hosting<br>(consola web)"),
    # seguridad
    (430, 1330, "KMS", "KMS<br>(cifrado)"),
    (640, 1330, "Secrets Manager", "Secrets Manager"),
    (850, 1330, "IAM", "IAM<br>(mínimo privilegio)"),
    (1060, 1330, "GuardDuty", "GuardDuty"),
    (1300, 1330, "CloudTrail", "CloudTrail<br>→ SIEM de la Caja"),
    # observabilidad
    (1700, 1330, "CloudWatch", "CloudWatch<br>(métricas, fecha del dato)"),
    (2060, 1330, "QuickSight", "QuickSight<br>(impacto por zona, sector y segmento)"),
]

# ---------------------------------------------------------------- flechas
STYLE = {
    "f": ("#232F3E", "", "mf"),          # flujo de control
    "d": ("#3F8624", "", "md"),          # datos
    "q": ("#3F8624", "7 5", "md"),       # consulta / re-identificacion
    "h": ("#C7131F", "", "mh"),          # supervision humana
    "e": ("#8A8F98", "7 5", "me"),       # retroalimentacion
}
# (path, estilo, flecha: "", "end", "both")
ARROWS = [
    # fuentes -> ingesta
    ("M192 175 H360 M192 315 H360 M192 455 H360 M360 175 V455", "f", ""),
    ("M360 315 H418", "f", "end"),
    ("M455 207 V276", "f", "end"),
    ("M455 347 V416", "d", "end"),
    # S3 raw -> Aurora (capas de peligro)
    ("M455 528 V605 H915 V753", "d", "end"),
    # S3 raw -> EventBridge -> Step Functions -> Monitor
    ("M487 455 H600 V165 H683", "f", "end"),
    ("M752 165 H863", "f", "end"),
    ("M900 222 V262 H735 V290", "f", "end"),
    # cadena de agentes
    ("M830 382 H841", "f", "end"),
    ("M1036 382 H1047", "f", "end"),
    ("M1242 382 H1253", "f", "end"),
    ("M1448 382 H1459", "h", "end"),
    # Monitor y Estratega consultan al LLM
    ("M790 295 V278 H1147", "q", ""),
    ("M1147 295 V266 H2130 V246", "q", "end"),
    ("M1897 165 H2093", "d", "end"),
    # Exposicion: cruce en Aurora y score
    ("M941 470 V753", "q", "end"),
    ("M941 612 H2000 V516", "q", "end"),
    ("M1867 440 H1963", "e", "end"),
    ("M2037 440 H2133", "e", "end"),
    # Orquestador crea el evento en Aurora
    ("M1300 470 V690 H967 V753", "d", "end"),
    # impacto en cartera e historico
    ("M978 790 H1113", "d", "end"),
    ("M1187 790 H1316", "d", "end"),
    ("M1353 753 V598 H1830 V516", "e", "end"),
    ("M1150 870 V1220 H2060 V1294", "d", "end"),
    ("M2097 1330 H2403", "d", "end"),
    # aprobacion humana
    ("M1574 470 V753", "h", "end"),
    ("M1626 754 V685 H2403", "h", "end"),
    ("M1478 1044 V475", "h", "end"),
    # reparto
    ("M1637 790 H2063", "f", "end"),
    ("M2137 790 H2330 V1110 H2403", "f", "end"),
    # usuarios -> web -> API
    ("M2403 715 H2360 V1080 H2227", "f", "end"),
    ("M2403 900 H2360", "f", ""),
    ("M2153 1080 H1987", "f", "end"),
    ("M1913 1080 H1752", "f", "end"),
    ("M1678 1080 H1515", "f", "end"),
    ("M1441 1080 H978", "f", "end"),
    # backend <-> Aurora (lista priorizada y resultados)
    ("M941 1044 V872", "d", "both"),
    # re-identificacion on-premise
    ("M904 1080 H262", "q", "end"),
    ("M230 1140 V1263", "q", "end"),
    # cartera mensual
    ("M95 792 V863", "d", "end"),
    ("M95 972 V1090 H195", "d", "end"),
    ("M230 1054 V790 H373", "d", "end"),
    ("M447 790 H563", "d", "end"),
    ("M637 790 H904", "d", "end"),
]

# ---------------------------------------------------------------- etiquetas y pasos
LABELS = [
    (382, 300, "HTTPS"),
    (548, 290, "aviso nuevo"),
    (700, 605, "capas de peligro"),
    (1600, 266, "consulta al LLM"),
    (1900, 612, "score"),
    (1600, 598, "reentrena cada mes"),
    (1130, 690, "crea el evento"),
    (2000, 685, "notifica: evento por aprobar"),
    (1418, 1000, "aprueba / ajusta"),
    (1760, 776, "evento aprobado"),
    (2235, 778, "solo con consentimiento"),
    (2070, 1066, "HTTPS 443"),
    (600, 1066, "re-identifica solo la cartera del asesor"),
    (300, 776, "archivo mensual sin PII"),
    (1600, 1220, "impacto en cartera"),
    (941, 915, "lista priorizada y resultados"),
]
BADGES = [
    (382, 350, 1), (230, 960, 2), (600, 225, 3), (941, 540, 4), (1046, 790, 5),
    (1250, 492, 6), (1574, 540, 7), (1870, 790, 8), (941, 965, 9),
]
STEPS = [
    "Cada 6 horas se leen avisos del SENAMHI, escenarios del ENFEN y zonas de peligro de SIGRID hacia S3.",
    "La Caja envía la cartera seudonimizada al menos una vez al mes por VPN: ningún dato personal sale de la Caja.",
    "Un aviso nuevo arranca el flujo; el Monitor lo lee con el LLM y decide si amerita abrir un evento.",
    "Exposición cruza aviso, zona de peligro y cartera en PostGIS y calcula la probabilidad de atraso mayor a 30 días en 3 escenarios.",
    "Se estima la pérdida esperada por zona, sector y segmento (referencia: 10% del saldo en el Niño 2017) y Clarify revisa sesgos.",
    "El Estratega asigna productos según las reglas y redacta el guion; el Orquestador verifica y optimiza los contactos por canal.",
    "El jefe de agencia recibe el evento, lo aprueba o lo ajusta. La alerta es un insumo, no una decisión crediticia automática.",
    "El asesor recibe su lista priorizada; los clientes con consentimiento reciben una alerta por SMS o push.",
    "El resultado de cada contacto vuelve a Aurora y al histórico, alimenta los indicadores y reentrena el modelo cada mes.",
]
CONTROLS = [
    ("Reto · alerta no es decisión:", "una persona aprueba cada evento; ningún agente decide créditos"),
    ("Reto · sesgos:", "Clarify compara la tasa de alertas entre zonas y sectores antes de aprobar"),
    ("Reto · calidad de datos:", "cartera mensual, clima cada 6 h y fecha del dato visible en cada alerta"),
    ("Ley 29733 · D.S. 016-2024-JUS:", "datos personales solo en la Caja; consentimiento por finalidad"),
    ("Ley 31814 (IA):", "supervisión humana obligatoria y explicación del score por cliente"),
    ("Res. SBS 053-2023:", "modelo en inventario con validación independiente"),
    ("Res. SBS 504-2021:", "nube como tercero: cifrado KMS, CloudTrail al SIEM, salida con contenedores"),
]
LEGEND = [("f", "Flujo de control"), ("d", "Datos"), ("q", "Consulta / re-identificación"),
          ("h", "Supervisión humana"), ("e", "Retroalimentación")]

# ---------------------------------------------------------------- render
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,'Helvetica Neue',Arial,sans-serif;background:#fff;color:#232F3E}
#c{position:relative;width:%dpx;height:%dpx}
.g{position:absolute;border:1.5px solid;border-radius:10px}
.gt{position:absolute;left:14px;top:9px;font-size:15px;font-weight:600;letter-spacing:.1px}
.n{position:absolute;width:170px;text-align:center;font-size:12px;line-height:1.3}
.n img{width:62px;height:62px;display:block;margin:0 auto 6px}
.card{position:absolute;background:#fff;border:1.5px solid;border-radius:10px;padding:12px 12px 10px;box-shadow:0 1px 0 rgba(0,0,0,.04)}
.card img{width:46px;height:46px;display:block;margin-bottom:8px}
.card b{display:block;font-size:14px;margin-bottom:4px}
.card span{font-size:12px;line-height:1.35;color:#454F5B}
.lbl{position:absolute;font-size:11.5px;color:#454F5B;background:#fff;padding:1px 5px;border-radius:4px;white-space:nowrap;transform:translate(-50%%,-50%%)}
.bd{position:absolute;width:26px;height:26px;border-radius:50%%;background:#FF9900;color:#fff;font-weight:700;font-size:14px;display:flex;align-items:center;justify-content:center;transform:translate(-50%%,-50%%);border:2px solid #fff;box-shadow:0 0 0 1px #E88B00}
svg{position:absolute;left:0;top:0}
""" % (W, H)

p = []
p.append('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
         '<title>Radar climático Caja Trujillo · arquitectura AWS v2</title>\n'
         f'<style>{CSS}</style>\n</head>\n<body>\n<div id="c">')
p.append('<div style="position:absolute;left:20px;top:14px;font-size:24px;font-weight:700">'
         'Radar climático Caja Trujillo · arquitectura v2 en AWS</div>')
p.append('<div style="position:absolute;left:20px;top:44px;font-size:13px;color:#5F6B7A">'
         'Predice el deterioro crediticio por eventos climáticos, estima el impacto en la cartera '
         'y entrega alertas con recomendación que una persona aprueba</div>')
p.append('<div class="g" style="left:315px;top:78px;width:1960px;height:1377px;'
         'border-color:#232F3E;border-width:2px;background:#fff"></div>')
p.append('<div style="position:absolute;left:330px;top:68px;font-size:14px;font-weight:700;'
         'background:#232F3E;color:#fff;padding:2px 10px;border-radius:4px">AWS Cloud</div>')
p.append('<div style="position:absolute;left:428px;top:68px;font-size:13px;color:#147EBA;'
         'border:1.5px dashed #147EBA;padding:1px 8px;border-radius:4px;background:#fff">'
         'Región sa-east-1 · solo datos seudonimizados</div>')

for l, t, w, h, bc, bg, title in GROUPS:
    p.append(f'<div class="g" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;'
             f'border-color:{bc};background:{bg}"><div class="gt" style="color:{bc}">{title}</div></div>')

for l, ic, title, text, bc in CARDS:
    p.append(f'<div class="card" style="left:{l}px;top:{CARD_TOP}px;width:{CARD_W}px;height:{CARD_H}px;'
             f'border-color:{bc}"><img src="{icon(ic)}"><b>{title}</b><span>{text}</span></div>')

p.append(f'<svg width="{W}" height="{H}"><defs>')
for key, (color, _, mid) in STYLE.items():
    if key == "q":
        continue  # comparte marcador con "d"
    p.append(f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             f'markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{color}"/></marker>')
p.append('</defs>')
for d, st, heads in ARROWS:
    color, dash, mid = STYLE[st]
    attrs = f'fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"'
    if dash:
        attrs += f' stroke-dasharray="{dash}"'
    if heads in ("end", "both"):
        attrs += f' marker-end="url(#{mid})"'
    if heads == "both":
        attrs += f' marker-start="url(#{mid})"'
    p.append(f'<path d="{d}" {attrs}/>')
p.append('</svg>')

for cx, cy, ic, label in NODES:
    p.append(f'<div class="n" style="left:{cx - 85}px;top:{cy - 31}px"><img src="{icon(ic)}">{label}</div>')
for x, y, text in LABELS:
    p.append(f'<div class="lbl" style="left:{x}px;top:{y}px">{text}</div>')
for x, y, n in BADGES:
    p.append(f'<div class="bd" style="left:{x}px;top:{y}px">{n}</div>')

# pie: flujo, controles, leyenda
FOOT = 1475
p.append(f'<div style="position:absolute;left:20px;top:{FOOT}px;width:1500px">'
         '<div style="font-size:15px;font-weight:700;margin-bottom:8px">Flujo E2E</div>'
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px 28px">')
for i, text in enumerate(STEPS, 1):
    p.append('<div style="display:flex;gap:8px;font-size:12.5px;line-height:1.35">'
             '<div style="flex:none;width:22px;height:22px;border-radius:50%;background:#FF9900;color:#fff;'
             'font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center">'
             f'{i}</div><div>{text}</div></div>')
p.append('</div></div>')

p.append(f'<div style="position:absolute;left:1560px;top:{FOOT}px;width:700px">'
         '<div style="font-size:15px;font-weight:700;margin-bottom:8px">Controles del reto y regulatorios</div>')
for head, text in CONTROLS:
    p.append('<div style="font-size:12.5px;line-height:1.35;margin-bottom:5px">'
             f'<b style="color:#C7131F">{head}</b> {text}</div>')
p.append('</div>')

p.append(f'<div style="position:absolute;left:2300px;top:{FOOT}px;width:280px;font-size:12.5px;line-height:1.9">'
         '<div style="font-size:15px;font-weight:700;margin-bottom:4px">Leyenda</div>')
for st, text in LEGEND:
    color, dash, _ = STYLE[st]
    da = f' stroke-dasharray="{dash}"' if dash else ""
    p.append('<div style="display:flex;align-items:center;gap:8px">'
             '<svg width="44" height="10" style="position:static">'
             f'<line x1="0" y1="5" x2="44" y2="5" stroke="{color}" stroke-width="2"{da}/></svg>{text}</div>')
p.append('</div>')

p.append('</div>\n</body>\n</html>')
OUT.write_text("\n".join(p), encoding="utf-8")
print(f"OK: {OUT.name} ({OUT.stat().st_size // 1024} KB, {len(NODES)} nodos, {len(ARROWS)} flechas)")
