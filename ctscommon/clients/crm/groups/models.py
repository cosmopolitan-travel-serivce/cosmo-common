from pydantic import BaseModel
from typing import List


class Group(BaseModel):
    code: str
    customers: List[str] = []


class GroupCreate(BaseModel):
    code: str
    customers: List[str] = []


class GroupUpdate(BaseModel):
    customers: List[str] = []


class GroupGet(BaseModel):
    code: str
    customers: List[str] = []


class GroupDelete(BaseModel):
    group_id: int
