
# C Advanced Ptrs, Dynamic Memory Allocation

static memory allocation;
`int arr[50]` = 200 bytes of memory
- wasting memory space if indices unused

WE need to ==DYNAMICALLY== allocate memory, only allocate at run-time rather than compile-time (static malloc)

## Reqs. for Dynamic Memory Allocation
Must used pointers in alternate, advanced manners

Using dynamic storage allocation, we can design data structures that grown (and shrink) as needed

## Memory Allocation Functions
most often used for strings, arrays, structures

The 3 allocation functions below are declared by `<stdlib.h>` header

`malloc`
- allocates a block of memory, does not initialize it

`calloc`
- allocates a block of memory and clears it (sets to 0)

`realloc`
- resizes a previously allocated block of memory

These return a value type of `void *`, aka a generic pointer

## Null Pointers

an example of testing `malloc`'s return value
```
p = malloc(10000);
if (p == null) {
	/* allocation failed; take appropriate action */
}
```
`NULL` is a macro (defined in various library headers) that represents the null pointer

some programmers combine the call of `malloc` with the `NULL` test:
```
if (p = malloc(10000)) == NULL) {
	/* alloc failed, take appropriate action*/
}
```


## Using `malloc` to allocate memory for a String
