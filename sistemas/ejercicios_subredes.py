from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER

pdf = SimpleDocTemplate(
    "ejercicios_subredes.pdf",
    pagesize=A4,
    topMargin=1.5*cm,
    bottomMargin=1.5*cm,
    leftMargin=2*cm,
    rightMargin=2*cm
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    "Title2", parent=styles["Heading1"], fontSize=18, spaceAfter=4, alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    "SubTitle", parent=styles["Heading2"], fontSize=14, spaceBefore=6, spaceAfter=4
))
styles.add(ParagraphStyle(
    "Body2", parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=4
))
styles.add(ParagraphStyle(
    "CodeStyle", parent=styles["Normal"], fontSize=9, leading=12,
    leftIndent=12, fontName="Courier", spaceAfter=2
))

elements = []

# ---------- PORTADA ----------
elements.append(Spacer(1, 4*cm))
elements.append(Paragraph("EJERCICIOS DE SUBREDES", styles["Title2"]))
elements.append(Spacer(1, 0.8*cm))
elements.append(Paragraph("Subredes Estáticas (FLSM) vs Dinámicas (VLSM)", styles["SubTitle"]))
elements.append(Spacer(1, 1*cm))
elements.append(Paragraph("Material de práctica para imprimir", styles["Normal"]))
elements.append(Spacer(1, 0.3*cm))
elements.append(Paragraph("Red base: 192.168.1.0/24", styles["Normal"]))
elements.append(PageBreak())

# ---------- TEORIA RAPIDA ----------
elements.append(Paragraph("Recordatorio rápido", styles["SubTitle"]))
elements.append(Paragraph(
    "<b>FLSM (estática):</b> Todas las subredes usan la <b>misma máscara</b>. "
    "Fácil de calcular, pero <b>desperdicia direcciones</b>.",
    styles["Body2"]
))
elements.append(Paragraph(
    "<b>VLSM (dinámica):</b> Cada subred usa la <b>máscara justa</b> para sus necesidades. "
    "Ahorra direcciones, pero requiere más planificación.",
    styles["Body2"]
))
elements.append(Spacer(1, 0.3*cm))

# Tabla de referencia
ref_data = [
    ["Máscara", "Tamaño", "Hosts útiles", "Empieza en múltiplo de"],
    ["/30", "4", "2", "0, 4, 8, 12..."],
    ["/29", "8", "6", "0, 8, 16, 24..."],
    ["/28", "16", "14", "0, 16, 32, 48..."],
    ["/27", "32", "30", "0, 32, 64, 96..."],
    ["/26", "64", "62", "0, 64, 128, 192..."],
    ["/25", "128", "126", "0, 128"],
    ["/24", "256", "254", "0"],
]
t = Table(ref_data, colWidths=[5*cm, 4*cm, 4*cm, 6*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2B579A")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#E8EDF5")]),
]))
elements.append(t)
elements.append(Spacer(1, 0.3*cm))
elements.append(Paragraph("Fórmula: <b>hosts útiles = 2<super>32-máscara</super> - 2</b>", styles["Body2"]))
elements.append(PageBreak())

# ============================================================
# EJERCICIO 1: FLSM (estática)
# ============================================================
elements.append(Paragraph("EJERCICIO 1: Subredes Estáticas (FLSM)", styles["SubTitle"]))
elements.append(Spacer(1, 0.2*cm))

elements.append(Paragraph("Enunciado:", styles["Heading3"]))
elements.append(Paragraph(
    "Se necesita dividir la red <b>192.168.1.0/24</b> en <b>4 subredes del mismo tamaño</b> "
    "usando FLSM. Cada subred debe tener la <b>misma máscara</b>.",
    styles["Body2"]
))
elements.append(Spacer(1, 0.3*cm))

elements.append(Paragraph("Paso 1: Calcular la máscara", styles["Heading3"]))
elements.append(Paragraph(
    "4 subredes → 2<super>n</super> ≥ 4 → n = 2 bits de subred. "
    "Máscara original /24 + 2 = <b>/26</b> (255.255.255.192).",
    styles["Body2"]
))
elements.append(Paragraph("Cada subred tendrá: 2<super>32-26</super> - 2 = 64 - 2 = <b>62 hosts útiles</b>.", styles["Body2"]))
elements.append(Spacer(1, 0.3*cm))

