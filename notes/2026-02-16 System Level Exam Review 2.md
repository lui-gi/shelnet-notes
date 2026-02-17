# System-Level Programming Review Day 2

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
### Software Component vs. Software Categories

