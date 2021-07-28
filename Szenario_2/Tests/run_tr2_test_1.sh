#!/bin/bash

cd ..

for i in 6 14 25 26 29
do
    cd "./$i/"
    konsole --hold -e "ip netns exec nns$i bpecho ipn:$i.2" &
    cd ..
    sleep 0.1
done
sleep 1
for x in 4 8 10 21
do

    cd "./$x/"
    
    if [[ $x == 4 ]]
    then
    	konsole --hold -e "ip netns exec nns4 bping -i 0.01 ipn:4.1 ipn:6.2" &
    elif [[ $x == 8 ]]
    then
    	konsole --hold -e "ip netns exec nns8 bping -i 0.01 ipn:8.1 ipn:14.2" &
    elif [[ $x == 10 ]]
    then
    	konsole --hold -e "ip netns exec nns10 bping -i 0.01 ipn:10.1 ipn:25.2" &
    elif [[ $x == 21 ]]
    then
    	konsole --hold -e "ip netns exec nns21 bping -i 0.01 ipn:21.1 ipn:26.2" &
    fi
    cd ..
    sleep 0.1
done
sleep 2
pwd
cd "./1/"
konsole --hold -e "ip netns exec nns1 bping -c 100 -i 1 ipn:1.1 ipn:29.2"

