from repositories.user_repository import UserRepository
from schemas.user import UserCreate
from models.user import User
from core.security import get_password_hash, verify_password, create_access_token
from fastapi import HTTPException, status

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, data: UserCreate):
        if self.repo.get_by_username(data.username):
            raise HTTPException(status_code=400, detail="Username already registered")
        if self.repo.get_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_pwd = get_password_hash(data.password)
        user = User(
            username=data.username,
            email=data.email,
            hashed_password=hashed_pwd,
            role=data.role
        )
        return self.repo.create(user)

    def login(self, username: str, password: str):
        user = self.repo.get_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        token = create_access_token({"sub": user.username, "role": user.role.value})
        return {"access_token": token, "token_type": "bearer"}
