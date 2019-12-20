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
    customer: Optional[str] = None
    permissions: Optional[List[str]] = None
    managed_customers: Optional[List[str]] = None
    offices: Optional[List[str]] = None
    is_cts_staff: Optional[bool] = None
    is_agency_admin: Optional[bool] = None
    force_change_password = None
    impersonator: Optional[str] = None

    def is_impersonated(self):
        return self.impersonator is not None
