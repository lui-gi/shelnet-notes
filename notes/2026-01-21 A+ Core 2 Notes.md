# A+ Core 2 (220-1202) Notes
*these notes are back from when I was currently studying Core 2, wanted to share them*

repair vs. refresh installation

repair:

• attempts to replace the existing version of the OS files with a new copy of the SAME version

• use when trying to repair a Windows that will not boot, or corrupted files

refresh:

• recopy system files and revert most settings to default, preserves personalization settings, data files, and apps that were installed ONLY through windows store

• apps installed outside of Windows store will be deleted

--------------------------------------------------------------------------------

Quick (Standard Format) vs. Low-level

Quick Format

• can be recovered with the right software

• sets up file system and installs a boot sector

• clears master file table but not the data

Regular format

• overwrites every sector with zeros

• default for Windows Vista and later

• cannot recover the data

Low-level

• provided at the factory

• not recommended for the user

• not something we do as the technician

--------------------------------------------------------------------------------

piggybacking

• employ mantrap or access control vestibule

• basically a turnstile or rotating door that opens only after you scan in

--------------------------------------------------------------------------------

(linux) chmod, ls

ls

• list directory contents

• shows us all of the files and directories in a particular subdirectory

• ls -l: long list of information such as permissions, file size, etc

• ls -la: also shows hidden

chmod [entity+-permission] [object]

• change mode

• its purpose is to 'modify the read, write, OR execution permissions of an obj in the Linux file system'

• can also change the mode of a file system object

• u = user/owner, g = group

• + means add permission

• x = execute permission

--------------------------------------------------------------------------------

SOP

standard operating procedure:

• list of step by step actions that must be completed for any given task

--------------------------------------------------------------------------------

tracert, ICMP, TTL

tracert

• trace route: determine the route a packet takes to reach a destination

• maps entire path

• a command in Windows

• diagnoses a network path

• uses ICMP packets with incrementally increasing TTL values

ICMP

• internet control message protocol

• used by ping and tracert

• sends control and error messages

TTL

• time to live: the number of hops a packet is allowed to travel

• hop, in this context, is a single connection when a packet PASSES a router

• each pass, the router is responsible for decreasing TTL by one

• if TTL = 0, packet is discarded and TTL exceeded msg is sent back to origin

--------------------------------------------------------------------------------

Udemy Test 4, 5 Wrong Answers

Wrong Answers | Corrections

trojan and virus:

• A trojan deceives the user by pretending to be something else

• A virus can reproduce and replicate itself: spreads through file systems or across the network

vishing

• vishing is when an attacker gets information by speaking (using VoIP) over the phone

• think: voice-fishing

other social engineering

phishing:

• when an attacker tries to trick someone into giving information by pretending to be someone trustworthy

• they differ in their communication methods

• 3 types of phishing -> phishing, vishing, smishing

phishing: email

vishing: over phone or voicemail

smishing: text messages (SMS)

targeted phishing:

• when attackers are more specific with their targets

spear phishing: aimed at a specific person or group, attacker uses inside information to seem more believable

whaling: spear phishing that targets a **high-profile executive**, like a CEO

shutdown command

context: shutdown /s on windows

/s: shut down

/l: log off

/h: hibernate or sleep

/r: reboot

editing text file on server (Linux)

vi: (visual utility) -> screen-oriented text editor, terminal screen acts as a window

WRONG: ps: current running processes

developer mode (android)

• should be disabled if not actively testing application

• why? --> exposes device to security risks

• using airplane mode is not practical because it blocks the network-based testing features of your app

Windows 10 Editions (CPU)

Home: one physical CPU, 128 GB RAM

Pro: two physical CPUS, 2 TB RAM

Enterprise: two physical CPUs, 6 TB RAM

Pro for Workstations: four physical CPUS, 6 TB RAM

Windows 11 Editions

Home: 128 GB RAM, Workgroup but NO DOMAIN, Remote Desktop CLIENT only, no full BitLocker

Pro: 2 TB RAM, Workgroup AND DOMAIN, Full Remote Desktop, BitLocker

