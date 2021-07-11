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
ip netns add nns10
ip netns add nns11
ip netns add nns12
ip netns add nns13
ip netns add nns14
ip netns add nns15
ip netns add nns16
ip netns add nns17
ip netns add nns18
ip netns add nns19
ip netns add nns20
ip netns add nns21
ip netns add nns22
ip netns add nns23
ip netns add nns24
ip netns add nns25
ip netns add nns26
ip netns add nns27
ip netns add nns28
ip netns add nns29
echo "Bringing loopback up..."
ip -all netns exec ip link set dev lo up
echo "Adding veth-interface..."
ip link add node-veth0 type veth peer name node-veth1 	#1->2
ip link add node-veth2 type veth peer name node-veth3 	#1->5
ip link add node-veth4 type veth peer name node-veth5 	#2->3
ip link add node-veth6 type veth peer name node-veth7 	#2->5
ip link add node-veth8 type veth peer name node-veth9 	#3->4
ip link add node-veth10 type veth peer name node-veth11	#4->5
ip link add node-veth12 type veth peer name node-veth13	#5->6
ip link add node-veth14 type veth peer name node-veth15	#6->7
ip link add node-veth16 type veth peer name node-veth17	#6->10
ip link add node-veth18 type veth peer name node-veth19	#6->11
ip link add node-veth20 type veth peer name node-veth21	#7->8
ip link add node-veth22 type veth peer name node-veth23	#7->10
ip link add node-veth24 type veth peer name node-veth25	#8->9
ip link add node-veth26 type veth peer name node-veth27	#8->10
ip link add node-veth28 type veth peer name node-veth29	#9->10
ip link add node-veth30 type veth peer name node-veth31	#11->12
ip link add node-veth32 type veth peer name node-veth33	#11->14
ip link add node-veth34 type veth peer name node-veth35	#11->25
ip link add node-veth36 type veth peer name node-veth37	#13->14
ip link add node-veth38 type veth peer name node-veth39	#14->17
ip link add node-veth40 type veth peer name node-veth41	#15->16
ip link add node-veth42 type veth peer name node-veth43	#16->17
ip link add node-veth44 type veth peer name node-veth45	#17->19
ip link add node-veth46 type veth peer name node-veth47	#18->19
ip link add node-veth48 type veth peer name node-veth49	#18->20
ip link add node-veth50 type veth peer name node-veth51	#19->20
ip link add node-veth52 type veth peer name node-veth53	#20->21
ip link add node-veth54 type veth peer name node-veth55	#21->22
ip link add node-veth56 type veth peer name node-veth57	#21->23
ip link add node-veth58 type veth peer name node-veth59	#22->23
ip link add node-veth60 type veth peer name node-veth61	#22->24
ip link add node-veth62 type veth peer name node-veth63	#23->26
ip link add node-veth64 type veth peer name node-veth65	#24->25
ip link add node-veth66 type veth peer name node-veth67	#25->26
ip link add node-veth68 type veth peer name node-veth69	#26->27
ip link add node-veth70 type veth peer name node-veth71	#26->28
ip link add node-veth72 type veth peer name node-veth73	#26->29

