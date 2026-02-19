# Cryptography (NCL)
Main objective in context of CTFs:
- identifying flawed implementation
- mathematical weaknesses
ALL to recover plaintext

## Encoding/Obfuscation ?
Data may not always be encrypted, but sometimes simply **encoded**
- Base64; alphanumeric char set and sometimes padded with `=`
- Hexadecimal; Base16, uses chars 0-9 and a-f
- Rot13/Caesar Cipher; substitution where letters are shifted. example; `cvpbPGS` shifted by 13 = `picoCTF`

*Look out for limited character set + no special symbols* -> Base decoder or Caesar shift

## Symmetric Cryptography
Where **one** key is used for both encrypting and decrypting.

### XOR 
very important bitwise operation, where
```
0 ^ 0 = 0
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1

Theory:
A ^ B = C
then
A ^ C = B
```
*basically, same bits return 0 whereas at least one difference returns 1*

- if we know part of the flag format, such as `flag{`, we can XOR this format against the ciphertext to recover the flag

### Block Ciphers (AES)
AES is modern standard
- ECB (Electronic Codebook): the same plaintext block always results in the same CIPHERTEXT block
- CBC (Cipher Block Chaining): vulnerable to padding oracle attacks or bit-flipping attacks

## Asymmetric Cryptography (RSA)
Math-heavy: relies on difficulty of factoring the product of two extremely large prime numbers

**Math behind RSA**
1. pick two large primes `p` and `q`
2. Calculate `n = p * q`
3. Calculate the totient `φ(n) = (p - 1)(q - 1)`
4. Choose encryption exponent `e` (usually large prime, but more often it is `65537)
5. Calculate private exponent `d`, where `(e * d)(mod φ(n)) = 1`

**CTF context**
Find small `e`, for example if e=3 and message block is small, just cube root ciphertext

If `n` is small, factor using `factordb.com` to find `p, q` then calculate `d`

If the same `n` is used with two different e values to encrypt the same message

## Hashing + MACs
Hashes are always one way functions
- (MD5, SHA-1, SHA-256)
Therefore the only way to "crack" them is to compare them against a list of known values via Brute Force (such as tools like [[2026-01-03 John the Ripper Hash Cracking]]) or Rainbow Tables (many tools online)

**Length Extension Attacks:**
- if server uses Hash(Password + Message (salt)), we can append data to message and calculate a valid new hash without knowing the password

## Common Tools
- CyberChef: great for XOR, simple ciphers, encoding
- RsaCtfTool: automates known attacks against weak RSA keys
- Hashcat or John: cracking password hashes
- SageMath: writing custom scripts to handle modular arithmetic
- Python, similar to ^

## NCL Scratch work

0x73636f7270696f6e 
- hex, convert to either UTF8 or decimal (UTF8 in this case for a string)

c2NyaWJibGU=, bG9sbGlwb3A=
- ends with `=` and limited char set, Base64

 ```
 01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101
 ```
 - returned Base64, convert that to UTF8
 
 iveghny ynxr
 - use shifter until plaintext deciphered

hzuvob lyerlfh xzev
- use CyberChef -> Atbash

```
- .... . / ... . -.-. .-. . - / --- ..-. / --. . - - .. -. --. / .- .... . .- -.. / .. ... / --. . - - .. -. --. / ... - .- .-. - . -.. / ... -.- -.-- / -.. -.- ...- -... / ----. ---.. .---- -....
```
- morse code


`Y ln xkv lubj swlzqvkht, A vmzb pjk bbua we ddgs ILQ-GQYU-8026` 
- vignere decode, use given key to decode
- characteristics:
- shifts with every letter

F daS-eefn n KZ3eheadty.YI8lta oiwy-Q0. r aI2
- rail fence decode (given key)

## RSA Math Scratch

```
n = 1079
e = 43
c = 996 894 379 631 894 82 379 852 631 677 677 194 893
```

-> remember n = pq

`c = m^e (mod n)`
```
c` = m^e` (mod n`)
996 ... = m^43 (mod 1079)
```

find p: (smaller prime)
`n/q` = 13

q, larger prime = 83

```
n = 1079
1079 = (13)(83)

```

https://www.cs.drexel.edu/~popyack/Courses/CSP/Fa17/notes/10.1_Cryptography/RSA_Express_EncryptDecrypt_v2.html

https://www.dcode.fr/rsa-cipher

- used dcode.fr to get d values as well as p,q
- used drexel to decrypt integer ciphertext

