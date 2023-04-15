from util.appData import app_data
from param.database import HOST,DB_NAME,USER,PASSWORD

def dbParam(serviceName,env,instance):
    host = ''
    username=''
    password=''
    dbName = ''
    
    if env != 'dev':
        database_param = app_data.getParamSSM(serviceName,env,instance)
        for parameter in database_param:
            if parameter['Name'] == f"/config/{serviceName}/{env}/{instance}/host":
                host = parameter['Value']
            elif parameter['Name'] == f"/config/{serviceName}/{env}/{instance}/username":
                username = parameter['Value']
            elif parameter['Name'] == f"/config/{serviceName}/{env}/{instance}/password":
                password = parameter['Value']
            elif parameter['Name'] == f"/config/{serviceName}/{env}/{instance}/name":
                dbName = parameter['Value']

    if env == 'dev':
        host = HOST
        username=USER
        password=PASSWORD
        dbName = DB_NAME
    
    return host,username,password,dbName