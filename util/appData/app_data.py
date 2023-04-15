from util.aws_session import aws_session
from botocore.exceptions import ClientError

session =aws_session.initialize().client('ssm')

def getParamSSM(serviceName,Env,instance):
    name = f"/config/{serviceName}/{Env}/{instance}"
    
    try:
        response = session.get_parameters_by_path(Path=name,
                                            WithDecryption=True, Recursive=True)

    
    except ClientError as e:
        print(e)
        return False

    return response['Parameters']