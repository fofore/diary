
1.广播和组播的泛洪.这是个独立的问题,是由于很多核心协议(ARP,IGP,PIM)协议都依赖广播或组播.这些报文应该发给广播域中的每个节点.在负载量大的网络(intense load network)中每个点都有可能变得拥挤.

2.生成树收敛. MSTP使用RSTP流程进行生成树的重新协商.因为这是基于距离矢量的行为,这样就倾向于一些收敛问题,例如计数到无穷大(老旧信息循环).这种情况尤其在有10个以上交换机的环境中更为突出,表现为选根桥失败.


MSTP域的概念允许边界STP的重计算.既然每个域中的MSTI是独立的,每个单个域中影响MSTI的变化不会影响其他域中的MSTI.这是M-Rocord不会在域间交换的一个直接的结果.然而,CIST重计算影响每个域而且可能会比较慢的收敛.这就是为什么不要将任何VLAN映射到CIST并且避免将MSTP域连接到IEEE STP域.

summary:mstp拓扑变化和stp一样,只有非edge口状态变化为forwarding才会有拓扑变化消息.

MSTP和RSTP用同样的方式处理(be treated)拓扑变化的.这就是,只有非edge链路转为转发状态才会引起一个拓扑变化并且检测到变化的交换机将会把消息泛洪到整个域.然而,单个的物理链路可能对于某个MSTI是转发,而对另一个是阻塞.这样,单独的物理链路的变化会对MSTI和CIST有不同的影响.MSTI的拓扑变化是绑定到单个的域的,而CIST的拓扑变化是传播(propagate)到所有的域的.每个域都把来自其他域的拓扑变化通知当做"外部的"来处理并且只把他们应用到CIST相关的端口.


CST(链接虚拟交换机的生成树)的拓扑变化会影响所有的域中的MSTI以及CIST.这是由于虚拟交换机的新的链路变为转发状态(这才是拓扑变换)有可能改变拓扑中的所有路径,这样就需要大量(massive)的MAC地址的重新学习.因此,从拓扑变化的观点来说,CST的事件对内部链接的MSTP会有最大的影响的泛洪.

**需要记住的是:拓扑变化==新的非edge链路转化为forward状态**

以上的观察(observation)建议了一个对MSTP网络来说的好的设计原则-在自己的域中分开的"互联"拓扑,以及互联的域使用"星形"互联,牢记(keep in mind)把冗余和拓扑变化的效应平衡好.这里有一个众所周知的适配形式:将复杂系统从复杂系统中分立开来,用来保持网络更健壮以及能够将错误域孤立开来.另外(in addtion),将大把的链路暴露在CST中将降低负载平衡的选择,因为CST只支持一个STP实例.你想避免设计成下面这个图这样的,这个图在CST中使用互联的链路有效的禁止了负载平衡.这是因为现在链路的全互联属于CST,同时它只在两个域间选举了一个非阻塞的路径.


尽管域划分(partition)提供了更好的错误孤立,但是它任然不能消除(eliminate)周知的以太网问题,比如单播和广播的泛洪.这些任然会发生并且破坏(disrupt)了网络的链接性.例如:单播泛洪可能由于单向的(undirectional)流量引起,广播泛洪可能是根失效时短暂的(transient)桥环路的结果.暂时的桥环路是RSTP/MSTP的现实问题,尤其是在大的拓扑情况下,由于不同的同步问题导致了计数到无穷大.这个问题在尤其危险,当一个桥崩溃同时现有的拓扑存在环路,旧的信息可能继续流通(circulate)直到它的寿命超过了使用跳数的计数(计数到了无穷大).





##hive环境
对于编译的问题,因为lua是自己编译的,名字也是liblua.a 而不是liblua52.a
所以无法找到,修改cygwin的sh的lb_library_path可以修正在cygwin的shell中的问题
在eclipe中,直接调用的gcc,没有shell的环境变量,在win中修改也不行,只能在makefile中指定路径-L(path)这样,所以一直找不到lua52,可以增加到usr/local/lib中找,因为编译出来是在那里的.

