# System-Level Final Review

## Exam Syllabus

New Chapters - worth 50%
- Chapter 12 (Pointers and Arrays)
- Chapter 13 (Strings)
- Chapter 16 (Structures, Unions, Enumerations)
- Chapter 17 (Dynamic Memory Allocation)
- Chapter 13 (File Management, Process Management using system calls)

Old Chapters - worth 50%
- see System-Level Midterm Review

## Topics to Know
- regular expression question
- file permission question
- variable naming rules/static variables
- increment/decrement operators, logical and relational operators, precedence
- continue/break/switch statement
- loops, arrays, functions
- call by value, call by reference
- enumerations constants
- linked list manipulation (delete/insert/search first/last/some node)
- simple recursion on linked list
- string printing/manipulation (ASCII manipulation)
- structure/union: learn to calculate sizes of a union/structure
- dynamic memory allocation: malloc and free
- file management system calls and flags: open, read, write()
- process creation (Specially nature of fork system call)
- precedence of operators in `*++p, ++*p, (*p)++, *p++`

Not exhaustive; see lectures slides for entire content

## Review from Exam 2
```
int main()
{
	int n;
	for (n = 9; n != 0; n--)
		printf("n = %d", n--);
	return 0;
}

What will happen and why?
9 7 5 3 1 -1 -3 ... (infinite loop)
```

```
void f(int *p, int *q)
{
	q = p;
	*p = 15;
}

int i = 0, j = 1;
int main() 
{
	f(&i, &j);
	printf("%d" %d", i, j);
	getchar();
	return 0;
}

Ans:
15 1
```

```
int main()
{
	int a1 = 9, a2 = 10, a3 = 3;
	
	if (a1 < a2 > a3)
		printf("TRUE");
	else
		printf("FALSE");
		
	return 0;
}

(a1 < a2) > a3
[true = 1] > a3
if (0)
FALSE

```

**Process Creation**
```
int main()
{
	printf("Before fork()\n");
	
	return 0;
}
```

```

How many times "Hello World" printed?
How many processes will be created altogether?
4
```

**Increment/Decrement Operators**
```
int main()
{
	int a, b, c, d;
	a = 15;
	b = 10;
	
	c = ++a - b;
	d = b++ + a;
}

a = 16
b = 11
c = 6
d = 26
```