elements.append(Paragraph("Paso 2: Completar la tabla", styles["Heading3"]))
elements.append(Paragraph("Salto = 256 - 192 = <b>64</b>. Cada subred empieza cada 64 direcciones.", styles["Body2"]))
elements.append(Spacer(1, 0.2*cm))

flsm_table_data = [
    ["Subred", "Red", "Rango útil", "Broadcast", "Máscara"],
    ["1", "192.168.1.0", "?.? - ?.?", "?", "/26"],
    ["2", "192.168.1.64", "?.? - ?.?", "?", "/26"],
    ["3", "?.?.?.?", "?.? - ?.?", "?", "/26"],
    ["4", "?.?.?.?", "?.? - ?.?", "?", "/26"],
]
t = Table(flsm_table_data, colWidths=[2.5*cm, 4*cm, 5*cm, 3*cm, 2.5*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D32F2F")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FFEBEE")]),
]))
elements.append(t)
elements.append(Spacer(1, 0.2*cm))
elements.append(Paragraph("Espacio para resolver:", styles["Body2"]))
elements.append(Spacer(1, 3*cm))

# SOLUCION FLSM
elements.append(Paragraph("SOLUCIÓN (no mires hasta intentarlo):", styles["Heading3"]))
flsm_sol = [
    ["Subred", "Red", "Rango útil", "Broadcast", "Máscara"],
    ["1", "192.168.1.0", "192.168.1.1 - 192.168.1.62", "192.168.1.63", "/26"],
    ["2", "192.168.1.64", "192.168.1.65 - 192.168.1.126", "192.168.1.127", "/26"],
    ["3", "192.168.1.128", "192.168.1.129 - 192.168.1.190", "192.168.1.191", "/26"],
    ["4", "192.168.1.192", "192.168.1.193 - 192.168.1.254", "192.168.1.255", "/26"],
]
t2 = Table(flsm_sol, colWidths=[2.5*cm, 4*cm, 5.5*cm, 3*cm, 2.5*cm])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E7D32")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#E8F5E9")]),
]))
elements.append(t2)
elements.append(Paragraph("<b>Problema:</b> Si solo necesitas 2 hosts en una subred, igual recibes 62. ¡Desperdicio!", styles["Body2"]))
elements.append(PageBreak())

# ============================================================
# EJERCICIO 2: VLSM (dinámica)
# ============================================================
elements.append(Paragraph("EJERCICIO 2: Subredes Dinámicas (VLSM)", styles["SubTitle"]))
elements.append(Spacer(1, 0.2*cm))

elements.append(Paragraph("Enunciado:", styles["Heading3"]))
elements.append(Paragraph(
    "Usando la misma red <b>192.168.1.0/24</b>, aplica VLSM para las siguientes necesidades:",
    styles["Body2"]
))

reqs = [
    "LAN 1: 80 hosts",
    "LAN 2: 60 hosts",
    "LAN 3: 28 hosts",
    "LAN 4: 14 hosts",
    "Enlace A: 2 hosts",
    "Enlace B: 2 hosts",
    "Enlace C: 2 hosts",
]
for r in reqs:
    elements.append(Paragraph(f"• {r}", styles["Body2"]))
elements.append(Spacer(1, 0.3*cm))

elements.append(Paragraph("Paso 1: Ordenar de mayor a menor necesidad", styles["Heading3"]))
elements.append(Paragraph("80 → 60 → 28 → 14 → 2 → 2 → 2", styles["Body2"]))
elements.append(Spacer(1, 0.2*cm))

elements.append(Paragraph("Paso 2: Elegir la máscara justa para cada una", styles["Heading3"]))
elements.append(Paragraph(
    "80 hosts → 2<super>n</super> - 2 ≥ 80 → n=7 (128-2=126) → <b>/25</b> (tamaño 128) → desperdicia 46<br/>"
    "60 hosts → 2<super>n</super> - 2 ≥ 60 → n=6 (64-2=62) → <b>/26</b> (tamaño 64) → desperdicia 2<br/>"
    "28 hosts → 2<super>n</super> - 2 ≥ 28 → n=5 (32-2=30) → <b>/27</b> (tamaño 32) → desperdicia 2<br/>"
    "14 hosts → 2<super>n</super> - 2 ≥ 14 → n=4 (16-2=14) → <b>/28</b> (tamaño 16) → desperdicia 0<br/>"
    "2 hosts → 2<super>n</super> - 2 ≥ 2 → n=2 (4-2=2) → <b>/30</b> (tamaño 4) → desperdicia 0",
    styles["Body2"]
))
elements.append(Spacer(1, 0.2*cm))

