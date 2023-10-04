# Argument for base image (default: slim)
ARG BASEIMAGE="debian-slim"

## Base image using Debian
FROM python:3.10 as debian

# Update/upgrade packages
RUN apt-get update && apt-get upgrade -y

## Base image using slim Debian
FROM python:3.10-slim as debian-slim

# Update/upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install git
RUN apt-get install git -y

## Ricardo-CommandServer image
FROM $BASEIMAGE

# Create command server directory
RUN mkdir /ricardo-commandserver

# Move to command server directory
WORKDIR /ricardo-commandserver

# Copy Python requirements file to allow for caching of the pip3 install command
COPY ./requirements.txt ./requirements.txt

# Install Python requirements
RUN pip3 install -r ./requirements.txt

# Copy command server files
COPY ./external ./external
COPY ./Commands ./Commands
COPY ./CommandServer ./CommandServer
COPY ./main.py ./main.py
COPY ./RicardoCommandServer.sh ./RicardoCommandServer.sh

# Make the backend script executable
RUN chmod +x ./RicardoCommandServer.sh

# Set default values for environment variables
ENV RICARDO_COMMANDSERVER_BACKEND_HOST=localhost
ENV RICARDO_COMMANDSERVER_BACKEND_PORT=1337
ENV RICARDO_COMMANDSERVER_NOFLASK=FALSE
ENV RICARDO_COMMANDSERVER_NOCLI=FALSE
ENV RICARDO_COMMANDSERVER_FLASK_PORT=1339
ENV RICARDO_COMMANDSERVER_VERBOSE=FALSE
ENV RICARDO_COMMANDSERVER_TEST=FALSE

# Run command server script
ENTRYPOINT [ "bash", "RicardoCommandServer.sh" ]
