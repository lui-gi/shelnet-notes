# Arrays and Functions in C

## Arrays
- scalar; capable of holding a single data item
- aggregate variables; capable of holding a collections of values

Array is a data structure; contains number of data values all of which have the **same type**.
- a derived data type, meaning we can apply the concept of array on any basic data type
- we can apply array -> integers or -> floating point or -> char

Structures (records): covered later

### One-Dimensional Arrays
- the simplest kind of array
- the elements, the values of items, of a 1D array are conceptually arranged one after another in a single row

**Declaration**
`int a[8];`
- an array of 8 integers
- 0 -> 8
- therefore, we are reserving 32 bytes
- 1 location = 4 bytes
`char ch[10]`
- array of 10 characters
- 0 -> 9
- reserving 40 bytes

or
```
#define N 20
float num[N];
```
- array of 20 floating point

`++a[i];`
- value at index i will increase

### Arrays + For Loop
```
# clears a
for(i = 0; i < N; i++) {
	a[i] = 0;
}

# sums elements of a
for(i = 0; i < N; i++) {
	sum += a[i];
}

# taking inputs into array

int myarray[10];
for(i = 0; i < N; i++) {
	scanf("%d", &myarray[i]);
}
```

```
#include <stdio.h>
#include <stdlib.h>

int main() {
    int a[5];
    int N = 5;
    int i;
    
    printf("Enter 5 integers: ");
    for(i = 0; i < N; i++) {
	    scanf("%d", &a[i]);
    }
    
    int sum = 0;
    for(i = 0; i < N; i++) {
	    sum += a[i];
    }
    printf("%d", sum);

    return 0;
}
```

### rand()
`int random_num = rand();`
if we want within a range: use modulus
`random_num = rand() % 10`
0 - 9

srand() -> seed
#look-up 

### indexing
C does not require that subscript bounds be checked
- thus, if a subscript goes out of range, the program's behavior is undefined

### array subscript
can be any integer expression, see below
```
a[i+k*10]

a[i++]
```

be careful for while loops:
```
i = 0;
while( i < N)
	a[i++] = 0; (CORRECT)
	
	the same as 
	a[i] = 0
	i++;
	
vs. a[++i] (WRONG)
the same as 
i++;
a[i] = 0;

^ wrong bc we are clearing the NEXT index, not the current


```

**in one single statement, do not use the same variable multiple times if we are updating its value via assignment (ex: `x*x*x++`)**

#question-a
**How can undesirable side effects be avoided when assigning values in an array using a loop structure in programming?**
-> Using a for loop with a separate increment statement

### array initialization
always initialize array when you declare it

`int a[2] = {1, 2};`

- if we do not initialize completely when we declare, the empty slots are automatically assigned 0s

`int a[5] = {1, 2};`
thus `{1, 2, 0, 0, 0}`

### sizeof Operator
- `sizeof` operator can determine the size of an array in bytes
ex: `int a[10]`
`sizeof(a)` returns 40 (as each int = 4 bytes)

measure size of an array:
- `sizeof(a) / sizeof(a[0]);`
give us the number of elements in the array

### Multidimensional Array
`int a[5][9];` -> 5 rows 9 columns
```
 0 1 2 3 4 5 6 7 8 
0
1
2
3
4
```

How are these stored in memory?
-> Row-Major order

First, see 1D arrays in memory:
`0 1 2 3 .. N-1`

2D in memory:
- represent in row order, ie. the first elements in memory is all of row 1, then row 2, etc..
`r1c1 r1c2 r1c3 ... r2c1 r2c2 r2c3 ... rnc1 rnc2 rnc3`
`ROW 1 -------------- ROW 2 ------------- ROW N-1`

### multidimensional initialization
```
int m[2][2] = {
	1,2,3,4
};```
 ^ is valid and possible
```

## Functions
Functions are defined in a C file instead of a class
- each function is, in essence, a small program with its own declarations and statements
- using functions, programs are divided into small pieces that are easier for us as well as others to understand and modify

### Defining / Calling Functions

Every function must have set of parameters, a name, and return type

- example of defining function
```
double average(double a, double b)
{
	return (a+b) / 2;
}
```

- example of calling a function
```
avg = average(x/2, y*2);
printf("Average: %g\n", average(x,y));
```

```
return-type function-name(parameters)
{
	declarations
	statements
}
```

- Function may not return arrays
- Specifying that the return type is void indicates that the function doesn't return a value
- If the return type is omitted, the function is presumed to return a value of type int

example of wrong syntax:
`double avg(double a,b)`
must specify b in full -> `double b`

**Not mandatory**: declarations