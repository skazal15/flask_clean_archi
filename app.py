from flask import Flask
from flask_restful import Api,Resource,request
from flask_cors import CORS
from usecase.Automatic import getAllData,getSpecific
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
CORS(app)

#class AnalyticsList(Resource):
#    @swag_from({
#        'summary': 'Get analytics list',
#        'responses': {
#            '200': {
#                'description': 'List of analytics data',
#                'schema': {
#                    'type': 'array',
#                    'items': {
#                        'type': 'object',
#                        'properties': {
#                            'id': {
#                                'type': 'integer',
#                                'description': 'ID of the batch'
#                            },
#                            'batch': {
#                                'type': 'string',
#                                'description': 'Batch name'
#                            },
#                            'num_sample': {
#                                'type': 'integer',
#                                'description': 'Number of samples'
#                            },
#                            'email': {
#                                'type': 'string',
#                                'description': 'Email address'
#                            },
#                            'group_sample_id': {
#                                'type': 'string',
#                                'description': 'ID of the group sample'
#                            },
#                            'status': {
#                                'type': 'string',
#                                'description': 'Status of the batch'
#                            }
#                        }
#                    }
#                }
#            }
#        }
#    })
#    def get(self):
#        try:
#            data = getDataAnalytics()
#            return data,200
#        except:
#            return {"error get data"},500
#
#
#class UploadFile(Resource):
#    @swag_from({
#        'summary': 'Upload file',
#        'parameters': [
#            {
#                'name': 'email',
#                'in': 'path',
#                'description': 'Email address',
#                'type': 'string',
#                'required': True
#            },
#            {
#                'name': 'file',
#                'in': 'formData',
#                'description': 'File to upload',
#                'type': 'file',
#                'required': True
#            }
#        ],
#        'responses': {
#            '201': {
#                'description': 'File uploaded successfully'
#            },
#            '500': {
#                'description': 'Internal server error'
#            }
#        }
#    })
#    def post(self,email):
#        try:
#            file = request.files['file']
#            print(file)
#            uploadDataSample(email,file)
#            return {},201
#        except:
#            return {"error upload sample"},500
#
#
#class RunTask(Resource):
#    @swag_from({
#        'summary': 'runtask',
#        'parameters': [
#            {
#                'name': 'groupid',
#                'in': 'path',
#                'description': 'group id',
#                'type': 'string',
#                'required': True
#            },
#            {
#                'name': 'batch',
#                'in': 'body',
#                'description': 'batch sample',
#                'type': 'string',
#                'required': True
#            },
#            {
#                'name': 'sample',
#                'in': 'body',
#                'description': 'sample group',
#                'type': 'array',
#                'required': True
#            }
#        ],
#        'responses': {
#            '201': {
#                'description': 'File uploaded successfully'
#            },
#            '500': {
#                'description': 'Internal server error'
#            }
#        }
#    })
#    def post(self,groupid):
#        try:
#            request_data = request.json
#            batch = request_data['batch']
#            sample = request_data['sample']
#            runTask(groupid,batch,sample)
#            return {},200
#        except :
#            return {"error run task"},500
        
class HEALTH_CHECK(Resource):
    def get(self):
        try:
            return {'status':'ok'},200
        except:
            return {'status':'failed'},500
        

class GET_AUTOMATIC_DATA(Resource):
    def get(self):
        try:
            print('run auto')
            data = getAllData()
            print(data)
            return data,200
        except:
            return {"error get iot data"},500
        
class GET_SPECIFIC_BOARD(Resource):
    def get(self,board):
        try:
            print("run spec")
            data = getSpecific(board)
            print(data)
            return data,200
        except:
            return {"error get iot board data"},500
        
base_url = '/v1/miniilumina'
base_iot_url = '/v1/iot'
task_url = 'task'
health_url = 'health_check'

#api.add_resource(AnalyticsList,f'{base_url}/')
#api.add_resource(UploadFile,f'{base_url}/{task_url}/upload/<string:email>')
#api.add_resource(RunTask,f'{base_url}/{task_url}/run/<string:groupid>')
api.add_resource(GET_AUTOMATIC_DATA,f'{base_iot_url}/')
api.add_resource(HEALTH_CHECK,f'{base_iot_url}/{health_url}/')
api.add_resource(GET_SPECIFIC_BOARD,f'{base_iot_url}/<int:board>')

if __name__ == '__main__':
    app.run(port=5000,host="0.0.0.0")