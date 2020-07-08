# fullcycle-django

### pre-requisites

```
- python
- django
- docker
```

## Run
```
py manage.py runserver
```

## Build Docker

```
docker build -t yourLogin/fullcycle-django:latest . 
```

## Run Docker
```
docker run -p 8000:8000 yourLogin/fullcycle-django
```

## Push to Docker Hub
```
docker login

docker push yourLogin/fullcycle-django:latest
