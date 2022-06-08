#!/bin/bash
#build cmd: docker build -t ecflow:latest .

docker run --rm -e DISPLAY=host.docker.internal:0 -P ecflow:latest