7. Proxy:
Proxy es un patrón de diseño estructural que proporciona un objeto que actúa como sustituto de un objeto de servicio real utilizado por un cliente. Un proxy recibe solicitudes del cliente, realiza parte del trabajo (control de acceso, almacenamiento en caché, etc.)

Estructura
Al definir una interfaz Asunto, la presencia del objeto Proxy en lugar de RealSubject es transparente para el cliente.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Proxy1-2x.png)

Ejemplo
El Proxy proporciona un sustituto o marcador de posición para brindar acceso a un objeto. Un cheque o giro bancario es un representante de los fondos en una cuenta. Se puede usar un cheque en lugar de efectivo para realizar compras y, en última instancia, controla el acceso al efectivo en la cuenta del emisor.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Proxy_example1-2x.png)

Lista de Verificación
1.se identifica el apalancamiento o "aspecto" que se implementa mejor como envoltorio o sustituto.
2.Define una interfaz que haga que el proxy y el componente original sean intercambiables.
3.la posibilidad de definir una fábrica que pueda encapsular la decisión de si es deseable un proxy o un objeto original.
4.La clase contenedora contiene un puntero a la clase real e implementa la interfaz.
5.El puntero se puede inicializar en la construcción o en el primer uso.
6.Cada método contenedor contribuye con su influencia y delega al objeto wrappee.