# Overview

Hello. This provides a command server to interract with the ricardo-backend. It provides two user interfaces, either a rest api served by flask, or a command line interface. A basic send_command_packet always exists. New commands are written in python using the `@CommandServer.register(command_name)` decorator and are automatically added as rest api endpoints and callable commands. Custom argparsers can be passed to. It communicates with the backend over socketio.

# Documentation
High level documentation is on the wiki (https://wiki.imperialrocketry.com/en/Electronics/Software/Ricardo-CommandServer).

# Configuration
Using the -c flag the Commands folder can be relocated to another location.
```
python ./main.py -c ../externalCommandFolder/
```
The external commands folder must be a valid python module and all the command python scripts must be added to the \__all\__ variable. Easiest way is to copy the existing \__init\__.py located inside Commands.

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
