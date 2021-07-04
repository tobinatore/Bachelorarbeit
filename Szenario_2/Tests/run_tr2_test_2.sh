#!/bin/bash

cd ..

for i in 4 6 8 10 14 21 25 26 29 1
do
    cd "./$i/"
    konsole --hold -e "ip netns exec nns$i python3 tr2_test_2.py" &
    cd ..
    sleep 0.1
done

