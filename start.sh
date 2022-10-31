#!/usr/bin/env bash -v

docker build -t linux_practice .
docker run -it --rm linux_practice bash
