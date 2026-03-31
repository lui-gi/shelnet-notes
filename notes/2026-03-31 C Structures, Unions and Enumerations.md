
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