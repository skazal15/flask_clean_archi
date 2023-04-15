from botocore.exceptions import ClientError
import param.s3 as param
from util.aws_session import aws_session
import os

session = aws_session.initialize().client('s3')
Bucket = param.BUCKET



def UploadS3(fileName,batch,groupId):
    ObjectName = os.path.basename(fileName)
    S3_folder = f"ilumina/{groupId}/{batch}/{ObjectName}"
    try:
        session.upload_file(fileName,Bucket,S3_folder)
    except ClientError as e:
        print(e)
        return False
    return S3_folder
