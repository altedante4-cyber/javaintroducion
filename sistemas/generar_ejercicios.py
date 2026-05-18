#!/usr/bin/env python3
"""
Genera un PDF de ejercicios de direccionamiento IP y subredes
sin soluciones, con la misma estructura que ejerciciomichael.pdf
pero con IPs y números diferentes.
"""

import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate

OUTPUT = "/home/michael/sistemas/ejercicios_ip_subredes.pdf"

styles = getSampleStyleSheet()

TITLE = ParagraphStyle('Title2', parent=styles['Title'], fontSize=18, spaceAfter=6)
SUBTITLE = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=11, alignment=TA_CENTER, spaceAfter=20)
SECTION = ParagraphStyle('Section', parent=styles['Heading1'], fontSize=14, spaceBefore=16, spaceAfter=8)
NORMAL = ParagraphStyle('Normal2', parent=styles['Normal'], fontSize=9, leading=13)
SMALL = ParagraphStyle('Small', parent=styles['Normal'], fontSize=8, leading=11)
IP_STYLE = ParagraphStyle('IP', parent=styles['Normal'], fontSize=10, fontName='Courier', leading=14)
TABLE_HEADER = ParagraphStyle('TH', parent=styles['Normal'], fontSize=8, fontName='Helvetica-Bold', alignment=TA_CENTER)
TABLE_CELL = ParagraphStyle('TC', parent=styles['Normal'], fontSize=8, fontName='Courier', alignment=TA_CENTER)

def encabezado(texto):
    return [HRFlowable(width="100%", thickness=1), Paragraph(texto, SECTION), Spacer(1, 6)]

secuencia = []

def p(txt, estilo=NORMAL):
    secuencia.append(Paragraph(txt, estilo))

def espacio(h=12):
    secuencia.append(Spacer(1, h))

def salto():
    secuencia.append(PageBreak())

def tabla(data, col_widths=None, style_extra=None):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    estilo = [
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]
    if style_extra:
        estilo += style_extra
    t.setStyle(TableStyle(estilo))
    secuencia.append(t)
    espacio(8)


# ============================================================
# PORTADA
# ============================================================
def portada():
    espacio(80)
    secuencia.append(Paragraph("DIRECCIONAMIENTO", ParagraphStyle('Big', parent=TITLE, fontSize=22)))
    secuencia.append(Paragraph("IP y SUBREDES", ParagraphStyle('Big2', parent=TITLE, fontSize=20)))
    espacio(12)
    secuencia.append(Paragraph("EJERCICIOS", ParagraphStyle('Big3', parent=TITLE, fontSize=18)))
    espacio(30)
    secuencia.append(HRFlowable(width="60%", thickness=2))
    espacio(10)
    secuencia.append(Paragraph("Generado automáticamente - Sin soluciones", SUBTITLE))
    salto()


# ============================================================
# 1. CONVERSIÓN BINARIO A DECIMAL
# ============================================================
def seccion_binario_decimal():
    secuencia.extend(encabezado("Conversión Binario a Decimal"))
    p("Convierta los siguientes números binarios de 8 bits a decimal:")
    espacio()

    bits_header = ['128', '64', '32', '16', '8', '4', '2', '1', 'Decimal']
    data = [bits_header]

    for _ in range(20):
        fila = []
        for _ in range(8):
            fila.append(str(random.randint(0, 1)))
        fila.append("______")
        data.append(fila)

    col_w = [30]*8 + [50]
    tabla(data, col_w)
    salto()


