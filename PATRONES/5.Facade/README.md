5. Fachada - Facade:
El patrón de diseño Fachada sirve para proveer de una interfaz unificada sencilla que haga de intermediaria entre un cliente y una interfaz o grupo de interfaces más complejas.

Estructura
Facade toma un "acertijo envuelto en un enigma envuelto en misterio", e intercala un envoltorio que domestica la masa amorfa e inescrutable del software.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Facade1-2x.png)

SubsystemOney SubsystemThreeno interactúan con los componentes internos de SubsystemTwo. Utilizan la SubsystemTwoWrapper"fachada" (es decir, la abstracción de nivel superior).

![Image text](https://sourcemaking.com/files/v2/content/patterns/Facade_1-2x.png)

Ejemplo
La fachada define una interfaz unificada de nivel superior para un subsistema que facilita su uso. Los consumidores se encuentran con una Fachada cuando ordenan de un catálogo. El consumidor llama a un número y habla con un representante de servicio al cliente. El representante de servicio al cliente actúa como una fachada, proporcionando una interfaz para el departamento de cumplimiento de pedidos, el departamento de facturación y el departamento de envío.

![Image text](https://sourcemaking.com/files/v2/content/patterns/Facade_example1-2x.png) 

Lista de Verificación
1.se Identifica una interfaz unificada más simple para el subsistema o componente.
2.el Diseño una clase 'envoltura' que encapsule el subsistema.
La fachada/envoltura captura la complejidad y las colaboraciones del componente y delega a los métodos apropiados.
4.El cliente utiliza (se acopla a) la Fachada únicamente.
