#!/bin/bash
while : ; do
  if [ ! -e .lock ] ; then
    break
  fi
done
touch .lock
./increment.sh
rm -f .lock
