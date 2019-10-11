from pydantic import BaseModel
from typing import List
from datetime import datetime
from ctscommon.clients.crm.cards.models import CardGet


class TravelerBase(BaseModel):
    first_name: str = None
    last_name: str = None
    birth_date: str = None
    phone: str = None
    address: str = None
    origin_country: str = None
    destination_country: str = None
    email: str = None
    customer: int = None


class TravelerCreate(TravelerBase):
    cards: List[str] = []
    created_at: datetime = None
    created_by: str = None


class TravelerGet(TravelerBase):
    id: int
    card: List[CardGet] = []
    created_at: datetime = None
    created_by: str = None
    updated_at: datetime = None
    updated_by: str = None


class TravelerUpdate(TravelerBase):
    cards: List[str] = []
    updated_at: datetime = None
    updated_by: str = None
