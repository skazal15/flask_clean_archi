from config.db import db_session
from models.automatic import TabelKontrol,TableKontrolSchema
from sqlalchemy.exc import SQLAlchemyError
from util.logger import logger

class Automatic:
    def getAllData():
        try:
            session = db_session
            automatic = TabelKontrol.query.all()
            automatic_schema = TableKontrolSchema(many=True)
            result = automatic_schema.dump(automatic)
            logger.info(result)
            return result
        except SQLAlchemyError as e:
            session.rollback()
            logger.info(e)
        finally:
            session.remove()
    
    def getSpecificBoardData(board):
        try:
            session = db_session
            automatic = TabelKontrol.query.filter_by(board = board)
            automatic_schema = TableKontrolSchema(many=True)
            result = automatic_schema.dump(automatic)
            logger.info(result)
            return result
        except SQLAlchemyError as e:
            session.rollback()
            logger.info(e)
        finally:
            session.remove()

    def setState(board,gpio,state):
        try:
            session = db_session
            automatic = TabelKontrol.query.filter_by(board = board,gpio = gpio)
            automatic.state = state
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            logger.info(e)
        finally:
            session.remove()