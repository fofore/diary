1.  the mstp bridge function-> the paramater not inlcude zg, and most of the functions the paramaters are with a mstp_bridge.

2.  我们代码中的动态和静态指的是对于内存的使用的动态和静态.
全局变量和静态变量都是静态区,因为对内存大小的取用在编译时候已经静态确定了.
而, 局部变量占用的空间->使用的是栈空间
    malloc出来的占用的空间->使用的是堆空间
这个堆栈区.静态区,在程序结束之后才结束.
堆栈区的内容是不断的在变化的.

3.  而静态区的又分了作用域,全局是所有文件,文件中的静态是本文件,函数中的静态是本函数.

4. cli:change_spanmode_why will add the bridge, at the begning, from which mode? and is disable will remove the bridge

5. all keyboard action make the more foucus, brain not in hand

6. how to gdb, is that in mind.
konw how to use gdb, but not the way to find a bug.

7. the strace valgrind jslint intellij.
the strace is useful, I have used the valgrind, and also used it.


8.test the vlan in cist, test the access port

