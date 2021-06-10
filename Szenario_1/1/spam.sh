#!/bin/bash

ip netns exec nns1 bping -i 0.1 ipn:1.1 ipn:2.1 &
ip netns exec nns1 bping -i 0.1 ipn:1.2 ipn:2.1 &
ip netns exec nns1 bping -i 0.1 ipn:1.3 ipn:2.1 &
ip netns exec nns1 bping -i 0.1 ipn:1.4 ipn:2.1 &
ip netns exec nns1 bping -i 0.1 ipn:1.5 ipn:2.1 &