elements.append(Paragraph("Paso 3: Completar la tabla (atención a los múltiplos)", styles["Heading3"]))
vlsm_table = [
    ["Subred", "Hosts", "Red", "Máscara", "Rango útil", "Broadcast"],
    ["LAN 1", "80", "192.168.1.0", "/25", "?.? - ?.?", "?"],
    ["LAN 2", "60", "?", "/26", "?.? - ?.?", "?"],
    ["LAN 3", "28", "?", "/27", "?.? - ?.?", "?"],
    ["LAN 4", "14", "?", "/28", "?.? - ?.?", "?"],
    ["Enlace A", "2", "?", "/30", "?.? - ?.?", "?"],
    ["Enlace B", "2", "?", "/30", "?.? - ?.?", "?"],
    ["Enlace C", "2", "?", "/30", "?.? - ?.?", "?"],
]
t3 = Table(vlsm_table, colWidths=[2.5*cm, 1.5*cm, 3.5*cm, 1.5*cm, 5*cm, 2.5*cm])
t3.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D32F2F")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FFEBEE")]),
]))
elements.append(t3)
elements.append(Spacer(1, 0.3*cm))
elements.append(Paragraph("Pista: la LAN 2 empieza en 192.168.1.128 (¿por qué no en 64?).", styles["Body2"]))
elements.append(Spacer(1, 3*cm))

# SOLUCION VLSM
elements.append(Paragraph("SOLUCIÓN (no mires hasta intentarlo):", styles["Heading3"]))
vlsm_sol = [
    ["Subred", "Hosts", "Red", "Máscara", "Rango útil", "Broadcast"],
    ["LAN 1", "80", "192.168.1.0", "/25", "192.168.1.1 - 192.168.1.126", "192.168.1.127"],
    ["LAN 2", "60", "192.168.1.128", "/26", "192.168.1.129 - 192.168.1.190", "192.168.1.191"],
    ["LAN 3", "28", "192.168.1.192", "/27", "192.168.1.193 - 192.168.1.222", "192.168.1.223"],
    ["LAN 4", "14", "192.168.1.224", "/28", "192.168.1.225 - 192.168.1.238", "192.168.1.239"],
    ["Enlace A", "2", "192.168.1.240", "/30", "192.168.1.241 - 192.168.1.242", "192.168.1.243"],
    ["Enlace B", "2", "192.168.1.244", "/30", "192.168.1.245 - 192.168.1.246", "192.168.1.247"],
    ["Enlace C", "2", "192.168.1.248", "/30", "192.168.1.249 - 192.168.1.250", "192.168.1.251"],
]
t4 = Table(vlsm_sol, colWidths=[2.5*cm, 1.5*cm, 3.5*cm, 1.5*cm, 5.5*cm, 2.5*cm])
t4.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E7D32")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#E8F5E9")]),
]))
elements.append(t4)
elements.append(Paragraph("<b>Usaste 252 de 256 direcciones.</b> Con FLSM habrías necesitado 320+ (imposible).", styles["Body2"]))
elements.append(Spacer(1, 0.3*cm))

# Explicacion de por que LAN 2 empieza en 128
elements.append(Paragraph("¿Por qué LAN 2 empieza en 192.168.1.128?", styles["Heading3"]))
elements.append(Paragraph(
    "LAN 1 usa <b>/25</b> (tamaño 128), ocupando de <b>.0 a .127</b>. "
    "El primer número <b>múltiplo de 64</b> después de 127 es <b>.128</b>. "
    "Aunque /26 tenga tamaño 64, no puede empezar en .64 porque esa dirección "
    "<b>ya está ocupada</b> por la LAN 1.",
    styles["Body2"]
))
elements.append(Spacer(1, 0.3*cm))

