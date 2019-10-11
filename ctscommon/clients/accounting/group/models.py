from pydantic import BaseModel
from typing import List


class Group(BaseModel):
    code: str
    name: str = None
    customers: List[str] = []

class GroupCreate(BaseModel):
    code: str
    name: str = None
    customers: List[str] = []


class CustomerGet(BaseModel):
    interface_id: str
    cts_country: str


class GroupUpdate(BaseModel):
    name: str = None
    customers: List[str] = []

class GroupDelete(BaseModel):
    id: int = None

class GroupGet(BaseModel):
    code: str
    name: str = None
    customers: List[CustomerGet] = []