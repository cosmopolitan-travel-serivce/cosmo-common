from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class AuditableEntity:
    created_date: datetime
    created_by: str
    last_updated: datetime
    last_updated_by: str


class LogicalDelete:
    deleted: bool
    deleted_by: str
    deleted_date: datetime


class CTSUser(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    customer: Optional[bool] = None
    permissions: Optional[List[str]] = None
    managed_customers: Optional[List[str]] = None
