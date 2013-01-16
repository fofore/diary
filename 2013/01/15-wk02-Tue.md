##Work projects
###I want to run the os that I compiled, and run ZebOS in it.
    
    1.I try to copy the modules into the mini-linux but it goes wrong, because the ZebOS use the linux modules, and the mini-linux's version is different from the centos that I used to build the ZebOS.
    2.As I only build the ZebOS, has no client and server commands, so I will try to copy these things into the ZebOS that I build in the centOS, and copy some centos to run the simulator.
    3.TODO one thing too verify what version the mini-linux use, and how can I make the new compiled file can run on it.
    

##linuxlearn
###ftp problem
when use the ftp to transfer files, there maybe some error happens, make sure the file size is the same in destination and target

###tar command
the tar command useage:

    for compress: tar czf [target] [source]
    for discompr: tar -xzf 
use tar packet can solve the wrong size transfer by ftp problem.

###the mv commad, change the file name 

###TODO
**should understand what the ko file is**

##zeboslearn
when I want to move the modules I compiled into the minilinux, there is a error message, shows the version was different, and I figured out by web that I should change the */include/linux/vermagic.h* for the words.

if I know what ko file is, and there is no need to build the new ko, because we don't ususally change the files that compiled into the ko file.

so next time, I only have to change the modules, and remember to use tar.gz file to transfer file, to ensure the right file.



##some commands
##As the mini-linux guide told:





    put authd
    put bgpd
    put dvmrpd
    put imi
    put imish
    put isisd
    put lacpd
    put mribd
    put mstpd
    put nsm
    put oamd
    put onmd
    put ospf6d
    put ospfd
    put pimd
    put ptpd
    put ripd
    put ripngd
    put rmond
    put run_client.sh
    put run_server.sh
    put run_zebos.sh
    put start.sh
    put switch-client
    put switch-server
    put topology.ini
    put update.sh
    put vlogd
    
    
    ftpget 192.168.10.111 authd
    ftpget 192.168.10.111 bgpd
    ftpget 192.168.10.111 dvmrpd
    ftpget 192.168.10.111 imi
    ftpget 192.168.10.111 imish
    ftpget 192.168.10.111 isisd
    ftpget 192.168.10.111 lacpd
    ftpget 192.168.10.111 mribd
    ftpget 192.168.10.111 mstpd
    ftpget 192.168.10.111 nsm
    ftpget 192.168.10.111 oamd
    ftpget 192.168.10.111 onmd
    ftpget 192.168.10.111 ospf6d
    ftpget 192.168.10.111 ospfd
    ftpget 192.168.10.111 pimd
    ftpget 192.168.10.111 ptpd
    ftpget 192.168.10.111 ripd
    ftpget 192.168.10.111 ripngd
    ftpget 192.168.10.111 rmond
    ftpget 192.168.10.111 run_client.sh
    ftpget 192.168.10.111 run_server.sh
    ftpget 192.168.10.111 run_zebos.sh
    ftpget 192.168.10.111 start.sh
    ftpget 192.168.10.111 switch-client
    ftpget 192.168.10.111 switch-server
    ftpget 192.168.10.111 topology.ini
    ftpget 192.168.10.111 update.sh
    ftpget 192.168.10.111 vlogd
    

    ftpput 192.168.10.111 authd
    ftpput 192.168.10.111 bgpd
    ftpput 192.168.10.111 dvmrpd
    ftpput 192.168.10.111 imi
    ftpput 192.168.10.111 imish
    ftpput 192.168.10.111 isisd
    ftpput 192.168.10.111 lacpd
    ftpput 192.168.10.111 mribd
    ftpput 192.168.10.111 mstpd
    ftpput 192.168.10.111 nsm
    ftpput 192.168.10.111 oamd
    ftpput 192.168.10.111 onmd
    ftpput 192.168.10.111 ospf6d
    ftpput 192.168.10.111 ospfd
    ftpput 192.168.10.111 pimd
    ftpput 192.168.10.111 ptpd
    ftpput 192.168.10.111 ripd
    ftpput 192.168.10.111 ripngd
    ftpput 192.168.10.111 rmond
    ftpput 192.168.10.111 run_client.sh
    ftpput 192.168.10.111 run_server.sh
    ftpput 192.168.10.111 run_zebos.sh
    ftpput 192.168.10.111 start.sh
    ftpput 192.168.10.111 switch-client
    ftpput 192.168.10.111 switch-server
    ftpput 192.168.10.111 topology.ini
    ftpput 192.168.10.111 update.sh
    ftpput 192.168.10.111 vlogd   
    ftpput 192.168.10.111 

    get run_client.sh
    get run_server.sh
    get run_zebos.sh
    get start.sh
    get switch-client
    get switch-server
    get topology.ini
