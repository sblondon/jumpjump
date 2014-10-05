#! /bin/sh

if [ "$#" -ne 1 ]; then
    env PYTHONPATH="." python2 ./src/run.py
else
    env PYTHONPATH="." python2 ./src/testlevel.py
fi

