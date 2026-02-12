# National Cyber League | Gymnasium Day 1

## OSINT Module

### Metadata

Image Metadata: make sure to look out for these
- make/model of camera
- coords
- date created
- exposure time

### DNS Lookup

DNS Records: know them and what they do | reference RFC XXXX

DNSKEY:
- this DNS record holds the DNSSEC public signing key

-> DNSSEC: Domain Name System Security Extensions
- it stores the public key used by resolvers to verify digital signatures, also authenticates DNS data integrity (so it can prevent DNS spoofing and hijacking)
- prevents attacks like cache poisoning and man-in-the-middle attacks
- uses 'chain of trust' from root zone -> indiv. domain

AAAA:
- used to map hostnames to IPv6 addresses
- know A (IPv4)

NS:
- delegates a DNS zone
- basically tells internet where to look for that specific domain's info
- `ns1.example.com`

### Threat Intel

CVE: Common Vulnerabilities and Exposures (see [[2026-01-03 John the Ripper Hash Cracking|hash cracking]] for working with discovered hashes)
- industry-standard
- publicly disclosed
- large large large list of cybersecurity vulnerabilities in software and hardware

--> use nvd.nist.gov or cve.org

- cisa.gov: allowed me to find the first 1.0.1 version of OpenSSL that was not affected by heartbleed (see [[2026-02-11 SSL Certificates|SSL certificates]])
- RFC 854: describes Telnet (first RFC num)
- SQL Slammer worm, 2003: it payload = 376 bytes; its tiny size allowed all of the malicious code to fit into a single UDP packet
- samy: computer worm; carries a payload that displays 'but most of all, samy is my hero"

### HTTP Headers

## Request Headers
Accept: used to identify the acceptable content types that can be returned
User-Agent: used to identify client software that made the request
Referer: used to show what URI linked to the resource being requested
