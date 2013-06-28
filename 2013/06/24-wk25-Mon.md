1.char prio[2]
so there are prio[0], prio[1]

2.the tlv:
means: type length value

3.use F2 in eclipse to read the macro, make reading it sometimes easy

4.char is integer
short is integer
long is integer
and the tyep can upgrade when there is bit move operation.
and in this **char pnt;
    
    **pnt << 8;
will make **pnt the int type;

    tlv->type = **pnt << 8 + *(*pnt+1);
    *pnt += 2;  // move the pointer next 2 char
    size -= 2;  // delete the size of the message
this will add the two char to a int, some the the message all in char.
they use a *char to store the message

5.the move of vim
move to the head of the func is [{
move to the end of the func is ]}

6.the F2 in function is also used to see the variable type

