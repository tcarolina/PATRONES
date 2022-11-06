3. Fábrica abstracta - Abstract factory:
Abstract Factory es un patrón de diseño creacional que nos permite producir familias de objetos relacionados sin especificar sus clases concretas.

Abstract Factory define un método de fábrica por producto. Cada Factory Method encapsula el newoperador y las clases de productos concretas y específicas de la plataforma. Luego, cada "plataforma" se modela con una clase derivada de Factory.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Abstract_Factory-2x.png)

Ejemplo:
para diferentes modelos de automóviles. Mediante el uso de rodillos para cambiar los troqueles de estampado, las clases de hormigón producidas por la maquinaria se pueden cambiar en tres minutos.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Abstract_Factory_example1-2x.png)

Lista de Verificación:
1.Decidir si la "independencia de la plataforma" y los servicios de creación son la fuente actual del dolor.
2.Trazar una matriz de "plataformas" frente a "productos".
3.Definir una interfaz de fábrica que consista en un método de fábrica por producto.
3.Definir una clase derivada de fábrica para cada plataforma que encapsule todas las referencias al newoperador.
5.El cliente debe retirar todas las referencias a newy usar los métodos de fábrica para crear los objetos del producto.