##为何丢弃mingw
因为不能完全的模拟linux,要做到同样的代码,即能在linux中,又能在win中,mingw做不到,这样就需要编译宏.比如socket就不能用,为了就是完全模拟linux,就是学习linux编程,所以要丢弃mingw,而是用cygwin,为了使eclipse能看到cygwin的编译环境,需要将make所在的目录放到path中,那样eclipse才能找到build tool chain,否则发现不了的.





##Caveates in MSTP region   MSTP设计的注意事项

这里会有一些问题,由于这个事实-生成树实例没有被映射(一个一个的)到VLAN.使用PVST,剪裁一个VLAN在一个链路上,会同样禁止相应的STP在同样的链路上.既然MSTI脱离(decouple)VLAN,每个MSTI都跑在每个link上(域中的).这个在MSTI实例之间,差异在-他们做决定让哪条链路转发或者阻塞.通过剪裁(prune)VLAN,你可以终止于一个情形-VLAN没有使能在链路-(这些链路:相应的MSTI是转发或者使能,相应的MSTI阻塞). 考虑下面的例子用于解释这个想法.


在这个拓扑中,VLAN被手动的剪裁了-在trunk中.TODO由于这个过滤是不符合相应(respective)的MSTI阻塞决定,VLAN2的流量是被阻塞了,在SW1和SW2之间.为了避免这种情况,不要用静态的"VLAN"剪裁方法-分配VLAN跨越trunk,当你有MSTP使能.一种情况相同于这个(描述的)就是当端口连接交换机是**接入(access)端口**.MSTP跑在这些端口上,并且有逻辑拓扑-可能是阻塞或者转发-在端口上.取决于VLAN到MSTI的映射,一个给定的VLAN可能被阻塞在接入端口-由于MSTP决定,尽管这个接入VLAN是不同的,他们使用相同的STP.为了避免这个问题,不要跑MSTP在接入端口,而且用他们于链接"末端"设备(只这样用)-例如,主机以及叶子(leaf)交换机.
(同一个实例中的vlan,不要使用access端口, 同一个实例中不要将VLAN允许到不同的躯干(trunk)中)


##MSTP Single-Region Configuration Example  MSTP单域配置实例

现在我们有了基础的认识-对于如何MSTP工作在一个域内.让我们创建一个样例配置.
考虑到如下的物理拓扑-这三个交换机的:

这个拓扑有这几个VLAN:1,10,20,30,40,50,60. 我们的目标-为了这个脚本(scenario)是:
    
    让VLANs 10,20,30跟随链路-从SW3-Sw1
    让VLANs 40 50 60跟随链路-从SW3-SW2
    如果任何上面的链路失效了,受影响的VLAN应该调整(fall-back)到其他的链路.
