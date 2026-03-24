# SysLevel Exam 2 Review

## IO / Format Specifiers
%d and %i are similar but behave differently,
- `%d` always reads the input as a DECIMAL, aka base-10 integer
- `%i` auto detects the base of the input, for example if the input is 0x, then it recognizes it as a hexadecimal

Examples, assume we are using scanf:
-> User types 0x10
- `%d` = reads 0
- `%i` = reads 16

Printing Output via printf:
both %d and %i will take an integer from memory and print to screen in the standard base-10 format
- thus printing `int myNum = 15` with both %d and %i will output 15

`%s` = reads or prints a string (sequence of chars)
- scanf: grab characters until first whitespace (space, tab, newline), then appends null terminator to the end `\0`
- printf: program goes to memory address of string, prints chars one by one, stops at null terminator

## scanf behavior

`scanf("%d %d", &a, &b)` and `scanf("%d%d", &a, &b)` behave the exact same
- they both read two integers separated by any amount of whitespace

`%c`
- unlike %d or %f which automatically ignores leading whitespace, %c is literal
- for example, if a user types `A B` and scanf stores two %c in &a and &b, a = A and B = ' '.

`scanf("%c %c", &a, &b)` is different than ^ :
- the explicit whitespace in the format string throws away any whitespace, including spaces, tabs, newlines. it consumes all the space after A
- for the same scenario as above, a = A and b = B

`%c` and `Enter`:
- assume there is already a scanf scanning for %d and loading into &num
- if we run scanf again with %c and &letter, then letter will be assigned the newline character due to the previous line
- to fix this, use a space before the %c like so -> `scanf(" %c", &letter)`

## Expressions 
Scratch work
```
int x = 5, y = 3, z;
z = (x < y) 
z = (5 < 3)
z = false = 0

int a, b, c, d;
a = 15; b = 10;
c = ++a - b; --> c = 16 - b = 6
(c = 6) (a = 16)
d = b++ + a; --> d = 10 + a = 26
(d = 26) (b = 11)

int i = 6;
int j = 4;
int y;
y = (j++) * (++i); --> (4) * (7) = 28
(y = 28; j = 5; i = 7)

int x, y = 10;
char z = '2';
x = y + z; --> 10 + 50
(x=60)

int n = 49;
n % 3 == 0 ? printf("Hello!") : printf("World");
49 % 3 = 1, thus World

#include 
int main() {
    int a = 0;
    a = (a == (a == 1));
    
    SCRATCH START
    a = (a == (0 ==1))
    a = (a == (0))
    a = (1)
    SCRATCH END
    printf("%d", a);
    return 0;
}

int x = 5;
int z = 1 || --x;
x = 5
```

**ask prof: do we need to know all ASCII values?**

## Selection
Scratch Work
```
int main() {
    int a = 5;
    switch(a) {
        case 5: printf("Five");
        case 6: printf("Six");
        case 7: printf("Seven");
        default: printf("Not Found");
    }
}

int a = 7;
if (a > 10)
    printf("Big");
else if (a > 5)
    printf("Medium");
else
    printf("Small");
```

### Switch Basics
basically a faster alternative to long chain of if-else statements
- only use if we have a single variable and want to execute different blocks of code depending on its value
- always include `break;` to avoid fall-throughs

Switch only takes `integers` and `characters`
- due to switch memory optimization

Default case == else
- optional but recommended, use as a catch-all


What is a 'fall through' in a `switch` statement?
-> after a matching case executes, execution continues into the next case without stopping

## Loops
Scratch Work
```
int i, j, sum = 0;
for (i = 1; i <= 10; ++i) {
    if (i % 2 == 0)
        continue;
    for (j = 1; j <= i; j++) {
        sum += j;
        break;
    }
}

start
i = 1; continue
i = 2; sum +=1 
i = 3; continue
i = 4; sum +=1
i = 5; continue
i = 6; sum +=1
i = 7;
i = 8; sum +=1
i = 9;
i = 10; sum += 1
end

int x = 1;
while (x < 20) {
    x *= 3;
}
printf("%d", x);

start
x = 1*3 = 3
x = 3 | 3 < 20 
x = 3*3 = 9
x = 9 | 9<20
x = 9*3 = 27
end
```

## Arrays
Scratch Work
```
int i, DATA[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
for (i = 0; i < 10; ++i) {
    if (i % 2 == 0)
        DATA[i] = 2 * DATA[i];
    else
        DATA[i] = 2 * DATA[i] - 1;
}

start

end

void double_first(int arr[]) {
    arr[0] *= 2;
}
int main() {
    int a[3] = {5, 10, 15};
    double_first(a);
    printf("%d", a[0]);
}

start

end
```
