from pydantic import BaseModel
from datetime import datetime
from typing import List
from ctscommon.clients.crm.pccs.models import PccGet


class OfficeBase(BaseModel):
    name: str = None
    address: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    telephone: str = None
    fax: str = None


class OfficeCreate(OfficeBase):
    code: str
    created_at: datetime = None
    created_by: str = None


class OfficeGet(OfficeBase):
    id: int
    code: str
    pccs: List[PccGet] = []
    created_at: datetime = None
    created_by: str = None
    updated_at: datetime = None
    updated_by: str = None


class OfficeFind(OfficeBase):
    id: int
    code: str
    created_at: datetime = None
    created_by: str = None
    updated_at: datetime = None
    updated_by: str = None


class OfficeUpdate(OfficeBase):
    updated_at: datetime = None
    updated_by: str = None