为了做到(accomplish)这个,我们创建两个MSTI,编号1和2.SW1将是根-用于实例1,SW2将是根-用于实例2.至于IST(MSTI0),我们使SW3为根交换机-给IST(尽管这不是提倡的recommended-指定根角色给接入交换机).至于VLAN到MSTI的映射,VLAN1将仍然映射到IST.剩下的VLANs 10,20和30将映射到MSTI1,同事VLANs 40 50和60将映射到MSTI2.
下面是配置:
    
    SW1:
    spanning-tree mode mst
    !
    spanning-tree mst configuration
     name REGION1
     instance 1 vlan 10, 20, 30
     instance 2 vlan 40, 50, 60
    !
    ! Root for MSTI1
    !
    spanning-tree mst 1 priority 8192
    !
    interface FastEthernet0/13
     switchport trunk encapsulation dot1q
     switchport mode trunk
    !
    interface FastEthernet0/16
     switchport trunk encapsulation dot1q
     switchport mode trunk
    
    SW2:
    spanning-tree mode mst
    !
    spanning-tree mst configuration
     name REGION1
     instance 1 vlan 10, 20, 30
     instance 2 vlan 40, 50, 60
    !
    ! Root for MSTI 2
    !
    spanning-tree mst 2 priority 8192
    !
    interface FastEthernet0/13
     switchport trunk encapsulation dot1q
     switchport mode trunk
    !
    interface FastEthernet0/16
     switchport trunk encapsulation dot1q
     switchport mode trunk
    
    SW3:
    spanning-tree mode mst
    !
    spanning-tree mst configuration
     name REGION1
     instance 1 vlan 10, 20, 30
     instance 2 vlan 40, 50, 60
    !
    ! Root for the IST
    !
    spanning-tree mst 0 priority 8192
    !
    interface FastEthernet0/13
     switchport trunk encapsulation dot1q
     switchport mode trunk
    !
    interface FastEthernet0/16
     switchport trunk encapsulation dot1q
     switchport mode trunk
    The following show commands will demonstrate the effect our configuration has on traffic forwarding:
    
    SW1#show spanning-tree mst configuration
    Name      [REGION1]
    Revision  0     Instances configured 3
    
    Instance  Vlans mapped
    --------  ---------------------------------------------------------------------
    0         1-9,11-19,21-29,31-39,41-49,51-59,61-4094
    1         10,20,30
    2         40,50,60
    -------------------------------------------------------------------------------
    
    SW1#show spanning-tree mst               
    
    ##### MST0    vlans mapped:   1-9,11-19,21-29,31-39,41-49,51-59,61-4094
    Bridge        address 0019.5684.3700  priority      32768 (32768 sysid 0)
    Root          address 0012.d939.3700  priority      8192  (8192 sysid 0)
                  port    Fa0/16          path cost     0
    Regional Root address 0012.d939.3700  priority      8192  (8192 sysid 0)
                                          internal cost 200000    rem hops 19
    Operational   hello time 2 , forward delay 15, max age 20, txholdcount 6
    Configured    hello time 2 , forward delay 15, max age 20, max hops    20
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Fa0/13 Desg FWD 200000    128.15   P2p
    Fa0/16 Root FWD 200000    128.18   P2p 
    
    ##### MST1 vlans mapped:   10,20,30
    Bridge        address 0019.5684.3700  priority      8193  (8192 sysid 1)
    Root          this switch for MST1
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Fa0/13 Desg FWD 200000    128.15   P2p
    Fa0/16 Desg FWD 200000    128.18   P2p 
    
    ##### MST2 vlans mapped:   40,50,60
    Bridge        address 0019.5684.3700  priority      32770 (32768 sysid 2)
    Root          address 001e.bdaa.ba80  priority      8194  (8192 sysid 2)
                  port    Fa0/13          cost          200000    rem hops 19
    
    Interface        Role Sts Cost      Prio.Nbr Type
    ---------------- ---- --- --------- -------- --------------------------------
    Fa0/13 Root FWD 200000    128.15   P2p
    Fa0/16           Altn BLK 200000    128.18   P2p 
    
    SW1#show spanning-tree mst interface fastEthernet 0/13
    
    FastEthernet0/13 of MST0 is designated forwarding
    Edge port: no             (default)        port guard : none        (default)
    Link type: point-to-point (auto)           bpdu filter: disable     (default)
    Boundary : internal                        bpdu guard : disable     (default)
    Bpdus sent 561, received 544
    
    Instance Role Sts Cost      Prio.Nbr Vlans mapped
    -------- ---- --- --------- -------- -------------------------------
    0        Desg FWD 200000    128.15   1-9,11-19,21-29,31-39,41-49,51-59
                                         61-4094
    1        Desg FWD 200000    128.15   10,20,30
    2        Root FWD 200000    128.15   40,50,60
    
    SW1#show spanning-tree mst interface fastEthernet 0/16
    
    FastEthernet0/16 of MST0 is root forwarding
    Edge port: no             (default)        port guard : none        (default)
    Link type: point-to-point (auto)           bpdu filter: disable     (default)
    Boundary : internal                        bpdu guard : disable     (default)
    Bpdus sent 550, received 1099
    
    Instance Role Sts Cost      Prio.Nbr Vlans mapped
    -------- ---- --- --------- -------- -------------------------------
    0        Root FWD 200000    128.18   1-9,11-19,21-29,31-39,41-49,51-59
                                         61-4094
    1        Desg FWD 200000    128.18   10,20,30
    2        Altn BLK 200000    128.18   40,50,60
    

