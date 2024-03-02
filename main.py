from CommandServer.commandserver import CommandServer
#ensure all commands defined in the external commands folder are imported so they are added to the command server
from Commands import * 

import argparse
import signal
import sys


ap = argparse.ArgumentParser()
ap.add_argument('--backend-host',help='ip of backend',default='localhost')
ap.add_argument('--backend-port',help='port of backend',type=int,default='1337')
ap.add_argument('--noflask',help='disable flask rest api',action='store_true',default=False)
ap.add_argument('--nocli',help='disable command line interface',action='store_true',default=False)
ap.add_argument('--flask_port',help='flask port',type=int,default=1339)
ap.add_argument('-v','--verbose',help='make thing printy printy',action='store_true',default=False)
ap.add_argument('--test',help='enable testmode, i.e disable sio client',action='store_true',default=False)
args = ap.parse_args()

def exitHandler(*args, **kwargs):
    # Exit process
    sys.exit()

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

