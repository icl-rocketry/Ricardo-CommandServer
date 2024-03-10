from CommandServer.commandserver import CommandServer

import argparse
import os
import sys
import importlib.util
import signal


ap = argparse.ArgumentParser()
ap.add_argument('-c','--commands',help='filepath to commands directory',type = str,default='./Commands/')
ap.add_argument('--backend-host',help='ip of backend',default='localhost')
ap.add_argument('--backend-port',help='port of backend',type=int,default='1337')
ap.add_argument('--noflask',help='disable flask rest api',action='store_true',default=False)
ap.add_argument('--nocli',help='disable command line interface',action='store_true',default=False)
ap.add_argument('--flask_port',help='flask port',type=int,default=1339)
ap.add_argument('-v','--verbose',help='make thing printy printy',action='store_true',default=False)
ap.add_argument('--test',help='enable testmode, i.e disable sio client',action='store_true',default=False)

args = ap.parse_args()

#import all commands from filepath
path = os.path.abspath(os.path.join(os.path.dirname(__file__), args.commands,'__init__.py')) #search for module from give file path
if not os.path.exists(path):
    print("Module path does not exist!")
    sys.exit(0)

try:
    spec = importlib.util.spec_from_file_location("_CommandsModule", path) # generate spec from path and generate new 
    _commands_module = importlib.util.module_from_spec(spec) #create module object
    sys.modules["_CommandsModule"] = _commands_module #add to sys modules
    spec.loader.exec_module(_commands_module) #execute module
    from _CommandsModule import * #import the custom module
except Exception as e:
    print (e)
    print('Error while importing command module!')
    sys.exit(0)

def exitHandler(*args, **kwargs):
    # Exit process
    sys.exit(0)

if __name__=='__main__':
    # Set signal handlers
    signal.signal(signal.SIGINT, exitHandler)
    signal.signal(signal.SIGTERM, exitHandler)

    cs = CommandServer(backend_host=args.backend_host,
                       backend_port=args.backend_port,
                       rest_port=args.flask_port,
                       verbose=args.verbose,
                       nocli=args.nocli,
                       noflask=args.noflask,
                       enable_test = args.test)
    cs.run()

