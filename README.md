# taller14

## Creación de Servicio Web y Consumo vía VueJS

### Revisar
* Ejemplo de servicios web con Django y Django-Rest [app-django/ejemplo3]
* Ejemplo de consumo de servicios web desde VueJS [app-consumo-2]
	* Considerar para la aplicación VueJS

```
Se trabajará con al versión: v16.16.0
Instalar la versión mediante:

nvm install v16.16.0

Usar la versión:

nvm use v16.16.0

Dentro de la carpeta de **app-consumo-2**, usar

npm install
npm run serve

```

### Ejemplos
* Usando curl

```

curl -H 'Accept: application/json; indent=4' -u user:pass http://127.0.0.1:8000/users/


curl -H 'Accept: application/json; indent=4' -iX POST -d 'telefono=1909091&tipo=personal&estudiante=http://127.0.0.1:8000/api/estudiantes/4/' -u user:pass 127.0.0.1:8000/api/numerost/

curl -iX PUT -d 'telefono=22909091&tipo=particular2&estudiante=http://127.0.0.1:8000/api/estudiantes/13/' -u user:pass http://127.0.0.1:8000/api/numerost/24/


curl -X DELETE -u user:pass http://127.0.0.1:8000/api/numerost/25/

curl -iX GET -u user:pass http://127.0.0.1:8000/api/numerost/24/

```

* Usando requests (librería de python)

```

# GET
import requests
r = requests.get("http://127.0.0.1:8000/api/estudiantes/", auth=('user', 'passs'))
r.content

# POST
r = requests.post('http://127.0.0.1:8000/api/numerost/', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/12/', 'telefono':'99999999', 'tipo'='principal' }, auth=('user', 'pass'))
print(r)

# PUT
r = requests.put('http://127.0.0.1:8000/api/numerost/26', data = {'estudiante':'http://127.0.0.1:8000/api/estudiantes/13/', 'telefono':'99999999', 'tipo':'principal' }, auth=('user', 'pass'))
print(r)

# DELETE
r = requests.delete('http://127.0.0.1:8000/api/numerost/26/', auth=('user', 'pass'))
print(r)
```


### Problemática

Dadas dos entidades:

* Propietario:
	* nombre
	* apellido
	* edad
	* nacionalidad [ecuatoriana, peruana, colombiana]

* Departamento
	* costo del departamento
	* número de cuartos
	* número de baños
	* valor de alícuota

Nota: Un departamento pertenece a un Propietario

### Tecnologías y herramientas:

- Base de datos Sqlite
- Lenguaje Python
- Framework Django
- Django-Rest
- VueJs


### Tarea a realizar:

- Crear un proyecto de Django en el directorio [desarrollo/proyecto-django]
- Crear una aplicación en el proyecto den Django.
- Generar el modelo de la aplicación usando las entidades descritas.
- Activar la interfaz de administración de la aplicación de Django.
- Crear una aplicación en VueJS (en el directorio [desarrollo/proyecto-vuejs])
	* Que permita listar, editar, eliminar y crear Propietarios, haciendo uso de los servicios web creados en el proyecto de Django.
	* Que permita listar, editar, eliminar y crear Departamentos, haciendo uso de los servicios web creados en el proyecto de Django.
