#!/bin/bash

cd ..

for i in 6 9 8 1
do
    cd "./$i/"
    konsole -e "ip netns exec nns$i python3 test_4.py" &
    cd ..
done
