##the telnetd configuration

ifconfig eth0 9.111.77.118 netmask 255.255.255.0
route add default gw 9.111.77.1

mkdir /dev/pts
mount -t devpts devpts /dev/pts

mdev -s

telnetd -l /bin/sh

