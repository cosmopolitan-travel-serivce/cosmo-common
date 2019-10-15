from pydantic import BaseModel
from typing import List
import datetime


class TemplateVariable(BaseModel):
    name: str = None
    default_value: str = None
    required: bool = False


class Template(BaseModel):
    uuid: str = None
    name: str = None
    slug: str = None
    variables: List[TemplateVariable] = None


class Notification(BaseModel):
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


class CreateTemplate(Template):
    uuid: str = None
    name: str = None
    slug: str = None
    variables: List[TemplateVariable] = None


class TemplateUpdate(Template):
    itemplate_id: int = None


class TemplateDelete(Template):
    itemplate_id: int = None


class TemplateGet(Template):
    uuid: str = None
    name: str = None
    slug: str = None
    variables: List[TemplateVariable] = None
