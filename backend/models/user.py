from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: Optional[datetime] = datetime.utcnow()
