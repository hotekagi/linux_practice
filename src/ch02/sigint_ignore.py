#!/usr/bin/python3
import os
import signal

print(f"pid={os.getpid()}")
signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    pass
