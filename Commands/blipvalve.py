from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

blipvalve_ap = Cmd2ArgumentParser()
blipvalve_ap.add_argument('--destination',type=int,required=True)
blipvalve_ap.add_argument('--destination_service',type=int,required=True)
blipvalve_ap.add_argument('--duration',type=float,required=False,default=1)
blipvalve_ap.add_argument('--open_position',type=int,required=False,default=180)
@CommandServer.register('blipvalve',argparse=blipvalve_ap)
def blipvalve(instance,args):

    command_packet_args = {"destination":args['destination'],
                           "destination_service":args['destination_service'],
                           "source":1,
                           "source_service":2,
                           "command_id":2,
                           "command_arg":args.get('open_position',180)}

    instance.send_command_packet(command_packet_args)
    time.sleep(args.get('duration',1))
    command_packet_args['command_arg'] = 0
    instance.send_command_packet(command_packet_args)

    return True