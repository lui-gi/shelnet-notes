# C Fundamentals
Characteristics:
- low level, small (relies on library for std functions), permissive (doesn't prevent you from making mistakes, assumes you know what you are doing)

Pros:
C is also portable and efficient (can be transferred over very easily). 
- flexible, powerful, has standard library
- great integration with UNIX

Weaknesses of C:
- error-prone
- difficult to understand/modify

Basic Syntax
```
#include <stdio.h> //pre-processor, import i/o library

int main(void) // main function for our outputs
{
	printf("Hello.");
	return 0; // Terminate this function
	
}
```
ANY line that starts with # is a preprocessor directive. (headers)
--> instructions to the compiler before the actual compilation begins

## Compiling and Linking
Before execution of a program:
1) **preprocessing**: obeys directives (#)
2) **compiling**: translates the program to machine instructions (object code)
3) **linking**: combines the object code by the compiler along with any additional code needed to yield a COMPLETE EXECUTABLE program (e.g. printf from library)
*preprocessor usually integrated with the compiler*

ie, linking connects our program to other required object files. For example, after compiling, our program is in machine instructions however anything from external libraries such as printf is still in a placeholder. Linker will link the additional object code for each placeholder.

## Directives
- commands intended for the preprocessor
- <stdio.h> is a header containing info about C's standard i/o library (headers file ext is `.h`)

Primary function of directives: ==to instruct the preprocessor about code compilation requirements==
## Functions

Library functions are provided as part of the C implementation
- function that computes a value -> uses return statement to specify what value it returns
`return x+1;`

a function's ==definition==: the block of code within the function
- writing piece of code to specify what the function shall do

function call ex: `printf("Hello.\n");`

## The `main` function
mandatory; gets called automatically when program is executed
- returns a status code; 0 = normal program termination
- if no return statement at end of main function, most compilers produce a warning message

## Statement
every line is a statement
- a command to be executed
- every statement terminated with ;

Asking a function to perform its assigned task = "calling" the function

## Printing Strings
when the printf function displays **string literal** (characters enclosed in double quotes), it doesn't show the quotes

printf doesn't automatically advance to the next output line (newline) when it finishes printing
- \n to do so, known as the new-line character

## Identifiers
names for variables, functions, macros, and other entities 

may contain letters, digits, and underscores but ==MUST begin with a letter or underscore==
- "-" is illegal

C is case-sensitive

