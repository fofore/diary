1.national anthem
2.enormous->enormously
3.mental->mentality
4.on the loose
5.gaol


##what revision used for?
see from the call functions to know
all the switched in one region must have the same revision level:
**what will happen if they have different level?**
what the std. write?
what the cisco action?
what the zebos action?


##if the instance vlan map diff?
are they really diff, must see the bpdu.
**when the vlan is not created, we map the vlan to the instance, will it success?** it seems not now. after create the vlan, the port state changed. **what should it be?**

##burden
it is a "management burden"




defect:
    
    mst configuration not effect
    or sometimes effect after two show run
    do show run will effect, quit not effect
    end will take effect

what could be the cause:
1.they miss the quit
2.mstp_custom_cli_apply_config   --- this function. use the error info find this function.

the problem is where the function called, it is applied only in the exit and end of the mst configuration.
but unable to reproduce the twice problem, the second time, it will apply the configuration.


