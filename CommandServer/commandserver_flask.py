from flask import Flask, request, Response, jsonify
import flask_cors

import eventlet
from eventlet import wsgi


class CommandServerFlask():
    def __init__(self,flaskhost:str = "0.0.0.0",flaskport:int=1337,verbose:bool=False):
        self.app = Flask(__name__)
        flask_cors.CORS(self.app, resources={r"/api/*": {"origins": "*"}})
        # self.app.config['DEBUG'] = False
        self.flaskhost = flaskhost
        self.flaskport = flaskport
        self.verbose = verbose
        self.api_prefix = '/api/'

    def run(self):
        wsgi.server(eventlet.listen((self.flaskhost,self.flaskport)),self.app)
        # self.app.run(host=self.flaskhost,port=self.flaskport,debug=self.verbose,use_reloader=False)
        
    def register_command(self,command_name:str = None, command_func = None):
     
        if command_name is None: 
            raise Exception('command_name cannot be empty')
        
        if command_func is None: 
            raise Exception('command_func cannot be empty')
        
        def wrapper():
            res = Response()
            res.headers['Access-Control-Allow-Credentials'] = 'true'

            if request.method == "OPTIONS":
                return res,200

            data = request.json
            if data is None:
                print('bad')
                res.data = 'Bad Request'
                return res,400
            
            command_func(data)
            res.data = 'OK'
            return res,200
    

        self.app.add_url_rule(self.api_prefix + command_name,endpoint=command_name,view_func=wrapper,methods=['POST','OPTIONS'])