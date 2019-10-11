from pydantic import BaseModel
from typing import List


class OfficePccBase(BaseModel):
    code: str
    booking: bool = False
    ticketing: bool = False


class OfficePccCreate(BaseModel):
    pccs: List[OfficePccBase] = []
