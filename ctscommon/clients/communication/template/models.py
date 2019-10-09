from pydantic import BaseModel
from typing import List
import datetime


class ITemplateVariable(BaseModel):
    name: str = None
    defaultValue: str = None
    required: bool = False


class ITemplate(BaseModel):
    uuid: str = None
    name: str = None
    slug: str = None
    variables: List[ITemplateVariable] = None


class INotification(BaseModel):
    template: str = None
    templateSlug: str = None
    sender: str = None
    senderName: str = None
    variables: object = None
    phone: List[str] = []
    emails: List[str] = []
    emailSubject: str = None
    emailCCs: str = None
    sentAt: datetime.date = None


class CreateITemplate(ITemplate):
    uuid: str = None
    name: str = None
    slug: str = None
    variables: List[ITemplateVariable] = None


class ITemplateUpdate(ITemplate):
    itemplate_id: int = None


class ITemplateDelete(ITemplate):
    itemplate_id: int = None


class ITemplateGet(ITemplate):
    uuid: str = None
    name: str = None
    slug: str = None
    variables: List[ITemplateVariable] = None
