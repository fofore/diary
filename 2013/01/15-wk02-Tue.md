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

###TODO
    **should understand what the ko file is**


##zeboslearn
when I want to move the modules I compiled into the minilinux, there is a error message, shows the version was different, and I figured out by web that I should change the */include/linux/vermagic.h* for the words.

if I know what ko file is, and there is no need to build the new ko, because we don't ususally change the files that compiled into the ko file.

so next time, I only have to change the modules, and remember to use tar.gz file to transfer file, to ensure the right file.


