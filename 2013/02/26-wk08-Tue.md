## test logs

###1.description command in interface mode

bug desc: command run successful but shows up the "No such command"

log info:

    bingo-10015(config-if)#description conncet-10006-port1
    % No such command
    bingo-10015(config-if)#show run int xe2
    !
    interface xe2
     description conncet-10006-port1

###2.the show interface command

bug desc:
    
    the interface status not clear.

log info:
    
when the connected port is up:

    bingo-10015#show interface xe2
    Interface xe2
      Scope: both
      Hardware is Ethernet  Current HW addr: 0098.28dd.0004
      Physical:0098.28dd.0004  Logical:(not set)
      Description: conncet-10006-port1
      index 5002 metric 1 mtu 1522 duplex-full arp ageing timeout 0
      <UP,BROADCAST,RUNNING,ALLMULTI,MULTICAST>
      VRF Binding: Not bound
      Bandwidth 40g
      VRRP Master of :  VRRP is not configured on this interface.
        input packets 011800, bytes 02625471, dropped 034, multicast packets 08312
                      FCS error 00 UndersizeErrors 00 OverSizeErrors 00
        output packets 02404718, bytes 0154888192, multicast packets 0108749 broadcast packets 03496
    bingo-10015#

when shutdown the connected port:

    bingo-10015#show interface xe2
    Interface xe2
      Scope: both
      Hardware is Ethernet  Current HW addr: 0098.28dd.0004
      Physical:0098.28dd.0004  Logical:(not set)
      Description: conncet-10006-port1
      index 5002 metric 1 mtu 1522 duplex-full arp ageing timeout 0
      <UP,BROADCAST,ALLMULTI,MULTICAST>
      VRF Binding: Not bound
      Bandwidth 40g
      VRRP Master of :  VRRP is not configured on this interface.
        input packets 011859, bytes 02630915, dropped 038, multicast packets 08367
                      FCS error 00 UndersizeErrors 00 OverSizeErrors 00
        output packets 02404718, bytes 0154888192, multicast packets 0108749 broadcast packets 03496
    bingo-10015#

the only difference is the RUNNING flag.


###3.the do write command in configuration mode
desc: show up no such command, but success

log:

    bingo-10015(config)#do write
    Building configuration...
    % No such command

###4.the bpdu guard action is different with webos
**description**
in webos, when detect BPDU packets in the BPDU-gurad enabled port. the port goes into errordisable status. 
in Zebos, it just shutdown the port(generate a shutdown command in running-config)

**log**
in webos the command :

    !
    interface port 5
            description "conncet-bingo-xe1"
            bpdu-guard
            spanning-tree portfast
            exit
    !
in webos the result:
    
    Gryphon10014(config-if)#show int status 5
    -----------------------------------------------------------------------
    Alias   Port   Speed    Duplex     Flow Ctrl      Link     Description
    ------- ----   -----   --------  --TX-----RX--   ------   -------------
    5         5     40000     full      no     no   errdisabled   conncet-bingo-xe1

in zebos the command:

    !
    interface xe1
     description conncet-10014-port-5
     switchport
     bridge-group 1
     no shutdown
     spanning-tree portfast
     spanning-tree bpdu-guard enable
    !
in zebos the result:

    MSTP[846]: MSTP: <PVR>: mstp_handle_bpdu: Received BPDU on bpdu-guard enable port. shutting down 5001 bridge 1

and the running configuration change to:

    bingo-10015#show run inte xe1
    !
    interface xe1
     description conncet-10014-port-5
     switchport
     bridge-group 1
     shutdown
     spanning-tree portfast
     spanning-tree bpdu-guard enable
    !

###5.do we need the global BPDU gurad command? 
**desc**
there are two ways to configure the BPDU guard. The port's BPDU status depend on the global command and the interface mode command.
and in the gap file, not memtioned the global command: bridge 1 spanning-tree portfast bpdu-guard.
cisco also have a global command: spanning-tree portfast bpduguard default.
if we want the global command, do we need to make it the same as cisco, add the default part?

**log**
command in zebos

    !
    bridge 1 protocol rstp
    bridge 1 spanning-tree portfast bpdu-guard

command is cisco catalyst 4500

    spanning-tree portfast bpduguard default

###6.the show spanning-tree detail command.
**description**
now the IPI "show spanning-tree" command is just like "show spanning-tree detail" command.
but there is a diff from cisco CLI. the show command should sort by port number.
now it is sorted by the time the port joined the bridge.

