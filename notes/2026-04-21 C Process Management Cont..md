# C Process Management Cont.

## Zombie Processes
- a process cannot leave the system until parent process accepts its termination code (returned by exit)
  
- if parent process is dead; `init` adopts process and accepts code -> `orphan process`
  
- if the parent process is alive but unwilling to accept the child's termination code -> `zombie process`
(it never executes `wait()`)
the child process will remain a `zombie process`

**Zombie Example**
```
(boilerplate headers)
int main() {
	pid _t pid;
	pid = fork();
	
	// branch based on return value from fork()
	
	if (pid != 0) {
		// never terminate, never execute a wait()
		while (1)
			sleep(1000);
	}
	else {
		exit(42); //exit with silly num
	}
	return 0;
}
```
- the parent process continues to run but it is not waiting/willing to receive the termination code from its child, eventually making the child a 'zombie' process

```
bash $
__________________________________
$ zombie & (ampersand = bg mode)
[1] 684
$ ps
	684 p4 S 0:00 zombie
	685 p4 Z 0:00 (zombie <zombie>)
	686 p4 R 0:00 ps
$ kill 684
[1]+ Terminated zombie
$ ps
	688 p4 R 0:00 ps
$

NOTE:
#### Why Did the Zombie Disappear When You Killed the Parent?

This is the key insight. When the parent died, the zombie child got **adopted by init (PID 1)**. Init automatically calls `wait()` on all adopted children — so it immediately reaped the zombie and cleaned it up. That's why it vanished from `ps`.
```

**Zombie vs. Orphan Process**
```
||Zombie|Orphan|
|---|---|---|
|Parent|Alive but ignoring|Dead|
|Child|Dead|Alive|
|Problem?|Yes — wastes resources|Not really — init adopts it|
|Fix|Parent calls `wait()`|Linux handles it automatically|
```

`wait()`
- makes the parent process pause and wait for one of its child processes to finish
- afterward, cleans up the child's leftover entry from the process table

## Waiting for a Child: `wait()`
- if a process executes a wait(),
- and one ore more children are already zombies,
- then `wait()` returns immediately with the status of one of the zombies

`wait()` is a system call!

Example Program
```
(boilerplate)

int main() {
	int pid, status, childPid;
	printf("I'm the parent and my PID is %d\n", getpid());
	
	pid = fork(); //duplicate
	
	if (pid != 0) {
		printf("I'm the parent with PID %d and PPID %d\n", getpid(), getppid());
		
		childPid = wait(&status);
		printf("A child with PID %d terminated with exit code %d\n", childPid, status >> 8);
		
	}
	else {
		printf("I'm the child with PID %d and PPID %d\n", getpid(), getppid());
		exit(42);
	}
	
	printf("PID %d terminates", getpid());
	return 0;
}
```

`pid`: unique numerical ID assigned by the kernel to every active process
`ppid`: PID of the process that spawned the ==current== one. every process has a "parent" that created it