# ============================================================
# 2. CONVERSIÓN DECIMAL A BINARIO
# ============================================================
def seccion_decimal_binario():
    secuencia.extend(encabezado("Conversión de Decimal a Binario"))
    p("Convierta las siguientes direcciones decimales a binario de 8 bits:")
    espacio()

    for n in [198, 45, 73, 156, 234, 12, 67, 189, 51, 220,
              101, 38, 177, 200, 88, 143, 250, 19, 61, 115]:
        bits_header = ['128', '64', '32', '16', '8', '4', '2', '1']
        data = [bits_header]
        fila = ["_", "_", "_", "_", "_", "_", "_", "_"]
        data.append(fila)
        data.append(["___", "___", "___", "___", "___", "___", "___", "___"])
        t = Table(data, colWidths=[30]*8)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, 0), 0.5, colors.grey),
            ('GRID', (0, 0), (-1, 0), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        secuencia.append(Paragraph(f"Decimal: {n}", TABLE_CELL))
        secuencia.append(t)
        espacio(6)
    salto()


# ============================================================
# 3. IDENTIFICACIÓN DE LA CLASE DE RED
# ============================================================
def clase_ip(ip):
    primero = int(ip.split('.')[0])
    if 1 <= primero <= 127:
        return 'A'
    elif 128 <= primero <= 191:
        return 'B'
    elif 192 <= primero <= 223:
        return 'C'
    elif 224 <= primero <= 239:
        return 'D'
    else:
        return 'E'


def seccion_clase_red():
    secuencia.extend(encabezado("Identificación de la Clase de Red"))
    p("Indique la clase (A, B, C, D o E) de cada dirección IP:")
    espacio()

    data = [["Dirección", "Clase"]]
    for _ in range(20):
        ip = generar_ip_aleatoria()
        data.append([ip, "______"])

    tabla(data, col_widths=[120, 80])
    salto()


# ============================================================
# 4. IDENTIFICACIÓN DE RED Y HOST
# ============================================================
def seccion_red_host():
    secuencia.extend(encabezado("Identificación de Red y Host"))

    # Columna izquierda: marcar parte de red
    p("Rodee con un círculo la parte de RED de cada dirección:", NORMAL)
    espacio(4)
    data_red = [["Dirección", "Red"]]
    for _ in range(15):
        ip = generar_ip_aleatoria()
        data_red.append([ip, ""])
    tabla(data_red, col_widths=[120, 80])

    espacio(12)

    # Columna derecha: marcar parte de host
    p("Rodee con un círculo la parte de HOST de cada dirección:", NORMAL)
    espacio(4)
    data_host = [["Dirección", "Host"]]
    for _ in range(15):
        ip = generar_ip_aleatoria()
        data_host.append([ip, ""])
    tabla(data_host, col_widths=[120, 80])

    salto()


# ============================================================
# 5. MÁSCARAS DE RED POR DEFECTO
# ============================================================
def mascara_por_defecto(ip):
    c = clase_ip(ip)
    if c == 'A':
        return "255.0.0.0"
    elif c == 'B':
        return "255.255.0.0"
    elif c == 'C':
        return "255.255.255.0"
    return "—"


def seccion_mascaras_defecto():
    secuencia.extend(encabezado("Máscaras de Red por Defecto"))
    p("Escriba la máscara de subred por defecto para cada dirección:")
    espacio()

    data = [["Dirección IP", "Máscara por defecto"]]
    for _ in range(20):
        ip = generar_ip_aleatoria()
        data.append([ip, "______ . ______ . ______ . ______"])

    tabla(data, col_widths=[110, 180])
    salto()


# ============================================================
# 6. MÁSCARAS DE SUBRED ADAPTADAS
# ============================================================
def generar_problema_mascara():
    bits_disponibles = {'A': 24, 'B': 16, 'C': 8}
    prob_type = random.choice(['A', 'B', 'C'])
    total_bits = bits_disponibles[prob_type]

    b_sub = random.randint(2, total_bits - 3)
    b_host = total_bits - b_sub

    total_sub = 2 ** b_sub
    utiles_sub = total_sub - 2
    total_h = 2 ** b_host
    utiles_h = total_h - 2

    if prob_type == 'A':
        r = random.randint(10, 126)
        red = f"{r}.0.0.0"
    elif prob_type == 'B':
        r1 = random.randint(128, 191)
        r2 = random.randint(1, 99)
        red = f"{r1}.{r2}.0.0"
    else:
        r1 = random.randint(192, 223)
        r2 = random.randint(1, 99)
        r3 = random.randint(1, 99)
        red = f"{r1}.{r2}.{r3}.0"

    return {
        'red': red,
        'hosts_needed': utiles_h,
        'subredes_needed': utiles_sub,
        'clase': prob_type,
        'bits_subred': b_sub,
        'bits_host': b_host,
    }


def seccion_mascaras_adaptadas():
    secuencia.extend(encabezado("Máscaras de Subred Adaptadas"))
    p("Para cada problema, determine la máscara de subred adaptada, "
      "el número de subredes y hosts totales y útiles, y los bits cogidos.", NORMAL)
    espacio()

    for i in range(1, 11):
        prob = generar_problema_mascara()
        secuencia.append(Paragraph(f"<b>Problema {i}</b>", NORMAL))
        espacio(4)

        fields = [
            f"Nº de subredes útiles necesarias: {prob['subredes_needed']}",
            f"Nº de hosts útiles necesarios: {prob['hosts_needed']}",
            f"Dirección de Red: {prob['red']}",
        ]
        for f in fields:
            secuencia.append(Paragraph(f, NORMAL))

        espacio(4)
        blanks = [
            "Clase: ________________",
            "Máscara de Subred (por defecto): ______ . ______ . ______ . ______",
            "Máscara de Subred (adaptada): ______ . ______ . ______ . ______",
            "Nº total de subredes: ________________",
            "Nº de subredes útiles: ________________",
            "Nº total de direcciones de host: ________________",
            "Nº de direcciones útiles: ________________",
            "Nº de bits cogidos: ________________",
        ]
        for b in blanks:
            secuencia.append(Paragraph(b, SMALL))

        espacio(6)
        secuencia.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))

        if i % 3 == 0:
            salto()
        else:
            espacio(10)

    salto()


