#!/bin/bash

for i in 1 2 3 4 5 6 7 8 9
do	
    cp "../framework/framework.py" "./$i/"
    cd "./$i/"
    konsole --hold -e "ip netns exec nns$i python3 framework.py config_$i.ini" &
    cd ..
done
