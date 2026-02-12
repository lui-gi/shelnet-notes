# System-Level Programming Exam Review 
- only highlights SOME important areas
- review Week 1 - Week 5 for Exam 1

## Topics of Review
1. Introduction
2. Unix Ch 1
3. Unix Ch 2
4. C Basics
   - Ch 1 - 4

## Exam Structure
**MCQ**
40 - 45%; conceptual

**SAQ**
50 - 55%
- conceptual
- writing Linux cmds
- explaining cmds
- explaining semantics of regex
- determining output of a code snipper
- writing small programs
- explaining a block of code, etc.

**One page A4 double-sided**
- handwritten by yourself for reference syntax


## Specific concepts to review
### sftp upload/download
- to download a dir, use -r (for recursive)
### system programming
- benefits of ^
- system programs vs. system calls
- exampels of system programs, calls
- difference between software component and software categories
- unix philosophy
- unix attributes/advantages
- unix architecture
- process vs. program

### linux commands
- cat, pipe
- head/tail cmds
- script cmd and terminal recording

### running utilities
- to run, type name of utility after prompt then press enter
- etc: clear

### special characters
- what does CTRL-H do?
- CTRL-W, U, R
- CTRL-C,Z,S,Q,D

for CTRL-D, remember cat > filename then CTRL-D when you are done typing


*fg* will resume the most recently suspended job in the foreground (CTRL-Z'd utility)
*bg*: in the background

### common UNIX utilities
- ls
- cat, more, page, head, tail
- mkdir, rmdir, cd, pwd
- mv, cp, rm
- wc
- file, groups, chgrp, chmod
- vi, emacs

### pathnames
- absolute vs. relative

### ls
- flags: fill in
- **a**
- **l**
- **g**
- F
- s
- d
- **R**

### permissions
rwx | rw- | r--
given `rwxrw-r--`
r = read
w = write
x = execute
`-` = no permissions set

#### changing permissions via commands
`chmod u+x,g-r,o-w`

**Octal nums:**
```
rwxrw-r--
111 110 100
7 6 4

or 

r---w---x
100 010 001
421
```

### vi 
- movement within vi
- delete
- move
- transfer/copy
- replace
- more
- quit, write, quit/write, exit/write, etc.
- regex `{} () [] * + . \ ^ $`

### practice regular expressions
- remember that `\` escapes the special meaning
- `^ and $` only if explicitly mentioned

### C Programming
- general C program structure -> compiling, linking, directives
- printf, scanf
- format specifies
- operators
- precedence
- associativity
- increment/decrement 

## Practice Exam Questions

### What is system programming?
Yes:
- managing system resources
- performing i/o
- file manipulation
- process control
- inter-process communication
No:
- developing website
- querying a database

### What is TRUE in terms of logical organization of a computer system?
Operating System coordinates between applications and computer hardware

### Use Flow Pipeline
Users -> Applications -> OS -> Hardware

### What does -r do in context of sftp get
recursively collects all files and directories within a directory

### System Calls
**Operating-system defined functions that we can use in our application programs to communicate with the operating system**

Names of five of them:
- ==fork()== -> creates new **process** (requesting the OS to clone a process)
- ==open()== -> requesting OS to open a file in file system
- ==write()== -> requests OS to write to a file
- ==read()== -> requests OS to read something from a file
- ==exec()== -> requests OS to execute a completely different program

**Process:** a program in action

### What is an API (Application Programming Interface)
Every OS provides collection of libraries so that application PROGRAMMERS can use them to communicate with the OS for any lower-level (usually hardware-level) tasks

Example:
```
#include <LIBRARY> } provided by OS
```
### System Software
Shell, Kernel, Missile Control Systems, Antivirus
Yes:
- S
- 
No:

#look-up 

### System Programs
Write 5, name what tasks they do

- cp
- ls
- pwd
- cat
- vi

### What is a system daemon?

Example:

### What is a pipe mechanism?

Example:


### Which command to see current terminal settings?
stty -a


### Erasing current command:
CTRL + U (entire line)

### What terminates a program?
CTRL + C - terminates

Stops printing on terminal: CTRL + S

### rmdir vs. rm -r
rmdir: removes dir if dir is empty

rm -r dir: removes all contents of dir + the dir itself

### ls -a?
lists all the files in the wd including hidden ones

### cat vs. more
cat displays contents of a file at once (entirety)

more displays contents of a file in screens (one screenful at a time)

### counting number of lines in a file
`wc -l`

characters:
`wc -c`

words:
`wc -w`

### vi commands
```
:2,10d
:1,3t 10
3yy
```

### Difference between `^[A-Z]+$` and `[A-Z]+?`
`^` ensures matched string starts at the beginning of the line
`&` ensures matched string is the last thing in the line
-> in tandem = matched string IS the whole line

### precedence
`5/4*2+2%7 --> ((5/4)*2) + (2%7) --> 1*2 + 2 -> 4`

```
x = 4
x++ * 3 --> compiler will process post-increment first

Therefore,
x is processed first, SEPARATElY it is incremented, thus
4*3 = 12

now x = 5

However,
++x*3
 is 5*3=15
```
==++== has higher precedence over these operators `*/%` no matter if it is post-increment or pre-increment

### righthand precedence
```
c = 10;
a = b = c+5;

(
b = 15;
a=b
a= 15;
)

c = 10, a = 2, b = 3;
a += b += (c+5)
b += (c+5)
b = 18
a+= b
a += 18
a = 20
```