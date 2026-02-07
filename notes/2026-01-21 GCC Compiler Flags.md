# CompOrg Lab: GCC Compiling

## Example program to input in hello.c
```
#include <stdio.h>

int main (int argc, char *argv[]) {
 printf("hello world.\n"); 
 return 0; 
 }
```

**gcc** --> the GNU C compiler
- GNU = Unix-like OS / collection of free software

## `gcc` usage

`-o`: specifies output filename
- `gcc source.c -o executable_file`
- creates an executable file named executable_file (default is a.out)
- used during compilation or linking to name the final binary

`-S`: tells GCC compiler to stop after generating assembly code (file.c --> file.s); creates .s file from OUR source code
- converts C source code to human-readable assembly language
- STOPS after generating assembly (compilation stage) but BEFORE the assembly and linking stages

`-c`: tells the GCC compiler to compile/assemble the source files but STOP before the linking stage; creates an object file (file.o) for each source file rather than one final executable program
- `gcc -c hello.s`

`-v`: verbose; prints detailed info about the compilation process, showing the version numbers of the compiler components + the actual cmds executed for each stage (preprocessing, compiling, assembling, linking) as they run

#look-up flows
## Other

`diff`: verify changes between two files
- `diff file1 file2`

