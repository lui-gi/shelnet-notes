# C Pointers pt2

**if i is a variable and p points to `i`, which of the following expressions are aliases for i?**
*note: `*` and `&` cancel each other out*

YES
- `*p`
- `*&i`

NOT
- `*&p`
Visual:
`[ MEM/VAL | 50  |        2001  |`
`ADDR      | 2001 |        2050 |`
`             i             p`

`&i = address of i`
`*(&i) == value STORED at the address of i, which is basically i`

`*p = i`, thus
`&(*p) = &i`

`&*i IS INVALID, can only use asterisk before POINTER`

#look-up 
**If `i` is an int variable and p and q are pointers to int, which of the following assignments are legal?**
p expects ADDRESS of an integer

YES
- `*p = *q`, we can assign integer to integer, legal
- `p = q` you can assign pointer to pointer (if types are the same)
- `p = *&q`

NO
- `p = i` , 
- `p = &q`, no, p is not expecting an address of a POINTER
- `&p = q`, you cannot change an address, only the value
- `*p = q`. `*p is an integer`, but `q` is the memory address of an integer, not compatible
- `*p = &i`


Example:
`p = *&q`
`addr [ value ] name/var`
`2050 [ 2000 ] q`

## Using const to Protect Arguments
- when we call function and pass it a pointer to a variable, we normally assume that the function will modify the variable

Sometimes we only want to EXAMINE the value of a variable and not change it

We can use `const` (constant) to document that a function won't change an object whose pointer is passed to the function


```
void example(int *p) --> p = &integer
	*p = *p + 5 (trying to modify content stored at address &integer)
	
x = 5;
example(&x);
(x is now 10)

void example(const int *p) --> we pass address but p should not try to modify content at location
	we cannot use *p = *p + 5
	we CAN printf("%d", *p)
	
Ultimately, we cannot MODIFY *p aka x
```

```
int main()
{
    int x,*q;
    const int *p;
    x = 5;
    p = &x;
    q = p;
    *q = 100;
    printf("%d", x);
    
    return 0;
}
```
warning: we are trying to assign const int type to ordinary int pointer, but we are still able to modify x
- we can bypass warning if we cast p as (`int *`)

## Pointers as Return Values
*remember, pointer p = address, *p = value*
return the location of an answer instead of returning its value

If x>y, return the address of x, otherwise return the address of y
```
int *max(int *a, int*b) {
	if (*a > *b)
		return a;
	else
		return b;
}

int *p, x, y;
p = max(&x, &y);
```

equivalently, `int* max(params)`

**Careful:** do not return pointer to local variable
```
int *f(void) {
	int a;
	return &a;
}
```
- when f returns, a does not exist anymore so the pointer to a will be invalid
- we are trying to return the address of a local variable, which gets terminated after function termination

## Pointer Arithmetic
- pointers can point to array elements, not just ordinary variables

For example
`int a[8], *p;`
`p = &a[0]`
p is pointing to the first element of array a

also,
`p = a;` p points to the first element
Why? because a = address of `a[0]` ALWAYS

Therefore we can also do these arithmetic:
```
p++;
p = p - 3;
^^ increments / adds index, not bytes of memory address
*p = 4;

also
p = &a[6];
q = p - 3;
p -= 6;

```
ensure we are within index range

## Use Pointers for Array Processing
- visit the elements of an array by repeatedly incrementing a pointer variable

Example: sum the elements of an array a
```
#define N 10

int a[N], sum, *p;
sum = 0;
for(p = &a[0]; p < &a[N]); p++)
	sum += *p;

```

## Combining `*` and `++` Operators
`*p++` or `*(p++)`
- postfix `++` has higher precedence than `*`
- access current value of p, then silently increment p
- p now points to `a[1]`
- we use indirection which means we accessed the CURRENT value of p, which was `a[0]`, so we see the VALUE of `a[0]`

`(*p)++`
- we emphasize `*p`, thus we are doing `a[0] ++, which is 1++`
- assign 1 first, but silently we increment by 1

`*++p or *(++p)`
- right associative
- ++p is `a[1]`
- `*p` tells us to access `a[1]`

`++*p or ++(*p)`
- access current value, then increase by 1

## Using an Array Name as a Pointer
the name of an array can be used as a pointer to the first element in the array
- FIRST ELEMENT, NO MODIFYING A
- think of int `a[]` as `const int *a`

Example
```
int a[10];
*a = 7; (we modify a[0])
*(a + 2) = 13; (modify a[2])

WRONG BELOW
while (*a != 0)
	a++;
	ARRAYNAME is a CONST pointer, we cannot modify it
```