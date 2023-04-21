from config.db import db_session
from models.automatic import TabelKontrol,TableKontrolSchema
from sqlalchemy.exc import SQLAlchemyError
from util.logger import logger

class Automatic:
    def getAllData():
        try:
            db_session
            automatic = TabelKontrol.query.all()
            automatic_schema = TableKontrolSchema(many=True)
            result = automatic_schema.dump(automatic)
            logger.info(result)
            return result
        except SQLAlchemyError as e:
            db_session.rollback()
            logger.info(e)
        finally:
            db_session.remove()
    
    def getSpecificBoardData(board):
        try:
            db_session
            automatic = TabelKontrol.query.filter_by(board = board)
            automatic_schema = TableKontrolSchema(many=True)
            result = automatic_schema.dump(automatic)
            logger.info(result)
            return result
        except SQLAlchemyError as e:
            db_session.rollback()
            logger.info(e)
        finally:
            db_session.remove()

    def setState(board,gpio,state):
        try:
            db_session
            automatic = TabelKontrol.query.filter_by(board = board,gpio = gpio).first()
            automatic.state = state
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            logger.info(e)
        finally:
            db_session.remove()

    def addBoard(device,board,gpio,state,tipe,email):
        try:
            db_session
            automatic = TabelKontrol(device,board,gpio,state,tipe,email)
            db_session.add(automatic)
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            logger.info(e)
        finally:
            db_session.remove()

            