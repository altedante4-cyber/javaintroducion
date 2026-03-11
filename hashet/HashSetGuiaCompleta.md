# 🎓 HashSet en Java - Guía Completa Senior

## 🎯 ¿QUÉ ES UN HashSet?

Un **HashSet** es una colección que almacena **elementos únicos sin ningún orden específico**. Implementa la interfaz `Set` y utiliza una **tabla hash** internamente para almacenar los datos.

```
HashSet ≈ Conjunto matemático (sin duplicados, sin orden)
```

---

## 🔑 CARACTERÍSTICAS PRINCIPALES

### 1. No permite duplicados
```java
HashSet<String> frutas = new HashSet<>();
frutas.add("manzana");
frutas.add("manzana");  // ← Se ignora silenciosamente
System.out.println(frutas.size()); // Imprime: 1
```

### 2. No garantiza orden
```java
// El orden puede variar cada vez que ejecutes
HashSet<Integer> numeros = new HashSet<>();
numeros.add(3);
numeros.add(1);
numeros.add(2);
System.out.println(numeros); // Podría ser: [1, 2, 3] o [3, 1, 2]
```

### 3. Permite un elemento null
```java
HashSet<String> conjunto = new HashSet<>();
conjunto.add(null);      // ✓ Permitido (una sola vez)
conjunto.add(null);      // Sin efecto
System.out.println(conjunto.size()); // 1
```

---

## ⚙️ ¿CÓMO FUNCIONA INTERNAMENTE?

HashSet usa **hashing** (función hash + tabla hash):

```
1. Llamas add("pera")
    ↓
2. Se calcula el hash: "pera".hashCode() → 3254192
    ↓
3. Se mapea a un índice: 3254192 % tablaTamaño → índice 5
    ↓
4. Se almacena en la tabla[5]
    ↓
5. Si hay colisión (dos elementos con mismo hash):
   → Se usan "buckets" con listas enlazadas
```

---

## 📋 OPERACIONES COMUNES

### Crear e insertar
```java
HashSet<String> conjunto = new HashSet<>();
conjunto.add("java");       // true
conjunto.add("python");     // true
conjunto.add("java");       // false (ya existe)
```

### Verificar existencia
```java
if (conjunto.contains("java")) {
    System.out.println("Java está en el conjunto");
}
```

### Eliminar elementos
```java
conjunto.remove("python");  // true
conjunto.remove("c++");     // false (no existe)
```

### Iterar sobre elementos
```java
// 1. For-each (recomendado)
for (String lenguaje : conjunto) {
    System.out.println(lenguaje);
}

// 2. Iterator (si necesitas eliminar durante iteración)
Iterator<String> iter = conjunto.iterator();
while (iter.hasNext()) {
    String elem = iter.next();
    if (elem.equals("java")) {
        iter.remove();  // ✓ Forma correcta
    }
}

// 3. Stream (moderno)
conjunto.stream().forEach(System.out::println);
```

### Operaciones de conjunto
```java
HashSet<Integer> a = new HashSet<>(Arrays.asList(1, 2, 3));
HashSet<Integer> b = new HashSet<>(Arrays.asList(2, 3, 4));

// Unión
a.addAll(b);  // {1, 2, 3, 4}

// Intersección
a.retainAll(b);  // Solo elementos comunes

// Diferencia
a.removeAll(b);  // Elimina elementos de b
```

---

## 🏆 BUENAS PRÁCTICAS

### 1. Implementa hashCode() y equals() correctamente
```java
class Persona {
    private String nombre;
    private int edad;

    @Override
    public int hashCode() {
        return Objects.hash(nombre, edad);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Persona persona = (Persona) obj;
        return edad == persona.edad && 
               Objects.equals(nombre, persona.nombre);
    }
}

// Ahora funciona correctamente:
HashSet<Persona> personas = new HashSet<>();
personas.add(new Persona("Juan", 30));
personas.add(new Persona("Juan", 30));  // Se detecta duplicado
```

### 2. Usa tipos genéricos
```java
// ❌ Evita esto (sin tipos)
HashSet conjunto = new HashSet();

// ✓ Haz esto (con tipos)
HashSet<String> conjunto = new HashSet<>();
```

### 3. No modifiques elementos mientras están en el conjunto
```java
HashSet<Persona> personas = new HashSet<>();
Persona p = new Persona("Juan", 30);
personas.add(p);

// ❌ NO hagas esto:
p.edad = 31;  // Cambia el hash, rompe la estructura

// ✓ Haz esto:
personas.remove(p);
p.edad = 31;
personas.add(p);
```

### 4. Inicializa con capacidad apropiada
```java
// Si sabes el tamaño aproximado:
HashSet<String> conjunto = new HashSet<>(100);  // Evita redimensionamientos
```

### 5. Usa LinkedHashSet si necesitas orden de inserción
```java
LinkedHashSet<String> conjuntoOrdenado = new LinkedHashSet<>();
conjuntoOrdenado.add("C");
conjuntoOrdenado.add("A");
conjuntoOrdenado.add("B");
System.out.println(conjuntoOrdenado);  // [C, A, B] - mantiene orden
```

---

## ⚡ COMPLEJIDAD DE TIEMPO

| Operación | Complejidad |
|-----------|------------|
| `add()` | O(1) promedio |
| `remove()` | O(1) promedio |
| `contains()` | O(1) promedio |
| `Iterar` | O(n) |

*Peor caso: O(n) si hay muchas colisiones, pero raro.*

---

## 📊 COMPARATIVA CON OTROS

