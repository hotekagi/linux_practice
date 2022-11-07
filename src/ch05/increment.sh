#!/bin/bash
TMP=$(cat count.txt)
echo $((TMP + 1)) > count.txt
