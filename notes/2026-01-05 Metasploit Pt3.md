# Metasploit Scanning

`/usr/share/wordlists/MetasploitRoom/MetasploitWordlist.txt`

'search portscan' -> modules that allow us to scan open ports on target machine

^ these require us to set options -> 'show options'
- CONCURRENCY (num of targets to be scanned concurrently)
- PORTS (range x-y)
- RHOSTS (target)
- THREADS (more = faster)

we can perform nmap scans from msfconsole prompt
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


