# Cryptography Cont.
___
## John the Ripper
hash-cracking tool, jumbo john is commonly used

SecLists: repository with collection of various types of lists used in infosec 
https://github.com/danielmiessler/SecLists

Identifying hashes
https://hashes.com/en/tools/hash_identifier
or via py3: https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master

john --format=[here] --wordlist=[path]

#look-up what "-iF" flag does for grep

### Practice Scenario
Hash = 2e728dd31fb5949bc39cac5a9f066498
- identified using online tool
- used john with format raw-md5
- cracked value = biscuit
D7F4D3CCEE7ACD3DD7FAD3AC2BE2AAE9C44F4E9B7FB802D73136D4C53920140A
- SHA256
- cracked val = microphone

## Windows Authentication Hashes

authentication hashes = stored by OS; hashed versions of passwords
- to access, usually need to have elevated privileges

**NTHash** = format that modern Windows OS machines use when hashing user passwords

Acquiring these hashes:
- dumping SAM (Security Acc. Mgr.) database
- using Active Directory DB

#look-up dumping process: 
- process of exporting a complete compy of information from a DB into one file

john --list=formats
- for finding formats, grep later to find the specific one you are looking for

NTLM format hashes -> use NT flag

## More Cracking

/etc/shadow
- where Linux machine passwords are stored
- also stores additional info regarding passwd, like date modified & expiration
- root access

john requires shadow + passwd due to formatting issues
john no format = john --wordlist= target.txt

Word Mangling: Single Crack Mode
Luigi -> LUigi LUIGi LUiGi Luigi1 Luigi2 (etc..)

GECOS: General Electric Comprehensive OS
- field used in UNIX OS and UNIX-like systems
- 5th field in user account record, stores user's full name, phone #, etc.
^ used in john mangling function within Single Crack Mode

Flag for single crack mode = --single

cat file.txt
482304972034jfhsdjfh
^ append username to beginning before using single mode
like this:
username:482304972034jfhsdjfh

Custom Rules
John wiki: https://www.openwall.com/john/doc/RULES.shtml

john.conf -> write out your rule in the first line
[List.Rules:NameOfRule]
[rules_here]
--rule=[your rule]

Appending all lowercase to end of word in rule format:
Az"[a-z]"

zip2john = converts Zip file to hash format that John can use

"unzip" to unzip via terminal

rar2john = for rar
unrar x filename.txt: extract rar via terminal

## SSH Cracking

private key passwd - rsa

ssh2john = another conversion tool

#look-up RSA: public-key cryptography system