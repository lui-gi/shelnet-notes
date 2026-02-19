# Unix Utils (final) + Intro to C
*system level prog*

## vi Editor

- two modes: command mode and text entry mode
- use ESC to switch back to command mode

text entry (INSERT): `i, I, a, A, o, O, R`
- `:wq` : write + quit

line ranges:
- 1,$
- 1,.
- .,$
- .,.-2
- 5,12
- .,.+12

==Indexing starts at 1, not 0==

Common commands:
- `:set number`: allows us to see line numbers
- `:3,7d` deletes lines from 3 to 7 (inclusive)
- `:.` refers to current line
- `:$` refers to the last line in the file
- `+ or -` moves range up or down relative to current line
- `:.,$d` deletes from the current line to the end of the file
- `:.,+3d` deletes from the current line to three lines after (below) the current line
- `u` undo
- `:1,3t 10` copies/transfers lines 1 to 3 and pastes them after line 10 ==(does not overwrite)==
- `:5,10m 15` moves lines 5 to 10 after line 15
- `start,ends/pattern/replacement/flags` 
- `1,10s/foo/bar/g`
- replaces 'foo' with 'bar' in lines 1 to 10; g means global; s means substitute
- `:noh` remove highlight (no highlight)
- `:n` go to line number n
- `:$` last line

Cursor Movement:
- `h` left
- `j` down
- `k` up
- `l` right
- `o` beginning of line 
- `^` first non-whitespace character in line
- `$` end of line
- `w` next word
- `b` prev word

Viewing:
- CTRL-D (down by half a screen)
- CTRL-U (up by half a screen)
- CTRL-F (forward one screen)
- CTRL-B (back one screen)

Deletion:
- `x` delete char under cursor
- `dw` delete word
- `dd` delete line (or D)
- `:(range)d` delete many lines 

Replacement:
- `r` replace char under cursor
- `cw` replace word under cursor
- `cc` replace entire line
- `4s` sub next 4 chars

Yanking (Copying):
- `:<range>y` yank lines
- `5yy` yank 5 lines from current location
- `p` paste from buffer after cursor
- `P` paste from buffer before cursor
- `:n` + `p` after line n, then p

Searching:
- `/w` seach forward
- `?w` search backward
- `n` next
- `N` next, opposite

Replacing:
- `:<range>s/old/new/` next occurrence in current lines
- `:<range>s/old/new/g` all occurrence in current lines
- `%s/old/new/g` all occurrences in file

Saving/Loading:
- `:w <filename>` write to file
- `:w` write again
- `:<range>w <filename>` write within range with filename
- `:wq` write and quit
- `:e <filename>` edit new file
- `:r <filename>` read (insert) a file

Quitting:
- `:q` quit
- `:q!` quit without writing
- `:x` exit and write IF changed

Miscellaneous:
- CTRL-L redraw screen
- `:!<cmd>` execute shell command

## Regular Expression | regex (see [[2026-01-29 Regular Expression Metacharacters|regex metacharacters]] for special characters)

- a pattern describing a certain amount of text
- a 'match' is a piece of text that pattern was found to correspond to by the ==regex== processing software

\d = decimal digit
{} = repetition operator
\d{1,2} = 1 to 2 decimal digits; at most two digits
\d{4} = 4 decimal digits 

/ = separator or enclosure
- some regex software uses / as a delimiter
- careful: sometimes we need a  LITERAL '/', if so we include a `'\'` to offset the delimiting 


`ex: /\d{1,2}\/\d{1,2}\/\d{4}/` for DD/MM/YYYY
- notice we use  `\` to offset the following `/`

`ex2: /\d{1,3}\.\d{1,3}\.\d{1,3}/`
for IP address (255.255.255.255 etc.)

Step 1) 
\d{1,3} x 3

Step 2)
`.` in between each instance, however
`.` has a special meaning in regex, known as a ==meta== character

Step 3)
'Escape' the special meaning of `.`, therefore we include a `\` to offset the following `.`

PRACTICE:
- MM-DD-YY
- (123)-456-7890

## [[2026-01-20 Unix Shell Commands|grep]]: general/global regex print

- `-E` flag for 'extended': allows the use of extended regular expressions (EREs) for pattern matching
- ^ sometimes, we have to use the `-P` flag (Perl-Compatible RegEx)
- rather than `/` as the delimiter, it will be `'`

#look-up delimiting syntax, grep vs. other regex processing software