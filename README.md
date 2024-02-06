# Overview

Hello. This provides a command server to interract with the ricardo-backend. It provides two user interfaces, either a rest api served by flask, or a command line interface. A basic send_command_packet always exists. New commands are written in python using the `@CommandServer.register(command_name)` decorator and are automatically added as rest api endpoints and callable commands. Custom argparsers can be passed to. It communicates with the backend over socketio.

# Documentation
High level documentation is on the wiki (https://wiki.imperialrocketry.com/en/Electronics/Software/Ricardo-CommandServer).

# Running 
## Local
Install dependancies using the requirements.txt:
```
pip install -r requirements.txt
```

Run:

```
python ./main.py
```

Use the -h flag to see all available command line args.

## Docker
Docker file provided for running command server under docker.

# Testing 
WIP
