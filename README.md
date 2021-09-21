Test task for CFT
=================

### App running with docker 

Run in this directory:

```
docker-compose -f .\docker-compose.prod.yml build
docker-compose -f .\docker-compose.prod.yml up -d
```

The app will be running at http://localhost

### App running with python and npm

####You should have python and node installed

Run in this directory:
```
pip install -r requirements.txt
flask run
```
In other terminal:
```
cd frontend
npm install 
npm run dev
```
The app will be running at http://localhost:8080