这个链路开销值是更高的-比默认的STP开销(IEEE标准值),并且MSTIx是叫做MSTx(例如IST是MST0).除此之外,注意到术语(term)"域根"-那将会被介绍-详细的-在下面.



##英语部分
****英语,不要想象去理解一整句话,按照英语的格式来读,写到哪里就理解这细节****

**理论**

    标准音和非标准音的对比,普通话,各地的对比.
    不要完全整句的翻译成中文再去理解,要翻译也要翻译成生活,成图片.
    让两种语言进行重叠,进入同一个区域,语法共有.元素独立.
    猜测--形成条件反射--建立语言区--实现语言思维
    别人在旁帮你纠正错误,这对你的语言掌握(不要用"学习")是没有任何帮助的.
    初学时的语法错误是很难避免的,没有必要太介意.
    只有当获得者接触到"可理解的语言输入",略高于现有的语言技能水平的第二语言的输入,他又能把注意力集中到对意义的理解而不是对形式的理解时,才能产生获得.
    理解输入语言的编码信息是语言获得的必要条件,不可理解的输入只是噪音.
    说话流利程度是自然达到的,是不能直接教会的.如何不断自己创造这个一点点难度的提高的条件.
    有动力.性格外向一点.情感状态放松,焦虑较少,感觉舒适.
    可理解输出,尝试做一些高于目前水平的输出练习.尝试一些新的规则.

**实践**

    "先听说,不读写" -- 外国小孩不学"认字",学习拼写规律.中文英文存储的不同.
    早期--提高期--增长期--高级期
    (看图识音)--避免使用中文翻译,充分建立条件反射.不要试图说,只练听.不看任何拼写,将听写放弃.如有外教,用肢体语言,不教课;不要怕听错,放松有信心.--1000词
    罗塞达石碑用来做这个阶段.
    TPR 听一个外语指令,用身体动作对他做出相应的反应.先建立听力能力,不强求说.
    TPR500词汇:
    
    General Body Movements 
    stand up，sit down，walk，stop，turn left，turn right，turn around，walk backwards，jump，hop， bend over，squat，walk 3 steps, 5 steps, etc.， face ___ (face me; face the wall, face the door, etc.)，lift up your right leg (left leg, right arm, etc.)，lower your leg (left leg, right arm, etc.)， shake my hand，kiss me (on the cheek!)，make a fist，clap your hands，wave。 
    
    Facial things 
    smile，cough，laugh，cry，sneeze，open your mouth，close your mouth，stick out your tongue，put your tongue back in，wink，blink，wiggle your nose 
    
    General verbs you can use with objects 
    where is， touch，show me，pick up，put down，put it back (return)，drop， move，give me (give him)，take it back，throw，catch，turn over (flip)，put the _____ on (under etc.) the ______，push，pull， lift 
    
    Kitchen table stuff 
    cup， plate， bowl， knife，fork，spoon， napkin / tissue， dish，big round serving tray，tray you’d serve tea or coffee on，table，chair 
    kitchen stuff 
    pan， oven，stove，sink，faucet，counter，cupboard，refrigerator 
    basic foods 
    flour，sugar，bread，tea leaves，coffee grounds，rice，nuts，yogurt，candy, etc. 
    drinks 
    water，milk，juice，soda，yogurt (drinking)，coffee，tea 
    fruits/vegetables 
    apple， banana， orange， plum， grapes， fig， dates， raisons， lemon，pomegranate，tomato， cucumber， zucchini， onion， carrot， eggplant， small eggplant，potato， garlic， parsley， lettuce， grape leaves， celery， mint，cabbage, etc. 
    
    "看图识音"和TPR是婴儿时期学习母语的的"提纯". -- 重点在于猜..猜错了也没关系. 区别"this is a door"--"where is the door"之间的区别,一个是纯粹的接受,一个是猜,动了脑筋的去思考.


**提高期 Upping the ANte**

现在支出成长的道理域做人的原则,根据自己的不同情况去分析和体会,而决不能说:用这个方法,你应该这样做.

