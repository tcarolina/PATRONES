6. Decorador - Decorator:
el patrón Decorator tiene como objetivo hacer que los componentes sean más flexibles y fáciles de reutilizar. Con este fin, el enfoque permite añadir y eliminar las dependencias de un objeto de manera dinámica y, cuando sea necesario, durante el tiempo de ejecución. 

Estructura
El cliente siempre está interesado en CoreFunctionality.doThis(). El cliente puede o no estar interesado en OptionalOne.doThis() y OptionalTwo.doThis(). Cada una de estas clases siempre delega a la clase base Decorator, y esa clase siempre delega al objeto "wrappee" contenido.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Decorator__1-2x.png)

Ejemplo
Otro ejemplo: la pistola de asalto es un arma letal por sí sola. Pero puedes aplicar ciertas "decoraciones" para hacerlo más preciso, silencioso y devastador.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Decorator_example-2x.png)

