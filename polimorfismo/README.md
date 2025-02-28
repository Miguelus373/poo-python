# Polimorfismo

Este programa implementa el concepto de polimorfismo a través de una clase base `Empleado` y tres clases derivadas: `Desarrollador`, `Diseñador` y `Gerente`.

## Clases
- **Empleado**: Clase base con un método `trabajar()`.
- **Desarrollador**: Implementa `trabajar()` devolviendo "Escribiendo código."
- **Diseñador**: Implementa `trabajar()` devolviendo "Creando diseño gráfico."
- **Gerente**: Implementa `trabajar()` devolviendo "Gestionando el equipo."

## Función
- `mostrar_trabajo(empleados)`: Muestra el resultado del método `trabajar()` de cada empleado.

## Ejecución
1. Asegúrate de tener Python instalado.
2. Navega a la carpeta principal `poo-python`
3. Ejecuta el archivo con el siguiente comando:
    ```bash
    python polimorfismo