echo "Moving  interface to network namespaces..."
ip link set node-veth0 netns nns1
ip link set node-veth1 netns nns2
ip link set node-veth2 netns nns1
ip link set node-veth3 netns nns5
ip link set node-veth4 netns nns2
ip link set node-veth5 netns nns3
ip link set node-veth6 netns nns2
ip link set node-veth7 netns nns5
ip link set node-veth8 netns nns3
ip link set node-veth9 netns nns4
ip link set node-veth10 netns nns4
ip link set node-veth11 netns nns5
ip link set node-veth12 netns nns5
ip link set node-veth13 netns nns6
ip link set node-veth14 netns nns6
ip link set node-veth15 netns nns7
ip link set node-veth16 netns nns6
ip link set node-veth17 netns nns10
ip link set node-veth18 netns nns6
ip link set node-veth19 netns nns11
ip link set node-veth20 netns nns7
ip link set node-veth21 netns nns8
ip link set node-veth22 netns nns7
ip link set node-veth23 netns nns10
ip link set node-veth24 netns nns8
ip link set node-veth25 netns nns9
ip link set node-veth26 netns nns8
ip link set node-veth27 netns nns10
ip link set node-veth28 netns nns9
ip link set node-veth29 netns nns10
ip link set node-veth30 netns nns11
ip link set node-veth31 netns nns12
ip link set node-veth32 netns nns11
ip link set node-veth33 netns nns14
ip link set node-veth34 netns nns11
ip link set node-veth35 netns nns25
ip link set node-veth36 netns nns13
ip link set node-veth37 netns nns14
ip link set node-veth38 netns nns14
ip link set node-veth39 netns nns17
ip link set node-veth40 netns nns15
ip link set node-veth41 netns nns16
ip link set node-veth42 netns nns16
ip link set node-veth43 netns nns17
ip link set node-veth44 netns nns17
ip link set node-veth45 netns nns19
ip link set node-veth46 netns nns18
ip link set node-veth47 netns nns19
ip link set node-veth48 netns nns18
ip link set node-veth49 netns nns20
ip link set node-veth50 netns nns19
ip link set node-veth51 netns nns20
ip link set node-veth52 netns nns20
ip link set node-veth53 netns nns21
ip link set node-veth54 netns nns21
ip link set node-veth55 netns nns22
ip link set node-veth56 netns nns21
ip link set node-veth57 netns nns23
ip link set node-veth58 netns nns22
ip link set node-veth59 netns nns23
ip link set node-veth60 netns nns22
ip link set node-veth61 netns nns24
ip link set node-veth62 netns nns23
ip link set node-veth63 netns nns26
ip link set node-veth64 netns nns24
ip link set node-veth65 netns nns25
ip link set node-veth66 netns nns25
ip link set node-veth67 netns nns26
ip link set node-veth68 netns nns26
ip link set node-veth69 netns nns27
ip link set node-veth70 netns nns26
ip link set node-veth71 netns nns28
ip link set node-veth72 netns nns26
ip link set node-veth73 netns nns29

