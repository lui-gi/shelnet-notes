# Unix Utils cont.

## File Attributes

use `ls -lsF filename` to see long list of all file attributes
- `-l`: long listing
- `-s`: size of file
- `-F`: display indicators such as a slash (‘/’) immediately after each pathname

File types:
- d for dir
- b for buffered file disk drive
- c for unbuffered file terminal
- l for link
- p for pipe
- s for socket
- f for regular file

`-rw-r--r--`
- First three = permissions for user owner
- next three = permissions for group owner
- last three = permissions for other

File permissions
- Every use in Unix is maintained in **groups**
- r = read
- w = write
- x = execute
- - = no permissions set

## File Type via `file`

`file <file-spec-list>`
- ascertains the type of file, such as binary, ASCII, etc.
## Groups via `groups, chgrp, newgrp`

`groups <userid>`
- Check groups a user belongs to

`chgrp -R <group-name> <file-spec>`
- Change group a file belongs to

`newgrp <group-name>`
- create subshell with effective group id = group
- original shell waits when you run this cmd

`ls -g`
- to include group information

## Changing File Permissions via `chmod`

`chmod` (**ch**ange file **mod**e)
- user, group, other, all = u, g, o, a
- read, write, execute, set = r, w, x, s
- + adds perms
- - removes perms

Example: `-rwxr-xr--`
- owner can read, write, execute
- group can read and execute, not write
- other can read only

`chmod g+w <file-spec>`
- add group with write permission

`chmod u-rw <file-spec>`
- remove user read and write permission

`chmod u+x,g-r <file-spec>`
- adds execution perm for user, removes read perm for group

### via binary/octal 
We can also assign permissions **absolutely** using octal number

`rw-r--r--`
`chmod 644 <file-spec>`

```
	     User.    group.    others
setting.  rw-      r--        r--
binary    110.     100.        100
octal      6         4           4
```
- like on/off switch
- assume any combo of perms is possible

users rwx
111 = 7
g rw-
110 = 6
o -wx
011