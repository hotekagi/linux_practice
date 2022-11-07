#!/usr/bin/python3
import os
import sys
import mmap

PAGE_SIZE  = 4096

non_shared_data = 1000
shared_data = 1000
shared_memory = mmap.mmap(-1, PAGE_SIZE, flags=mmap.MAP_SHARED)
shared_memory[0:8] = shared_data.to_bytes(8, sys.byteorder)

print("*** 子プロセス生成前 ***")
print("非共有メモリ：", non_shared_data)
print("共有メモリ：", shared_data)
print()

pid = os.fork()
if pid < 0:
	print("fork()に失敗しました", file=os.stderr)
elif pid == 0:
	non_shared_data *= 2
	shared_data = int.from_bytes(shared_memory[0:8], sys.byteorder)
	shared_data *= 2
	shared_memory[0:8] = shared_data.to_bytes(8, sys.byteorder)

	print("*** 子プロセス ***")
	print("非共有メモリ：", non_shared_data)
	print("共有メモリ：", shared_data)
	print()
	sys.exit(0)

os.wait()
shared_data = int.from_bytes(shared_memory[0:8], sys.byteorder)
print("*** 子プロセス終了後 ***")
print("非共有メモリ：", non_shared_data)
print("共有メモリ：", shared_data)
