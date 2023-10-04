#!/bin/bash

# Generate the list of arguments
args=()

# Backend arguments
args+=(
    "--backend-host $RICARDO_COMMANDSERVER_BACKEND_HOST"
    "--backend-port $RICARDO_COMMANDSERVER_BACKEND_PORT"
)
# No Flask flag
if [[ $RICARDO_COMMANDSERVER_NOCLI == "TRUE" ]]; then
    args+=("--noflask")
fi
# No CLI flag
if [[ $RICARDO_COMMANDSERVER_NOFLASK == "TRUE" ]]; then
    args+=("--nocli")
fi
# Flask arguments
args+=("--flask_port $RICARDO_COMMANDSERVER_FLASK_PORT")
# Verbose flag
if [[ $RICARDO_COMMANDSERVER_VERBOSE == "TRUE" ]]; then
    args+=("--verbose")
fi
# Test flag
if [[ $RICARDO_COMMANDSERVER_TEST == "TRUE" ]]; then
    args+=("--test")
fi

# Convert argument array to string
args_str="${args[@]}"

# Print the arguments
echo "Ricardo Backend arguments:"
for arg in "${args[@]}"
do
   echo $arg
done

# Print start message
echo "Starting the Ricardo Command Server"

# Execute the Ricardo Command Server main file
python3 main.py $args_str

# Print exit message
echo "Ricardo Command Server exited"