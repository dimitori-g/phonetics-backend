## API for phonetics

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
docker-compose up
```
### Stop container
```
docker-compose down
```
### Use data below for seeding DB

https://github.com/dimitori-g/phonetics-tools/blob/master/data/

### Interactive API docs
http://0.0.0.0:8000/docs
![screencapture-0-0-0-0-8000-docs-2023-06-29-17_03_48](https://github.com/dimitori-g/fastapi-sample/assets/37291504/29079542-6765-4820-8cd9-d04724cae1b6)

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


