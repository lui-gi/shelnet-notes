# PGP Lookup

## What is PGP?
Pretty Good Privacy: it is an encryption program that provides cryptographic privacy + authentication for data communication

### Uses
- used to verify identities via digital signatures
- used to decrypt hidden messages via Public/Private key pair system

## How it Works

Asymmetric Encryption (see also [[2026-02-11 SSL Certificates|SSL/TLS]]);
- public key; anyone can use it to encrypt a message to send to you OR to verify a signature that YOU made
- private key; secret key that only you can use to decrypt messages sent to YOU or to sign messages to prove that they came from YOU

Look out for the metadata or the trust relationship associated with a key

1. Identity Verification
   PGP key often contains User ID (real name + email addr.)
   -> therefore person 1 signs person 2's key, it proves they know each other (proves connection)
2. Finding Keys
   - keys are stored on keyservers, public directories
   - if given a handle, we can search PHP keyservers for said handle to find an associated email or comment
   - common keyservers: `keyserver.ubuntu.com`, `pgp.mit.edu`, `keys.openpgp.org`

## GPG Commands

import key
- `gpg --import key_filename.asc`
list keys
- `gpg --list-keys`
decrypt a file
- `gpg -d encrypted_file.gpg`
verify a signature
- `gpg --verify signature.asc original_file.txt`

### Example
Find username --> search keyserver via `gpg --search-keys username`
Search returns key with email `username@user.com`
Use the email to search for registered domains/social accounts

## NCL Scratch Notes

UTC format: terminates via Z
example: `2050-12-26T20:36:17Z`

Finding key fingerprint given email:
- navigate to keyserver, this case `keyserver.ubuntu.com`
- search database using given email
- download key, then navigate to directory and run `gpg --import [key].asc`
- run `gpg --fingerprint [email]`

Fingerprint looks something like:
```
pub   rsa4096 2013-02-25 [SC]
      DED3 8747 CEEF C789 FDC3  A615 4CF2 79C5 C042 4907
uid           [ unknown] cPanel Master Key <security@cpanel.net>
```
(full hash)
