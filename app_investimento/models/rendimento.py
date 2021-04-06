from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app_investimento.database.database import DeclarativeBase
from app_investimento.models.investimento import Investimento


class Rendimento(DeclarativeBase):
    __tablename__ = "rendimento"

    id = Column(Integer, primary_key=True)

    investimento_id = Column(Integer, ForeignKey("investimento.id"))
