from config.db import db_session
from models.automatic import TabelKontrol
from sqlalchemy.exc import SQLAlchemyError
from util.logger import logger

class Automatic:
    def getAllData():
        print('get all')
        session = db_session
        try:
            automatic = TabelKontrol.query.all()
            logger.info(automatic)
            print(automatic)
            return automatic
        except SQLAlchemyError as e:
            session.rollback()
            logger.info(e)
        finally:
            session.remove()
    
    def getSpecificBoardData(board):
        session = db_session
        try:
            automatic = TabelKontrol.query.filter_by(board = board)
            return automatic
        except SQLAlchemyError as e:
            session.rollback()
            logger.info(e)
        finally:
            session.remove()

    def setState(board,gpio,state):
        session = db_session
        try:
            automatic = TabelKontrol.query.filter_by(board = board,gpio = gpio)
            automatic.state = state
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            logger.info(e)
        finally:
            session.remove()