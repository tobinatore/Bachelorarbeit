#!/bin/bash

for i in 2 3 6 7 8
do
    cd "./$i/"
    konsole -e "ip netns exec nns$i python3 test_2.py" &
    cd ..
done

cd "./1/"
konsole --hold -e "ip netns exec nns1 bping -c 100 ipn:1.1 ipn:9.2" &
cd ..
cd "./9/"
konsole -e "ip netns exec nns1 bpecho ipn:9.2" &

