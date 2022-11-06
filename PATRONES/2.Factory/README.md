2. Fabrica - factory:
Los métodos fábrica pueden ser reconocidos por métodos de creación, que crean objetos de clases concretas.
Estructura
La implementación de Factory Method discutida en Gang of Four (abajo) se superpone en gran medida con la de Abstract Factory. Por esa razón, la presentación de este capítulo se centra en el enfoque que se ha vuelto popular desde entonces.

https://sourcemaking.com/files/v2/content/patterns/Factory_Method-2x.png

método de fábrica es: un staticmétodo de una clase que devuelve un objeto del tipo de esa clase. Pero a diferencia de un constructor, el objeto real que devuelve podría ser una instancia de una subclase. A diferencia de un constructor, se puede reutilizar un objeto existente, en lugar de crear un nuevo objeto. A diferencia de un constructor, los métodos de fábrica pueden tener nombres diferentes y más descriptivos (por ejemplo, Color.make_RGB_color(float red, float green, float blue)y Color.make_HSB_color(float hue, float saturation, float brightness)

![Image text](https://sourcemaking.com/files/v2/content/patterns/Factory_Method_1-2x.png) 

El cliente está totalmente desvinculado de los detalles de implementación de las clases derivadas. La creación polimórfica ahora es posible.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Factory_Method__-2x.png) 

Ejemplo
Factory Method define una interfaz para crear objetos, pero permite que las subclases decidan qué clases instanciar. Los fabricantes de juguetes de plástico procesan polvo de moldeo de plástico e inyectan el plástico en moldes de las formas deseadas. La clase de juguete (automóvil, figura de acción, etc.) está determinada por el molde.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Factory_Method_example1-2x.png)

Lista de Verificación
1.al tener una jerarquía de herencia que ejerce el polimorfismo, considere agregar una capacidad de creación polimórfica definiendo un staticmétodo de fábrica en la clase base.
2.se diseña los argumentos para el método de fábrica. ¿Qué cualidades o características son necesarias y suficientes para identificar la clase derivada correcta para instanciar?
3.Considerar al diseñar un "grupo de objetos" interno que permita que los objetos se reutilicen en lugar de crearlos desde cero.
4.Considerar hacer que todos los constructores privateo protected.