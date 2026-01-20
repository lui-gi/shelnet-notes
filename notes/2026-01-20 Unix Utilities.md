# Basic Unix Utilities

recap: use `script [filename.txt]` to record terminal session in file named 'filename.txt'

- sometimes, there will be additional, unwanted characters, they are here for formatting purpose (terminal uses for formatting)
- for submission purposes, clean these unwanted characters 

(my workaround:) I don't want to manually clean up the formatting
-> still use `script`
-> after finished, copy the terminal session
-> echo '[paste]' >> target.txt
- works for now

## Shells

- Bourne Shell
- Korn Shell
- C Shell
- Bourne Again Shell
- Z Shell

many different shells, they have common core functionality
- some differences, of course

Each shell has own programming language

## Running utils

- shell helps us execute the utility
- ex: `date, man, clear, stty, passwd`
- CTRL+D to logout/exit

`stty`: sets or reports terminal I/O characteristics for the device that is standard input | used to modify and print terminal settings
- ex: `stty sane` --> resets all terminal modes to a reasonable, default state
- `stty -a` --> list meta characters (settings)
- interrupt = `^C`, quit = `^\`, kill = `^U`, start = `^Q`, stop = `^S`, suspend = `^Z`

tty = 'tele type writer'

## Special Characters

Erase char before cursor:`^H`
Erase word before cursor:`^W
Erase entire print line: `^U`
Reprint line: `^R`

Interrupt running program (terminate): `^C`
Suspend running program: `^Z`
Stop printing to screen:`^S / ^Q`
Give program end of file: `^D`
^ example:
- cat > test.txt
- [typing]
- `^D` to tell `cat` that we are finished with input

`fg` -> resumes the most recently stopped (SUSPENDED) program in the **f**ore**g**round
- `traceroute [IP]`
- `^Z`
- wait
- `fg`

`bg` -> resumes but does not show in terminal
## More common utils

Word count: `wc` 
File permissions:`file, groups, chgrp, chmod`
Directories: `mkdir, rmdir, cd, pwd`
File manipulating: `mv, cp, rm`
File contents: `cat, more, page, head, tail`
Text editors: `nano, vi, emacs`

## Pathnames

Files stored in secondary storage and arranged in a hierarchical structure

**Absolute** pathname: relative to root dir
- `/` root dir
**Relative** pathname: relative to current working dir
- `./file.txt` (current dir)
- `../other_dir/other_file.txt` (parent dir)
-> (remember LFI; traversal exploit)

## List Files `ls`

`ls -[flag(s)] <file-spec-list`
- input can be set of elements, separated by space
- file-spec = pathname for dir/file

flags of `ls`
- `a`: hidden files
- `l`: long listing (mods/perms, num of blocks, owner of file, bytes, date modified, filename)
- `g`: group
- `F`: put character after file name indicating executable `*`, link @, directory /, socket =
- `s`: number of disk blocks
- `d`: dir details
- `R`: recursive listing

## Showing File Contents

`more <file-spec-list>`
- pauses after each screen like `cat`
- space bar takes to next screen
- `q` is quit
- `enter` shows next line
- `h` help key for commands

`page <file-spec-list`
- same are `more`, clears screen before each page
- quicker

`head -n <file-spec-list>`
- displays n lines from FRONT of file
- `tail` rather than head = n lines from END of file

## Renaming Files with `mv`

Renaming files actually means to change labels in the file hierarchy

`mv -i <old> <new>`
- `i` = inquire (as to double-check our intent)
- ex of i: 'do you want to overwrite?'
`mv -i <dir> <dir>`
- renaming directory

`mv` also used for moving files to new directory
`mv -i <file-spec>`

## Copying Files with `cp`

`cp -i <old> <new>`
- `-r` for recursive

`cp -i <file-spec> <dir>`
`cp -ir <dir> <dir>`
- needs to be recursive to move entire directories

``