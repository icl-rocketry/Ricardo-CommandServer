from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

oxvent_srv_blip_ap = Cmd2ArgumentParser()
oxvent_srv_blip_ap.add_argument('--duration',type=float,required=False,default=1)
oxvent_srv_blip_ap.add_argument('--open_position',type=int,required=False,default=180)
@CommandServer.register('oxvent_srv_blip',argparse=oxvent_srv_blip_ap)
def oxvent_srv_blip(instance,args):

    command_packet_args = {"source":1,
                           "source_service":instance.source_service,
                           "destination":103,
                           "destination_service":11,
                           "command_id":2,
                           "command_arg":args.get('open_position',180)}

    instance.send_command_packet(command_packet_args)
    time.sleep(args.get('duration',1))
    command_packet_args['command_arg'] = 0
    instance.send_command_packet(command_packet_args)

    return True