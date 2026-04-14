# C Standard Library vs. System Calls

## Opening a file: `open()`

## Mode Flags
r/w flags: O_RDONLY, O_WRONLY, O_RDWR
misc. flags:
- O_APPEND: position file pointer at the end of file before each write
- O_CREAT: if file does not exist, create it
- O_EXCL: if O_CREAT is set and file exists, then open() fails,  (O_CREAT|O_EXCL are used together, open will create the file *only if it does not already exist*)
- O_NONBLOCK: for named pipes
- O_TRUNC:  if file exists, it is truncated to length 0 (remove all characters of existing content)

## `open()` Example
- tmpfd = open(tmpName, O_CREAT | O_RDWR, 0600)
- the file should be created if it doesn't exist
- it should be opened in read-write mode
- only read-write permissions for the user

- fd = open(fileName, O_RDONLY);
- if the file does not exist or there is no permission to read it, it returns -1

## Read from a regular file: `read()`

`ssize_t read(int fd, void *buf, size_t count)`

- copies up to `count` bytes from the file referenced by `fd` into the buffer pointer to by `buf`
- the bytes are read from current position (maintained by offset/file position) which is then updated accordingly

It returns ==num of bytes copied==
- returns 0 if attempts to copy after end of file
- returns -1 if unsuccessful

Example:
- charsRead = read(fd, buffer, BUFFER_SIZE);
- if (charsRead == 0) break;
- if (charsRead == -1) fatalError();

## Example: `read()` system call
```
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

int main()
{
	int fd = open("filename.txt", O_RDONLY);
	if (fd == -1) {
		printf("Error Number %d\n", errno);
		perror("Wrong happened");
		exit(1);
	}
	
	char buffer[100];
	ssize_t bytesRead = read(fd, buffer, sizeof(buffer));
	write(STDOUT_FILENO, buffer, bytesRead); //STDOUT_FILENO is a constant
	return 0;
}
```

## Write to a regular file: `write()`
`ssize_t write(int fd, void *buf, size_t count)`
- writes the count bytes in buf to the file referenced by fd, and returns the number of bytes written
- the bytes are written into current position (File position or offset), which is then updated accordingly
- if O_APPEND was set, file position is set to end of file before each write

## Example: writing using `write()`

```
int main()
{
	int fd, bytes written;
	char str_to_write[] = "Computer Science!\n";
	
	fd = open("unbuffered.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
	if (fd == -1) {
		exit(1);
	}
	for (int i = 0; i < 1000000; i++) {
		bytes_written = write(fd, str_to_write, strlen(str_to_write));
		printf("%d bytes were written.\n", bytes_written);
		close(fd);
		return 0;
	}
}
```

## Moving the file pointer: `lseek()`
`off_t lseek (int fd, off_t offset, int mode)`
- changes file pointer
- mode determines how offset is to be used
- mode = SEEK_SET //offset relative to start of file
- mode = SEEK_CUR //offset relative to current position of file
- mode = SEEK_END //offset relative to end of file

aside: `fscanf, fread, fwrite, fclose` = file-related standard library functions

lseek fails if moved before start of file
- returns new file position if successful
- returns -1 if unsuccessful

Example:
`lseek(fd, lineStart[i], SEEK_SET); //lineStart[i] is an offset in bytes`
`charsRead = read(fd, buffer, lineStart[i+1] - lineStart[i]);`

To find out current position use:
`currentOffset = lseek(fd, o, SEEK_CUR);

lseek() Example:
```
int main(void) {
	int fd;
	char buffer[20];
	ssize_t bytesRead;
	
	fd = open("example.txt", O_RDONLY);
	if (fd == -1 ) {
		perror("open");
		return 1;
	}
	
	if (lseek(fd, 5, SEEK_SET) == -1) {
		perror("lseek");
		close(fd);
		return 1;
	}
	
	 bytesRead = read(fd, buffer, sizeof(buffer) - 1);
	 buffer[bytesRead] = '\0';
	 printf("Data read: %s\n", buffer);
	 close(fd);
	 return 0;
}
```

## `unlink()`
- unlink is a UNIX/POSIX system call used to remove a name (link) from the filesystem
- if the file has no other ==hard links== and no process has it open, the file's data is deleted immediately
- if the file is open by a process, the data remains until the last file descriptor is closed

unlink() Example:
```
int main(void) {
	int fd;
	char buffer[50];
	fd = open("unlink_example.txt", O_CREAT | O_WRONLY, 0644);
	if (fd == -1) {
		perror("open");
		return 1;
	}
	
	write(fd, "Hello..unlinking example\n", 25);
	sleep(10);
	
	if (unlink("unlink_example.txt") ==1) {
		perror("unlink");
		close(fd);
		return 1;
	}
	
	printf("File unlinked, but still open.\n");
	sleep(10);
	close(fd);
	printf("File descriptor closed. File is now fully removed.\n");
	return 0;

}
```

## Hard Link / Soft Link
- a hard link is another directory entry that points to the same inode as the original file
```
multiple filenames -> same inode
all hards linsk are equal (no "original" file)
file data exists as long as at least one hard link remains
```

- a soft link (symbolic link) is a separate file that stores the pathname of another file (works for both file and directory)
```
points to a filename, not an inode
has its own inode
can point to a file across filesystems
can become dangling if the target is deleted
```
## Writing binary files
```
int main()
{
	FILE *wf;
	int number = 33;
	
	//open the file in binary write mode
	wf = fopen("data.bin", "wb");
	if (wf == NULL) {
		perror("Error opening file");
		return 1;
	}
	
	//write the integer to the file
	fwrite(&number, sizeof(int), 1, wf));
	fclose(wf);
	return 0;
}
```

## Reading binary files
```
int main() {
	FILE *rf;
	int num;
	rf = fopen("data.bin", "rb");
	if (rf == NULL ) {
		perror("Error opening file");
		return 1;
	}
	if (fread(&num, sizeof(int), 1, rf) != 1) {
		perror("Error reading file");
		fclose(rf);
		return 1;
	}
	fclose(rf);
	printf("The number read from the file is %d\n", num);
	return 0;
}
```

## Process
a process is an instance of a running program
(not the same as program or processor)

process provides each program with two key abstractions:
- logical control flow (each program seems to have exclusive use of the CPU)
- private address space (each program seems to have exclusive use of main memory)

How are these illusions maintained?
- process executions interleaved (multitasking)
- address spaces managed by virtual memory system

