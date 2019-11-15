from ctscommon.data.database import Base
from ctscommon.data.mixins import AuditTableMixin, IdTableMixin
from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy_utils.types.choice import ChoiceType

from ctscommon.urls.schemas import HttpMethod


class UrlMapping(Base, IdTableMixin, AuditTableMixin):
    __table_args__ = (
        UniqueConstraint('url', 'method', 'service', name='ux_url_mapping_table_url_method_service'),
    )

    operation_id = Column(String(100), nullable=True)
    url = Column(String(100))
    name = Column(String(100))
    permissions = Column(String(255))
    method = Column(ChoiceType(HttpMethod))
    service = Column(String(50))
