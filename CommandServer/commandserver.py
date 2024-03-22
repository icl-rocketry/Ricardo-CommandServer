import socketio
import socket
import time
from cmd2 import Cmd2ArgumentParser
import threading
import logging
import copy

from pylibrnp import defaultpackets

from .commandserver_cli import CommandServerCLI 
from .commandserver_flask import CommandServerFlask

class CommandServer():

    _command_register = []

    def __init__(self,
                 backend_host:str='localhost',
                 backend_port:int=1337,
                 rest_port:int=1339,
                 verbose:bool=False,
                 nocli:bool=False,
                 noflask:bool=False,
                 enable_test:bool = False):
        self.sio = socketio.Client(logger=False,engineio_logger=False)
        self.backend_host = backend_host
        self.backend_port = backend_port
        self.rest_port = rest_port
        self.verbose = verbose
        self.nocli = nocli
        self.noflask = noflask
        self.enable_test = enable_test
        self.ip = self.__getIP__()

        self.source_service = 0

        self.flask_interface = CommandServerFlask(flaskport=self.rest_port,verbose=self.verbose)

        #manually register send command pakcet endpoints 
        CommandServerCLI.register_command(command_name='send_command_packet',parser=self.send_command_packet_ap,command_func=self.wrapped_send_command_packet)
        self.flask_interface.register_command(command_name='send_command_packet',command_func=self.wrapped_send_command_packet)
        #register all other endpoints
        self._register_endpoints()

        #initialize cli after to process the added member functions
        self.cli = CommandServerCLI()


    send_command_packet_ap = Cmd2ArgumentParser(description='send simple command packet')
    send_command_packet_ap.add_argument('--command_id',type=int,required=True)
    send_command_packet_ap.add_argument('--command_arg',type=int,required=True)
    send_command_packet_ap.add_argument('--source_service',type=int,required=True)
    send_command_packet_ap.add_argument('--destination_service',type=int,required=True)
    send_command_packet_ap.add_argument('--source',type=int,required=True)
    send_command_packet_ap.add_argument('--destination',type=int,required=True)
    def send_command_packet(self,args:dict):
        cmd_packet : defaultpackets.SimpleCommandPacket = defaultpackets.SimpleCommandPacket(command = int(args['command_id']), arg = int(args['command_arg']))
        cmd_packet.header.destination_service = int(args['destination_service'])
        cmd_packet.header.source_service = args['source_service']
        cmd_packet.header.source = int(args['source'])
        cmd_packet.header.destination = int(args['destination'])
        cmd_packet.header.packet_type = 0

        self.send_packet(cmd_packet.serialize())

        return True
    
    #wrapped send command packet function to allow event logging of command when send command packet fucntion is called through an endpoint
    def wrapped_send_command_packet(self,args:dict):
        self.__sendSystemEvent__("send_command_packet",args)
        return self.send_command_packet(args) #why does this return true????

    def send_packet(self,data:bytes):
        #if we want to make this multiprocessing safe, this is the only function which 'shares a resource' so deal with it here only
        self.sio.emit('send_data',{'data':data.hex()},namespace='/packet')

    def run(self):
        #try to connect to backend sio server
        if not self.enable_test:
            while True:
                try:
                    self.sio.connect('http://' + self.backend_host + ':' + str(self.backend_port) + '/',namespaces=['/','/packet','/system_events'])
                    break
                except socketio.exceptions.ConnectionError:
                    print('Server not found, attempting to reconnect!')
                    time.sleep(1)
        # self.flask_interface.run()
        if not self.nocli:
            cli_thread = threading.Thread(target=self.cli.run,daemon=True)
            cli_thread.start()
        
        if not self.noflask:
            self.flask_interface.run()
        

    def _register_endpoints(self):
        for entry in self._command_register:
            command_function = getattr(self,entry["name"])
            CommandServerCLI.register_command(command_name=entry["name"],parser=entry["argparse"],command_func=command_function)
            self.flask_interface.register_command(command_name=entry["name"],command_func=command_function)
    #register a new command with the approparite endpoints for flask and cli
    @classmethod
    def register(cls,command_name,argparse=None,command_func=None):
        #generate wrapper to register command
        def register_command(command_func):
            #create wrapper to wrap actual command, spawning the command function in a new thread as a deamon and 
            #passing the instance of the current class
            def command_function_wrapper(instance,args:dict):
                cls.__sendSystemEvent__(instance,command_name,args)
                t = threading.Thread(target=command_func,args=(instance,args,),daemon=True)
                t.start()
            #register this wrapped function as a member function of the current class
            setattr(cls,command_name,command_function_wrapper)
            #add command_name to commandList
            cls._command_register.append({"name":command_name,"argparse":argparse})
            #return a reference to this new member function for vibes
            return getattr(cls,command_name)
        
        #this allows the method to be used as a decorator as well as just a normal function
        if command_func is None:
            return register_command
        register_command(command_func)

    #broadcast command executed on system event channel
    def __sendSystemEvent__(self,command_name:str,command_args:dict):
        # filter out cmd2 specific keys in dict
        filtered_command_args =  {key: command_args[key] for key in command_args.keys() - {'cmd2_statement','cmd2_handler'}}
        event_msg:str = command_name + " exectued with the following arguments: " + str(repr(filtered_command_args))
        event = {
                "level":"info",
                "name":command_name + " Command",
                "msg":event_msg,
                "time":time.time_ns()*(1e-6), #conversion to milliseconds?? idk
                "source":{
                            "application":"Ricardo-CommandServer", #TODO maybe add versioning?
                            "ip":self.ip
                        }
                }
        try:
            self.sio.emit('forward_event',event,namespace='/system_events')
        except socketio.exceptions.BadNamespaceError:
            pass
        

    def __getIP__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('192.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP