# Metasploit Cont.

*watching One Piece before this.. I'm on Skypiea*

Exploit: takes advantage of a vulnerability on a target machine (code)

Vulnerability: flaw in the design of the target machine that allows attackers to get hands on confidential information or control of the target machine

Payload: code that run on the target machine; more specific use of exploit, allows us to specify the outcome we want such as gaining access to confidential info

## Modules
Auxiliary: supporting modules like crawlers and scanners

Encoders: allows the attacker to "encode" the exploit/payload, this attempts to bypass signature-based antivirus software
- signature-based antivirus compare suspicious files to their large database of known threats

Evasion: direct attempt to evade the antivirus

Exploits

NOPs: No OPeration; does nothing, so it is useful to "cushion" a long stream of payloads

Payloads: code that runs on the target machine, executed to achieve desired result
- Adapters: converts payloads to different format (example: we can wrap a normal payload inside a bash adapter -> one bash command that executes the entire payload)
- Singles: no additional components needed to run (no additional download)
- Stages: allows us to use large payloads; stages are downloaded by a stager

Identifying single vs. staged payloads
shell_reverse_tcp -> single
shell/reverse_tcp ->staged

Post: modules post-exploitation

### Clarification
Exploits: the 'how'
Payloads: the 'what'
Exploit = code that leverages vulnerabiliies to gain access
Payloads = code that is malicious and delivered by the exploit to perform malicious actions such as stealing data
## Command Line Usage

'use' + index#

'show options' = shows the context of module we are currently using
- depending on selected exploit, there are variables we must set
- ^ these will reset if we change to another exploit unless explicitly set as global var.

'show' + module_type = lists avilable modules

'back' = leave context

'info' = author, relevant sourdces, references

'search' + [CVE nums, exploit names, target system]
- enter 'use' + output_number (alternative way to use)
- append 'type:[module type]'

Exploit Rankings: https://github.com/rapid7/metasploit-framework/wiki/Exploit-Ranking; https://docs.metasploit.com/docs/using-metasploit/intermediate/exploit-ranking.html

'set' + PARAM_VAL
- once we enter the context of a module

'unset' | 'unset all'

'setg' = global
- will be used until Metasplo
- it is exited or 'unsetg'

'exploit' :: 'run' -> launch module after vars set
- '-z' = run exploit+bg session as soon as it opens
- ^ creates session in backgrund rather than in a new shell; allows us to remain in main msfconsole interface

'check' = checks if target machine is vulnerable; does not exploit target machine

'background' = backgrounds current session prompt so we can continue typing commands in msfconsole
- alt: CTRL + Z

'sessions' = see all current running sessions
- '-i' to interact with specified session


### Common Params
- RHOSTS: ipaddr of target machine; can be single IP or range; can also set path to file that contains IPs
- RPORT: port on target system that contains vulnerability (typically an application port)
- PAYLOAD
- LHOST: our attacking machine
- LPORT: port we use for reverse shell to connect to; must set it to a port num that is not being used
- SESSION: every connection to target machine has session ID






