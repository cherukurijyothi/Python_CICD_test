from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    id: int
    name: str
    age: int
    grades: List[int] = []
