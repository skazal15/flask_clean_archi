from repository.automatic_repo import Automatic
from util.logger import logger

def getAllData():
    print('get')
    result = Automatic.getAllData()
    return result

def getSpecific(board):
    result = Automatic.getSpecificBoardData(board)
    return result

def updateState(board,gpio,state):
    Automatic.setState(board,gpio,state)

def postNewBoard(device,board,gpio,state,tipe,email):
    Automatic.addBoard(device,board,gpio,state,tipe,email)