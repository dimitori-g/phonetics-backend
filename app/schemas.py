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


class Phonetic(BaseModel):
    id: int
    glyph: str
    phonetic: str
    class Config:
        orm_mode = True


class Glyph(BaseModel):
    id: int
    glyph: str
    pinyin: str
    cantonese: str
    on: str
    kun: str
    korean: str
    vietnamese: str
    class Config:
        orm_mode = True
