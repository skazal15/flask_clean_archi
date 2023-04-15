from sqlalchemy import Column,Integer,String,Enum,TIMESTAMP
from config.db import Base

class TabelKontrol(Base):
    __tablename__ = 'tabel_kontrol'
    id = Column(Integer, primary_key=True)
    device = Column(String(20), nullable=False)
    board = Column(String(20), nullable=False)
    gpio = Column(Integer, nullable=False)
    state = Column(Integer, nullable=False)
    type = Column(Enum('Active High', 'Active Low'), nullable=False)
    logtime = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    def __init__(self,device,board,gpio,state,type,logtime):
        self.device = device
        self.board = board
        self.gpio = gpio
        self.state = state
        self.tipe = type
        self.logtime = logtime
