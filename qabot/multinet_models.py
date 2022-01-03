from datetime import datetime
from sqlalchemy import Integer, BigInteger, SmallInteger, Float, Boolean, String, DateTime, Column

# We are importing SQL Alchemy's Enum column datatype as SQLEnum to avoid ambiguity + conflict with Python's Enum class type
from sqlalchemy import Enum as SQLEnum

from db import Base
from multinet_types import MultinetSorts, MultinetGenerality, MultinetDetermination, MultinetFacticity, MultinetVariability

class MultinetNode(Base):
    __tablename__ = "MultinetNodes"

    # Housekeeping data
    id = Column(BigInteger, primary_key=True)
    creation_time = Column(DateTime, nullable=False, default=datetime.now())

    # Ontological Sort
    sort = Column(SQLEnum(MultinetSorts), nullable=False, index=True)

    #
    # LAY Attributes
    ###########################################################################
    #- GENER
    generality = Column(SQLEnum(MultinetGenerality), nullable=True)
    #- REFER
    determination = Column(SQLEnum(MultinetDetermination), nullable=True)
    #- FACT
    facticity = Column(SQLEnum(MultinetFacticity), nullable=True)
    #- VARIA
    variability = Column(SQLEnum(MultinetVariability), nullable=True)
    #- QUANT
    quantification = Column(String(30), nullable=True)
    #- CARD
    ### NOTE: Cardinality can be an integer, or is an interval. The interval may have an upper and/or lower bound.
    cardinality_integer = Column(Integer, nullable=True)        # Cardinality is an exact integer (ie 1)
    cardinality_upper_bound = Column(Integer, nullable=True)    # Cardinality is upper bounded    (ie < 3)
    cardinality_lower_bound = Column(Integer, nullable=True)   # Cardinality is lower bounded    (ie > 0)
    #- ETYPE
    extensionality = Column(Integer, nullable=True)


    def validate_node(self):
        """Helper function to self-check that a node doesn't break any of Multinet's ontologies.
        Returns an empty string if the node is valid. Returns a string describing why the node is invalid if it is invalid."""
        if (cardinality_integer is not None) and ((cardinality_lower_bound is not None) or cardinality_upper_bound is not None):
            return "Invalid Node! Cardinality must either be an integer or an interval, cannot be both!"
        return ""