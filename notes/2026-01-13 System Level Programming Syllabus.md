# SysLevel Concept Outline 
## Table of Contents
- [[2026-01-20 Unix Shell Commands|Unix commands]]
- Basic [[2026-02-02 awk and Shell Scripting|shell scripting]]
- C program
- System programming: file management (see [[2026-01-22 Unix File Permissions and chmod|chmod]])
- System programming: process management

## Unix

Why Unix? (/Unix-like, such as Linux)
- free, open-source
- secure, well-documented
- Originally written in C
--> Good practice to use C to communicate with Unix 

## C

Why C? (see [[2026-02-03 C Fundamentals and Compilation|C fundamentals]])
- provides direct access to system resources
- C can manipulate hardware resources
- used to write drivers, firmware, other critical software
- control + compile is significantly faster
Python 
- standard libraries for file manipulation
- faster development times, less control

## SSH
Secure Shell Protocol
- already know about SSH, we need to use it to connect to remote server for labs

Refresher
- Secure Shell, Port 22
- network protocol for sending data (encrypted) over unsecured network
- remote log-in

## Transferring Files for Lab
SFTP | Simple File Transfer Protocol
- `sftp server_addr`
- `sftp> get filename` | client pulls file from server
- `sftp> put filename` | client uploads file to server
- `sftp> get -r dirname` | flag `-r` means recursively, fetches entire file
OR
Use FileZilla to transfer files
- `filezilla` or open for GUI


