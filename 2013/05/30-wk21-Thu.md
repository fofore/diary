1.to the C language there's no difference between a string and an array of characters.

2.To C, a "character" is just an integer. It's a really small integer, but that's all it is. 

3.In C, there's not really a "boolean" type, and instead any integer that's 0 is "false" and otherwise it's "true". In the last exercise the expression i < argc actually resulted in 1 or 0, not an explicit True or False like in Python. This is another example of C being closer to how a computer works, because to a computer truth values are just integers.
