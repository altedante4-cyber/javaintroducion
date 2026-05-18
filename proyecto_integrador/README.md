# Proyecto EcoDrive — Entrega Académica

## Estructura del proyecto

```
03_Practica_Evaluacion_NoSQL.tex   — Documento principal (memoria técnica)
03_analisis_auditoria.tex          — Apartado C: Análisis de Auditoría (CE.a, CE.c)
analisis_auditoria_completo.md     — Versión en Markdown del mismo contenido
README.md                          — Este archivo
```

## Contenido del Apartado C (Análisis de Auditoría)

El archivo `03_analisis_auditoria.tex` contiene el desarrollo completo del entregable 3:

| Sección | Contenido |
|---|---|
| 3.1 | Introducción: auditoría IA, sesgo relacional, agregados, Query-First, persistencia políglota, CE.a/CE.c |
| 3.2 | Auditoría MongoDB: Normalización Encubierta (código erróneo + corregido, justificación) |
| 3.3 | Auditoría Cassandra: Hotspot por Partition Key de baja cardinalidad (código erróneo + corregido) |
| 3.4 | Auditoría Redis: Strings JSON sin TTL (código erróneo + corregido con HASH + HINCRBY + EXPIRE) |
| 3.5 | Auditoría Neo4j: Nodos-Tabla y relaciones genéricas (código erróneo + corregido con relaciones semánticas) |
| 3.6 | Resumen global de correcciones (tabla comparativa) |
| 3.7 | Conclusión técnica |

## Compilación

Para generar el PDF:

```bash
pdflatex 03_Practica_Evaluacion_NoSQL.tex
```

Pueden ser necesarias 2-3 pasadas para resolver referencias cruzadas y el índice.

## Dependencias LaTeX

- `goyabase` (paquete personalizado de la universidad)
- `listings` (código fuente)
- `xcolor` (colores para listings)
- `tcolorbox` (cajas de objetivo/criterio)
- `babel` / `csquotes` (español)

## Notas sobre el Apartado C

- Cada subsección incluye el código **erróneo generado por la IA** y el **código corregido**.
- Todas las correcciones están justificadas técnicamente según los principios del Anexo.
- Se cubren los criterios **CE.a** (características NoSQL) y **CE.c** (elementos: agregados, claves, nodos, tipos de datos).
- Se documentan **4 antipatrones** diferentes, uno por cada motor NoSQL.

## Autor

Víctor de Juan — Curso 2025-2026
