#!/usr/bin/env bash -v
docker build -t linux_practice .
docker image prune -f
docker run -it --rm --name linux_practice linux_practice bash
