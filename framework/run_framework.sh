#!/bin/bash

konsole -e "sudo ip netns exec nns1 python3 framework.py config_1.ini" &
konsole -e "sudo ip netns exec nns2 python3 framework.py config_2.ini" &
konsole -e "sudo ip netns exec nns3 python3 framework.py config_3.ini" &
konsole -e "sudo ip netns exec nns4 python3 framework.py config_4.ini" &
konsole -e "sudo ip netns exec nns5 python3 framework.py config_5.ini" &
konsole -e "sudo ip netns exec nns6 python3 framework.py config_6.ini" &
konsole -e "sudo ip netns exec nns7 python3 framework.py config_7.ini" &
konsole -e "sudo ip netns exec nns8 python3 framework.py config_8.ini" & 
konsole -e "sudo ip netns exec nns9 python3 framework.py config_9.ini" &
