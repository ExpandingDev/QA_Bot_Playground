import csv
from datetime import datetime
from sqlalchemy import Integer, BigInteger, Float, Boolean, String, DateTime, Column

from db import Base
from multinet_types import MultinetSorts

class MultinetNode(Base):
    __tablename__ = "MultinetNodes"

    id = Column(BigInteger, primary_key=True)

    type = Column(String(3), nullable=False)

    creation_time = Column(DateTime, nullable=False, default=datetime.now())