| Colección | Orden | Duplicados | Velocidad |
|-----------|-------|-----------|-----------|
| **HashSet** | No | No | ⚡⚡⚡ (Rápida) |
| **TreeSet** | Sí (ordenado) | No | ⚡⚡ |
| **LinkedHashSet** | Sí (inserción) | No | ⚡⚡ |
| **ArrayList** | Sí | Sí | ⚡⚡ |

---

## 💡 CUÁNDO USAR HashSet

### ✅ Usar cuando:
- Necesitas almacenar elementos únicos
- La velocidad es crítica (O(1))
- No importa el orden
- Necesitas búsquedas rápidas

### ❌ NO usar cuando:
- Necesitas mantener orden
- Tienes muchas iteraciones (mejor List)
- Necesitas acceso por índice

---

## 🎓 EJEMPLO PRÁCTICO COMPLETO

```java
import java.util.*;

public class EjemploHashSetAvanzado {
    public static void main(String[] args) {
        // Conjunto de palabras únicas
        HashSet<String> palabras = new HashSet<>();
        String[] texto = {"java", "python", "java", "c++", "python", "go"};
        
        for (String palabra : texto) {
            palabras.add(palabra);
        }
        
        System.out.println("Palabras únicas: " + palabras.size());
        System.out.println(palabras);
        
        // Búsqueda rápida
        if (palabras.contains("java")) {
            System.out.println("Java está presente");
        }
        
        // Eliminar mientras iteras (forma correcta)
        Iterator<String> iter = palabras.iterator();
        while (iter.hasNext()) {
            if (iter.next().length() > 4) {
                iter.remove();
            }
        }
        
        System.out.println("Después de filtrar: " + palabras);
    }
}
```

---

## 🔍 ERRORES COMUNES

### Error 1: Intentar obtener por índice
```java
HashSet<String> set = new HashSet<>();
set.add("Java");
// String elemento = set.get(0);  // ¡ERROR! HashSet no tiene get()
```

### Error 2: Esperar un orden específico
```java
for (String s : set) {
    System.out.println(s);  // Orden impredecible
}
```

### Error 3: Modificar durante iteración (INCORRECTO)
```java
// ❌ NUNCA hagas esto:
for (String s : set) {
    if (s.equals("Java")) {
        set.remove(s);  // ¡Causa ConcurrentModificationException!
    }
}

// ✓ Correcto:
Iterator<String> it = set.iterator();
while (it.hasNext()) {
    if (it.next().equals("Java")) {
        it.remove();  // Seguro
    }
}
```

---

## 📌 RESUMEN EJECUTIVO

| Aspecto | Detalle |
|---------|---------|
| **Uso** | Almacenar elementos únicos sin orden |
| **Velocidad** | Muy rápida O(1) |
| **Memoria** | Más que ArrayList |
| **Thread-safe** | No (usa `Collections.synchronizedSet()` si lo necesitas) |
| **Alternativa thread-safe** | `ConcurrentHashMap.newKeySet()` |

---

## 🔐 THREAD-SAFETY (Seguridad en hilos)

```java
// ❌ NO es thread-safe:
HashSet<String> set = new HashSet<>();

// ✓ Para múltiples hilos:
Set<String> syncSet = Collections.synchronizedSet(new HashSet<>());

// Mejor opción (Java 7+):
Set<String> concurrentSet = ConcurrentHashMap.newKeySet();
```

---

## 📚 MÉTODOS PRINCIPALES

```java
HashSet<String> set = new HashSet<>();

// Añadir
set.add("elemento");           // boolean

// Eliminar
set.remove("elemento");        // boolean

// Verificar
set.contains("elemento");      // boolean
set.isEmpty();                 // boolean
set.size();                    // int

// Limpiar todo
set.clear();                   // void

// Operaciones de conjuntos
set.addAll(otroSet);          // Unión
set.retainAll(otroSet);       // Intersección
set.removeAll(otroSet);       // Diferencia

// Iterar
Iterator<String> iter = set.iterator();
```

---

## 🎯 CASOS DE USO REALES

### 1. Eliminar duplicados
```java
List<String> lista = Arrays.asList("a", "b", "a", "c", "b");
HashSet<String> unicos = new HashSet<>(lista);
System.out.println(unicos);  // [a, b, c]
```

### 2. Búsqueda rápida
```java
HashSet<String> palabrasProhibidas = new HashSet<>(
    Arrays.asList("spam", "bad", "inappropriate")
);

for (String palabra : documento.split(" ")) {
    if (palabrasProhibidas.contains(palabra)) {
        System.out.println("Palabra prohibida encontrada");
    }
}
```

### 3. Intersección de colecciones
```java
HashSet<Integer> grupo1 = new HashSet<>(Arrays.asList(1, 2, 3, 4));
HashSet<Integer> grupo2 = new HashSet<>(Arrays.asList(3, 4, 5, 6));

grupo1.retainAll(grupo2);  // grupo1 ahora es {3, 4}
```

### 4. Validar unicidad
```java
HashSet<String> emails = new HashSet<>();
for (String email : listaEmails) {
    if (!emails.add(email)) {
        System.out.println("Email duplicado: " + email);
    }
}
```

---

## 🚀 CONSEJOS FINALES

1. **Elige el tipo correcto de colección**: Si necesitas orden, usa `TreeSet` o `LinkedHashSet`
2. **Implementa correctamente equals() y hashCode()**: Son fundamentales para el buen funcionamiento
3. **Usa generics**: Evita errores de casting y proporciona mayor seguridad de tipos
4. **Evita modificar objetos**: Una vez insertados, sus atributos que afecten al hash no deben cambiar
5. **Considera el tamaño inicial**: Para conjuntos grandes, inicializa con capacidad suficiente
6. **Usa Stream API cuando sea posible**: Es más limpio y funcional

---

**Última actualización**: 11 de marzo de 2026
**Nivel**: Senior/Avanzado
