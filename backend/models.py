from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from database import Base



class Match(Base):

    __tablename__ = "matches"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    api_match_id = Column(
        String,
        unique=True,
        index=True
    )


    league = Column(
        String
    )


    country = Column(
        String
    )


    home_team = Column(
        String
    )


    away_team = Column(
        String
    )


    status = Column(
        String
    )





class Signal(Base):

    __tablename__ = "signals"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    match = Column(
        String
    )


    market = Column(
        String
    )


    confidence = Column(
        Float
    )


    odds = Column(
        Float
    )


    result = Column(
        String,
        default="PENDING"
    )