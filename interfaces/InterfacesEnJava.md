# Interfaces en Java

## 🧩 ¿Qué es una interfaz?
Una **interfaz** en Java es un tipo de referencia que define un contrato (un conjunto de métodos) que las clases pueden implementar. Una interfaz no puede instanciarse directamente; en cambio, una clase que implementa la interfaz debe proporcionar una implementación concreta de sus métodos (salvo métodos `default` o `static`).

> 🔑 **Idea clave:** Una interfaz define **qué** debe hacerse, no **cómo** se hace.

---

## ✅ ¿Por qué usar interfaces?
- Permiten **desacoplar** la definición de un comportamiento de su implementación.
- Facilitan el diseño orientado a **polimorfismo**: puedes usar el tipo de la interfaz para trabajar con múltiples implementaciones.
- Soportan **herencia múltiple de tipo** (una clase puede implementar varias interfaces) sin los problemas de herencia múltiple de clases.
- Son fundamentales para escribir código **testable** y seguir principios SOLID (especialmente el **Principio de Segregación de Interfaces** y la **Inversión de Dependencias**).

---

## 🧠 Sintaxis básica
```java
public interface Vehiculo {
    void arrancar();
    void detener();
}

public class Coche implements Vehiculo {
    @Override
    public void arrancar() {
        System.out.println("Coche arrancando");
    }

    @Override
    public void detener() {
        System.out.println("Coche detenido");
    }
}
```

---

## 📌 Tipos de métodos dentro de una interfaz (Java 8+)
### 1) Métodos abstractos (sin cuerpo)
Son el núcleo de la interfaz; deben ser implementados por la clase.

### 2) Métodos `default`
Permiten enviar implementación por defecto dentro de la interfaz. No obliga a la clase que implementa la interfaz a redefinirlos.

```java
public interface Vehiculo {
    void arrancar();

    default void acelerar() {
        System.out.println("Acelerando...");
    }
}
```

### 3) Métodos `static`
Son métodos utilitarios asociados a la interfaz. Se invocan con `NombreInterfaz.metodo()`.

```java
public interface Vehiculo {
    static void tipoInformacion() {
        System.out.println("Interfaz Vehiculo");
    }
}
```

---

## 🧩 Herencia múltiple de interfaces
Una clase puede implementar varias interfaces, lo que facilita combinar comportamientos.

```java
public interface Volador {
    void volar();
}

public interface Nadador {
    void nadar();
}

public class Pato implements Volador, Nadador {
    @Override
    public void volar() {
        System.out.println("El pato vuela");
    }

    @Override
    public void nadar() {
        System.out.println("El pato nada");
    }
}
```

---

## ⚖️ Interface vs Abstract class
| Característica | Interface | Clase abstracta |
|---|---|---|
| Puede tener implementación (Java 8+) | Sí, `default` y `static` | Sí (métodos con cuerpo)
| Herencia múltiple | Sí (varias interfaces) | No (solo una superclase)
| Variables | `public static final` (constantes) | Campos de instancia/estáticos con cualquier modificador
| Instanciación | No | No (no se puede instanciar directamente)

> 💡 Usa interfaces cuando quieras definir **un contrato de comportamiento** independiente de la jerarquía de clases.

---

## 🔧 Interfaces funcionales (Java 8+)
Una **interfaz funcional** tiene exactamente un método abstracto. Son esenciales para usar expresiones lambda.

```java
@FunctionalInterface
public interface Operacion {
    int aplicar(int a, int b);
}

Operacion suma = (a, b) -> a + b;
System.out.println(suma.aplicar(3, 4)); // 7
```

### Ejemplos de interfaces funcionales en `java.util.function`
- `Predicate<T>`
- `Function<T,R>`
- `Consumer<T>`
- `Supplier<T>`

---

## 🧪 Buenas prácticas
- Define *interfaces pequeñas y específicas* (Principio de Segregación de Interfaces).
- Nombra interfaces con sufijos como `-able` (`Serializable`, `Comparable`), o con un sustantivo claro (`Repositorio`, `Servicio`).
- Usa interfaces como tipos en los parámetros y campos para aumentar la flexibilidad.
- Evita `default` a menos que sea necesario (por compatibilidad o comportamiento por defecto).

---

## 📌 Ejemplo de uso en una aplicación simple
```java
public interface Repositorio<T> {
    void guardar(T entidad);
    T buscarPorId(int id);
}

public class UsuarioRepositorio implements Repositorio<Usuario> {
    @Override
    public void guardar(Usuario usuario) {
        // guardar en BD
    }

    @Override
    public Usuario buscarPorId(int id) {
        // buscar en BD
        return null;
    }
}

public class ServicioUsuario {
    private final Repositorio<Usuario> repositorio;

    public ServicioUsuario(Repositorio<Usuario> repositorio) {
        this.repositorio = repositorio;
    }

    public void crearUsuario(Usuario u) {
        repositorio.guardar(u);
    }
}
```

---

## ✅ Resumen rápido
- Una interfaz define **métodos, constantes y comportamiento opcional** (`default`/`static`).
- Puedes implementar varias interfaces en una clase.
- Son clave para lograr **polimorfismo**, **desacoplamiento** y **testabilidad**.
- Las **interfaces funcionales** permiten usar lambdas y APIs modernas.

¡Listo! Tienes un archivo completo que reúne los conceptos esenciales sobre interfaces en Java. Si quieres, puedo agregar diagramas UML, ejemplos prácticos más extensos o ejercicios con soluciones.
