# SSL Certificates

## What is SSL?
**Secure Sockets Layer**
- security protocol that creates an encrypted link between a web server and browser (see also [[2026-02-11 PGP  Lookup|PGP encryption]])
- ensures that all data passed between them remains private
- technically succeeded by TLS (Transport Layer Security) even though the term 'SSL' is still widely used 

## SSL/TLS Certificates
Often contain important metadata, such as
- organization names, physical locations
- alternative domain names --> shows us related infrastructure
- validity dates (helps us establish timelines)

**Handshake**
User visits website : SSL handshake occurs
1. Authentication; ensures the server is who it claims to be
2. Encryption; establishing unique key to obfuscate data sent back/forth

## SSL vs. TLS
Technical distinctions between the two

**SSL**
- deprecated/legacy
- vulnerable to modern attacks, such as POODLE
- developed by Netscape in the 90s
**TLS**
- active
- stronger + more secure algorithms
- developed by IETF as an upgrade to SSL 3.0

## Practical
If investigating target, check SSL Fingerprint (ex. JA3) to identify specific types of servers or clients (like bots or malware) EVEN IF they change their IP addr.

`crt.sh` or `Censys`
- use these to search certificate transparency logs for subdomains the target thought were private

check 'issued to' section of a cert to find an email addr. or a specific individual's name

given `.pcap` file
- provide a private key to decrypt SSL traffic and find the flag hidden in payload
### Commands
`openssl s_client -connect example.com:443 -showcerts`
- pull certificate directly without browser (if openssl installed)

or, equivalently with nmap,
`nmap -p 443 --script ssl-cert example.com`

Finding # of certificates in certificate chain:
`openssl s_client -connect cyberskyline.com:443 -showcerts | grep -i "begin"`
- count "begin"