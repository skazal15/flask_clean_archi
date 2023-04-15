from config.db import db_session
from models.automatic import TabelKontrol
from sqlalchemy.exc import SQLAlchemyError
from util.logger import logger

class Automatic:
    def getAllData():
        print('get all')
        try:
            automatic = TabelKontrol.query.all()
            logger.info(automatic)
            print(automatic)
            return automatic
        except SQLAlchemyError as e:
            db_session.rollback()
            logger.info(e)
        finally:
            db_session.remove()
    
    def getSpecificBoardData(board):
        try:
            automatic = TabelKontrol.query.filter_by(board = board)
            return automatic
        finally:
            db_session.remove()

    def setState(board,gpio,state):
        try:
            automatic = TabelKontrol.query.filter_by(board = board,gpio = gpio)
            automatic.state = state
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            logger.info(e)
        finally:
            db_session.remove()