# Functions in C and Pointers

## Function declaration / definition
`return-type function-name(parameters)`
- we announce that we are going to use a function with x return type, y name, z parameters
- we do not specify what it does yet
- we can omit name of parameters if we want -> `double avg(double, double);`
- always has terminating `;`

Function definition is the block within the `{}`
- no ending `;`

## Arguments vs. Parameters

**Parameters**
- placeholders, var names in a function
- dummy names that represent valuers to be supplied when the function is called

**Arguments**
- expressions that appear in function calls

Arrays are often used as arguments
```
int f(int a[])
{

}
```
- behaves like a **pointer** rather than an array

```
void f(int b[])
{
	...
}

main() 
{
	int a[5] = {1,2,3,4,5,6};
	f(a);
}
```
--> when we pass `a[]` to `f()`, `b` POINTS to the original array, it holds the memory address of the first element
-> `b = &a[0]`
- thus, we we use `sizeof(b)`, we do not get 20 bytes like `sizeof(a)`, instead we get the size of the pointer (4 bytes for 32 bit systems)

pointers hold the memory address of a variable

**Array Arguments**
- C does not know how long the array is
- we need to supply the length (if needed in function) as additional argument
```
int funct(int a[], int n)
 where n = len(a[])
```

## Program Termination
return statement
- using return in main is one way to exit the program;
- `return expr;`

exit function
- calling `exit` it any function is another way to terminate a program
- `exit` belongs to **stdlib.h** , be sure to include if we want to use exit
- `exit(expr);`

## Recursion
when function calls itself to solve a smaller version of the same problem
- recursive case

cannot use recursion if we cannot break it down to smaller pieces of the same task

each recursive function needs a base case to stop calling itself

Example:
`f(n) = 1 + 2 + 3 + ... + n`
`f(10) = 1 + 2 + ... + 10`
etc.

`f(10) = 10 + f(9)`
`f(9) = 9 + f(8)`
...
`f(1) = 1 + f(0)`
TERMINATE @ f(0) | Base Case

**Russian Nesting Doll Example**
```
int count_dolls(this doll)
	answer = this_doll + all dolls inside outer doll
	return answer
```

## Recursive Functions
- a function is recursive if it calls itself

**Factorial Example**
```
int fact(int n)
{
	if(n <= 1)
		return 1;
	else
		return n * fact(n-1);
}
```
STACK below (for fact(3))
```
fact(3)
	fact(2)
		fact(1), return 1
	fact(2), return 2*1
fact(3), return 3*2

similarly,

fact(1)
fact(2)
fact(3)
```

**Power function**
```
int power(int x, int n)
	return n == 0 ? 1 : x * power(x, n-1)
	
	equivalently,
	
	if n == 0
		return 1
	else
		return x * power(x, n-1)
```
Trace
```
power(5,3)
	power(5,2)
		power(5,1)
			power(5,0) return 1
		power(5,1) return 5*1
	power(5,2) return 5*5
power(5,3) return 5*25
```

## math.h and GCC
math.h is not automatically linked by GCC
- we should `#include <math.h>`

to compile: `gcc *.c -o * -lm`
- link *l*ibrary *m*ath

## Static Variables
- local variables
- hold values even after you exit the function

**LOCAL VARIABLE EXAMPLE**
```
int f( int a, int b)
{
	int sum = 0;
	sum = sum + a + b;
	return sum;
}

main()
{
	f(5,3);
}
```
- after we exit `f(5,3)`, variables a and b are trashed
- `static int sum = 0` -> even after we exit, the value of sum will be retained 
- thus, we we ^ run `f()` again, sum will be 8

**STATIC EXAMPLE**
```
int incr(int i)
{
	static int count = 0; // only initializes as 0 once, further iterations of this function will keep count maintained and not reinitialize as 0
	
	count = count + i;
	return (count);
}

main() 
{
	int i, j;
	for (i = 0; i <= 4; i++)
	{
		j = incr(i);
	}
}
```

```
test()
	static int x = 5;
	int y = 5;
	x++;
	y++;
	print x y

test()
	x = 5
	y = 5
	x = 6
	y = 6
	print 6 6
test()
	x = 6
	y = 5
	x = 7
	y = 6
	print 7 6
test()

```

## Pointers 
How do variables store in memory?
- main mem is divided into bytes
- each byte has a unique address
- each variable occupies one or more memory
- the address of the first byte is said to be the address of the variable

## Pointer Variable
ex:
- int i = 1; (suppose sizeof(int) is 4 bytes)
- address of variable i is 2000

**Pointer Variable ^**
- we can store the memory address of a variable 

## Declaring Pointer Variables
- pointer variable must be preceded by an asterisk
- every pointer variable points to objects of a particular type (reference type)

Examples:
- 