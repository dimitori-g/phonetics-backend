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

### For example using TablePlus

https://github.com/dimitori-g/phonetics-backend/assets/37291504/7159dcb9-fd6b-4b3f-b6c1-ee6922142047


### Interactive API docs
http://0.0.0.0:8000/docs
![2b3b563a-22e0-4baa-ac33-4bacbdbe9c66](https://github.com/dimitori-g/phonetics-backend/assets/37291504/18c3562b-6b37-4e06-8007-4d6e1bbcb51d)


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