echo "Adding IP's..."
ip netns exec nns1 ip addr add 10.0.0.1/24 dev node-veth0
echo "veth0: 10.0.0.1"
ip netns exec nns2 ip addr add 10.0.0.2/24 dev node-veth1
echo "veth1: 10.0.0.2"
ip netns exec nns1 ip addr add 10.0.1.1/24 dev node-veth2
echo "veth2: 10.0.1.1"
ip netns exec nns5 ip addr add 10.0.1.2/24 dev node-veth3
echo "veth3: 10.0.1.2"
ip netns exec nns2 ip addr add 10.0.2.1/24 dev node-veth4
echo "veth4: 10.0.2.1"
ip netns exec nns3 ip addr add 10.0.2.2/24 dev node-veth5
echo "veth5: 10.0.2.2"
ip netns exec nns2 ip addr add 10.0.3.1/24 dev node-veth6
echo "veth6: 10.0.3.1"
ip netns exec nns5 ip addr add 10.0.3.2/24 dev node-veth7
echo "veth7: 10.0.3.2"
ip netns exec nns3 ip addr add 10.0.4.1/24 dev node-veth8
echo "veth8: 10.0.4.1"
ip netns exec nns4 ip addr add 10.0.4.2/24 dev node-veth9
echo "veth9: 10.0.4.2"
ip netns exec nns4 ip addr add 10.0.5.1/24 dev node-veth10
echo "veth10: 10.0.5.1"
ip netns exec nns5 ip addr add 10.0.5.2/24 dev node-veth11
echo "veth11: 10.0.5.2"
ip netns exec nns5 ip addr add 10.0.6.1/24 dev node-veth12
echo "veth12: 10.0.6.1"
ip netns exec nns6 ip addr add 10.0.6.2/24 dev node-veth13
echo "veth13: 10.0.6.2"
ip netns exec nns6 ip addr add 10.0.7.1/24 dev node-veth14
echo "veth14: 10.0.7.1"
ip netns exec nns7 ip addr add 10.0.7.2/24 dev node-veth15
echo "veth15: 10.0.7.2"
ip netns exec nns6 ip addr add 10.0.8.1/24 dev node-veth16
echo "veth16: 10.0.8.1"
ip netns exec nns10 ip addr add 10.0.8.2/24 dev node-veth17
echo "veth17: 10.0.8.2"
ip netns exec nns6 ip addr add 10.0.9.1/24 dev node-veth18
echo "veth18: 10.0.9.1"
ip netns exec nns11 ip addr add 10.0.9.2/24 dev node-veth19
echo "veth19: 10.0.9.2"
ip netns exec nns7 ip addr add 10.0.10.1/24 dev node-veth20
echo "veth20: 10.0.10.1"
ip netns exec nns8 ip addr add 10.0.10.2/24 dev node-veth21
echo "veth21: 10.0.10.2"
ip netns exec nns7 ip addr add 10.0.11.1/24 dev node-veth22
echo "veth22: 10.0.11.1"
ip netns exec nns10 ip addr add 10.0.11.2/24 dev node-veth23
echo "veth23: 10.0.11.2"
ip netns exec nns8 ip addr add 10.0.12.1/24 dev node-veth24
echo "veth24: 10.0.12.1"
ip netns exec nns9 ip addr add 10.0.12.2/24 dev node-veth25
echo "veth25: 10.0.12.2"
ip netns exec nns8 ip addr add 10.0.13.1/24 dev node-veth26
echo "veth26: 10.0.13.1"
ip netns exec nns10 ip addr add 10.0.13.2/24 dev node-veth27
echo "veth27: 10.0.13.2"
ip netns exec nns9 ip addr add 10.0.14.1/24 dev node-veth28
echo "veth28: 10.0.14.1"
ip netns exec nns10 ip addr add 10.0.14.2/24 dev node-veth29
echo "veth29: 10.0.14.2"
ip netns exec nns11 ip addr add 10.0.15.1/24 dev node-veth30
echo "veth30: 10.0.15.1"
ip netns exec nns12 ip addr add 10.0.15.2/24 dev node-veth31
echo "veth31: 10.0.15.2"
ip netns exec nns11 ip addr add 10.0.16.1/24 dev node-veth32
echo "veth32: 10.0.16.1"
ip netns exec nns14 ip addr add 10.0.16.2/24 dev node-veth33
echo "veth33: 10.0.16.2"
ip netns exec nns11 ip addr add 10.0.17.1/24 dev node-veth34
echo "veth34: 10.0.17.1"
ip netns exec nns25 ip addr add 10.0.17.2/24 dev node-veth35
echo "veth35: 10.0.17.2"
ip netns exec nns13 ip addr add 10.0.18.1/24 dev node-veth36
echo "veth36: 10.0.18.1"
ip netns exec nns14 ip addr add 10.0.18.2/24 dev node-veth37
echo "veth37: 10.0.18.2"
ip netns exec nns14 ip addr add 10.0.19.1/24 dev node-veth38
echo "veth38: 10.0.19.1"
ip netns exec nns17 ip addr add 10.0.19.2/24 dev node-veth39
echo "veth39: 10.0.19.2"
ip netns exec nns15 ip addr add 10.0.20.1/24 dev node-veth40
echo "veth40: 10.0.20.1"
ip netns exec nns16 ip addr add 10.0.20.2/24 dev node-veth41
echo "veth41: 10.0.20.2"
ip netns exec nns16 ip addr add 10.0.21.1/24 dev node-veth42
echo "veth42: 10.0.21.1"
ip netns exec nns17 ip addr add 10.0.21.2/24 dev node-veth43
echo "veth43: 10.0.21.2"
ip netns exec nns17 ip addr add 10.0.22.1/24 dev node-veth44
echo "veth44: 10.0.22.1"
ip netns exec nns19 ip addr add 10.0.22.2/24 dev node-veth45
echo "veth45: 10.0.22.2"
ip netns exec nns18 ip addr add 10.0.23.1/24 dev node-veth46
echo "veth46: 10.0.23.1"
ip netns exec nns19 ip addr add 10.0.23.2/24 dev node-veth47
echo "veth47: 10.0.23.2"
ip netns exec nns18 ip addr add 10.0.24.1/24 dev node-veth48
echo "veth48: 10.0.24.1"
ip netns exec nns20 ip addr add 10.0.24.2/24 dev node-veth49
echo "veth49: 10.0.24.2"
ip netns exec nns19 ip addr add 10.0.25.1/24 dev node-veth50
echo "veth50: 10.0.25.1"
ip netns exec nns20 ip addr add 10.0.25.2/24 dev node-veth51
echo "veth51: 10.0.25.2"
ip netns exec nns20 ip addr add 10.0.26.1/24 dev node-veth52
echo "veth52: 10.0.26.1"
ip netns exec nns21 ip addr add 10.0.26.2/24 dev node-veth53
echo "veth53: 10.0.26.2"
ip netns exec nns21 ip addr add 10.0.27.1/24 dev node-veth54
echo "veth54: 10.0.27.1"
ip netns exec nns22 ip addr add 10.0.27.2/24 dev node-veth55
echo "veth55: 10.0.27.2"
ip netns exec nns21 ip addr add 10.0.28.1/24 dev node-veth56
echo "veth56: 10.0.28.1"
ip netns exec nns23 ip addr add 10.0.28.2/24 dev node-veth57
echo "veth57: 10.0.28.2"
ip netns exec nns22 ip addr add 10.0.29.1/24 dev node-veth58
echo "veth58: 10.0.29.1"
ip netns exec nns23 ip addr add 10.0.29.2/24 dev node-veth59
echo "veth59: 10.0.29.2"
ip netns exec nns22 ip addr add 10.0.30.1/24 dev node-veth60
echo "veth60: 10.0.30.1"
ip netns exec nns24 ip addr add 10.0.30.2/24 dev node-veth61
echo "veth61: 10.0.30.2"
ip netns exec nns23 ip addr add 10.0.31.1/24 dev node-veth62
echo "veth62: 10.0.31.1"
ip netns exec nns26 ip addr add 10.0.31.2/24 dev node-veth63
echo "veth63: 10.0.31.2"
ip netns exec nns24 ip addr add 10.0.32.1/24 dev node-veth64
echo "veth64: 10.0.32.1"
ip netns exec nns25 ip addr add 10.0.32.2/24 dev node-veth65
echo "veth65: 10.0.32.2"
ip netns exec nns25 ip addr add 10.0.33.1/24 dev node-veth66
echo "veth66: 10.0.33.1"
ip netns exec nns26 ip addr add 10.0.33.2/24 dev node-veth67
echo "veth67: 10.0.33.2"
ip netns exec nns26 ip addr add 10.0.34.1/24 dev node-veth68
echo "veth68: 10.0.34.1"
ip netns exec nns27 ip addr add 10.0.34.2/24 dev node-veth69
echo "veth69: 10.0.34.2"
ip netns exec nns26 ip addr add 10.0.35.1/24 dev node-veth70
echo "veth70: 10.0.35.1"
ip netns exec nns28 ip addr add 10.0.35.2/24 dev node-veth71
echo "veth71: 10.0.35.2"
ip netns exec nns26 ip addr add 10.0.36.1/24 dev node-veth72
echo "veth72: 10.0.36.1"
ip netns exec nns29 ip addr add 10.0.36.2/24 dev node-veth73
echo "veth73: 10.0.36.2"

