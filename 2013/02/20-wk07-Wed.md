##bring up the bingo

    defaultenv
    reset
    
    setenv ipaddr 9.111.77.119
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/gryphonr/BladeUboot-gryphon
    flimage 2000000
    
    reset
    
    setenv ipaddr 9.111.77.119
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/gryphonr/gryphon_ubi.img
    flimage 2000000
    
    defaultenv




    defaultenv
    reset
    
    setenv ipaddr 9.111.77.121
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/gryphonr/BladeUboot-gryphon
    flimage 2000000
    
    reset
    
    setenv ipaddr 9.111.77.121
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/gryphonr/gryphon_ubi.img
    flimage 2000000
    
    defaultenv

    defaultenv
    reset
    
    setenv ipaddr 9.111.77.130
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/gryphon/BladeUboot-gryphon
    flimage 2000000
    
    reset
    
    setenv ipaddr 9.111.77.130
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/gryphon/gryphon_ubi.img
    flimage 2000000



    defaultenv
    reset
    
    setenv ipaddr 9.111.77.118
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/bingo/BladeUboot-bingo
    flimage 2000000
    
    reset
    
    setenv ipaddr 9.111.77.118
    setenv netmask 255.255.255.0
    setenv gatewayip 9.111.77.1
    setenv serverip 9.111.86.13
    
    tftp 2000000 qmm/drop3/bingo/bingo_ubi.img
    flimage 2000000
