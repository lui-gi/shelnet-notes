# Computer Organization Review Session

- make sure to study existing code for our labs (notably 7, 8, 9)

side note: pattern-matching brain is more efficient for our age as opposed to a memorizing brain (adolescent brain)

## Function Calls
`call`: located in main
- `ra` records the call location in `PC`
- `PC = PC + 4`
`ret`: located in function call block
- memorizing the location of function call of main program


```
START OF CALL
addi sp, sp, -N # allocate stack frame of N bytes
sw ra, N-4(sp) # save return address
sw s0, N-8(sp) # save any s-registers we will use

CALL A FUNCTION
call foo
(equivalently: jal ra, foo)

END OF CALLEE
lw ra N-4(sp) # restore return address
lw s0, N-8(sp) # restore saved registers
addi sp, sp, N # deallocate stack frame
ret # jump to ra
```

## Recursive Function
- type of function that calls itself

```
factorial(n) = n * factorial(n-1);

base case -> step

recursive case -> call the next function inside the recursive expression

What do we need to implement this in RISC-V?

1) function call -> store ra
2) variable needed to complete the recursive expression
3) 
   
   
Stack is FILO
```

## Logic Circuits

smaller logic circuit component -> `logic gates`

### Combinational Logic

Adder: 1-bit
```
HALF ADDER -----

A | B | Sum | Carry
0 | 0 | 0   | 0
0 | 1 | 1   | 0
1 | 0 | 1   | 0
1 | 1 | 0   | 1

SUM = XOR
CARRY = AND

HALF ADDER -----
```

### Minterms and Maxterms
assume logic variables A, B, C

`minterms`: SOP, sum of products, combination of A, B, C -> ABC (with or without negation)
- ABC + AB(notC) + A(notB)C + ...
- 

`maxterms`: product of sums, POS, 
- (A + B + C)(A + B + notC)...(...)
- 

```
Minterms Conversion
A + A` = 1
A * 1 = A

AB*1 = AB(C + C`)
AB(C+C`) * 1 = AB(C+C`)(D+D`)

Separating [AB + CD]

1. Separate variables that are being 'AND' together
-> we can use distribution law

AB+C = (A+C)(B+C)
AB + CD = (A+CD)(B+CD)
		= (A+C)(A+D)(B+C)(B+D)
		
^ looks like a maxterm with a couple missing variables

2. fill in this missing variables with the following laws
   POS: AA` = 0, A+0=A
   SOP: A+A`=1, A*1=A
   
(A+C) = (A+C+BB`+DD`)
```

## Datapath

Integer Addition
```
7 + 6

FA <- FA <- FA <- FA <- FA <- HA
```

**Arithmetic Logic Unit**
```
r1 + r2  (both 32 bits) -> ALUOP (ALU1->ALU2->ALU3...) -> OUT(1,2,3,4,5)
```