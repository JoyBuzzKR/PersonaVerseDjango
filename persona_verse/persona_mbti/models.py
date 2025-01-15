# myapp/beanie_models.py

from beanie import Document
from pydantic import Field
from typing import Optional
from datetime import datetime

class MyBeanieDocument(Document):
    """
    예시 Beanie Document
    - '_id' 필드는 자동 생성되며, ObjectId를 가짐
    """
    title: str = Field(...)
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "my_beanie_collection"  