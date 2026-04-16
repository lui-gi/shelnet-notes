# C Process Management

## Process Management
- every process in UNIX has
- some code
- some data
- a stack
- a unique process ID / PID

## Init Process
when UNIX boots, there is only process, called init, with PID = 1

the only way to create a new process it to ==duplicate an existing process==
thus, init is the ancestor of all subsequent processes

initially, `init` duplicates (`forks`) several times, and each child process replaces it code (`execs`) with the code of the executable `getty` which is responsible for user logins

tree-like structure

## Process in Memory
```
[ stack ] max
	|
	|
	V
			available memory for heap & stack
	^
	|
	|
[ heap ]
[ data ]
[ text ] 0

```

## Memory Layout of a C program
```
[ arc, argv ] = int main(int argc, char *argv[])
[ stack ]  int *values; int i
	|
	V
	
	^
	|
[ heap ] = (int *)(malloc(sizeof(int)*5);
[ uninitialized data ] = int x;
[ initialized data ] = int y = 15;
[ text ] = the executable version of our program
```

## Process States

```
new --(admitted)--> ready --(scheduler dispatch)--> running --(exit)--> terminated

running --(interrupt)--> ready
running --(I/O or event wait)--> waiting --(I/O or event completion)--> ready
```

"`new`" = just created, not ready for execution
- perhaps OS is still allocating memory for the process
- does not immediately mean it is ready for execution
- when sys ready to provide sufficient resources, then the process will be formally `admitted` to `ready` state

## Process Creation and Termination

```
at first, only init process

fork() --parent--> wait --resumes-->
	|
	+ --child--> exec() --> exit() --> wait --resumes-->
```

Examples:
```
[ Terminal ]
$ gcc hello.c -o hello
$ ./hello

```
note: terminal itself is a process, when we try to execute `hello`,
- terminal executes an instruction called `fork()`
- `fork()` duplicates terminal
- the CODE of this *duplicate terminal* will be replaced with the CODE of `hello` 
- thus, this new process is now the `hello` process

^ uses the system calls: `fork()` and `exec()`

## What's a Fork()
``` 
parent     fork()     child
[ code ] -----------> [ code ] 
PID = 100             PID = 240
```
- child is an exact copy of the parent process
-  they have their own memory space

`fork()` returns the value of the PID of its child (the duplicate)
- thus, the child (duplicate) will be assigned a PID of 0

Example:
```
parent | PID = 100
int main() {
	printf("Hello");
	pid = fork(); ==== LEFT OFF HERE ====
	printf("World");
	return 0;
}

child | PID = 240
int main() {
	printf("Hello");
	pid = fork(); (locally, PID = 0)
	printf("World"); === STARTS HERE ====
	return 0;
}

Output:
HelloWorldWorld
```
Return type of pid = predefined pid type
aka unsigned int
`pid_t pid = fork();`

## How to use a fork()?

Related header files
- `#include <sys/types.h> and <unistd.h>`

Call once but return twice

cannot predict which process runs first

run the same code concurrently, but have completely separate stack and data space

## Process Creation
```
#include <stdio.h>
#include <unistd.h>

int main() {
	printf("Before fork()\n");
	
	pid_t pid = fork();
	if (pid == 0) {
		//code executed by the child process
		printf("Child Process: PID = %d\n", getpid());
	}
	else if (pid > 0) {
		// code executed by the parent process
		printf("Parent PID = %d, Child PID = %d\n", getpid(), pid);
	}
	else {
		// fork() failed
		perror("fork failed");
	}
	printf("This line is executed by both parent and child processes\n");
	return 0;
}
```

who is calling `getpid()`?
- `getpid()` returns pid of the CALLING process

## Observing Parallelism

```
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	printf("Start of the program (PID = %d)\n", getpid());
	pid_t pid = fork();
	if (pid == 0) {
		// child
		for (int i = 0; i < 5; i++) {
			printf("Child process (PID = %d): i = %d\n", getpid(), i);
			sleep(1);
		}
	} else if (pid > 0) {
		//parent
		for (int i = 0; i < 5; i++) {
			printf("Parent process (PID = %d): i = %d\n", getpid(), i);
			sleep(1);
		}
	}
	else {
		perror("fork failed");
	}
	return 0;
}
```

key takeaways ^:
- we do not know which process will execute first, thus we cannot predict the output
- the output could either be `2400` or `0240`, it's really up to the OS

Example:
```
fork()
fork()
print()
```
fork()
- fork()
- ---print()
- print()
fork()
- print
print()
- 4 processes

how about 
```
fork()
fork()
fork()
print()
```
- 8 processes

## More about fork()
reasons for fork to fail
- too many processes in the system
- the total number of processes for the real uid (user ID) exceeds the limit
- CHILD_MAX

usages of fork
- duplicate a process to run different sections of code
- (network servers)
- want to run a different program
- fork+exec

## Example Using `execl()`
```
#include <unistd.h>
#include <stdio.h>

int main() 
{
	printf("I'm process %d and I'm about to exec a ls-l\n", getpid()); // pid of parent
	execl("/bin/ls", "ls", "-l", NULL); //executes ls
	printf("The line should never be executed\n");
	return 0;
}

Output --------------------------- >

$ ./myexec
I'm process 61713 and I'm about to exec a ls -l
total 6
-rwxr-xr-x 1 mrahman21 staff 33736 Nov 18 00:08 a.out
-rwxr-xr-x 1 mrahman21 staff 33736 Nov 18 00:08 a1.out
-rwxr-xr-x 1 mrahman21 staff 33736 Nov 18 00:08 a2.out
etc..
```

exec with list

Why does printf not print?
- exec replaces the current parent code with the other program's code (in this case, the code of `ls`)

## A simple example using fork()
```
getpid() returns the PID(int) of current process
getppid() returns the PID(int) of parent process

#include <stdio.h>
#include <unistd.h>

int main() {
	int pid;
	printf("I am the original process with PID %d and PPID %d\n", getpid(), getppid());
	pid = fork();
	if (pid != 0)
	{
		printf("i am parent with PID %d and PPID %d", getpid(), getppid());
		printf("my child's pid is %d", pid);
	}
	else {
		printf("i am th child with pid %d and ppid %d", getpid(), getppid());
	}
}
```
```
Output:
$ ./myfork
I'm the original process with PID 639 and PPID 416
I'm the parent with 639..;
(fill in)
```