# Diagrama visual
elements.append(Paragraph("Diagrama visual:", styles["Heading3"]))
elements.append(Paragraph(
    "<font face='Courier' size='8'>"
    ".0  ├────────────── LAN 1 (/25) ──────────────┤ .127<br/>"
    "    &nbsp;&nbsp;&nbsp;&nbsp;.128 ├────── LAN 2 (/26) ──────┤ .191<br/>"
    "    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.192 ├── LAN 3 (/27) ──┤ .223<br/>"
    "    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.224 ├─ LAN 4 (/28) ─┤ .239<br/>"
    "    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.240 ├ EnA ┤ .243<br/>"
    "    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.244 ├ EnB ┤ .247<br/>"
    "    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.248 ├ EnC ┤ .251<br/>"
    "    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.252-255 → libres"
    "</font>",
    styles["Body2"]
))
elements.append(PageBreak())

# ============================================================
# EJERCICIO 3: Comparativa
# ============================================================
elements.append(Paragraph("EJERCICIO 3: Comparativa FLSM vs VLSM", styles["SubTitle"]))
elements.append(Spacer(1, 0.2*cm))

elements.append(Paragraph("Enunciado:", styles["Heading3"]))
elements.append(Paragraph(
    "Tienes que dividir <b>192.168.1.0/24</b> para: <b>LAN X = 100 hosts</b>, "
    "<b>LAN Y = 50 hosts</b>, <b>Enlace = 2 hosts</b>. "
    "Resuélvelo con FLSM y con VLSM, y compara el desperdicio.",
    styles["Body2"]
))
elements.append(Spacer(1, 0.2*cm))

comp_data = [
    ["Método", "Subred", "Máscara", "Hosts\nnecesarios", "Hosts\ndisponibles", "Desperdicio"],
    ["FLSM", "LAN X", "/25", "100", "126", "26"],
    ["FLSM", "LAN Y", "/25", "50", "126", "76"],
    ["FLSM", "Enlace", "/25", "2", "126", "124"],
    ["VLSM", "LAN X", "/25", "100", "126", "26"],
    ["VLSM", "LAN Y", "/26", "50", "62", "12"],
    ["VLSM", "Enlace", "/30", "2", "2", "0"],
]
t5 = Table(comp_data, colWidths=[2*cm, 2.5*cm, 1.5*cm, 2.5*cm, 2.5*cm, 2.5*cm])
t5.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2B579A")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("SPAN", (0, 1), (0, 3)),
    ("SPAN", (0, 4), (0, 6)),
    ("BACKGROUND", (0, 1), (0, 3), colors.HexColor("#FFCDD2")),
    ("BACKGROUND", (0, 4), (0, 6), colors.HexColor("#C8E6C9")),
]))
elements.append(t5)
elements.append(Spacer(1, 0.3*cm))
elements.append(Paragraph(
    "<b>Conclusión:</b> FLSM desperdicia 226 direcciones. VLSM desperdicia solo 38. "
    "Y ni siquiera cabrían más subredes en FLSM.",
    styles["Body2"]
))
elements.append(PageBreak())

# ============================================================
# EJERCICIO 4: ¿Qué máscara elegir?
# ============================================================
elements.append(Paragraph("EJERCICIO 4: Elige la máscara correcta", styles["SubTitle"]))
elements.append(Spacer(1, 0.2*cm))

elements.append(Paragraph("Para cada cantidad de hosts, escribe la máscara VLSM que da justo lo necesario:", styles["Body2"]))
elec_data = [
    ["Hosts", "2ⁿ - 2 ≥ ...", "mínimo n", "Máscara\n(32-n)", "Tamaño\nde subred"],
    ["100", "2⁷ - 2 = 126 ≥ 100", "7", "/25", "128"],
    ["45", "?", "?", "?", "?"],
    ["20", "?", "?", "?", "?"],
    ["8", "?", "?", "?", "?"],
    ["4", "?", "?", "?", "?"],
    ["2", "2² - 2 = 2 ≥ 2", "2", "/30", "4"],
]
t6 = Table(elec_data, colWidths=[2.5*cm, 4*cm, 2.5*cm, 2.5*cm, 3*cm])
t6.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D32F2F")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FFEBEE")]),
]))
elements.append(t6)

# Build PDF
pdf.build(elements)
print("✅ PDF creado: ejercicios_subredes.pdf")
