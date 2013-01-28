##TODO for week 4
1. review the FDD
2. understand mstp, rstp
3. write the rstp unit test cases
4. testing for the gap, and the function details.


##why use github for diary
1. the search function make it more easier to find what you need.

##3.1 I am learning linux
1. when I want delete two files, *openssl-fips-ecp-2.0.2* and *openssl-fips-ecp-2.0.2.tar.gz*, I want to delete them with one commnad, then I try a * after the same part of the two name, like **openssl-fips-ecp-2.0.2***

##4.1 learning record
###4.1.1 some port types in spanning tree protocol
1. when learning RSTP, it use the Uplink-fast feature in, I have read the Uplink-fast, the only thing here to study and learn effective is to call the Uplink-fast up. There is a alternate port in Uplink-fast, and what's the condition the alternate port change to root port? Can not remember that? and why when I reading that content, I have not pay enought attention to that?
2. remember the key topic, and the key things. not only the names, I should realise how to remember the key points.
3. the case, when read the RSTP, I can call the uplink-fast(something I have read in STP)
4. must make the tree model more clear, and think things in tree. the root bridge is a node, that means the tree root. and every bridge are all means nodes. mean where there is another way. and every line means the branch of the tree. every branch connect can connect up to two node. if it is the edge, it collcet to the host, and the host is just like the leaf. 
5. there are some ports in a spanning tree, the root port recieve things from upstream, the designated port going downstreams.
6. the block port, when the strange things happen, a node have several ways to the root, it must choose only one way to get there, so there must be some blocked ports. and when the topo begins, we want to do the fast reaction whent the topology changes, there is another port called **alternate** port.
7. what is the forwarding and listening, the root port is in forwarding status, the designated port also, the blocked port was not, the alternate port is not , but forwarding is a state, and the root, designated, alternate, bolcked port is a type. but there still stuff for me to do to understand the forwarding exactily.

###4.1.2 the election of root bridge this should be remember, and to varify.
1. there are some types of nodes, one is **root**, and **designated bridges** and some **edge node**.
2. why I always forget the election process. 
3. what should know about the root bridge, there is only one **root bridge** in a tree. the **root bridge** is not all the time, can modify. only the root bridge can send BPDUs. so at the beginning, because everyone thinks itself the root, they all send out the BPDUs, after the root was choose, there is only one root bridge, and only this bridge send out BPDUs.
4. because the root is the top, all other designated bridges' upstearm, so all the ports in the root bridge are all designated ports. they are all for downstreams.
5. **how many things need to selected and what vector needed for the selected?** need to pay attention to some infomations: 
    
    **root bridge ID** comprises the priority and the MAC address of the root bridege
    **root path cost** cost of the path to the root bridge
6. at the beginning, every one thinks itself the root, so 


