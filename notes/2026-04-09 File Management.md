# File Management in C

## Quick Recap: `struct` Memory Alignment
```
struct stu_a {
	int i;
	char c;
}

size = 8, because 4 bytes + 1 bytes, but we round up to 8 because memory addr. has to be multiple of largest member 

thus, the 3 additional bytes are used for padding
```

## File Management
- managing a file:
Open -> Read/Write -> Close

e.g.
open a text file for reading
```
FILE *fp; -> specialized data type
fp = fopen("test.txt", "r");
```
read up to n-1 characters from input stream referenced by file pointer
```
char buff[255]; //n = 255
fgets(buff, 255, (FILE*)fp);
printf("%s\n", buff);
```

Format:
`fgets(buffer, sizeof(buffer), (FILE *)fp)`
- last arg = read from file, not `stdin`

## Writing string to a file
- write the stream to the output stream referenced by file pointer
`fputs("hello from System-kevek programming", fp);`

- close a file
`fclose(fp);`

Example: writing to a file
```
#include <stdio.h>
#include <stdlib.h>

int main() 
{
	FILE *fp;
	char *filename = "filename.txt";
	char text[] = "system level programming";
	
	// OPEN FILE IN WRITE MODE
	fp = fopen(filename, "w");
	if (fp == NULL) {
		printf("Error opening file for writing.\n");
		return 1;
	}
	
	// WRITE TEXT TO THE FILE
	fprint(fp, "%s\n", text);
	printf("Text written to the file successfully.\n");
	
	// CLOSE the file after writing
	
	fclose(fp);
	return 0;
}
```

Example: reading from a file
```
#include <stdio.h>
#include <stdlib.h>

int main() 
{
	FILE *fp;
	char *filename = "filename.txt";
	char text[] = "system level programming";
	
	// OPEN FILE IN READ MODE
	fp = fopen(filename, "r");
	if (fp == NULL) {
		printf("File cannot be opened.\n");
		return 1;
	}
	
	// READ THE CONTENT OF THE FILE AND DISPLAY IT
	fprint("reading from the file:\n");
	while (fgets(buffer, sizeof(buffer), fp) != NULL)
	{
		printf("%s", buffer);
	}
	
	// CLOSE the file after reading
	
	fclose(fp);
	return 0;
}


```

FILE OPENING ERRORS;
- if DNE
- disk is full
- invalid path
- file permission error, etc.

## File Opening Modes
Text Files modes
- r = reading
- w = writing (file need not exist, overwrites if exists)
- a = appending, file need not exist, appends if exists
- r+ = reading and writing, starting at beginning, overwrites without truncation
- w+ = reading and writing, truncate if file exists
- a+ = reading and writing, append if file exists/goes at the end

Binary files modes
- rb = reading
- wb = writing
- ab = appending, file need not exist/appends if exists
- r+b or rb+ = reading and writing, starting at beginning
- w+b or wb+ = reading and writing, truncate if file exists
- a+b or ab+ = reading and writing, append if file exists

Binary stores in bytes / binary sequence

Example: `representing 123`
- Text mode: `ASCII -> binary` aka `49 50 51 -> 00110010, etc`
- Binary mode: `00...0001111011`

## Systems Programming
UNIX System Calls: C functions that provide access to the fiule system, processes, and error handling

System Calls grouped into 3 main categories:
- File Management
- Process Management
- Error Handling

`User -> System Calls -> UNIX (OS)`
- system calls written in C (Unix written in C)

Everything we do must go through system calls

Example:
```
[ printf ] -- standard C function
	|
	|
	|
	V
[ write() ] -- system call
	|
	|
	|
	V
[ Unix Kernel ]
```

## Error Handling
- function perror() describes the system-call error
- void perror(char * str)
^
standard C function in stdio.h
displays str followed by a description of the last system call error.
error 0 is displayed if no error (May show success)

Ex:
```
perror("wrong");
Wrong: ______
Wrong: ______
```

## File Management
- system calls: open, read, write, lseek (traverse within file), unlink, close
- typical sequence:
`Open -> read/write -> close`

fopen() vs. open() example
`fopen`: C's standard library
`open`: unix-provided API (system call)

similarly, fscanf() vs. read()
similarly, fprintf(), vs. write()

`scanf`(): reads from keyboard
`read`(): system call

## Standard Library vs. System Calls

Standard library functions (e.g., fopen, fclose, fscanf, fprintf):
- higher level, handle buffered I/O, and work with FILE * pointers
- optimized performance but no direct control

System calls (open, read, write, close):
- lower level, handle unbuffered I/O, and work with file descriptors (not with FILE * pointers)
- provide finer control over file permissions, modes, and flags
- less optimized but direct real-time processing

## Typical File I/O Sequence
- int fd; -> file descriptor 0: stdin, 1: stdout, 2: stderror (shows on terminal)
- fd = open(fileName, ...);
- if (fd == -1) // DEAL WITH ERROR
- read(fd, ...) // READ FROM FILE
- write(fd, ...) // WRITE TO FILE
- lseek(fd, ...) // SEEK WITHIN FILE
- close(fd); // CLOSE FILE

## Opening a File: open()
```
int open(char *filename, int mode [,int permissions])
```

Allows you to open an existing file or create a new file for r/w
- fileName: absolute or relative path name
- mode: bitwise or-ing of a r/w flag together with zero or mre miscellaneous flags (next slide)
- permissions (optional): supplied only when file is created (ex. 0600 octal)

## Mode Flags
r/w flags: O_RDONLY, O_WRONLY, O_RDWR
misc. flags:
- O_APPEND: position file pointer at the end of file before each write
- O_CREAT: if the file does not exist, create it
- O_EXCL: if O_CREAT is set and file exists then open() fails (O_CREATE | O_EXCL are used together, open will create the file only if it does not already exist)
- O_NONBLOCK: for named pipes (file-like interface for IPC)
- O_TRUNC: if file exists it is truncated to length 0 -> opens file, it exists, truncates ALL existing contents

## Open() Example
`tmpfd = open(tmpName, O_CREAT | O_RDWR, 0600);`
the file should be created if it doesn't exist
it should be opened in read-write mode
only read-write permissions for the user

