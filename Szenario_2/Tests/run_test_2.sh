#!/bin/bash

cd ..

for i in 2 3 4 7 8 9 10 12 13 15 16 18 19 20 21 22 24 27 28
do
    cd "./$i/"
    konsole --hold -e "ip netns exec nns$i python3 test_2.py" &
    cd ..
done

cd "./1/"
konsole --hold -e "ip netns exec nns1 bping -c 100 ipn:1.1 ipn:29.2" &
cd ..
cd "./29/"
konsole -e "ip netns exec nns29 bpecho ipn:29.2" &

