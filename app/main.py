from typing import Annotated
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas, security
from .database import engine
from .services import get_db

models.Base.metadata.create_all(bind=engine)


tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Glyphs",
        "description": "Manage glyphs & phonetics.",
    },
]

app = FastAPI(
    title="Phonetics API",
    openapi_tags=tags_metadata
    )


@app.post("/user/", tags=["Users"], response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", tags=["Users"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", tags=["Users"], response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/login", tags=["Users"], response_model=schemas.Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, email=form_data.username)
    if (not user
            or not security.verify_password(
            form_data.password, user.hashed_password
            )):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/glyph", tags=["Glyphs"], response_model=list[schemas.Glyph])
def read_glyph(glyph: schemas.Glyph = Depends(), db: Session = Depends(get_db)):
    filters = {key: val for key, val in glyph if val is not None}
    if not filters:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Require at least one param"
            )
    db_glyph = crud.get_glyph(db, filters=filters)
    if db_glyph is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Glyph not found"
        )
    return db_glyph
