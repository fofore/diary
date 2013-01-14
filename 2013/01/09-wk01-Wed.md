TODO:
1.Continue the compare job: 
    today, have no need to find out the diff between zebos commands and cisco nexes.
    read the cap excel files, find the detial diffs


2.How to use diff in VIM: 
    the tool used to compare two files, how to use diff in vim, or should I found another diff file, for checkin files.

3.Atuo checkin script: this can be done long time later, not so busy.
    Do i need to add script for checkin files, just to ensure not make any mistakes.

4.What the difference between catalyst and Nexus switch, and what zebos like, we use the Nexus to do the comparation job.

    the answer from internet:

    Other than FCoE, the major difference is L3 switching. The 5010 is a
    Layer2-only device and the 4900M can do routing. If you're trying to
    shave off microseconds, the 5010 will beat the 4900M in switching
    latency. On the other hand, the 4900M is modular and well suited for
    mixed, low-density 1gig/10gig deploymen


    The difference between Nexus and an normal Catalyst is the nexus is an cut-though switch where the catalyst is an store-and forward. we use Nexus for backup service.
    I can recommend using Nexus, it works fine, and it's fastere. The interface is a bit different but not much. I'll say you'll get it running real fast. 
        
    Basically the whole Nexus family is running a different OS (NX-OS) which
    is based on the MDS storage OS line.
    http://www.cisco.com/en/US/products/ps9372/index.html
    
    There are a few differences between Catalyst switches and Nexus
    switches.
    
    For example, Nexus supports vPC, which means that you have a
    multi-chassis EtherChannel trunk from a pair of Nexus 5000/7000
    distribution switches to any EtherChannel enabled access switch. This
    basically doubles the Access->Distribution bandwidth as you have no
    links blocked by Spanning Tree.
    
    Another major difference is the integration of Nexus 2000 Fabric
    Extenders with Nexus 5000 switches. The Nexus 2000 switches basically
    act as remote (over 10Gig fiber) "linecards" of the Nexus 5000. This
    allows deploying top of the rack switches without the additional
    management overhead:
    http://www.cisco.com/en/US/products/ps10110/index.html
        


Linuxlearn:
1.the telnet service in centos, 
problem describe: can't telnet centos after restart, it's OK yesterday.
figure out: add an iptables entire
    
    -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 23 -j ACCEPT

after this

    service iptables restart

additional infomation: maybe I use the port 22 yesterday, because is orginal in the iptables.

Tooluse:
putty check never. and the session will never end.

WorkTODO:
learn how to use gdb to debug.


betterlife:
research, the info is personal research, very good, what we do in before, not research but only view, to get, research is the duty of system team, here everybody do the research and discuss about in

