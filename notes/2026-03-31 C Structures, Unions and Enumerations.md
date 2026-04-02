
# C Structures, Unions and Enumerations

C has no classes, but C has structures

Structures =
- a collection of values(members), possibly of different types

In other languages, structures are often called records; ==members== of structures known as ==fields==

The members of a structure are stored in memory in the order in which they are declared

```
struct employee
{
	char name[50];
	__ age;
	__ salary;
}
```

new data type, called struct employee

`Struct employee empl1, empl2;`

Purpose of struct: composite data type, made up of multiple data types
## Declaring Structure Variables

example with no struct name;
```
struct {
	int number;
	char name[NAME_LEN + 1];
	int on_hand;
} part1, part2;
```

`struct{...}` specifies a type
`part1` and `part2` are variables of that type
`number`, `name`, and `on_hand` are members of this structure

## Structure Initialization

```
struct {
	int number;
	char name[nameLen + 1]'
	int on_hand;
} part1 = {528, "Disk drive", 10}, part2 = {914, "Printer cable, 5};
```

to access members:
`part1.number`
`part1.name`
etc..

## Operations on Structures
use period `.` to access a member within a structure
`part1.on_hand++;`
`part1.number = 258;`


Scanning applies:
```
scanf("%d", &part1.on_hand);
```

use `=` to copy structures
```
part1 = part2;
```

## Structure Types

we can declare structure tag:
```
struct part {
	...
}

struct part part1, part2;

WRONG -> part part1, part2'
```

we can declare a structure type:
```
typedef struct {
	...
} Part;

Part part1, part2;
```

So either 
`struct [TAG] part1, part2`
OR
`[TYPENAME] part1, part2`

## Structures as Arguments
Pass by values
```
void print_part (struct part p)
{
	printf("Part numer : %d\n", p.number);
}
```

Pass by addresses
```
void update_part (struct part *p)
{
	p->number = 123; // (*p).number = 210; is valid
}
```
==for pointers to a structure, use -> to access the members instead of period==

Effect of passing structures:
```
What is the difference in effect between passing a structure by value and passing it by address to a function in C?

A

Passing by value copies the structure, while passing by address allows modifications to the original structure.

B

Passing by value and by address both modify the original structure.

C

Passing by value creates a new pointer to the same structure, while passing by address creates a duplicate structure.

D

Passing by value modifies the original structure, while passing by address copies the structure.
```

Example code:
```
#include <stdio.h>

struct Part
{
	int number;
};

void update(struct Part *p)
{
	(*p).number - 210;
}

void display(struct Part p)
{
	printf("\nNumber = %d", p.number);
}

int main()
{
	struct Part p1={.number-120}, p2={.number=205}; // initialization or p1={120}
	
	display(p1);
	display(p2);
	update(&p1);
	display(p1);
	
	return 0;
	
}
```

## Structures as Return Values

```
struct part build_part (int number, const char * name, int on_hand)
{
	struct part p;
	p.number = number;
	strcpy(p.name, name);
	p.on_hand = on_hand;
	return p;
}
```
returning a struct p variable

if we used typedef, we can use the alias rather than `struct part`

## Arrays of Structures

```
struct part inventory[100]; //array of type part

print_part(inventory[i]); /print the ith part

inventory[i].number = 883; // assign 883 to the number member of inventory at ith

inventory[i].name = "Disk Drive"; // assign "Disk Drive" to the name member of inventory[i]
```

## Nested Structures

structure within a structure

example (person_name within student)
```
struct person_name {
	char first[]
	char middle[]
	char last[]
}

struct student {
	struct person_name name;
	int id, age;
	char sex;
} student1, student2;

strcpy(student1.name.first, "Fred");
```

## Unions

A union, like a structure, consists of one or more members

The difference is that compiler allocates ==only enough space for the largest of the members in a union==

The members of the union overlay each other within this space

Assigning a new value to one member alters the values of all the other members as well
- why? because 

example
```
union student {
	char name[];
	int age;
	int roll;
};

union student std;
std.age = 30;
(thust std.roll also = 30)

strcpy(std.name, "Barack Obama");
std.age = 10;
std.name = ? --> UNDEFINED + parts of "Barack Obama", assuming null terminator comes later

allocated 4 bytes only
```


## Using Unions to Save Spaces

```
Books: Title, author, number of pages
Mugs: Design
Shirts: Design. colors available, sizes available
```

```
struct catalog item {
	int stock_number
	float price
	char title[len + 1]
	char author[len + 1]
	int num_pages
	char design[len + 1]
	int colors;
	int sizes;
}
```

wasting memory space bc we now allocate memory space of unneeded members

thus, here is the fix to save memory:
```
struct catalog_item {
	int stock_numer;
	float price;
	int item_type;
	union {
		struct {
			char title[len + 1]
			char author[len + 1]
			int num_pages
		} book;
		struct {
			char design[len + 1]
		} mug;
		struct {
			char design[len + 1]
			int colors;
			int sizes;
		} shirt;
	} item;
};
```

On the outer block are the shared members, which are the stock_number, price, and the item_type

then we use union to save space of the unique members

how much bytes does one catalog_item take up at assuming len + 1 = 10 bytes?
-> 36 bytes

Example Question:
```
int main()
{
	union {
		int i1;
		int i2;
	} myVar = {.i2, = 100};
	
	printf("%d %d", myVar.i1, myVar.i2);
	
	return 0;
	

}
```

## Enumerations

Assume a variable that stores the suit of a playing card having only four potential values: "clubs", "diamonds", "hearts", and "spades"

```
Solution 1:
int s; (s will store suit)
s = 2; (where 2 represents hearst)
```

```
Solution 2:
#define SUIT int
#define CLUBS 0
#define DIAMONDS 1
#define HEARTS 2
#define SPADES 3
```

now our previous example will become easier to read
```
SUIT S;
S = HEARTS;
```

thus,

an enumeration is a type whose values are listed (ENUMERATED) by the programmer

each value has name defined by the programmer

example below
```
enum {CLUBS, DIAMONDS, HEARTS, STPADES} s;

int i;
i = DIAMONDS; /* i is now 1 */
s = 0; /* s is now 0 clubs */
s++; /* s is now 1 diamonds */
i = s + 2; /* i is now 3 */
```

example, we can give tag name to enum data type
```
enum colors {BLACK, LT_GRAY = 7, DK_GRAY, WHITE = 15};

enum colors c;
black = 0, dark gray = 8
```
IMPORTANT ^ notice the DK_GRAY indexing

Enum Exercise
```
struct point {
	int x;
	int y;
};

struct rectangle {
	struct point upper_left, lower_right;
};
```
Task ^: write function that computes the area of a rectangle structure passed as an argument

Enum Exercise Ans:
```
struct recrangle r;
r.upper_left.x = 30;
r.upper_left.y = 50
r.lower_left.x = 50;
r.lower_right.y = 20;

int compute_area(struct rectangle r)
{
	int length, width;
	length = ;
	width = ;
	return;
}
```

