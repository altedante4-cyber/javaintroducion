# Practica: Saneamiento y Actualizacion de Bases de Datos

## Archivos Disponibles

| Archivo | Descripcion |
|---------|-------------|
| `00_practica_setup.sql` | Crea la base de datos y datos iniciales "sucios" |
| `01_safe_updates.sql` | Practica 2: Modo seguro y Error 1175 |
| `02_fk_checks.sql` | Practica 3: Claves foraneas y FOREIGN_KEY_CHECKS |
| `03_insert_select.sql` | Practica 4: INSERT SELECT y UPSERT |
| `05_update_saneamiento.sql` | Practica 5: UPDATE, JOIN, CASE, subconsultas |
| `06_null_handling.sql` | Practica 6: IFNULL y COALESCE |
| `07_ddl_modify.sql` | Practica 7: ALTER TABLE (columnas, tipos, constraints) |
| `08_performance.sql` | Practica 8: SARGability e indices |
| `09_delete_audit.sql` | Practica 9: DELETE, TRUNCATE, auditoria |
| `10_ejercicios_repaso.sql` | Ejercicios integrados de tous los temas |

## Orden de Ejecucion

1. Ejecutar `00_practica_setup.sql` una vez
2. Ejecutar los demas archivos en orden
3. Si hay errores, volver a ejecutar `00_practica_setup.sql` para reiniciar

## Ejecucion rapida

```bash
mysql -u root -p < 00_practica_setup.sql
mysql -u root -p Practica_Sanamiento < 01_safe_updates.sql
# ... continuar con el resto
```
