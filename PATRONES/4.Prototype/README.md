4. Prototipo-Prototype:
Prototype es un patrón de diseño creacional que permite la clonación de objetos, incluso los complejos, sin acoplarse a sus clases específicas.

se declara una clase base abstracta que especifique un método de "clon" virtual puro y mantenga un diccionario de todas las clases derivadas concretas "clonables". Cualquier clase que necesite una capacidad de "constructor polimórfico": se deriva de la clase base abstracta, registra su instancia prototípica e implementa la clone()operación.

Estructura
La Fábrica sabe cómo encontrar el Prototipo correcto, y cada Producto sabe cómo generar nuevas instancias de sí mismo.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Prototype-2x.png)

Ejemplo
El patrón Prototype especifica el tipo de objetos que se crearán utilizando una instancia prototípica.  La división mitótica de una célula, que da como resultado dos células idénticas, es un ejemplo de un prototipo que juega un papel activo en la copia de sí mismo y, por lo tanto, demuestra el patrón Prototipo. 

![Image text](https://sourcemaking.com/files/v2/content/patterns/Prototype_example1-2x.png)

Lista de Verificación
1.Agrega un clone()método a la jerarquía de "producto" existente.
2.Diseña un "registro" que mantenga un caché de objetos prototípicos. El registro se podría encapsular en una nueva Factoryclase o en la clase base de la jerarquía del "producto".
3.Diseña un método de fábrica que: pueda (o no) aceptar argumentos, encuentre el objeto prototipo correcto, llame clone()a ese objeto y devuelva el resultado.
4.El cliente reemplaza todas las referencias al new operador con llamadas al método de fábrica.