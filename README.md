## Movies API

## Cómo ejecutar el código

Requisito:
1. Tener docker instalado

Primero debes clonar este repositorio, puedes hacerlo con el siguiente comando:

`git@github.com:iKenshu/movies-api.git`

Usar docker compose para hacer build de la aplicación y ejecutarla

`docker-compose up -d --build`

A continuación necesitarás ejecutar la migración para la base de datos:

`docker-compose exec web python manage.py migrate`

Lo siguiente será crear un super usuario para aprovechar el prefill de datos:

`docker-compose exec web python manage.py createsuperuser`

Ahora ejecutaremos un comando para cargar la base de datos con algo de información:

`docker-compose exec web python manage.py loaddata movies.json`

## URLs

**Movies**

`/movies/ GET` Lista todas las películas disponibles.
`/movies/collections/ GET` Muestra todas las colecciones públicas de los usuarios.
`/movies/my-collections/ GET` Muestra todas las colecciones públicas y privadas creadas por el usuario. Recibe token de autenticación.
`/movies/my-collections-private/ GET` Muestra todas las colecciones privadas creadas por el usuario. Recibe token de autenticación.
`/movies/my-collections/create POST` Crea una colección. Recibe token de autenticación.
`/movies/my-collections/:id/ GET` Muestra solo una colección creada por el usuario. Recibe el ID de la colección.
`/movies/my-collections/:id/edit/ PATCH` URL para editar nombre, películas o su privacidad. Recibe el ID de la colección.

**Users**

`/users/register/` Para crear un nuevo usuario, necesita email, contraseña y confirmación de contraseña. Responderá con el email creado exitosamente.
`/users/login/` Para iniciar sesión con una cuenta existente, necesita email y password. Responderá con un token de autenticación.
