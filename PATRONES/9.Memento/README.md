9. Memento:
Memento es un patrón de diseño de comportamiento que te permite guardar y restaurar el estado previo de un objeto sin revelar los detalles de su implementación.

![Image text](https://refactoring.guru/images/patterns/content/memento/memento-es-2x.png)

Memento es un patrón de diseño de comportamiento que permite tomar instantáneas del estado de un objeto y restaurarlo en el futuro.

El patrón Memento no compromete la estructura interna del objeto con el que trabaja, ni la información que se encuentra dentro de las instantáneas.

Ejemplos de uso: El principio del patrón Memento puede cumplirse utilizando la serialización, que es bastante habitual en Python. Aunque no es la única forma ni la más efectiva de realizar instantáneas del estado de un objeto, permite almacenar copias de seguridad del estado mientras protege de otros objetos la estructura del originador.