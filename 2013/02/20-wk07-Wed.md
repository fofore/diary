##bring up the bingo
defaultenv
reset

setenv ipaddr 9.111.77.118
setenv netmask 255.255.255.0
setenv gatewayip 9.111.77.1
setenv serverip 9.111.86.13

tftp 2000000 qmm/BladeUboot-bingo
flimage 2000000

reset

setenv ipaddr 9.111.77.118
setenv netmask 255.255.255.0
setenv gatewayip 9.111.77.1
setenv serverip 9.111.86.13

tftp 2000000 qmm/BladeBoot-bingo
flimage 2000000

defaultenv
