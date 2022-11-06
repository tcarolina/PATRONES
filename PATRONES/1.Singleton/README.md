1. Singleton:
Singleton es un patrón de diseño creacional que garantiza que tan solo exista un objeto de su tipo y proporciona un único punto de acceso a él para cualquier otro código.

Estructura
![Image text](https://sourcemaking.com/files/v2/content/patterns/singleton1-2x.png)

Lista de Verificación:
1.Definir un staticatributo privado en la clase de "instancia única".
2.Definir una staticfunción de acceso público en la clase.
3.Realizar una "inicialización diferida" (creación en el primer uso) en la función de acceso.
4.Definir todos los constructores para que sean protected o private.
5.Los clientes solo pueden usar la función de acceso para manipular el Singleton.
    
![Image text](https://refactoring.guru/images/patterns/content/singleton/singleton.png?id=108a0b9b5ea5c4426e0afa4504491d6f) 