Enteprise: 6 TB RAM, everything^

SPICE

Simple Protocol for Independent Computing Environments

• remote desktop tool for controlling VMs

• use it to view and interact with screen of virtual machine

RDP vs. VNC

RDP (Remote Desktop Protocol)

• not just sending a video of the screen, digital

• data is encrypted, if port is open it can be a target for brute-force attacks

• mostly for Windows

VNC (Virtual Network Computing)

• sharing graphical desktop

• connects to and from various OS like macOS, Linux, Windows

• slower than RDP

Cache Clearing

increases browser performance, does not directly mitigate multimedia-based exploits

Change Types

Standard Change

• A low risk pre-approved task that happens frequently

• does not need the full approval process every time bc it is common and well-documented

• ex: replacing a broken monitor

Normal Change

• planned change that is not an emergency BUT not a routine (not pre-approved)

• MUST follow entire change management process, submits formal request, risk analysis, and approval from change board

• ex: replacing a core network switch

Emergency Change

• high-risk change

• must be implemented immediately

• it can bypass some of the slower approval steps bc it is urgent

• ex: deploying a patch for a zero-day vulnerability

End-of-life support

LTS (Long-time support): supported for ~10 years

Rolling release: app is frequently updated through the release of new features over time

TACACS+

Terminal Access Controller Access-Control System

security protocol to handle remote authentication: AAA (Authentication, Authorization, Accounting) protocols, similar to RADIUS

• controls who can log in and manage network devices like routers and switches

RADIUS

Remote Authentication Dial-In User Service

• centralized doorman for network

• all network devices check in with central RADIUS server to see who is allowed in

A common use case would be WPA2/WPA-3 Enterprise WI-Fi

• WPA-Personal: one single shared password, used at home

• WPA-Enterprise: for business, each user logs into the network with their own username and password, these credentials are sent into a RADIUS server who checks them in (against an Active Directory database)

bootrec /fixmbr

the first 512-byte sector on the hard disk is ALWAYS THE MBR

• if that is broken, use /fixmbr

Cross-site scripting vs. SQL Injection

Cross site scripting: malicious scripts are injected into trusted websites, attacker uses web app to send malicious code in browser side script to a different end-user

SQL: code injection that attacks data-driver applications, SQL statements are inserted into an entry field

• the SQL statement is inserted into an entry field, usually dumping database contents to attacker

Kerberos

a network authentication protocol that allows devices to prove their identity over a non-secure network

• SSO, you sign in once and Keberos gives you a ticket that allows you to access different services without re-authenticating

• mutual authentication: protection against on-path attacks

• ^ you verifies server's identity, server verifies your identity

• default authentication in Microsoft Windows Active Directory

On-path attack

An attack where it occurs on the victim's own device, usually through malware; it acts as a proxy and intercepts traffic before it gets to the final destination

• man-in-the-middle

• ARP poisoning: attacker sends fake ARP response (their device claims to have the router's IP address but contains attacker's MAC address),your PC now updates its own ARP with this new malicious info, all the traffic we send (meant for router) now directs to the attacker

• ^ Address Resolution Protocol -> used by network devices to associate an IP address with a physical MAC address, no security

Screened subnet

a buffer zone between the untrusted public internet and your secure internal network

--additional layer of security

WPA-TKIP, WPA-CCMP

Explain these acronyms please:

BEC EDR IAM MDR PAM RADIUS RSR SAML TKIP TOTP UAC WinRM XDR

robocopy

--robust copy

command to move files: can mirror source to destination, copy files along with permissions, attributes, timestamps

--------------------------------------------------------------------------------

backups

incremental backup:

• saves all the files that have changed since the last backup of ANY kind (can be last incremental or full backup)

• full restore = last full backup + ALL incremental backups since then

differential backup

• saves all the files that have changed since the last full backup

• Monday (_) , Tuesday (M + T), Wednesday(M+T+W)

• full restore = Last full backup + most recent differential backup

synthetic backup:

• shortcut to making a new full backup

