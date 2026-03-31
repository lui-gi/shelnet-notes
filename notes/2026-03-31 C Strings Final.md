# C Strings Final

## Reading and Writing Strings

```
char str[] = "Are we having fun yet?";
printf("%s\n", str); --> entirety ^
```

If we want to print only a part of a string, see below
```
printf("%.6s\n", str); --> Are we
```

`%ms` will display a string in a field of size m
- string will not be truncated if length > m (prints entire string)
- `-` left justified

example:
`%10.3s` --> reserve 10 spaces but only use 3 characters

`puts(str)` = write strings, new line is auto-added
- `== printf("%s\n" , str);`
- takes only one

## Reading Strings

`scanf("%s", str);`
- cannot read whitespaces -> "Hello World!"
- ^ str = "Hello" 
- this is because scanf stops when it sees whitespace

**Alternatives:**
`gets(str)` --> DEPRECATED: DO NOT USE
- however, ==saves newline character==, so you have to get rid of it manually
`scanf("%99[^\n]", str);`
- at most 99 chars long
- every char EXCEPT newline character

no need to put the `&` operator in front of str in the call of scanf
- this is bc `str` is already treated like a pointer

## String Handling Functions

-> requires `#include <ctype.h>`

```
char ch = 'A';
char ch2 = '';

isalnum(ch) // returns true (ALPHANUMERIC OR NUM)
toupper(ch) // keep it 'A'
tolower(ch) // make it 'a'


```

## Exercise 1

What's wrong below?
```
char *duplicate(const char *p) {
	char *q;
	
	strcpy(q,p);
	return q;
}
```

```
p -> const char[]
q -> char

not enough space, we must allocate space to q

char q[100];
or
q = malloc(100); --> memory allocate
```