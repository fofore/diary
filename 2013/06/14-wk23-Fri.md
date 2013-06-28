###usage of strrchr
strrchr be used in find the programe name. 
because the program name sometimes include the slash"/", and the programe name is always after the last slash. so strrchr used to find the last symble in a specified string. 
char *p = strrchr(argv[0], "/")
but when there be no "/", then p will be NULL
so at that situation, the (argv[0]) will be oK;
so the logic is this:
    
    char *p = strrchr(argv[0], '/');
    if (p) {
        char *progname = ++p;       //because p is the position of '/'
    } else {
        char *progname = argv[0];
    }

or use the ternary operator:

    char *p = NULL;
    progname = (p = strrchr(argv[0], '/')) ? ++p : argv[0];



###handle the arguments
in a deamon function, always need to handle the arguments
if don't want to handle manually, need one lib called **getopt.h**
and there are some info in getopt lib:
    
    man 3 getopt
to see the detail programing information about getopt

###what is man 3, instead of man
the banner of man 3 teel the function of man 3.

    GETOPT(3)                  Linux Programmer’s Manual                 GETOPT(3)
so it is the linux programmer's manual, and we can see the usage of the lib.
I learn man 3 from learn_c_the_hard_way.



###the usage of getopt_long
if use this, we can use the long type optinos, like a lib in python

first need a struct option type:
    
    static struct option longopts[] = {
        {"help",        no_argument,        NULL, 'h'}
        {"config_file", required_arguments, NULL, 'f'}
    }
then it will show like this '--help' is the same as '-h'
and in the futrue, it will be more easier to write the main.
or someday need to write a deamon.

###what is the signal 
how the signal works, where get to know how the signal works.

