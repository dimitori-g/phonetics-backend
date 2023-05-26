## Virtual environment
### Init
```
python3 -m venv venv
```

#### Activate
```
source venv/bin/activate
```

#### Deactivate
```
deactivate
```

## Install requirements
```
pip install -r requirements.txt
```

## Start dev server
```
uvicorn main:app --reload
```

## Interactive API docs
http://127.0.0.1:8000/docs
<img width="1438" alt="スクリーンショット 2023-05-25 12 26 33" src="https://github.com/dimitori-g/fastapi-sample/assets/37291504/6acbdd7c-d695-415f-b177-d2759c1c5e55">
http://127.0.0.1:8000/redoc
<img width="1696" alt="スクリーンショット 2023-05-25 12 26 50" src="https://github.com/dimitori-g/fastapi-sample/assets/37291504/1ab493af-8c34-49d4-b2a9-2eadc9389ee3">


## Using docker
### Create image
```
docker build -t fastapi .
```
### Run container
```
docker run -d --name fastapicontainer -p 80:80 fastapi
```