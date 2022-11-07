#!/usr/bin/python3
import os

print(f"これはプロセス：pid={os.getpid()}")
os.posix_spawn("/bin/echo", ["echo", f"pid={os.getpid()}　からこんにちは！"], {})
