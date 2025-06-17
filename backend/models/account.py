from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Account(BaseModel):
    user_id: str
    created_at: Optional[datetime] = datetime.utcnow()
