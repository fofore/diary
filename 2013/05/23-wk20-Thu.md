1.the err-disable default value shows in the run-config


for STP part, here are the comments.

1.Row 11: no command can show the errdisable default recovery time. & if type "errdisable recovery interval 300" it also shows in the running-command.
  so there are two thing for IPI to verify, 1.is the default time realy 300?  	2.if it is 300, then "errdisable recovery interval 300" should not show up.
  this will be files a CSR.

2.Row 64: the default link-type is error. Now it is point-to-point. Because when we configure link-type to "auto", when show spanning-tree, it shows "auto"
  like this:
    (none)(config-if)#spanning-tree link-type auto 
    (none)(config-if)#do show span 
    Interface        Role Sts cost      priority  Type                            
    ---------------- ---- --- --------- --------- --------------------------------
    Ethernet40       Disb DSC 4         128       auto                             
    Ethernet52       Desg FWD 2         128       point-to-point          

3.Row 72: "spanning-tree mst port-priority" should not default value command.

4.Row 76: "spanning tree port-priority" when typed 128(default value) should not show in the 

5.forward delay follow 6.x