# ============================================================
# 7. SUBREDES (con preguntas adicionales)
# ============================================================
def generar_problema_subredes():
    bits_disponibles = {'A': 24, 'B': 16, 'C': 8}
    prob_type = random.choice(['A', 'B', 'C'])
    total_bits = bits_disponibles[prob_type]

    b_sub = random.randint(2, total_bits - 3)
    b_host = total_bits - b_sub

    total_sub = 2 ** b_sub
    utiles_sub = total_sub - 2
    total_h = 2 ** b_host
    utiles_h = total_h - 2

    if prob_type == 'A':
        r = random.randint(10, 126)
        red = f"{r}.0.0.0"
    elif prob_type == 'B':
        r1 = random.randint(128, 191)
        r2 = random.randint(1, 99)
        red = f"{r1}.{r2}.0.0"
    else:
        r1 = random.randint(192, 223)
        r2 = random.randint(1, 99)
        r3 = random.randint(1, 99)
        red = f"{r1}.{r2}.{r3}.0"

    return {
        'red': red,
        'hosts_needed': utiles_h,
        'subredes_needed': utiles_sub,
    }


def seccion_subredes():
    secuencia.extend(encabezado("Subredes"))
    p("Para cada problema, calcule la máscara adaptada y responda las preguntas "
      "sobre rangos, subredes, broadcast y direcciones asignables.", NORMAL)
    espacio()

    for i in range(1, 11):
        prob = generar_problema_subredes()
        secuencia.append(Paragraph(f"<b>Problema {i}</b>", NORMAL))
        espacio(4)
        secuencia.append(Paragraph(f"Nº de subredes útiles necesarias: {prob['subredes_needed']}", NORMAL))
        secuencia.append(Paragraph(f"Nº de hosts útiles necesarios: {prob['hosts_needed']}", NORMAL))
        secuencia.append(Paragraph(f"Dirección de Red: {prob['red']}", NORMAL))
        espacio(4)

        blanks = [
            "Clase: ________________",
            "Máscara de Subred (por defecto): ______ . ______ . ______ . ______",
            "Máscara de Subred (adaptada): ______ . ______ . ______ . ______",
            "Nº total de subredes: ________________",
            "Nº de subredes útiles: ________________",
            "Nº total de direcciones de host: ________________",
            "Nº de direcciones útiles: ________________",
            "Nº de bits cogidos: ________________",
        ]
        for b in blanks:
            secuencia.append(Paragraph(b, SMALL))

        espacio(6)
        extra_questions = [
            "¿Cuál es el 1er rango útil de subredes?",
            "¿Cuál es el número de subred para la 3ª subred útil?",
            "¿Cuál es la dirección de difusión (broadcast) para la 2ª subred útil?",
            "¿Cuáles son las direcciones asignables a la 1ª subred útil?",
        ]
        for q in extra_questions:
            secuencia.append(Paragraph(f"   • {q}", SMALL))

        espacio(8)
        secuencia.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))

        if i % 3 == 0:
            salto()
        else:
            espacio(10)

    salto()


