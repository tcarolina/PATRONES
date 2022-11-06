12. DAO - Data Access Object:
Dado lo anterior, el patrón DAO propone separar por completo la lógica de negocio de la lógica para acceder a los datos, de esta forma, el DAO proporcionará los métodos necesarios para insertar, actualizar, borrar y consultar la información; por otra parte, la capa de negocio solo se preocupa por lógica de negocio y utiliza el DAO para interactuar con la fuente de datos.

![Image text](https://www.oscarblancarteblog.com/wp-content/uploads/2018/12/UML-clases-1024x493.png)

Los compones que conforman el patrón son:

-BusinessObject: representa un objeto con la lógica de negocio.
-DataAccessObject: representa una capa de acceso a datos que oculta la fuente y los detalles técnicos para recuperar los datos.
-TransferObject: este es un objeto plano que implementa el patrón Data Transfer Object (DTO), el cual sirve para transmitir la información entre el DAO y el Business Service.
-DataSource: representa de forma abstracta la fuente de datos, la cual puede ser una base de datos, Webservices, LDAP, archivos de texto, etc.

#https://python.hotexamples.com/es/examples/models/DAO/-/python-dao-class-examples.html