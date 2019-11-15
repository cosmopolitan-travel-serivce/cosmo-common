from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ctscommon.core.config import get_config
from ctscommon.data.mixins import BasicTableMixin


db_url = get_config("DATABASE_URL")
log_sql = get_config("LOG_SQL", False, bool)
pool_size = get_config("SQL_POOL_SIZE", 5, int)

engine = create_engine(db_url, pool_pre_ping=True, echo=log_sql, pool_size=pool_size)
Session = sessionmaker(bind=engine)
Base = declarative_base(cls=BasicTableMixin)
# Base = declarative_base()
