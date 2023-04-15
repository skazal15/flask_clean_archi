from repository.automatic_repo import Automatic
from util.logger import logger

def getAllData():
    print('get')
    result = []
    for data in Automatic.getAllData():
        result.append({
          'id':data.id,
          'device':data.device,
          'board':data.board,
          'gpio':data.gpio,
          'state':data.state,
          'type':data.type
        })
    return result