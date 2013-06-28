1.what is err disable.
when use a bpdu guard in a port, then also receive bpdu in the port. this port goes into errordisable.
there is a errerdisable recovery timer. after the timer, it will clear the port status. if agian revice a bpdu, keep checking the bpdu. if receive, go to errordisable.

2.what will edge port do
if an edge port recive a BPDU, remove the edge flag, start a 3 second timer.

3.the **cist root**         --> the lowest of all bridges.
the **cist regional root**  --> a boundary bridge(must), have the shortest path cost to the root.  &&& cist regional root becomes the root of the region.
if the cist regional root hear a shorter cist external root path cost in its internal region, it will relinquish it's role of **cist regional root**

4.the **cist external root path cost** not change in the region. only change when through the boundary.

5.the whole region will looks like a virtual bridge with bridge ID = **cist external root bridge ID**
and  a single root port elected int the **cist external root bridge**

6.**cst** connect all boundary switches, and perceives every region as a single virtual bridge.


7.CST这种架构能够使MSTP可以和IEEE STP/RSTP域协同工作.传统的交换机域将他们的STP实例与CST结合到一起,并且将MSTP域作为"透明"的虚拟桥,不去感知他们内部的拓扑.这样,链接到IEEE STP/RSTP域将扩展CST.MSTP通过在边界链路侦听外部信息来发现合适的STP版本,并且切换到相应的操作模式(例如:RSTP/STP).有可能发生这种情况:一个拥有最低的bridgeID的交换机属于RSTP/STP域.这种情况将导致所有的MSTP域选取本地的CIST域根,并且认为新的CIST根位于MSTP域外.

summary:第二层是由mst ist组成.每个region有最优的内部拓扑.并且使用cist regional root作为ist root.cst的拓扑改变可能影响ist拓扑,因为cist regional root可能改变.但是ist的拓扑改变一般不影响cst,除非域分裂了.

CIST的分层架构的第二层由众多的MSTP域IST组成.每个MSTP域使用内部路径开销建立IST实例,并且遵循最优(optimal)内部拓扑,使用CIST域根作为IST根.CST的变化可能影响所有域中的IST,因为这些变化可能导致新的CIST域根的选举(CIST域根就是IST根).域内的拓扑的变化一般不会影响CST,除非这些变化分裂了这个域.


将MSTI映射到CIST
MSTI在每个域中都是独立建立的,但是它们必须映射到CIST,在CIST的边界端口.这就意味着如果将VLAN映射不同的实例则不能在边界端口对VLAN流量进行负载分担.所有的VLAN使用相同的非阻塞边界端口,不管对于(with repect to)CIST根来说是上流还是下游.这个声明只在CST路径连接到域虚拟桥.在任何域中,VLAN遵循内部拓扑路径,基于相对应的MSTI配置.

summary:master port.msti对cist根不知情.他们只知道一个master端口,并且将这个端口作为关口.master端口只在所有的msti端口同步之后转发,这样是为了避免临时的环路.丢了一个并行的收敛特性.

MSTI完全不知晓CIST根;它们只是用域内路径以及域内MSTI根来建立生成树.然后所有的MSTP实例看得到CIST域根的根端口(通往CIST根的),并将它作为特殊的**管理**端口,这个端口将他们连接到CIST根桥.这个端口就类似于"网关"的功能,将MSTI连接到其他的域.(recall that)需要注意的是,交换机并将M-记录(MSTI信息)发送出域边界端口.只发送CIST信息.这样,CIST和MSTI能独立并且并行的(in parallel)收敛.**管理**端口为了避免临时环路,只会在相关的MSTI端口都同步了以后才进入转发状态.


##MSTP 多域的设计考虑

以太网的广播特性将导致错误在整个2层域中传播是为人所知的.这里有3个以太网影响MSTP设计的主要问题.

1.未知单播的泛滥导致了拓扑变化时候的流量突发.这是非对称路由或者持续的拓扑的变化.每个拓扑的变化将导致大量的无效的MAC地址以及单播流量泛滥.这是以太网拓扑未知导致的-网桥无法得知MAC地址的位置.

2.






