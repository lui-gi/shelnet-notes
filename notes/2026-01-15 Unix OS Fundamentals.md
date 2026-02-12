# Introduction to Unix

## Computer Systems
- consists of both hardware and software
- hardware - cpu, mem, disks, gpu, keyboard, mouse, ethernet interface, etc.
- software - os, application programs

RAM: random access memory, our main memory
- collection of locations, each location has one data item
- memory addresses randomly selected, can read or write from any location using the same amount of time
- differs from sequential access, where the first selected location is the first available in line
- random access allows us to perform read/write operation using the SAME amount of time
-> Read already stored ata
-> Write data

CD's memory is only semi-random; due to its circular shape

ROM: read-only memory
- reads programs already written by manufacturer of motherboard
- responsibility of these programs is to initialize the system
-> Read only

Secondary storage: SSD, HDD

(Hardware/Peripherals (Computer (I/O Interface (CPU, Memory))))

## Hardware Key Components

### CPU and Main Memory

What does the CPU actually do?
- a chip that executes program commands 
- "integrated circuit"

Programs are just a series of commands that need to be executed by the **CPU**

Main memory:
- the primary storage for programs/data that are **active** in use
- "RAM"

Applications not running/already installed are located in SSD/HDD

Direct communication:
CPU <--> Main Memory
Generates results <--> Stores results

### Secondary Memory Devices

Hard Disk/SSD
- info is moved between main memory and secondary as needed
- these devices provide long-term storage

Example: writing and pressing "CTRL + S" = secondary storage
writing and not saving = main memory

### I/O Devices

facilitate use interaction
- monitor, keyboard, mouse

## Software Components
2 main: Application Software, System Software

Application Software:
- meets end-user requirements
- wants to satisfy our needs
- ex: PPT

System Software:
- ex: we want to print our document, so we need extra internal processes not present in application software, like a **printer driver**
- helps application software be executed smoothly 
- "master" system programs


What does the Operating System do?
- provides us an API, application program interface, allows us to facilitate communication between the system and the application software

API:
- messenger between different software applications and Operating System

Kernel
- core component of the operating system
- (memory management, resource scheduling, program communication, security)
- bridge between software apps and computer hardware, manages essential resources

Data analysis is a function of the application programs, not the OS kernel
#look-up are OS and kernel synonymous?
### Software Categories

Operating System
- controls all machine activities
- [[2026-01-20 Unix Shell Commands|shell commands]]/terminal (passes commands to the kernel)
- controls all machine activities
- store and retrieve files
- providers the user interface to the computer
- manages resources like CPU, memory
- utility software: disk defragmenter

Application Program
- generic term for any other kind of software
- word processor, games, missile control system

Most OS and application programs have a GUI

### Shell
the interface between users and the operating system

Users(Shell (Operating System))

If using terminal to talk to OS, we must go through the shell

### Bootstrap Program
initializes operating system; 
- machine executes the bootstrap program already in memory, OS stored in disk
- then, bootstrap program **directs transfer of OS to main memory** then transfers control to it

## Unix
An operating system
- not really used today, but we do use variants of Unix
- Linux, macOS

Provides framework for executing programs/storing files
- file: collection of data normally stored on disk
- program: collection of instructions/data store in a file
### Unix API
everything works through system calls

X = GUI system/windowing system
![[Pasted image 20260115133543.png]]

### System Daemons

daemons:
- a program with a unique purpose
- run in the background, utility programs
- printing services? --> printing daemon
- network comms? --> network daemon
- ex: httpd (HTTP service manager, run with Apache, sshd
- note: 'd' at the end of system programs
- `pstree` -> identify daemons
```
systemd─┬─NetworkManager───2*[{NetworkManager}]

        ├─VGAuthService

        ├─abrt-dbus───3*[{abrt-dbus}]

        ├─abrt-watch-log

        ├─abrtd

        ├─agentid-service───10*[{agentid-service}]

        ├─agetty

        ├─atd

        ├─auditd───{auditd}

        ├─bash───infinite_loop

        ├─cgrulesengd

        ├─chronyd

        ├─crond

        ├─cylancesvc───42*[{cylancesvc}]

        ├─dbus-daemon───{dbus-daemon}

        ├─fail2ban-server───12*[{fail2ban-server}]

        ├─firewalld───{firewalld}

        ├─7*[homework5]

        ├─4*[homework5───homework5]

        ├─irqbalance

        ├─lsmd

        ├─lvmetad

        ├─mysqld_safe───mysqld───18*[{mysqld}]

        ├─oddjobd

        ├─polkitd───6*[{polkitd}]

        ├─qualys-cep───7*[{qualys-cep}]

        ├─qualys-cloud-ag───9*[{qualys-cloud-ag}]

        ├─rngd

        ├─rpcbind

        ├─rsyslogd───2*[{rsyslogd}]

        ├─smartd

        ├─sshd─┬─4*[sshd───sshd───bash]

        │      ├─4*[sshd───sshd───sftp-server]

        │      ├─3*[sshd───sshd]

        │      └─sshd───sshd───bash───pstree

        ├─sssd─┬─sssd_be

        │      ├─sssd_nss

        │      ├─sssd_pac

        │      └─sssd_pam

        ├─systemd-journal

        ├─systemd-logind

        ├─systemd-udevd

        ├─tuned───4*[{tuned}]

        └─vmtoolsd───2*[{vmtoolsd}]
```

### Process
When a program is executed -> loaded into memory.
When it is executing, it is called a process.

When a program runs in main memory, it is a process.
Process = in action

- most processes read/write data from/to files
- processes and files have an **owner** (see [[2026-01-22 Unix File Permissions and chmod|file permissions]])

Unix context:
- support hierarchical dir structure
- files and processes have a location within the dir structure
- provides the capabilities to create, modify and delete files, programs, processes

## Unix Attributes
- sharing resources: time slices of CPU, memory (pages), disk (blocks)
- ex: server allocates resources amongst all the students and instructors
- communication: process-device controller, process-process, etc. (pipes 1-way, sockets 2-way)
- utils: comes with a large collection of utils
- programmer support: provides us standard compilers for common system programming languages such as C/C++
- ^ also gives us access to parallel processing, file handling and interprocess comms via system calls in C

GCC: Gnome C Compiler, pre-built into Snowball

### Advantages

Multitask
Multiuser
Safe

### Unix Tree/Variants

Unics: Uniplexed Information and Computing Service, originally written in Assembly, then later in C

Unics 2 branches: SVR5 (ATT), BSD (UC Berkeley)

System V
BSD
Linux
Solaris, Sun Java
Apple OS/X

### Pipe Mechanism
Output of one process can be used as input for another process 
`psaux | grep 'ssh'`
- complex tasks can be broken down into simpler ones, combined using pipes, etc. (example workflow)
`ls | wc -l`
"Word count" 
-l; outputs number of LINES
### Super user
user who has complete control over system resources
- typically, the system's administrator
- `sudo`
### cat, pipes
`>>` append
`cat test.txt | head -2`
shows only the first two lines of the output of test.txt

### script
record what we are doing in terminal
`script filename.txt`

to exit the recording session -> `exit`