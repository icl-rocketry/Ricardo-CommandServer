from CommandServer.commandserver import CommandServer
import time

@CommandServer.register('armpyroeng')
def armpyroeng(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":107,
<<<<<<< HEAD
<<<<<<< HEAD
                        "destination_service":12,
=======
                        "destination_service":10,
>>>>>>> 81c1bab (hotfire - 9/2/24 v1)
=======
                        "destination_service":12,
>>>>>>> eabd863 (Added More hotfire commands)
                        "command_id":3,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)