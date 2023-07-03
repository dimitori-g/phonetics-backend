from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class Glyph(BaseModel):
    id: int | None = None
    glyph: str | None = None
    phonetic: str | None = None
    pinyin: str | None = None
    cantonese: str | None = None
    on: str | None = None
    kun: str | None = None
    korean: str | None = None
    vietnamese: str | None = None
    class Config:
        orm_mode = True
