from repository.automatic_repo import Automatic
from util.logger import logger

def getAllData():
    print('get')
    result = Automatic.getAllData()
    return result

def getSpecific(board):
    result = Automatic.getSpecificBoardData(board)
    return result