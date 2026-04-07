# C Memory Allocation cont.

## Null Pointers
- NULL is a macro (defined in various library headers) that represents the null pointer
- programmers combine the call of `malloc` with the `NULL` test:
```
if ((p = malloc(10000)) == NULL) {
	allocation failed; take appropriate action
}
```

## Using `malloc` to Allocate Memory for a String

prototype for `malloc` function:
`void *malloc(size_t size);`

`malloc` allocates a block of `size` bytes and returns a pointer to it

`size_t` is an unsigned int type defined in the library

malloc returns a `void*` pointer, can be converted to any pointer type

**If we want to store a string of `n` characters:**
```
p = malloc(n+1);
p is a char* variable

equivalently, explicitly cast

p = (char *) malloc(n+1);
```

Allocating storage for an array of integers
```
int *p;
p = (int *) malloc(10 * sizeof(int));
```
- good practice to use `sizeof(int)` 

Example - Primitive Integer
```
int n, i, *ptr, sum=0;

printf("Enter number of elemebtns");
scanf("%d", &n);

ptr = (int*) malloc(n * sizeof(int));

printf("Enter elements: ");
for (i = 0; i<n; ++i) {
	scanf("%d", ptr+i);
	sum += *(ptr+i);
}
```

Example - structure
```
struct rec
{
	char LastName[41];
	char FirstName[41];
};

struct rec *r;
r = (struct rec *) malloc(sizeof(struct rec));
```

String input - a caution
```
struct course
{
	int marks;
	char subject[30];
};

int main()
{
	struct course *ptr;
	
	<-- CLEAR THE INPUT BUFFER -->
	fflush(stdin);
	
	<-- MALLOC OF STRUCT -->
	ptr = (struct course *) malloc(sizeof(struct course)); (auto -determines 34 bytes)
	
	printf("Enter subject name.");
	
	<-- fgets allows us to include spaces but also includes newline char \n -->
	fgets(ptr->subject, sizeof(ptr->subject), stdin);
	
	<-- remove trailing newline \n char -->
	size_t len = strlen(ptr->subject);
	if (len > 0 && ptr -> subject[len - 1] == '\n')
	{
		ptr->subject[len - 1] = '\0';
	}
	printf("Enter marks:");
	scanf("%d", &ptr->marks);
}
```

## calloc() example
clear + allocate
```
int main()
{
	int n = 5;
	int *ptr;
	
	(USE CALLOC TO ALLOC MEM)
	ptr = (int *) calloc(n, sizeof(int));
	
	if (ptr == NULL)
	{
		fprint(stderr, "Memory allocation failed!\n");
		return 1;
	}
	
	(display arr value)
	printf("Array elements after calloc: ");
	for (int i = 0; i < n; i++)
	{
		printf("%d ", ptr[i]);
	}
	printf("\n");
	
	(FREE ALLOCATED MEMORY)
	free(ptr);
	return 0;
}
```

## realloc() example
if we need to increase size of previously allocated block,
however we need both the OLD and NEW pointers and to specify the new size
```
int main() 
{
	int *ptr = malloc(2*sizeof(int));
	if(ptr == NULL) {
		fprint(stderr, "Memory alloc failed");
		return 1;
	}
	
	ptr[0] = 5, ptr[1] = 10;
	
	(INCREASE SIZE OF INTEGER)
	int *ptr_new = realloc(ptr, 3 * sizeof(int));
	free(ptr);
	return 1;
}

ptr
```

## Linked List Example
```
#include <stdio.h>
#include <stdlib.h>

(define structure for a node in linkedlist)
struct Node
{
	int data;
	struct Node *next;
};

// create a node and must MAINTAIN A HEAD
struct Node *head = NULL; //head points to the start node
struct Node *current = NULL; //latest created node
struct Node *new = NULL; //newly created node

printf("Add a record:\n");
new = (struct Node *) malloc(sizeof(struct Node));
printf("\nEnter your data:");
scanf("%d", &new->data);
new->next = NULL;
head = current = new;

//whenever we want to create a new node, we can use the following:

printf("Add another record:\");
new = (struct Node *) malloc(sizeof(struct Node));
printf("\nEnter your data:");
scanf("%d", &new->data);
new->next=NULL;
current->next = new;
current = current->next;
```

## Traversing Linked List
```
// traverse the linkedlist and print the data

current = head; //very important pointer
while (current != NULL) {
	printf("%d ", current->data);
	current = current->next;
}
```

## Deallocating Storage

`malloc` and the other memory allocation functions obtain memory blocks from a storage pool known as the `heap`
- calling these functions too often (or asking for large blocks of memory) can exhaust the heap -> causes functions to return a null pointer

Even worse, a program may allocate blocks of memory and then lose track of them, which wastes space

memory leakage = losing track of allocated memory blocks

example:
```
p = malloc(...);
q = malloc(...);
p = q;

original block allocated by p is still allocated, but we lost track of it
```

a block of memory that is no longer accessible to a program is said to be `garbage`

a program that leaves `garbage` behind has a **memory leak**

some languages provide a `garbage collector` that automatically locates and recycles garbage, but C does not

instead, each C program is responsible for recycling its own garbage by calling the `free` function to release unneeded memory

`free()`
- expects the pointers returned by `malloc` as the argument
- `free(ptr);`

Note: to free up linked list, we need to free node-by-node, not just `head`

example:
```
char *p = malloc(4);
...
free(p);
...
strcpy(p, "abc"); //<-- WRONG, p is a dangling pointer

BEST/SAFE practice:

free(p);
p = NULL;
```

Dangling Pointer Example
```
int main()
{
	int *p = malloc(sizeof(int));
	*p = 42;
	
	printf("%d\n", *p);
	free(p);
	*p =99; //UNDEFINED BEHAVIOR, COULD BE ALLOCATED TO OTHER PROGRAMS AT THIS TIME, INVADING
	
	printf("%d\n", *p);
	
	//try allocating memory, it may take up the freed space
	
	int *q = malloc(sizeof(int));
	*q = 22;
	
	printf("%d\n", *p); //garbage or irrelevant data
	
	return 0;
}
```