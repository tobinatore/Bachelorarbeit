#!/bin/bash

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
do
    cd "./$i/"
    ip netns exec nns$i ionstart -I n"$i"1.rc &
    cd ..
    sleep 0.1
done
