from sqlalchemy.orm import Session

from . import models, schemas, security


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.encrypt_password(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_phonetic_by_glyph(db: Session, glyph: str):
    return db.query(models.Phonetic).filter(models.Phonetic.glyph == glyph).first()

def get_glyph(db: Session, glyph: str):
    return db.query(models.Glyph).filter(models.Glyph.glyph == glyph).first()

