# Tivix Test

A Django and frontend (Quasar) test to Tivix.

## Instalation

This application was developed on Linux Ubuntu 20.04. For carrying out this application, you need to have already installed these frameworks:

* Docker (https://www.docker.com/)
* Docker-Compose (https://docs.docker.com/compose/install/)

For install the application, follow these steps bellow:

* Clone the application from github with:

```bash
      https://github.com/diemancini/tivix_test.git
```
After cloning, run these commands in the root project:

```bash
    chmod +x app/entrypoint.sh /* it is needed to wait until the Postgres database get ready to build de app. */
    docker-compose up -d --build
    docker-compose exec web python teacher_student/manage.py makemigrations
    docker-compose exec web python teacher_student/manage.py migrate --noinput
```
If you get an error during executing makemigrations or migrate commands, run:

```bash
    docker-compose down -v
```

To remove the volumes along with the containers. After that, re-build the images, run the containers, and apply the migrations again.
After executing the above-mentioned commands, open a browser and put on address bar the following link:

* http://localhost:8000/

You should see a screen with a two buttons to choose the list of students or teachers.

## Start with data
If you want to start with data in database, just run:

```bash
    docker-compose exec web python teacher_student/manage.py loaddata teacher_student/crud/fixtures/all.json
```

## Tests

To run tests, run:

```bash
    docker-compose exec web python teacher_student/manage.py test crud
```
