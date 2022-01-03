from datetime import datetime

from sqlalchemy import Integer, BigInteger, SmallInteger, Float, Boolean, String, DateTime, ForeignKey, Column
# We are importing SQL Alchemy's Enum column datatype as SQLEnum to avoid ambiguity + conflict with Python's Enum class type
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship

from db import Base
from multinet_types import MultinetSorts, MultinetGenerality, MultinetDetermination, MultinetFacticity, MultinetVariability, MultinetKType

class MultinetNode(Base):
    """Defines a node in the Multinet Semantic Network"""
    __tablename__ = "MultinetNodes"

    # Housekeeping data
    id = Column("id", BigInteger, primary_key=True)
    creation_time = Column("created_time", DateTime, nullable=False, default=datetime.now())

    # Ontological Sort
    #   Naming this column nodesort to avoid collision with SQL's "SORT" keyword
    sort = Column("nodesort", SQLEnum(MultinetSorts), nullable=False, index=True)

    #
    # LAY Attributes
    ###########################################################################
    #- GENER
    generality = Column("gener", SQLEnum(MultinetGenerality), nullable=True)
    #- REFER
    determination = Column("refer", SQLEnum(MultinetDetermination), nullable=True)
    #- FACT
    facticity = Column("fact", SQLEnum(MultinetFacticity), nullable=True)
    #- VARIA
    variability = Column("varia", SQLEnum(MultinetVariability), nullable=True)
    #- QUANT
    # TODO: quantification points to another node in the semantic network that is of the nn or nu sort
    quantification = Column("quant", String(30), nullable=True)
    #- CARD
    ### NOTE: Cardinality can be an integer, or is an interval. The interval may have an upper and/or lower bound.
    cardinality_integer = Column("card_int", Integer, nullable=True)          # Cardinality is an exact int   (ie 1)
    cardinality_upper_bound = Column("card_upper", Integer, nullable=True)    # Cardinality is upper bounded  (ie < 3)
    cardinality_lower_bound = Column("card_lower", Integer, nullable=True)    # Cardinality is lower bounded  (ie > 0)
    #- ETYPE
    extensionality = Column("exten", Integer, nullable=True)

    def has_layer_information(self):
        """Returns True if the node has Layer attributes/information."""
        return sort.is_ositl()

    def has_cardinality(self):
        """Returns True if the node has an cardinality attribute set."""
        return (cardinality_integer is not None) or (cardinality_lower_bound is not None) or (cardinality_upper_bound is not None)

    def carinality_string(self):
        """Returns a textual representation of the integer or interval cardinality, or an empty string if there is no cardinality set."""
        if cardinality_integer is not None:
            return str(cardinality_integer)
        elif (cardinality_lower_bound is not None) and (cardinality_upper_bound is not None):
            return str(cardinality_lower_bound) + " < " + str(cardinality_upper_bound)
        elif (cardinality_upper_bound is not None):
            return "< " + str(cardinality_upper_bound)
        elif (cardinality_lower_bound is not None):
            return str(cardinality_lower_bound) + " >"
        return ""

    def validate_node(self):
        """Helper function to self-check that a node doesn't break any of Multinet's ontologies.
        Returns an empty string if the node is valid. Returns a string describing why the node is invalid if it is invalid."""
        if (cardinality_integer is not None) and ((cardinality_lower_bound is not None) or cardinality_upper_bound is not None):
            return "Invalid Node! Cardinality must either be an integer or an interval, cannot be both!"
        if facticity is not None and not sort.is_ositl():
            return "Invalid Node! " + sort.name + " nodes cannot have FACT attribute!"
        if generality is not None and not sort.is_ositl():
            return "Invalid Node! " + sort.name + " nodes cannot have GENER attribute!"
        if quantification is not None and not sort.is_otl():
            return "Invalid Node! " + sort.name + " nodes cannot have QUANT attribute!"
        if determination is not None and not sort.is_otl():
            return "Invalid Node! " + sort.name + " nodes cannot have REFER attribute!"
        if has_cardinality() and not sort.is_otl():
            return "Invalid Node! " + sort.name + " nodes cannot have CARD attribute!"
        if extensionality is not None and not sort.is_otl():
            return "Invalid Node! " + sort.name + " nodes cannot have ETYPE attribute!"
        if variability is not None and not sort.is_otl():
            return "Invalid Node! " + sort.name + " nodes cannot have VARIA attribute!"

        return ""

class MultinetArc(Base):
    """Defines an arc/edge in the Multinet Semantic Network."""
    __tablename__ = "MultinetArcs"

    # Housekeeping data
    id = Column("id", BigInteger, primary_key=True)
    creation_time = Column("created_time", DateTime, nullable=False, default=datetime.now())

    start_node = Column("start_node", Integer, ForeignKey("MultinetNodes.id"), nullable=False)
    end_node = Column("end_node", Integer, ForeignKey("MultinetNodes.id"), nullable=False)

    relation = Column("relation", String(30), nullable=False)

    knowledge_type = Column("ktype", SQLEnum(MultinetKType), nullable=False)