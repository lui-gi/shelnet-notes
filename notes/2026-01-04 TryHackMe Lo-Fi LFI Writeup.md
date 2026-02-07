# Lo-FI Room (THM)

## Scenario:
Vulnerable machine was set up at IP; the challenge directed me to navigate to the URL of the target machine.

The URL loaded a web page that displayed Lo-Fi videos (YT embed) as well as a search bar.
## Steps
Examined the website. Scanned the URL and the webpage itself. 

At first, I thought I had to inject a script in the input field/search bar, however in the url, the query was '?search='

Changed direction, I then began tinkering with the URL itself. When the hyperlinks were clicked, the site would load the respective .php files. I attempted a simple Local File Inclusion Vulnerability, so I started with replacing "game.php" with "../../../../../etc/passwd"

The webpage successfully loaded the sensitive information. I scanned the output, but found no leads.

I then changed course again and tried entering common flag file names, such as flag.txt.

To my surprise, the first attempt worked
Input: ../../../../../flag.txt

Got the flag and completed the room.

## Concepts to Review

- Local File Inclusion
- Path Traversal
- PHP Wrappers
## Reflection

- Do more reading on LFI and LFI Path Traversal
- Figure out the common # of levels it takes to reach root directory
- Find out another way to complete the room, maybe using curl or netcat listener to reverse shell

After reading some of the write-ups of other users, I realized that this room could easily be automated with a custom python script. I'll look into that later -> a lot of these scripts involve a .txt file that includes common paths for path traversal. I'll definitely make one soon.

I also realized that a lot of these more seasoned users have routine they conduct for every CTF room. Some users go ahead and complete an Nmap scan, whilst others went directly to path traversal. --> in summary, I will get used to finding a routine that works the more I complete these CTFs.

### Nmap scan example:
nmap -T4 -n -sC -sV -Pn IP

Flag explanations:
- -T4 | timing; T3 is default, T4 is aggressive, T5 is unstable
- -n | never reverse DNS resolve; by default nmap tries to resolve IPs to hostnames
- -sC | runs NSE (Nmap Scripting Engine); basically a set of common scripts used to gather extra info, very basic
- -sV | scans version of target
- -Pn | does not ping; assumes host is online; [did not realize this, but a lot of CTF machines block ICMP requests, so this is a necessary flag for most Nmap scans during CTFs]

:)