#!/usr/bin/bash

if [ $# -ne 1 ]; then
    echo "Wrong number of arguments";
    exit -1;
fi

if [ -d $1 ]; then
    echo "Directory already exists";
    exit -2
fi

mkdir $1;
touch $1/input
cp starter.py $1/$1.py
chmod +x $1/$1.py
