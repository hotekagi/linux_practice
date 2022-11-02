#!/usr/bin/python3
import os
import sys

ret = os.fork()

if ret == 0:
    print(f"これは子プロセス：pid={os.getpid()}，親プロセス：{os.getppid()}")
    os.execve("/bin/echo", ["echo", f"pid={os.getpid()}　からこんにちは！"], {})
    # unreachable
    # exit()
elif ret > 0:
    print(f"これは親プロセス：pid={os.getpid()}，子プロセス：{ret}")
    exit()

sys.exit(1)
