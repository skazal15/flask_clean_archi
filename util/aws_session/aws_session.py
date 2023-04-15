import boto3
import param.s3 as param

def initialize():
    session = boto3.Session(
        region_name=param.AWS_REGION,
        #aws_access_key_id= param.id,
        #aws_secret_access_key= param.access
        #profile_name=param.PROFILE
    )
    return session