from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Order(BaseModel):
    user_id: str
    account_ids: List[str]
    created_at: Optional[datetime] = datetime.utcnow()
