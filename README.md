# Dev-Market
Simple app to gather developers and make it easy to find by skill and location.

# Backend
The backend is a Restful API built in Django Rest Framework. Database is sqlite3.

# Deploy
Create a ".env" file with:
```
SECRET_KEY=<key>
DEBUG=False
```

Run:
```
docker-compose build
docker-compose up -d
```
The application will be accessible on port 80.

# API