**log**

    bingo-10015#show span
    % 1: Bridge up - Spanning Tree Enabled  - topology change detected
    % 1: Root Path Cost 0 - Root Port 0 -  Bridge Priority 32768
    % 1: Forward Delay 15 - Hello Time 2 - Max Age 20 - Transmit Hold Count 6
    % 1: Root Id 80000003a3950003
    % 1: Bridge Id 80000003a3950003
    % 1: last topology change Thu Jan  1 23:48:28 1970
    % 1: 3 topology change(s)  - last topology change Thu Jan  1 23:48:28 1970
    
    % 1: portfast bpdu-filter disabled
    % 1: portfast bpdu-guard disabled
    % 1: portfast errdisable timeout disabled
    % 1: portfast errdisable timeout interval 300 sec
    %   xe4: Port Number 908 - Ifindex 5004 - Port Id 838c - Role Designated - State Forwarding
    %   xe4: Designated Path Cost 0
    %   xe4: Configured Path Cost 200  - Add type Explicit ref count 1
    %   xe4: Designated Port Id 838c - Priority 128  -
    %   xe4: Root 80000003a3950003
    %   xe4: Designated Bridge 80000003a3950003
    %   xe4: Message Age 0 - Max Age 20
    %   xe4: Hello Time 2 - Forward Delay 15
    %   xe4: Forward Timer 0 - Msg Age Timer 0 - Hello Timer 0 - topo change timer 0
    %   xe4: forward-transitions 1
    %   xe4: Version Rapid Spanning Tree Protocol - Received None - Send RSTP
    %   xe4: No portfast configured - Current  portfast off
    %   xe4: bpdu-guard  default  - Current bpdu-guard off
    %   xe4: bpdu-filter default  - Current bpdu-filter off
    %   xe4: no root guard configured     - Current root guard off
    %   xe4: Configured Link Type point-to-point - Current point-to-point
    %   xe4: No auto-edge configured - Current port Auto Edge off
    %
    %   xe3: Port Number 907 - Ifindex 5003 - Port Id 838b - Role Designated - State Forwarding
    %   xe3: Designated Path Cost 0
    %   xe3: Configured Path Cost 200  - Add type Explicit ref count 1
    %   xe3: Designated Port Id 838b - Priority 128  -
    %   xe3: Root 80000003a3950003
    %   xe3: Designated Bridge 80000003a3950003
    %   xe3: Message Age 0 - Max Age 20
    %   xe3: Hello Time 2 - Forward Delay 15
    %   xe3: Forward Timer 0 - Msg Age Timer 0 - Hello Timer 1 - topo change timer 0
    %   xe3: forward-transitions 1
    %   xe3: Version Rapid Spanning Tree Protocol - Received None - Send RSTP
    %   xe3: No portfast configured - Current  portfast off
    %   xe3: bpdu-guard  default  - Current bpdu-guard off
    %   xe3: bpdu-filter default  - Current bpdu-filter off
    %   xe3: no root guard configured     - Current root guard off
    %   xe3: Configured Link Type point-to-point - Current point-to-point
    %   xe3: No auto-edge configured - Current port Auto Edge off
    %
    %   xe1: Port Number 905 - Ifindex 5001 - Port Id 8389 - Role Disabled - State Discarding
    %   xe1: Designated Path Cost 0
    %   xe1: Configured Path Cost 200  - Add type Explicit ref count 1
    %   xe1: Designated Port Id 0 - Priority 128  -
    %   xe1: Message Age 0 - Max Age 0
    %   xe1: Hello Time 0 - Forward Delay 0
    %   xe1: Forward Timer 0 - Msg Age Timer 0 - Hello Timer 0 - topo change timer 0
    %   xe1: forward-transitions 0
    %   xe1: Version Rapid Spanning Tree Protocol - Received None - Send RSTP
    %   xe1: Portfast configured - Current portfast on
    %   xe1: bpdu-guard  default  - Current bpdu-guard off
    %   xe1: bpdu-filter default  - Current bpdu-filter off
    %   xe1: no root guard configured     - Current root guard off
    %   xe1: Configured Link Type point-to-point - Current point-to-point
    %   xe1: No auto-edge configured - Current port Auto Edge off
    %
    %   xe2: Port Number 906 - Ifindex 5002 - Port Id 838a - Role Designated - State Forwarding
    %   xe2: Designated Path Cost 0
    %   xe2: Configured Path Cost 200  - Add type Explicit ref count 1
    %   xe2: Designated Port Id 838a - Priority 128  -
    %   xe2: Root 80000003a3950003
    %   xe2: Designated Bridge 80000003a3950003
    %   xe2: Message Age 0 - Max Age 20
    %   xe2: Hello Time 2 - Forward Delay 15
    %   xe2: Forward Timer 0 - Msg Age Timer 0 - Hello Timer 1 - topo change timer 0
    %   xe2: forward-transitions 1
    %   xe2: Version Rapid Spanning Tree Protocol - Received None - Send RSTP
    %   xe2: No portfast configured - Current  portfast off
    %   xe2: bpdu-guard  default  - Current bpdu-guard off
    %   xe2: bpdu-filter default  - Current bpdu-filter off
    %   xe2: no root guard configured     - Current root guard off
    %   xe2: Configured Link Type point-to-point - Current point-to-point
    %   xe2: No auto-edge configured - Current port Auto Edge off
    %

**it should sort by port number. just show xe1 first, then xe2, xe3 and xe4...**

###7.err-disable bug
**description**
when enable error disable after the port error disabled, it doesnot function well.
need more test in the error disable function test.

**log**


###8.
















