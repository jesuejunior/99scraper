from sqlalchemy.orm import relationship

__author__ = 'jesuejunior'
from sqlalchemy import Integer, Column, String, Float
import core


class Company(core.db.Model):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    rank = Column(Float, nullable=False)
    vacancy = Column(Integer, nullable=False)
    follows = Column(Integer, nullable=False)
    mission = Column(String, nullable=False)
    about = Column(String, nullable=False)
    path = Column(String)
    thumb = Column(String)

    # stats = relationship("Stats", uselist=False, backref="profile")

