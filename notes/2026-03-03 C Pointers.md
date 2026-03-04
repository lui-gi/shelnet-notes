# C Pointers

## Declaring Pointer Variables
the pointer variable must be preceded by an asterisk
- every point var points to OBJECTS of a particular type (reference type)

Examples:
```
int *p; (only points to integers)
char *str; (points only to characters)
double *q; (only points to doubles)
etc.
```
ALSO: there are no restrictions on what referenced type may be
- a point variable can even point to another pointer, like `int **q = &p;` assuming p is a pointer

## Address and Indirect Operators

`&` operator: get the address of a variable
`*` operator: gain the access to the object that a pointer points to

Examples:
```
int i=2, j, *p; (p points to nothing right now)
p = &i; (points to int var i)
j = *p; (equivalent to j = i)
```
- the address operator can appear in declaration to initialize a pointer
- `int i = 2; *p = &i;`

More examples:
```
int i, j, *p = &i;
i = 1;

printf("i = %d", i);
printf("*p = %d", *p);

^^^ BOTH PRINT 1 ^^^

*p = 4; (this is equivalent to i = 4)

printf("i = %d", i);
printf("*p = %d", *p);

^^^ BOTH PRINT 4 ^^^

j = *&i; (equivalent to j = i)
printf("j = %d", j);

^^^ PRINTS 4 ^^^
```

==remember: `*` tells the computer to "gain access" to the object that a pointer points to==

Note: never apply the indirection operator to an uninitialized pointer variable, such as below
```
int *p;
printf("%d", *p);
```

## Pointer Assignment
Examples:
```
int i=1, j=2, *p, *q;
p = &i;
q = p;

(p and q both point to i)

*p = 5; (same as i = 5)
```

```
int i=1, j=2, *p, *q;
p = &i; 
q = &j;
(p points to i, q points to j)

*q = *p;
(equivalently, j = i;)
```

## What is saved in a pointer variable?
```
int a, *p;
p = &a; (p now points to a)

printf("%p", &a); (prints memory addr of a)
printf("%p", p); (p = &i, prints memory addr of a)
```
NOTE: `%p` used to print memory addr of a pointer variable

## Pointers as Arguments
```
main()
{
	int x = 1, y = 2;
	swap(&x, &y);
	printf("x = %d, y = %d", x, y);
}

void swap(int *p, int *q)
{
	int temp = 0;
	temp = *p; (temp = x)
	*p = *q; (same as x = y)
	*q = temp; (same as y = temp)
}
```
FINAL OUTPUT:
- x = 2
- y = 1

Trace summary:
main initializes x=1, y=2
- swap is called, taking the memory address of x and y as arguments
- we know x and y hold memory addresses
- the memory address of x is assigned to y, vice versa
- ^ in other words, x = old(y), y = old(x)
- we know print x and y, which are just integers are not pointers
- because x holds the memory address of old y, that memory address holds the value of 2, and y now holds 1