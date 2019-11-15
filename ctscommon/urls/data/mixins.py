from sqlalchemy import Integer, Column, String, DateTime, func
from sqlalchemy.ext.declarative import declared_attr

from auth.utils import SnakeNamingStrategy

naming_strategy = SnakeNamingStrategy()


def get_table_name(cls):
    """
        A get table name method.
        :return: the name of class transfomer to snack case
        """
    return naming_strategy.class_to_table_name(cls.__name__)
    # return cls.__name__.lower()


class BasicTableMixin(object):
    """
    A Basic table mixin.
    """
    @declared_attr
    def __tablename__(cls):
        """
        this methode call the get_table_name method
        :return: the table name
        """
        return get_table_name(cls)


class IdTableMixin(object):
    """
    An id table mixin.
    it is not to repeat the creation of the id in all the models
    class models must inherit it
    """
    id = Column(Integer, primary_key=True)


class AuditTableMixin(object):
    """
    An Audit table mixin.
    it is not to repeat the creation of the flowing name in all the models
    class models must inherit it
    """
    created_by = Column(String(30))
    updated_by = Column(String(30))
    created_at = Column(DateTime, default=func.now())
    last_updated = Column(DateTime)


class VersionedSchemaMixin(object):
    """
    This mixin will add a field to identify the current version of a schema. This will help to know if
    a given row from database benefits from a specified list of data migrations
    """
    schema_version = Column(Integer, default=0)

    @classmethod
    def current_schema_version(cls):
        return 0
