1.the problem:
vlan 22 not created, they will think   "instance 2 vlan 22,33" the same as "instance 2 vlan 33"
is this the expect behavior?


2.just find the state machine:
mstp_process_bpdu

3.I find the 403 in git
to solve the problem


4.understand the pointer.
need to initial the pointer first.
declare is not initial.
pointer must point to someplace first. must to the stack, the heap, or some known place. then can give const to pointer.
int *intptr;   this ptr is a wild pointer, it pointer to some unknow place.
so to protect this: int *intptr = NULL; this make the pointer to (void *)0;
and if use the *intptr = xxxx; will cause the run problem very quickly. but it not show any warning;
make sure you know the pointer point to where.


to the decalre sentence:
int *intptr = NULL;
it just equal to  
    
    int *intptr;
    intptr = NULL;

but not the
    
    int *intptr;
    *intptr = NULL; // it just include two operation.

the way to understand typedef: put the vari into where the type in the typedef sentence


5.. the folding function of the c editor
enable the folding for control flow statement (if...)
