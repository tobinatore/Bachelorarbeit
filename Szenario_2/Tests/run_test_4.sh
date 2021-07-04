#!/bin/bash

cd ..

for i in 6 29 4 1
do
    cd "./$i/"
    konsole --hold -e "ip netns exec nns$i python3 test_4.py" &
    cd ..
done
