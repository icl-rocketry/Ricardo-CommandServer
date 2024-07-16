from CommandServer.commandserver import CommandServer

@CommandServer.register('armservo_cosmos')
def armservo_cosmos(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":104,
                        "destination_service": 10,
                        "command_id":3,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)