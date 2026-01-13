# System-Level Programming

- application programs use i/o devices, memory space, interacts with other processes
- by default, not allowed to use these resources (i/o, cpu, printer, monitor, etc.)
- every interaction/instruction is written in our application program, eventually goes through the OS

So what is it exactly?
- writing the software that directly interacts with and manages the OS, hardware, core sys. services

[written program] -> [operating system]

ls: system program command
- system program cmds like this provide access to i/o devices, files, program control, memory management, network communication etc.
- also: graphics card drivers, printer drivers --> system program that knows traits of the graphics card
directory: still a FILE, just one that contains other files

