## Simple CRUD app with Fastapi and Postgresql

### Create .env file with credentials
```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_SERVER=your_server
POSTGRES_PORT=your_port
POSTGRES_DB=your_db
SECRET_KEY=your_secret_key_for_token
```

### Run container
```
docker-compose -f docker-compose-dev.yml up
```
### Stop container
```
docker-compose -f docker-compose-dev.yml down
```
### Interactive API docs
http://0.0.0.0:8000/docs
<img width="1438" alt="スクリーンショット 2023-05-25 12 26 33" src="https://github.com/dimitori-g/fastapi-sample/assets/37291504/6acbdd7c-d695-415f-b177-d2759c1c5e55">
http://0.0.0.0:8000/redoc
<img width="1696" alt="スクリーンショット 2023-05-25 12 26 50" src="https://github.com/dimitori-g/fastapi-sample/assets/37291504/1ab493af-8c34-49d4-b2a9-2eadc9389ee3">

### Init venv
```
python3 -m venv venv
```
#### Activate venv
```
source venv/bin/activate
```
#### Deactivate venv
```
deactivate
```

### Install requirements
```
pip install -r requirements.txt
```

### Start dev server
```
uvicorn app.main:app --reload
```


