# System Programming and Unix (Exam Review)

## System Programming

### Benefits of System-Level programming
System level programming allows
- direct hardware control
- control over resources
by operating close to the machine level.

### System Programs
System programs are utilities such as `vi`, `ls`, `mv` that provide access to system resources

-> designed to manage and control a computer's hardware and software resources 
-> layer between OS kernel and user application software
-> often pre-installed
-> crucial for system maintenance, file management, program execution

### System Calls
System calls are Operating-System defined functions used in code (via the API) to request services from the **kernel**.

-> allows applications to request services from the kernel
-> acts as a bridge for tasks like I/O and process management

Examples:
- fork()
- open()
- write()
- read()
- exec()

**Kernel:** acts as the primary bridge between computer hardware and software applications

-> manages system resources (CPU, memory, I/O devices), runs with highest privilege

-> applications interact with the hardware by sending requests, aka system calls, to the kernel, which then executes these actions

-> the first program that loads when you turn your computer on, stays in control

**API (Application Programming Interface):** set of rules and protocols that allows applications to exchange data, perform actions, and interact in a well-documented way

-> an intermediary, allows developers/users to access features or data from another service or library

-> allows software to interact directly with an operating system, driver, or hardware component

Flow:
- API takes your request, tells the system what we want, then brings the response back


### System Programs vs. Calls

System programs are complete, standalone executable programs that perform system-level tasks (such as file management), meanwhile system calls are the programmatic interface used by ALL software (including system programs) to request services from the OS's kernel.

### Hierarchy / User Flow

```
[ Saving a document via text editor ]

1. System Program
   the text editor sends save request to the OS
   
2. API
   text editor uses an API like (WriteFile) to format our 'save' request
   
3. System Call
   API triggers a write() call 
   
4. Kernel
   kernel now manages RAM and SSD to fulfill the 'write' request by directly managing the hardware
   
5. Response
   the system now sends the response back, telling us our document has been saved
```
### Software Component
Modular, independently replaceable and reusable units of software that encapsulate specific functionality

-> improves maintainability by hiding implementation details behind interfaces

Examples:
- Frontend: buttons, input fields
- Backend: logic, models, API endpoints
- System software: operating systems, device drivers, firmware

### Software Categories

**System software:** manages hardware and provides a platform for applications
example: operating systems, device drivers, firmware, utility software

**Application software:** designed for specific user tasks, such as word proccessors, web browsers, etc.

## Unix 

### Unix Philosophy
**modularity**: build small, simple, and clear programs that can be easily combined

**==pipes==:** design programs to read from standard input and write to standard output, which allows them to be chained together using pipes `|`

**==superuser==**: 
- user who has complete control over system resources
- usually SysAdmin

**textual interfaces:** use plain text streams as the universal interface, daya is easy to view, manipulate, and filter with standard tools

Examples:
- pipeline processing like `cat file.txt | grep 'yoo' | sort`
- use `grep` to find text, `awk` to process data fields, `sed` to 

### Unix Attributes
Shares resources
- CPU gets time slices
- Memory in pages
- Disk has blocks

Communication:
- process-device controller, process-process (pipes 1-way and sockets 2-way)

Large collection of utilities
- such as vi, awk, grep, etc.

Programmer support
- provides standard compilers for common system programming languages like C and C++
- access to parallel processing, file handling and interprocess communication via System calls in C

### Unix Advantages
Multitasking
- multiple programs can run at one time
Multiuser
- more than one single user can work at any given time
- done by sharing processing time between each user and utilizing distributed computer systems
Safe
- prevents one program from accessing memory or storage space allocated to another
- enables protection

### Unix Architecture
(higher # = closer to center)
1. Application Programs
2. Shell
3. Kernel
4. Hardware

The shell is an interface between users and the operating system

User -> Shell -- Operating System
User <- Shell -- Operating System

### System Daemons
**Daemon** is a program with unique purpose.
- utility programs
- run silently in background
- monitor and takes care of certain subsystems

Examples:
- printer daemon monitors printing services
- network daemon for network communications

-> **httpd**: HTTP service manager
-> **sshd**: responsible for managing SSH
*'d' at the end of system programs*
`pstree` = identify some daemons

### Process vs. Program
When a **program** is executed, it is loaded into memory
When a 'program' is execuTING, it is called a **process**

Most processes read/write data to and from files
- also have an owner
- UNIX supports hierarchical directory structure
- files AND processes have a location within the directory structure
- UNIX provides capabilities to create, modify, and destroy files, programs, and processes

## Utilities
`stty` -> a utilitiy used to modify and print terminal line settings
- we can list meta charactes with `stty -a`

### Special Characters

**Line Manipulation**
Erase: `CTRL-H`
- erases character BEFORE cursor

Werase: `CTRL-W`
- erases WORD before cursor

kill: `CTRL-U`
- erases entire line

rprnt: `CTRL-R`
- reprint line

**Program Manipulation**
int: `CTRL-C`
- interrupt running program

susp: `CTRL-Z`
- suspend running program
- we can use `fg` and `bg` to resume this

stop: `CTRL-S or CTRL-Q`
- stops printing to screen

eof: `CTRL-D`
- give program the end of file
- used for `cat > file.txt`, when we are done inputting we press `CTRL-D` to end input

fg: `fg`
- will resume the most recently suspended job in the foreground
bg : `bg`
- will resume the most recently suspended job in the background

### ls
list directory contents

**Flags**
`-a`: lists all files
`-l`: long listing
- displays file mode, number of links, owner, group, size, and modification time
`-g`: like -l, but do not list owner
`-R`: recursive
- lists contents of the current directory
- descends into EVERY SUBdirectory and lists its contents as well
- continues for all subdirectories and their subdirectories down the entire directory tree from the starting point

**Lesser important flags**
`-F`: lists contents of directory AND appends a special character to each entry to indicate its ==file type==
- `/` for directories
- `*` for executable files or programs
- `@` for symbolic links
- `=` for sockets
- `|` for FIFOs / pipes
`-s`: displays size of each files in blocks
`-d`: lists information about a directory itself, not its contents