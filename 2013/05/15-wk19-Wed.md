1.the mst configuration why added an exit in the runing configuration? is it accessable.

2.the name command

    Gry13(config-mst)#name $%^&*()$%^&UILPGIMODFGHJKL:ERTYUIOPERTYUIOPERTYUIOPWERTYUIOPWERTYUIOP
    Gry13(config-mst)#do show run
    !
    spanning-tree mst configuration
     instance 1 vlan 10-30
     name $%^&*()$%^&UILPGIMODFGHJKL:ERTYU
     exit
    
    must show the error message, but not just cut the name

    N3K(config-mst)# name TYUIOPFGHJKL:FGHJKL:TYUIOFGHJKL:NM<RTYUIFGHJKL
    ERROR: Configuration name has been truncated to 32 characters!



3.the instance command is error:

    instance 1 vlan 10-20,30-40-50-60-70-17
    and the no command, also have the range problem
    and this command's output is error. the show run confing is like this
    spanning-tree mst configuration
     instance 1 vlan 10-30
     name III
     exit
    must show error information, but not apply to the running configuratino with a error configuration.

4.do show must not return config mode, thus will apply the mst configuration, while the user just want show the last time configuration.

5.


