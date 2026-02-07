# System-Level Programming Intro

## Intro 
- application programs use i/o devices, memory space, interacts with other processes
- by default, not allowed to use these resources (i/o, cpu, printer, monitor, etc.)
- every interaction/instruction is written in our application program, eventually goes through the OS

So what is it exactly?
- writing the software that directly interacts with and manages the OS, hardware, core sys. services

[written program] -> [operating system]

`ls`: system program command
(also `pwd, cd, cat, ps, etc.`)
- system program cmds like this provide access to i/o devices, files, program control, memory management, network communication etc.
- also: graphics card drivers, printer drivers --> system program that knows traits of the graphics card
directory: still a FILE, just one that contains other files

OS = software written with programming language, big "master" program

Course: Learn fundamentals of C first -> Communicating with Unix/Linux

## Outline
*top to bottom*
user <-> application programs <-> OS <-> computer hardware

application programs
- compilers, web browsers, dev kits, etc.
computer hardware
- CPU, memory, I/O devices, etc.

#look-up Why is the OS integral to syslevel programming?
- because the operating system allows our application programs to interact with our computer's resources

## Additional Notes
- lab quizzes starting from lab 9 (post-lab)
- paper exams, concept-based
- 2 pop quiz drops, total 7-8 
- allowed one handwritten, double-sided A4 paper
- we use [gcc compiler], no IDEs only terminals in course
#look-up installing/usage of gcc compiler
--> ssh into the uni's server

Subject line, incl "CSC 3320PSC"

GNU Compiler Collection

