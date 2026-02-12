# C Types Cont. and Common Functions

## User-defined types (builds on [[2026-02-05 C Data Types and Type Casting|C data types]])
`typedef` gives names to types
- good for making programs more human-understandable
- allows us to 'create' our own data type
- we don't actually making a NEW data type, just renaming/assigning aliases to existing data types

Let's suppose we want to make a data type for a student's marks...
```
typedef int Marks
Marks a;
```

Example:
```
typedef int BOOL
BOOL flag;
```

Example 2:
```
typedef shortint Int16
typedef long int Int32
typedef unsigned char Byte

Int16 = 0;
Int32 b = 12;
Byte c = 1;
```
*Recap: short int takes 2 bytes, aka 16 bits*

Example 3:
```
typedef struct {int age; char *name} person;
person people;
```

## Formatted Input/Output

read input: `scanf` (see [[2026-02-03 C Fundamentals and Compilation|C fundamentals]] for basics)
- `scanf("%d", &x)`
- Read an integer (%d) and put it into the address of x

print output: `printf`
- `printf("%d", x)`
- print an integer, that integer will COME from the variable x

Both of these must be supplied with a *format string* as a 1st argument.
- the format string may contain both ordinary characters and conversion specifications (format specifier)

### Common Errors
These examples will cause meaningless input (no compile errors though)
`printf("%d %d\n", i);`
- because we only supply one integer
`printf("%d\n", i, j);`
- because we supply two integer
`printf("%f %d\n", i, x);`
- because we supply them in the wrong order (assuming int is i and x is float)

Casting works ^
`printf(%f %d\n", i, (int) x);`

**For `scanf`, ensure to include ampersand `&`**
(usually but not always)

Do not use `&` in printf when wanting to print vars

### printf Example

```
int main(void)  
{  
	int i; float x;  
	i = 40;  
	x = 839.21f;  
	printf(" %d|%5d %-5d|%5.3d|\n", i, i, i, i);  
	printf("%10.3f %10.3e|%-10g|\n", x, x, x);  
	return 0;  
}  
Output:  
40| 40 40 | 040|  
839.210 8.392e+02|839.21 |  
8
```
The vertical line `|` divides the screen as a collection of symbols

`%5d` reserves 5 spaces for the 40, 40 is 2 digits, so 2 spaces are used on the right hand side to print 40
`%-5d` the same, so it uses the lefthand side to print 40
`%5.3d` means we will at least fill 3 spaces, so we fill the last 1 out of 3 spaces (bc 2 were used for 40) with 0

`%10.3f` means reserve 10 but use 3 decimal places after decimal point
`%10.3e` means reserve 10 but print in scientific notation 
`%-10g `means use 10 significant digits

#elaborative-interrogation 
What would happen if we had a number greater than 10 digits?
 
### scanf Example
Taking this example input:
`1-20.3-4.0e3`

Call of scanf is 
`scanf("%d%d%f%f", &i, &j, &x, &y)`

scanf would process this input as
- %d: 1 into j
- %d: -20 into j
- %f: 0.3 into x
- %f: -4.0x10^3 into 

```
$ ./test

Hello. Enter nums:

123-23.45-26.56

123-230.450000-26.559999%
```
==Some numbers cannot be accurately represented using binary number system, which is why we see 26.559999==

`scanf("%d, %d", &i, &j);`
- this will try to match the comma literally, therefore an input such as `12 34` will not match

### Exercise

`scanf("%4d %*d%d", &year, &code, &count);`
Input: 1234567 89

What values does our computer assign to each variable?
- year = first 4 integer digits, 1234
- `%*d` ignore the immediate next in the input buffer (567) =/= 567
- code = then read from the next, 89
- count = 

## Why float, double, long double?
For increased precision + bigger range

```
int main() 
{
	float f = 1.0f / 3.0f;
	double d = 1.0 / 3.0;
	long double ld = 1.0L / 3.0L;
	printf("float: %.20f\n", f);
	printf("double: %.20lf\n", d);
	printf("long double: %.20Lf\n", ld);
	return 0;

Output:
float: 0.33333334326744079590
double: 0.33333333333333331483
long double: 0.33333333333333333334
}
```

## Adding Fractions `addfrac.c`
```
/* Adds two fractions */  
#include<stdio.h>  

int main(void)  
{  
	int num1, denom1, num2, denom2;  
	int result_num, result_denom;  
	printf("Enter first fraction: ");  
	scanf("%d/%d", &num1, &denom1);  
	printf("Enter second fraction: ");  
	scanf("%d/%d", &num2, &denom2);  
	result_num = num1 * denom2 + num2 *denom1;  
	result_denom = denom1 * denom2;  
	printf("The sum is %d/%d\n",result_num, result_denom) ;  
	return 0;  
}  
```
Include `/` in the scanf because we want to literally match the desired input

## Expressions
Arithmetic operators
`+ - * / % ++ --` etc..
- `++` is increment, equivalent to x = x +1
- `--` is decrement, equivalent to y = y + 1
- similar to other programming languages

Relational operator
`< > <= >= !=`
- In C, they return values 0 and 1 rather than FALSE and TRUE
- 0 is false
- and non-zero values including 1 is TRUE, even negative vals

## Operator Precedence
*priority = precedence*

Highest: unary operators
Same precedence: `* / %`; therefore this will go from left to right
Lowest: binary operators

**Unary operations example:**
+3    -5

**Binary operations example:**
2+3    4-5

## Precedence and Associativity
i + j * k is equivalent to `i + (j*k)`
`-i * -j` is equivalent to `(-i) * (-j)`
#elaborative-interrogation What is another example of a unary operator that may have not been covered?

An operator is left associative if it groups from left to right;
binary arithmetic operators are all left associative

An operator is right if it groups from right to left;
binary arithmetic operators are right associative

*group terms based on their associativity*

## Assignment Operator

since assignment is an operator, several assignments can be chained together;
`i = j = k = 0;`

The `=` operator is right associative, so this assignment is equal to
`i = (j = (k = 0));`
The effect is to assign 0 first to k, then to j, then finally to i

Left side always requires address, therefore
`12 = i;`
IS WRONG

## Compound Assignment
these operators have the same properties as the = operator;
they are ==right associative==

`i += j += k;` means `i += (j += k);`
#look-up 
## Increment-Decrement Operators
```
i = 1;  
printf("i is %d\n", ++i); /* prints "i is 2" */  
printf("i is %d\n", i); /* prints "i is 2" */
```

++ after variable is post increment; a++
++ before variable is pre increment ++a
a++; equals ++a; equals a = a +1;

Explanation:
`a = 6`
`m = a++;`
Post increment, therefore we assign a to m first, THEN we increment the value of a by 1.
Thus, `m = 6` and `a=7`

Therefore, post increment
1) assign a to m
2) increment a

Suppose
`m = ++a;`
Thus, `m=7, a=7`

Therefore, pre increment
1) increment a
2) assign to m

==Thus, look for the position of the increment operator. If it comes before, then increment before assignment. If it comes after, assign and then increment==