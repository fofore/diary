1.把工作当作实现价值的过程。2.品味成长中点滴进步。3.从成功中获得满足和快感。4.体会人际关系的真挚情谊。5.有节律地安排生活与工作。6.倾心做好每一件事。7.分享团队的努力与成就。8.珍惜每次合作机会。9.不忘闲情逸致。10.忘掉烦恼，把心事交给清风。


教育应该是这样：被传授的知识应该被当成宝贵的礼物，而不是沉重的任务。


1.when rapid-pvst in vlan 2 and tagged. then rstp is webos will be in FWD DESG and port in N3K is in FWD DESG.
2.see the bpdu that webos received:
before:
vlan 1中发送的bdpu type2 

    Cisco-N3K(config-if)# switchport access vlan 2
    Cisco-N3K(config-if)# show run2013 Apr 18 14:23:28.323336 stp: RSTP(2): transmitting RSTP BPDU on Ethernet1/26
    2013 Apr 18 14:23:28.323428 stp: vb_vlan_shim_send_bpdu(1981): VDC 1 Vlan 2 port Ethernet1/26 enc_type 2 len 36

vlan 2 trunk中发送 bpdu type1
带了tag的发送bpdu1格式为1
    
    Cisco-N3K(config-if)# 2013 Apr 18 14:22:08.323340 stp: RSTP(2): transmitting RSTP BPDU on Ethernet1/26
    2013 Apr 18 14:22:08.323439 stp: vb_vlan_shim_send_bpdu(1981): VDC 1 Vlan 2 port Ethernet1/26 enc_type 1 len 42


当为带tag时候,webos上抓不到bpdu报文,可能是debug命令不认识这个报文,就没有debug显示出来,只能在cisco上通过bpdu_tx来查看.


2.need default forward time
need default hello time
port can not be in new instance 

