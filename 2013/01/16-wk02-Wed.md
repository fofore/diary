##the job
1.the first thing is why can't ping each other after I success runt the simulator in the centos.

**ping is not problem in mini-linux, so there must be some configuration problems. and because of the document is too old, the new one says should close the firewall, after disable all the filewall, the ping problem solved**

2.the mstpd process can't run in the mini-linux

**when use the shell script to run the mstpd process, there is nothing show, and after simple run it , it shows symbol md5 not found, after us command to find out where the symbol belong to, and copy the right lib into the right file, the problem fixed.**


##linuxlearn

###1.command mv
    
    mv source  destination

###2.command ldd 
**this command is about the lib, and that one thing I need to learn**

###3.how to link the lib there are some commands I used today:
**should pay attention to the line4 problem**

    ftpget 192.168.10.111 libcrypto.so.1.0.0
    mv libcrypto.so.1.0.0 /usr/lib/
    ln -s /usr/lib/libcrypto.so.1.0.0 /usr/lib/libcrypto.so.10
    rm /lib/libcrypto.so.10

###ps command 
**this command is about task, need to see the help infomation**
    
    ps -ux (when in the centos)
    ps (when in minilinux) 

###kill command 
**this command is used to kill a task int linux**
    
    kill [the task number]

##the work progress
I have finished how to run the newest the compiled zebos in mini-linux, and got the answer, why can't ping in centos,  why mstpd can't run in minilinux, next day job is to run the system in minilinux, to compare with cisco.

