# C Strings pt2

## String Functions
- strlen
- strcpy
- strcat
- strcmp

For all string examples, ensure `n`, if `str[n]`, is large enough for the below functions.

### strcpy (String Copy)
copies entire string character including null terminator

`char *strcpy(char *dest, const char *src);`
copies the string src into the string dest

Ex:
```
str2 = "abcd";

strcpy(str2, "abcd"); (copy "abcd" into str2)

strcpy(str1, str2);

strcpy(str1, strcpy(str2, "abcd));


```

We CANNOT use `s = "abcd";`

### strncpy (different from strcpy)
`char *strncpy(char *dest, const char *src, size_t s);`
copies s amount of characters from src string to dest string

Class example:
```
char str1[50] = "Hello", str2[50] = "Computers";

strncopy(str1, str2, 3);

printf(""%s", str1); --> "Comlo"
```

### strcat (String Concatenate) + strncat
`char *strcat(char *dest, const char *src);`

appends the contents of the string src to the end of the string dest, and return dest

Ex:
```
strcpy(str1, "abc");
strcpy(str1, "def");
(str1 now contains abcdef)
```

Note: do not forget how much space is left, see below
```
char str1[6] = "abc";
strcat(str1, "def"); (WRONG)
```

Correct below:
```
char str1[BUFFER_SIZE];
char *str2 = "def";

strncpy(s1, s2, BUFFER_SIZE - 1);
strncat(s1, s2, BUFFER_SIZE - 1 - strlen(s1));
```

Class example:
```

```

### strcmp (String Compare)

`int strcmp(const char *dest, const char *src);`

compare dest and src
- returning a value less than equal to or greater than 0, depending on whether dest is less than equal to or greater than src

ex:
```
strcpy(str1, "abc");
strcat(str2, "def");
if(strcmp(str1, str2)<0)
	(if str1 <= str2, return True)
```

class ex:
```
char str1[50] = "cat", str2[50] = "dog";

if (strcmp(str1, str2) < 0)
	printf("First string appears earlier in dictionary order) (NEGATIVE NUM)
else
	printf("First string appears later in dictionary order) (POSITIVE NUM)
	
always see what happens to the FIRST string RELATIVE to the SECOND

-       str2         +
```

scratch work
```
char str1[50] = "cat", str2[50] = "bat";

if (strcmp(str1, str2) < 0)
	strcat(str1, str2);
else
	strcat(str2, str1); <-- this runs, thus str2 = "batcat"
	
printf("%s\n", str1)
str1 = cat
str2 = batcat

-     str2     +
    bat.     cat   
```

### ASCII Vals
A = 65
B = 66
C = 67
D = etc ..
Z = 90

a = 97
b = 98
c = 99
d = etc..
z = 

### String Exercises

```
strcpy(s1, "computer");
strcpy(s2, "science");

if (strcmp(s1, s2) < 0) (returns negative)
	strcat(s1, s2) --> s1 = "computerscience"
else
	strcat(s2, s1)
	
s1[strlen(s1)-6] = '\0';
s1[15 - 6] = '\0'
s1[9] = '\0'
s1 = "computers\0"
printf(s1) --> "computers"
```

Scratch Work
```
s1 = "science", s2 = "fiction"

if (strcmp(s1, s2) < 0) --> strcmp returns positive value
	strcat(s1, s2)
else
	strcat(s2, s1) --> runs, s2 = fictionscience
	
printf(s1) 
-> science
printf(s2)
-> fictionscienec

-     fiction    +
               science

```