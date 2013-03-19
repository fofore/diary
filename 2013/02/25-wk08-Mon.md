##the spanning-tree

###
the process of the proposal and acknowledge
1.  root port receive proposal
2.  block all the designated port
3.  reply the agreement
4.  change the root port to forward
5.  send the proposal in all designated port
6.  receive the acknowledge message
7.  change all the designated port to forwading.

1.if one send a proposal, the port role is desinated port, with the proposal flag.
2.if one send an agreement, the port role is root port, with a proposal flag.

###the BPDU
1.  rstp not send the TCN topology change notification messages
2.  but for interoperability with 802.1D switches, the rstp switches will send TCN to.

###the RSTP BPDU flags
1.  bit 
    0   topology change (TC)
    1   proposal
    2-3:
    00  unknown
    01  alternate port
    10  root port
    11  designated prot
    4   learning
    5   forwarding
    6   blocking
    7   topology change acknowledgement (TCA)

what is the link-type:
only in the point-to-point link-type can the rstp runs
and when using the auto link-type command, link-type decided by the duplex mode, full duplex mode regard as the point-to-point, half duplex regard as the shared link-type
and link-type command can designate the link-type and regardless of the duplex settings.

superior BPDU:


