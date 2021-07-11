#!/bin/bash

echo "Adding network namespaces..."
ip netns add nns1
ip netns add nns2
ip netns add nns3
ip netns add nns4
ip netns add nns5
ip netns add nns6
ip netns add nns7
ip netns add nns8
ip netns add nns9
echo "Bringing loopback up..."
ip -all netns exec ip link set dev lo up
echo "Adding veth-interface..."
ip link add node-veth0 type veth peer name node-veth1 	#n1->n2
ip link add node-veth2 type veth peer name node-veth3 	#n2->n3
ip link add node-veth4 type veth peer name node-veth5 	#n3->n4
ip link add node-veth6 type veth peer name node-veth7 	#n3->n5
ip link add node-veth8 type veth peer name node-veth9 	#n4->n6
ip link add node-veth10 type veth peer name node-veth11	#n5->n6
ip link add node-veth12 type veth peer name node-veth13	#n6->n7
ip link add node-veth14 type veth peer name node-veth15	#n7->n8
ip link add node-veth16 type veth peer name node-veth17	#n7->n9
echo "Moving  interface to network namespaces..."
ip link set node-veth0 netns nns1
ip link set node-veth1 netns nns2
ip link set node-veth2 netns nns2
ip link set node-veth3 netns nns3
ip link set node-veth4 netns nns3
ip link set node-veth6 netns nns3
ip link set node-veth5 netns nns4
ip link set node-veth8 netns nns4
ip link set node-veth7 netns nns5
ip link set node-veth10 netns nns5
ip link set node-veth9 netns nns6
ip link set node-veth11 netns nns6
ip link set node-veth12 netns nns6
ip link set node-veth13 netns nns7
ip link set node-veth14 netns nns7
ip link set node-veth16 netns nns7
ip link set node-veth15 netns nns8
ip link set node-veth17 netns nns9
echo "Adding IP's..."
ip netns exec nns1 ip addr add 10.0.0.1/24 dev node-veth0
echo "veth0: 10.0.0.1"
ip netns exec nns2 ip addr add 10.0.0.2/24 dev node-veth1
echo "veth1: 10.0.0.2"
ip netns exec nns2 ip addr add 10.0.1.1/24 dev node-veth2
echo "veth2: 10.0.1.1"
ip netns exec nns3 ip addr add 10.0.1.2/24 dev node-veth3
echo "veth3: 10.0.1.2"
ip netns exec nns3 ip addr add 10.0.2.1/24 dev node-veth4
echo "veth4: 10.0.2.1"
ip netns exec nns4 ip addr add 10.0.2.2/24 dev node-veth5
echo "veth5: 10.0.2.2"
ip netns exec nns3 ip addr add 10.0.3.1/24 dev node-veth6
echo "veth6: 10.0.3.1"
ip netns exec nns5 ip addr add 10.0.3.2/24 dev node-veth7
echo "veth7: 10.0.3.2"
ip netns exec nns4 ip addr add 10.0.4.1/24 dev node-veth8
echo "veth8: 10.0.4.1"
ip netns exec nns6 ip addr add 10.0.4.2/24 dev node-veth9
echo "veth9: 10.0.4.2"
ip netns exec nns5 ip addr add 10.0.5.1/24 dev node-veth10
echo "veth10: 10.0.5.1"
ip netns exec nns6 ip addr add 10.0.5.2/24 dev node-veth11
echo "veth11: 10.0.5.2"
ip netns exec nns6 ip addr add 10.0.6.1/24 dev node-veth12
echo "veth12: 10.0.6.1"
ip netns exec nns7 ip addr add 10.0.6.2/24 dev node-veth13
echo "veth13: 10.0.6.2"
ip netns exec nns7 ip addr add 10.0.7.1/24 dev node-veth14
echo "veth14: 10.0.7.1"
ip netns exec nns8 ip addr add 10.0.7.2/24 dev node-veth15
echo "veth15: 10.0.7.2"
ip netns exec nns7 ip addr add 10.0.8.1/24 dev node-veth16
echo "veth16: 10.0.8.1"
ip netns exec nns9 ip addr add 10.0.8.2/24 dev node-veth17
echo "veth17: 10.0.8.2"
echo "Bringing veth up..."
ip netns exec nns1 ip link set dev node-veth0 up
ip netns exec nns2 ip link set dev node-veth1 up
ip netns exec nns2 ip link set dev node-veth2 up
ip netns exec nns3 ip link set dev node-veth3 up
ip netns exec nns3 ip link set dev node-veth4 up
ip netns exec nns4 ip link set dev node-veth5 up
ip netns exec nns3 ip link set dev node-veth6 up
ip netns exec nns5 ip link set dev node-veth7 up
ip netns exec nns4 ip link set dev node-veth8 up
ip netns exec nns6 ip link set dev node-veth9 up
ip netns exec nns5 ip link set dev node-veth10 up
ip netns exec nns6 ip link set dev node-veth11 up
ip netns exec nns6 ip link set dev node-veth12 up
ip netns exec nns7 ip link set dev node-veth13 up
ip netns exec nns7 ip link set dev node-veth14 up
ip netns exec nns8 ip link set dev node-veth15 up
ip netns exec nns7 ip link set dev node-veth16 up
ip netns exec nns9 ip link set dev node-veth17 up

for i in 1 2 3 4 5 6 7 8 9
do
    ip netns exec nns$i sysctl -w net.ipv4.ip_forward=1
done