echo "Bringing veth up..."
ip netns exec nns1 ip link set dev node-veth0 up
ip netns exec nns2 ip link set dev node-veth1 up
ip netns exec nns1 ip link set dev node-veth2 up
ip netns exec nns5 ip link set dev node-veth3 up
ip netns exec nns2 ip link set dev node-veth4 up
ip netns exec nns3 ip link set dev node-veth5 up
ip netns exec nns2 ip link set dev node-veth6 up
ip netns exec nns5 ip link set dev node-veth7 up
ip netns exec nns3 ip link set dev node-veth8 up
ip netns exec nns4 ip link set dev node-veth9 up
ip netns exec nns4 ip link set dev node-veth10 up 
ip netns exec nns5 ip link set dev node-veth11 up
ip netns exec nns5 ip link set dev node-veth12 up
ip netns exec nns6 ip link set dev node-veth13 up
ip netns exec nns6 ip link set dev node-veth14 up
ip netns exec nns7 ip link set dev node-veth15 up
ip netns exec nns6 ip link set dev node-veth16 up
ip netns exec nns10 ip link set dev node-veth17 up 
ip netns exec nns6 ip link set dev node-veth18 up
ip netns exec nns11 ip link set dev node-veth19 up
ip netns exec nns7 ip link set dev node-veth20 up
ip netns exec nns8 ip link set dev node-veth21 up
ip netns exec nns7 ip link set dev node-veth22 up
ip netns exec nns10 ip link set dev node-veth23 up 
ip netns exec nns8 ip link set dev node-veth24 up
ip netns exec nns9 ip link set dev node-veth25 up
ip netns exec nns8 ip link set dev node-veth26 up
ip netns exec nns10 ip link set dev node-veth27 up
ip netns exec nns9 ip link set dev node-veth28 up
ip netns exec nns10 ip link set dev node-veth29 up
ip netns exec nns11 ip link set dev node-veth30 up
ip netns exec nns12 ip link set dev node-veth31 up
ip netns exec nns11 ip link set dev node-veth32 up
ip netns exec nns14 ip link set dev node-veth33 up
ip netns exec nns11 ip link set dev node-veth34 up
ip netns exec nns25 ip link set dev node-veth35 up
ip netns exec nns13 ip link set dev node-veth36 up
ip netns exec nns14 ip link set dev node-veth37 up
ip netns exec nns14 ip link set dev node-veth38 up
ip netns exec nns17 ip link set dev node-veth39 up
ip netns exec nns15 ip link set dev node-veth40 up
ip netns exec nns16 ip link set dev node-veth41 up
ip netns exec nns16 ip link set dev node-veth42 up
ip netns exec nns17 ip link set dev node-veth43 up
ip netns exec nns17 ip link set dev node-veth44 up
ip netns exec nns19 ip link set dev node-veth45 up
ip netns exec nns18 ip link set dev node-veth46 up
ip netns exec nns19 ip link set dev node-veth47 up
ip netns exec nns18 ip link set dev node-veth48 up
ip netns exec nns20 ip link set dev node-veth49 up
ip netns exec nns19 ip link set dev node-veth50 up
ip netns exec nns20 ip link set dev node-veth51 up
ip netns exec nns20 ip link set dev node-veth52 up
ip netns exec nns21 ip link set dev node-veth53 up
ip netns exec nns21 ip link set dev node-veth54 up
ip netns exec nns22 ip link set dev node-veth55 up
ip netns exec nns21 ip link set dev node-veth56 up
ip netns exec nns23 ip link set dev node-veth57 up
ip netns exec nns22 ip link set dev node-veth58 up
ip netns exec nns23 ip link set dev node-veth59 up
ip netns exec nns22 ip link set dev node-veth60 up
ip netns exec nns24 ip link set dev node-veth61 up
ip netns exec nns23 ip link set dev node-veth62 up
ip netns exec nns26 ip link set dev node-veth63 up
ip netns exec nns24 ip link set dev node-veth64 up
ip netns exec nns25 ip link set dev node-veth65 up
ip netns exec nns25 ip link set dev node-veth66 up
ip netns exec nns26 ip link set dev node-veth67 up
ip netns exec nns26 ip link set dev node-veth68 up
ip netns exec nns27 ip link set dev node-veth69 up
ip netns exec nns26 ip link set dev node-veth70 up
ip netns exec nns28 ip link set dev node-veth71 up
ip netns exec nns26 ip link set dev node-veth72 up
ip netns exec nns29 ip link set dev node-veth73 up

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
do
    ip netns exec nns$i sysctl -w net.ipv4.ip_forward=1
done

