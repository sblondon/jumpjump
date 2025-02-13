#! /bin/sh

if [ "$#" -ne 1 ]; then
    env PYTHONPATH="." python3 ./src/run.py
else
    env PYTHONPATH="." python3 ./src/testlevel.py
fi

