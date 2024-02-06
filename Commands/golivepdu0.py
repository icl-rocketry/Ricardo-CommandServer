from CommandServer.commandserver import CommandServer
import time


@CommandServer.register('golivepdu0')
def golivepdu0(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":7,
                        "destination_service":2,
                        "command_id":2,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)