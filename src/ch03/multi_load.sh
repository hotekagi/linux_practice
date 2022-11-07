#!/bin/bash
MULTI_CPU=0
PROG_NAME=$0
SCRIPT_DIR=$(cd $(dirname $0) && pwd)

# multi_load.sh [options] [arg for concurrency]
# -m enable to use multi cpu
# examples: $ multi_load.sh 1 ; $ multi_load.sh -m 3

while getopts "m" OPT ; do
    case $OPT in
        m)
            MULTI_CPU=1
            ;;
    esac
done

shift $((OPTIND - 1))
CONCURRENCY=$1

if [ $MULTI_CPU -eq 0 ] ; then
    taskset -p -c 0 $$ > /dev/null
fi

for ((i=0;i<CONCURRENCY;i++)) do
    time "${SCRIPT_DIR}/loop.py" &
done

for ((i=0;i<CONCURRENCY;i++)) do
    wait
done