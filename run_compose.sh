docker-compose up -d --build

# make sure the postgres container is ready, then run migrations
sleep 5
docker exec django-car-db-api-1 python manage.py makemigrations 
docker exec django-car-db-api-1 python manage.py migrate

docker exec django-car-db-db-1 python manage.py migrate