from sqlalchemy import Column,Integer,String,Enum,TIMESTAMP
from config.db import Base
from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import SQLAlchemyAutoSchema

ma =Marshmallow()

class TabelKontrol(Base):
    __tablename__ = 'tabel_kontrol'
    id = Column(Integer, primary_key=True)
    device = Column(String(20), nullable=False)
    board = Column(String(20), nullable=False)
    gpio = Column(Integer, nullable=False)
    state = Column(Integer, nullable=False)
    type = Column(Enum('Active High', 'Active Low'), nullable=False)
    logtime = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    email = Column(String(100),nullable=True)

    def __init__(self,device,board,gpio,state,type,email):
        self.device = device
        self.board = board
        self.gpio = gpio
        self.state = state
        self.type = type
        self.email = email

class TableKontrolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TabelKontrol