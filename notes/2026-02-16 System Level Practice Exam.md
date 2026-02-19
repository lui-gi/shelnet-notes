# System Level Practice Exam
### What is system programming?
Ans: Give 2-4 lines of definition in your own words
```
System programming is programming low-level software that provides services to computer hardware. Lies between applications and the opearting system.
It manages hardware resources (CPU, memory) directly. It is involved with the development of operating systems, firmware, drivers.
```

### Q. Which is not system programming?
a. managing system resources
b. performing I/O
c. developing a website
d. file manipulation
e. Querying a database (e)
f. process control and inter-process communication
```
c, e
```

### Which one is TRUE in terms of logical organization of a computer system?
a. Application programs lie between users and computer hardware.
b. Operating systems lie between Users and computer hardware.
C. Users lie between OS and hardware.
D. OS coordinates between applications and computer hardware.
```
D
```
### Write how would you log-in to the snowball server.
```
ssh user@snowball.cs.gsu.edu
```
### What does the -r flag do in the following command?
sftp> get -r remote_directory
```
-r means recursive, meaning it will also get all the files and subdirectories + their contents within the target directory
```
### Write names of five system calls.
```
fork()
open()
write()
read()
exec()
```

### What is an application programming interface (API)?
```
An API is a collection of libraries provided by the host operating system so that application programmers can use them to communicate with the OS for any hardware-level tasks.
```

### Q. Which is not a system software?
A. Antivirus
B. Missile control systems
C. Shell
D. Kernel
```
B
```
### Write names of five system programs. What tasks they do?
```
1. mv
2. cp
3. vi
4. ls
5. mkdir
```

### What is a system daemon? Give an example.
```
A system daemon is a program with a unique process that run silently in the background and they monitor and take care of certain subsystems. An example is httpd.
```

### What is a pipe mechanism? Give examples.
Examples: who | sort, ls -l | grep -E '\.c'

### How would you record a terminal session? Give an example.

### Which command you will issue to see the current terminal settings?
A. stty -a
B. man terminal -a
C. set terminal -a
D. show settings -a

### Imagine you are typing a command on your terminal and you realized you wanted to issue a different command. To erase the current command, which characters (key combination) you will use?
A. CTRL + H
B. CTRL + U
C. CTRL + R
D. CTRL + W

### Which combination terminates a program?
A. CTRL + C
B. CTRL + Z
C. CTRL + S
D. CTRL + D
Ans. A

### What is the difference between CTRL-Z and CTRL-C?

### Understand the common UNIX utilities very well-mv, cp, rm, mkdir, cd, cat, more, page, and many more. 

For example:
What does the command do?
rmdir dir

### What would happen if the dir is not empty? How would you solve the issue?
Ans: rm -r dir

### Suggestion: Learn about absolute and relative path. Know how you can create directory tree and traverse over the tree using absolute and relative paths (lab 2 and HW may help)

### What does ls -a command do?
Ans. This command shows all the files in the current directory,
including hidden ones.

### What is the difference between cat and more command?

### How can you rename a file named file1.txt to new.txt? Write the command.

### What does `cp -ir <dir> <dir>` command do? Explain the flags.

### Which command counts the number of lines in a file?
A. wc -l file.txt
B. wc -cl file.txt
C. wc -w file.txt
D. wc -c file.txt

### Can you interpret the following file permission r-xrwx--x for the file example.txt?

### How would you change it so that user can also write to the file?
Ans: chmod u+w example.txt

### Change the file permission using octal numbers of the file so that only user can read, write, and execute and group members and others only can execute.
(Consider variations)

### Which command you will issue in vi editor to delete lines from 2 to 10?
Ans: :2,10d

### What does the following command do?
:1,3t 10

### What does 3yy do?

### Suggestion: Learn other vi editor commands

### Suggestion: Practice Regular expressions (See slides and HW2). Also practice email address detection using regex

One example could be: `grep -E --color=auto '^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' regex_practice.txt`

### What is the difference between ^[A-Za-z]+$ and [A-Za-z]+?
Ans: ^ ensures if the matched string starts at the beginning of a
line, whereas $ ensures if the matched string is the last thing in the
line.

### Suggestion: Study HW1 and HW2 well.

### How would you compile and run your C program prog.c? Show.

### What will be the value of the following expression?
```
A. 5*3%2 => (5*3)%2
B. 5/4*2+2%7 => ((5/4)*2) + (2%7) => 1*2+2 => 4
```


### What will be printed on the terminal?
```
#include <stdio.h>
int main(){
int x = 2;
printf("\n%d", ++x*5);
printf("\n%d", ++x*5);
return 0;
}
```
Ans:15

### What if we would use `printf("\n%d", x++ *5);`?
Note: The pre-increment (++x) or the post-increment operator has a
higher precedence than the multiplication (* , /, %) operator in C.
what will be the value of x++ % 5 when the initial value of x is 22?

### Supply parenthesis so that it specifies how C compiler will evaluate the following expressions?
```
(a) a * b - c * d + e => (a * b) - (c * d) + e
(b) a / b %c / d => ((a / b) % c) / d
(c) - a - b + c - + d = > (((-a) - b) + c)- (+d)
```


### What will be printed on the terminal, when all i, j, k are int variables?
```
i = 7; j = 8; k = 9;
printf("%d", (i + 10) % k / j);
what will be the value of a and b?
c = 10;
a = b = c+5;
```


### What will be printed?
```
i = 6;
j = i += 1; => i = i + 1; j = i;
printf("%d. %d", i, j);
```


### what will be the output?
```
i = 7; j = 8;
i *= j + 1; => i = i*(j+1);
printf("%d %d", i, j);
a +=b; => a = a+b
i +=5;
a /= b+c => a = a/(b+c);
```