第二阶段的原则:

    1.要学会听懂单句子,建立整句的英文思维;
    2.达到能听懂简单的,可能是慢语速的整段英文;
    3.在提高期的后期开始尝试简单"说"英语,实现简单沟通;
    4.开始引入阅读材料.(但不是学习如何阅读)

另外**需要了解一点英文语法**

**关键:**
    
    要提供"可理解性输入i+1":新增内容是我们现有水品下"可预测的predictable"

**比较理想的条件:**

    1.续列法
    2.生成对话

续列法:
    
    外教用简单英语结合肢体语言,实物实景描述日常生活的熟悉的一个连续动作,难度控制在有大约10%-20%为新词汇:如何泡茶?如何开车?如何打开房门?刷牙.

生成对话:
    
    不是自己试着对话,还是挺别人对话.对话是从续列法中的独白,变成了有交流有反应的对话.

使用这两个方法的原则:
    
    1.使用生活中熟悉的场景-或能预测是的情景.
    2.使用视觉或动作代替语言解释,全过程"亲身经历"完成
    3.起始囊度控制在第一遍能动80%-90%
    4.听,不试图说
    5.禁止阅读和笔记
    6.可以录音,以后听

有个节目:"You can talk" --就是可理解输入的完美体系.
    
    英文无论语音和文字,不是靠多看,多写和记忆.

**关键点**
    
    1.千万不要急着学文字,语言掌握的关键解决"声音"
    2.不依赖语法知识和中文翻译,重点是"猜测"着听
    3.参考Series Method
    4.后期能提供简单段落和简单对话时,可以模仿和重复一些句子并尝试自己说
    5.最后,可以阅读一些与听到的对话相关的文字.一定是听后才能读,不能一发现听不懂就马上翻看文字帮忙.

**第二阶段结束**
    
    应该有2k-4k单词.

**关于背单词**

    如果是纯粹的背中文解释,词性和拼写的话.都是在背知识,结果是哑巴英语.
    但是超过5000个极其常用词,就可以背单词了,这时候就不能再死抱着"英文思维"的帽子了.
    并且5k-15k之间的单词利用词根,都非常好背.
    每天30分钟100个单词,10分钟复习昨天的,三个月就能背10k.
    背单词不能提高能力,但是背单词是很简单的.

**外语成功因素**
    
    方法,愿望,自律

**第三阶段**
    
    听力过程和认知策略-依旧是遵循大量的"可理解行输入i+1",不能是无效输入.

**最重要:可理解输入**

**听力策略**
    
    1."从上之下"的听力处理-先理解整体的题目,不至于迷失.
    2."从下到上"通过听到单个音到单个词的声音识别,再词组,再整句.--这一阶段最重要的是听懂单词.
    3.

**选择思维语言**

语言的选择往往是被迫的,大部分往往不是主动进行"选择".是不自觉的根据情况进行选择的.
有时候,因为某种语言的能力太低,使用者往往更主动的"选择"语言了(选择自己更熟的).

**什么时候可以用母语思维**

在阅读和写作,阅读时候使用母语思维可以加深理解.但是,学习过程中不能使用.
写作时候,使用母语,对构造文章有一定帮助.不是不可以,但是不纯正,毕竟还是在思维上有很大的差别,写出来的句子的感觉也不会那么地道.

**语法**

语法是专家分析和总结语言的,不是给大家用来掌握语言的.
没建立好英文思维的时候,如果急着尝试交流,就会出现几乎句句都错的情况.


**基本原理**

    1.建立外语思维
    2.语言的掌握不是靠翻译和记忆,而是与思维,概念或图像建立直接联系
    3.语法的掌握是下意识的,不应该是有意识的学习
    4.要注重礼节的含义而非结构
    5.语言环境和掌握语言的关系
    6.关键是提供可输入的条件  --- 这在任何学习中都是通用的.




**不要相信只凭听说的任何事物.不要相信世世代代流传下来的传统.不要因为众人都这么说而相信它.不要因为经典上的记载而相信他.不要相信权威,导师或长辈的教导.当你经过观察和分析后,认为事物与原则一致,并且有助于个人和大家的善行与利益,才接受实行.**




##小孩
小时候记忆力最差,不要背诵什么诗词,就是玩,培养性格.