• at the end of the week, it takes original full backup from Sunday and merges it with all the incremental changes from Mon-Thur

--------------------------------------------------------------------------------

Splash Screens: Compliance and Branding

A **splash screen** is a graphic, message, or logo that is displayed on the screen during the startup process of a system or application, or sometimes upon logging in 

--------------------------------------------------------------------------------

ESD strap

An **ESD strap** (Electrostatic Discharge strap), also often referred to as an anti-static strap, is a critical tool used to protect sensitive electronic components.

**ARP Spoofing (or ARP Poisoning) Explained:**

This is a specific type of on-path network attack performed on a local IP subnet. It works because the Address Resolution Protocol (ARP) itself has no inherent security built in 

An attacker exploits this by sending a fraudulent ARP response directly to a device, such as a laptop, even though the laptop never sent an ARP request. This malicious response spoofs the IP address of the legitimate router but includes the attacker's own MAC address.

The victim's device receives this response and modifies its internal ARP cache, redirecting traffic meant for the router to the attacker's workstation instead . The attacker can now sit in the middle and monitor the conversation 


--------------------------------------------------------------------------------

Resilient File System 

ReFS is not available across all versions of Windows; it is generally limited to versions designed for high-end usage and servers:

• **Windows Server:** ReFS has integration available starting with **Windows Server 2012 and later** .

• **Windows 10:** It is supported by **Windows 10 Pro for Workstations** .

• **Windows 11:** It is supported in **Windows 11 Enterprise** editions .


--------------------------------------------------------------------------------

incident response

1. identify

2. report

3. preserve data/device

--------------------------------------------------------------------------------

Resource Monitor vs Performance Monitor

**Resource Monitor** gives you a snapshot of performance right now, while **Performance Monitor** focuses on gathering historical data over time.

Resource Monitor (`resmon.exe`)

Resource Monitor provides a **detailed, real-time view** of your system's performance metrics 

Performance Monitor (`perfmon.msc`)

Performance Monitor is designed for comprehensive **long-term analysis** 

--------------------------------------------------------------------------------

Kerberos Protocol and Single Sign-On Authentication

Kerberos is a foundational network authentication protocol designed primarily to enable **Single Sign-On (SSO)** across a network 

--------------------------------------------------------------------------------

WPA2-PSK and Enterprise Authentication


The **-PSK** (Pre-Shared Key) part defines the authentication mode of that protocol

**WPA2/WPA3-Personal (PSK):** This is the configuration where everyone uses the **same 256-bit key** (password or passphrase) to gain access to the wireless network . This mode is primarily used for personal use or in SOHO environments 

--------------------------------------------------------------------------------

degaussing

• demagnetizing a hard drive to erase its stored data

• CANNOT reuse after

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------

antimalware service executable

• a sign that your workstation has outdated virus definitions

• to resolve efficiently, update Windows Defender and reboot

--------------------------------------------------------------------------------

ransomware step 1

always isolate host if infected, get it away from the rest of the network

--------------------------------------------------------------------------------

practice test 1

Of course. Here is a list of the topics we've covered:

• rm -rf command 111

• rm -f on a directory 2

• SOW (Statement of Work)

• msinfo32 vs. msconfig 3

• UPnP (Universal Plug and Play) 4

• Hardware token 5555

• Smart card 66

• PIV card 7

• Credential manager / Password manager 8

• Group Policy 9999

• Group Policy vs. security groups 10

• "Windows Update service not running" troubleshooting

• Reboot vs. re-registering DLLs

• Botnet vs. zombie

• Refresh installation

• Refresh vs. repair installation 11111111

• Smart card vs. key fob 12121212

• Smart card for digitally signed emails 13131313

• SFTP

• DMZ / screened subnet 14

• Print Spooler log location 15

• Chain of custody 16

• Legal hold

• Change request 17

• Backout plan vs. backup plan 18181818

• su command 19

• X.509 format

• Rooting 20

• Sideloading vs. rooting 21

• rebuildbcd vs. fixboot 22

--------------------------------------------------------------------------------

rollback plan vs. backup plan

rollback: aka backout