# ============================================================
# 8. DIRECCIONES IP VÁLIDAS E INVÁLIDAS
# ============================================================
def seccion_ip_validas():
    secuencia.extend(encabezado("Direcciones IP válidas e inválidas"))
    p("Identifique si las siguientes direcciones IP son válidas y utilizables. "
      "Si no lo son, explique por qué.", NORMAL)
    espacio()

    casos = [
        ("0.230.190.192", "255.0.0.0"),
        ("192.168.10.1", "255.255.255.0"),
        ("245.150.190.10", "255.255.255.0"),
        ("127.100.100.10", "255.0.0.0"),
        ("200.10.10.128", "255.255.255.224"),
        ("172.16.255.255", "255.255.0.0"),
        ("10.0.0.1", "255.0.0.0"),
        ("192.168.1.255", "255.255.255.0"),
        ("169.254.10.5", "255.255.0.0"),
        ("224.0.0.5", "240.0.0.0"),
        ("198.51.100.0", "255.255.255.0"),
        ("203.0.113.15", "255.255.255.248"),
    ]

    data = [["#", "Dirección IP", "Máscara de Subred", "¿Válida?", "Explicación"]]
    for idx, (ip, mask) in enumerate(casos, 1):
        data.append([str(idx), ip, mask, "______", "______________________________________"])

    tabla(data, col_widths=[20, 100, 100, 50, 180])
    salto()


# ============================================================
# 9. GUÍA DE DIRECCIONAMIENTO (tablas de referencia)
# ============================================================
def seccion_guia():
    secuencia.extend(encabezado("Guía de direccionamiento"))

    for clase, bits_max in [('A', 24), ('B', 16), ('C', 8)]:
        secuencia.append(Paragraph(f"<b>Clase {clase}</b>", NORMAL))
        espacio(4)

        data = [["Bits", "Máscara", "Total Subredes", "Subredes Útiles", "Total Hosts", "Hosts Útiles"]]
        for bits in range(2, min(bits_max + 1, 16)):
            mascara = calcular_mascara_clase(clase, bits)
            total_sub = 2 ** bits
            utiles_sub = total_sub - 2
            total_hosts = 2 ** (bits_max - bits)
            utiles_hosts = total_hosts - 2
            data.append([
                str(bits),
                mascara,
                str(total_sub),
                str(utiles_sub) if utiles_sub > 0 else "0",
                str(total_hosts),
                str(utiles_hosts) if utiles_hosts > 0 else "0",
            ])

        t = Table(data, colWidths=[30, 100, 60, 60, 60, 60], repeatRows=1)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 7),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.85, 0.85, 0.85)),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        secuencia.append(t)
        espacio(12)

    salto()


def calcular_mascara_clase(clase, bits):
    if clase == 'A':
        base = [255, 0, 0, 0]
    elif clase == 'B':
        base = [255, 255, 0, 0]
    else:
        base = [255, 255, 255, 0]

    remaining = bits
    idx = 1 if clase == 'A' else (2 if clase == 'B' else 3)
    while remaining > 0 and idx < 4:
        take = min(remaining, 8)
        base[idx] = 256 - (2 ** (8 - take))
        remaining -= take
        idx += 1

    return ".".join(str(x) for x in base)


# ============================================================
# UTILIDADES
# ============================================================
def generar_ip_aleatoria():
    primero = random.choice([random.randint(1, 126), random.randint(128, 191), random.randint(192, 223)])
    if primero <= 126:
        return f"{primero}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    elif primero <= 191:
        return f"{primero}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    else:
        return f"{primero}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"


# ============================================================
# MAIN
# ============================================================
def generar():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
    )

    portada()
    seccion_binario_decimal()
    seccion_decimal_binario()
    seccion_clase_red()
    seccion_red_host()
    seccion_mascaras_defecto()
    seccion_mascaras_adaptadas()
    seccion_subredes()
    seccion_ip_validas()
    seccion_guia()

    doc.build(secuencia)
    print(f"PDF generado: {OUTPUT}")


if __name__ == "__main__":
    generar()
