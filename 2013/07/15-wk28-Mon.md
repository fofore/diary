1.realloc learn

vector learn, use the vector machanism to make a expandable list.

realloc do two things: 1. expand the space 2.copy the original infor to new.
two: realloc may or may not return a new pointer.(if not enough, will get a new one)

    realloc 用过很多次了。无非就是将已经存在的一块内存扩大。
    
    char* p = malloc(1024);
    char* q = realloc(p,2048);
    
    现在的问题是我们应该如何处理指针 p。 刚开始按照我最直观的理解，如果就是直接将 p = NULL;。 到最后只需要释放 q的空间就可以了。
    
    因为最近在做个封装。结果在做单元测试的时候发现。有时候我在 free(q); 的时候会出错。这样我就郁闷了。
    
    后来仔细一跟踪，发现 realloc 完以后 q 和 p 的指针地址是一样。不过有时候又不一样。
    
    仔细查了下资料。得到如下信息：
    
           1.如果 当前连续内存块足够 realloc 的话，只是将p所指向的空间扩大，并返回p的指针地址。 这个时候 q 和 p 指向的地址是一样的。
    
           2.如果 当前连续内存块不够长度，再找一个足够长的地方，分配一块新的内存，q，并将 p指向的内容 copy到 q，返回 q。并将p所指向的内存空间删除。
    
    这样也就是说 realloc 有时候会产生一个新的内存地址 有的时候不会。所以在分配完成后。我们需要判断下 p 是否等于 q。并做相应的处理。
    
    这里有点要注意的是要避免 p = realloc(p,2048); 这种写法。有可能会造成 realloc 分配失败后，p原先所指向的内存地址丢失。


1.target
make the notes, log the learning process
do hava progress every day.

today, learn the vector.
and the dynamic array in C.

无条件相信教条的人，是不会成长的。

typedef究竟是不是朋友？
云风：

    在我的项目中，反对随意的使用 typedef ，因为那意味着不断的新概念的加入，为此，付出更大的体力代价也是值得的。也就是说，宁可在每个结构和联合前显式的敲上 struct 和 union 。

减少了字符的输入。
是不是有云风所说的新概念的加入。为什么他认为是个新概念。


为什么使用typedef，为什么结构体使用typedef
只发生在现实的type变化的时候，union变化成了struct，struct与普通类型的变化。

这个论据也不会很成立，type变化的机会很少。struct的成员的变化不会影响到类型的变化的。

首先：什么是type，并且，C语言中有哪些的type？

change the timer from int16 to long.
but this is not the structure.
if you use structure for the time, then there is no need to modify the definition.

and in the program we are writing, we don't waste using typedef.

typedef一般都用在函数指针的定义上。
还有就是他的本行，创建一个新的类型。typedef为数据类型创建别名，而不是创建新的数据类型。

C专家编程里面说：不要为了方便对结构使用typedef。
typedef应该使用在：数组，结构，指针以及函数的组合类型。可移植类型。


只研究C语言和计算机科学的是不可能成为专业的程序员。
正如，研究画笔和颜料的是不可能成为专业的画家的。

你能够教别人如何雕塑，但是对于米开朗基罗的是，反倒是教他不要做什么。对于卓越的程序员，也是一样的。

要做的是程序设计，而不是学会C语言。








