# C pt2

**Keywords** can't be used as **identifiers** (variable names) see [[2026-02-03 C Fundamentals and Compilation|C fundamentals]] for basics

ex:
- auto
- break
- case
- char
- const

## Basic Data Types
char: 1 byte
- -128 .. 127
short: 2 bytes
- -32768 .. 32767
int: 4 bytes
- -2,147,483,648 .. 2,147,483,647
long: 4 bytes (8 on 64-bit)
- -2,147,483,648 .. 2,147,483,647
long long: 8 bytes
- -2^63 .. 2^63-1
float: 4 bytes
- 3.4E+/-38 (7 digits)
double: 8 bytes
- 1.7E+/-308 (15 digits)

==1 byte = 8 bits==

Checking via compiler:
```
printf("Bytes reserved by short int: %d", sizeof(short));

printf("Bytes reserved by long int: %d", sizeof(long));

printf("Bytes reserved by double: %d", sizeof(double));

```

## 32-bit vs. 64-bit
ALU: Arithmetic Logic Unit
- does all the calculations on the computer
capped by the bit-architecture of the local machine

## Signed vs. Unsigned Integers
Signed: sign matters
Unsigned: positive only

Range change:

- example: char range is -128 .. 127, however unsigned char range is 0 .. 255 (2x;  for all types of data)

characters are represented in memory with numbers
- ex: A -> 65, '0' -> 48 .. '9' -> 57

## Constants
int x = 25;
float f = 2.75;
char ch = 'A';
^ all constants

### There are rules for constants:

--Int--
octal constants must begin with 0 
- ex: int a = 053; (compiler recognizes it as octal)
hexadecimal must begin with 0 and x

long type must end with l or L

unsigned must end with U or u

--Floating--
floating point must be stored as a double-precision number
- ex: 57.0 or 57. or 57.0e0
- NOT 57 only

floating single precision must end with F or f

floating long type must end with L or l
- ex: 57.0L

Char: single quotes 'char'
String literal: double quotes "string"
Special chars: 
- \n: newline
- \t: tab
- `\\`: backslash
- `\"` double quotes

## Declaring variables

int height;
float profit;
height and profit = identifiers

We can also declare several at the same time:
`int height, length, width, volume;`

## Assignment

Assigning a constant to a variable
profit = 2150;

Assign the value of an expr. to a variable.
density = `mass * volume`;
## Initialization
both declaration and assignment in one line

assigning some values to a variable

note: some uninitialized variables are automatically set to zero when a program begins to execute

## Automatic Initialization

local variables: only exist within functions
- unknown automatic initialization
static variables: does not get destroyed after function call #look-up 
- automatically initialized to 0
global variables: not part of any functions
- automatically initialized to 0

## Format Specifiers
(reading and writing integers)

```
usigned int u;
scanf("%u", &u);  /* reads u in base 10 */ 
printf("%u", u);  /* writes u in base 10 */ 

scanf("%o", &u);  /* reads u in base 8 */ 
printf("%o", u);  /* writes u in base 8 */ 

scanf("%x", &u);  /* reads u in base 16 */ 
printf("%x", u);  /* writes u in base 16 */ 

long int x;
scanf("%ld", &x);
printf("%ld", x);

short int x;
scanf("%hd", &x);
printf("%hd", x);
```

For a single character: %c

If we want a float with only 3 digits after decimal point: %.3f

## Type Casting/Conversions

### Implicit conversion
- narrower types are converted into wider types ==automatically==

Compiler marks our highest data type per operation, attempts to convert to higher size with higher range

```
int a = 2, b = 3;
float c = 2.25, d;
d = a + b + c;
/*   Result is d = float + float + float    */
```

Size (increasing)
Float -> double -> long double

int -> unsigned int -> long int -> unsigned long int

==Operations between floats and doubles== will cause data loss
```
int a=1, d=0;
double b=2.55, c=0;

c = a + b; // a is converted to double

HOWEVER (replacing ^)
d = a + b; // causes data loss
int = double + double;
```
^ that is to say, cannot have 
smaller = larger 
due to smaller range of the left-hand side 

### Explicit Conversions
- conversion forced by casts
- may lose precision
examples of loss:
float to int causes truncation of fractional part
double to float causes rounding of digits
long to int causes dropping of the higher order bits

```
int a=1, d=0;
double b=2.55, c=0;

d = (int) (a + b); 

a converted to double FIRST
(int) (3.55)
AFTER, a + b is casted to int
3
```

More examples:
```
float f, frac_part;
frac_part = f - (int) f;

example:
14.235 - (int) 14.235
= 0.235
```

```
float quotient;
int dividend, divisor;
quotient = (float) dividend, divisor

^ must convert at least one of them

example:

int a = 43;
int b = 4;
float c;
c = a/b;

(c = 10.0)
```

```
short in i;
int j = 1000;
i = j*j; (WRONG)
```