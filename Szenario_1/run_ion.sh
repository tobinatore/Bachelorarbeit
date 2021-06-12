#!/bin/bash

for i in 1 2 3 4 5 6 7 8 9
do
    cd "./$i/"
    ip netns exec nns$i ionstart -I n"$i".rc &
    cd ..
    sleep 0.1
done
