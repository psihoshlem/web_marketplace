from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

from functions.db_models import (
    engine,
)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)