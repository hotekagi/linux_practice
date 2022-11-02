#!/usr/bin/python3
import os
import sys

print(f"これはプロセス：pid={os.getpid()}")
os.posix_spawn("/bin/echo", ["echo", f"pid={os.getpid()}　からこんにちは！"], {})