• details how to revert system to original if update fails

backup

• alternate ways to complete a change successfully when the original fails

--------------------------------------------------------------------------------

sideloading vs. rooting

sideloading:

• allows Android device to install apps without Play Store using APKs

rooting:

• is an Android device that has been hacked to provide the user with administrative rights to install unapproved apps, update OS, delete unwanted apps, underclock or overclock the processor, replace firmware and customize anything else

rooting is not required to sideload

--------------------------------------------------------------------------------

reboot!

reboot if arbitrary software issue

--------------------------------------------------------------------------------

bootrec /rebuildbcd

bcd:

• boot configuration data

• if cannot find Windows installation

• OR one of the operating systems is missing from the menu

bootrec /fixboot

• repair boot sector of a drive (corrupted/damaged boot sector)

• malware, disk error, failed OS update

the difference:

• rebuildbcd: OS MISSING

• fixboot: BOOT MGR MISSING

--------------------------------------------------------------------------------

change request

Elements of a Change Request

For the exam, you should be familiar with the common elements included in a change request form and the overall management process. These typically include:

• **Purpose of the Change:** A clear reason why the change is necessary, such as applying a security fix or upgrading an applicaiton.

• **Scope of the Change:** Details on what systems will be affected and the expected duration or downtime

• **Risk Analysis:** An evaluation of what could go wrong during the change and the potential impact of _not_ making the change

• **Rollback Plan:** A documented procedure for reverting to the original state if the change fails

• **End-User Acceptance:** Confirmation from the people who use the system that they approve of the change and the plan

• **Change Board Approval:** The final approval from a committee that oversees and approves all changes

--------------------------------------------------------------------------------

channel availability

channel availability

• reducing: reduces bandwidth for all users

--------------------------------------------------------------------------------

smart card v. key fob

smart card:

• securely stores digital certificate

• important in PIV devices

key fob

• uses RFID for proximity access, like a door

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

net

net:

• relates to OS's network features and connectivity

net view:

• used to determine what network shares might be available on a specified server or device

net use:

• connects to an available network share and assign it a LOCAL drive etter

• syntax: net use

--------------------------------------------------------------------------------


--------------------------------------------------------------------------------


• **netstat** provides the network connections (active TCP connections and ports) 

• The **-b** option adds the name of the executable file (`.exe`) that initiated that network communication 

This combination (`netstat -b`) is exactly what a system administrator needs to track down a suspicious application (`Chrome.exe` in one example) making unauthorized connections 


--------------------------------------------------------------------------------

tracert vs. pathping

tracert:

• determines the entire route a packet takes to reach destination, maps its path

• uses ICMP and TTL, each hop TTL -= 1

pathping:

• operates tracert and roundtrip test

• shows additional detailed statistics such as round trip time and network packet loss

--------------------------------------------------------------------------------

Default Gateway

The **default gateway** is indeed the device (usually a router) that a network device, like your PC, uses to send traffic to devices that are **outside** of its immediate local network (subnet) 

--------------------------------------------------------------------------------

Registry Editor

regedit.exe

• master database in Windows

• hierarchical structure, stores configuration information for everything in the OS

• details about kernel, device drivers, services, UI, SAM (Security Account Manager), applications, etc.

--------------------------------------------------------------------------------


32-bit vs 64-bit

32-bit max RAM is 4 GB, 64-bit architecture allows for vastly more

--------------------------------------------------------------------------------

Windows Versions RAM

Max RAM:

Windows 10 Home 32 - 4 GB

Windows 10 Pro 32 - 4 GB

Windows 10 Enteprise 32 - 4 GB

Windows 10 Home 64 - 128 GB

Windows 10 Pro 64 - 2 TB

Windows 10 Pro for workstations 64 - 6 TB

Windows 10 Enterprise 64 - 6 TB

Windows 11 - ALL 64-Bit

Windows 11 Home - 128 GB

Windows 11 Pro - 2 TB

Windows 11 Enterprise - 6 TB



--------------------------------------------------------------------------------



--------------------------------------------------------------------------------

