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
or
http://127.0.0.1:8000/redoc
