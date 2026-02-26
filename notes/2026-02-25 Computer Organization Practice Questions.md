# Computer Organization Practice Questions

## Conversion
**-22 into 8-bit Two's Complement**
11101010

**Two's Complement (11001010) to hexadecimal**
```
1100 1010
12.  10
    
10 11 12 13 14 15 16
a   b. c  d. e. f. g

CA
```

**Overflow**
- 4 bit Two's Complement: add `0111` and `0010`
- did overflow occur? 

7 + 2 = 9
4 bit Two's Complement = 3 usable bits, therefore max value is 2^n - 1, which is 7. 

We can tell it is overflow because adding even just 1 to 0111 renders an overflow, due to the sign bit having to be used for the value.

## Floating Points
**-5.25 to IEEE 754**
`(signbit) | integer.fractional
`negative| 0101.01 ` 

```
0) DETERMINE SIGN BIT
-5.25 = 1
S = 1

i) CALCULATE THE INTEGER AND FRACTIONAL PART
0.25 x 2 = 0.5 R 0
0.5  x 2 = 1 R 1
0 x 2 = 0

NOTE: Remember, top to bottom = .01

5 = 101
0.25 = .01

ii) NORMALIZE BINARY NUM (Scientific Notation)
5.25 = 101.01
--> 1.0101 x 2^2
--> moved 2 decimal places to the LEFT. Save '2'

iii) CALCULATE BIASED EXPONENT, E
Saved '2'
2 + 127 = 129

# Convert 129 to binary
129 = 128 + 1
10000001
E = 10000001

iv) DETERMINE FRACTION/MANTISSA
Recall 1.0101 x 2^2

Fraction bits = 0101
Fractional field is 23 bits long, add 0s as necessary

F = 01010000000000000000000

v) ADD S, E, F

S E F
1 10000001 01010000000000000000000

vi) HEX (IF NEEDED)

1100 0000 1010 1000 0000 0000 0000 0000
12   0.    10.   8.  0-->
C    0     a     8   0000

```

**Hex to Floating Point**
`0x40400000`

```
4    0     4    0    0.    0    0   0. 
0100 0000 0100 0000 0000 0000 0000 0000

S = 1 bit
E = 8 bits
F = 23 bits

S  E          F
0 10000000  100 0000 0000 0000 0000 0000

True Exponent = E - 127
TE = 10000000 - 127
   = 128 - 127
   = 1
TE = 1

F + Implicit = 1.10000000000000000000000
TE = 1

11.0000000000000000000000

3 (CORRECT)
```

## Instructions in the Computer
- every instruction is 32 bits long; 
- these 32 bits are further divided into "fields", see below
- ^ according to six core formats (R, I, S, B , U, J)
- allows processor to decode and execute instructions quickly and efficiently

#elaborative-interrogation  Why do we need instructions?
- because at the hardware level, our processor does not read plaintext like `add x1, x2, x3`, but rather, 32-bit binary numbers that are stored in *memory*
- the CPU then fetches the 32-bit strings and 'decodes' them to figure out what operation to perform

What are instruction formats?
- allow us to keep the hardware simple and fast
- all standard instructions are exactly 32 bits wide
- 6 main formats:

**R-type (Register)**
- we use with for arithmetic or logical operations that involve three registers, where two are sources and one is the destination
- `add rd, rs1, rs2`
**I-type (Immediate)**
- we use this when an operation requires one source register and a small built-in **constant** (which we call an **immediate**) or for loading data from memory
- `addi rd, rs1, 10` aka rd = rs1 + 10
- `lw rd, 0(rs1)` aka load  word into register rd starting from first index of rs1
**S-type (Store)**
- we use this specifically for storing data from a register back into memory
- `sw rs2, 0(rs1)` aka save the contents of rs2 into the memory address stored in rs1 aka memory_address(index of rs1 + immediate) = rs2
- `[ MEMORY    | (addr = rs1): (val = rs2) | next addr | ...               ]`
**B-type (Branch)**
- we use this for if/else statements and loops (conditional branching)
- we compare two registers then jump to a memory address if a condition is met
- `beq rs1, rs2, target` aka if rs1 = rs2, then we jump to target for our next instructions rather than the next sequential instruction
**U-type (Upper Immediate)**
- we use this to load large constant values (~ 20 bits wide) into destination register
- `lui rd, 100` aka rd = 100
**J-type (Jump)**
- we use this for jumping without a condition (opposed to B-types), usually for calling functins, etc.
- `jal rd, label`

**R-Type Instruction | Register**  
```
funct7  rs2.    rs1     funct3   rd      opcode
7 bits  5 bits  5 bits  3 bits   5 bits  7 bits
31-25   24-20   19-15   14-12    11-7    6-0
```
opcode:
- tells the CPU it is an R-type format
**I-Type Instruction | Immediate** 
```
-->     imm[11:0]    rs1     funct3   rd      opcode
7 bits  5 bits       5 bits  3 bits   5 bits  7 bits
31-25   24-20        19-15   14-12    11-7    6-0
```
 example of `imm[11:0]`
 Let's use `addi x5, x6, 10` aka add immediate where x5 = x6 + 10
 10 in binary is `0000001010`
`0000001010` is a 12 bit sequence; THIS is `imm[11:0]`
`imm[0] = 0; imm[1] = 1; imm[2] = 0; imm[3] = 0`

**S-Type Instruction | Store**
```
imm[11:15]  rs2.    rs1     funct3   imm[4:0]      opcode
7 bits      5 bits  5 bits  3 bits   5 bits        7 bits
31-25       24-20   19-15   14-12    11-7          6-0
```
**B-Type Instruction | Branch**
```
imm[12,10:5]  rs2.    rs1     funct3   imm[4:1,11]      opcode
7 bits        5 bits  5 bits  3 bits   5 bits           7 bits
31-25         24-20   19-15   14-12    11-7             6-0
```
**U-Type Instruction | Upper Imm**
```
imm[31:12]                       rd      opcode
7 bits  5 bits  5 bits  3 bits   5 bits  7 bits
31-25   24-20   19-15   14-12    11-7    6-0
```
**J-Type Instruction | Jump**
```
imm[20,10:1,11,19:12]            rd      opcode
7 bits  5 bits  5 bits  3 bits   5 bits  7 bits
31-25   24-20   19-15   14-12    11-7    6-0
```

How many bits are allocated to identify a single register? What is the mathematical reason for that?
- ALWAYS 5 bits
- The reason it is 5 bits is because 5 bits has a max value of 31 and a minimum of 0; this is a total of **32 values** `11111 = 31 `
- 32 values is important because we have 32 integer registers: x0 -> x31

What is the difference between funct3 and funct7?
- Firstly, opcode tells the processor the broad category of the instruction (register to register or load from mem, etc.)
- THEN, funct3 and funct7 act as subcodes which narrow the operation
- funct3 splits a category into up to 8 specific operations
- funct7 distinguishes between closely related operations that share the same funct3, such as add vs. sub

## Memory Allocation, Arrays

**Memory Layout**

Text: where the machine code instructions live

Global Data: for variables declared outside of functions that exist for the duration of the program

Heap: dynamic memory allocated at runtime; grows "up" toward higher addresses

Stack: used for local variables and function call frames; it grows "down" toward lower addresses
- the Stack pointer (sp or x2) always points to the "top" of the stack aka the lowest address

**Arrays in Memory**
array is a contiguous block of memory; to access element, processor needs Base Address (start of arr) and an offset (indices)

RV32 (32-bit), data types have differing sizes:
- Byte = 1 Byte (8 bits)
- Half-word = 2 bytes (16 bits)
- Word = 4 bytes (32 bits) 
- ^ standard size for int

**Addressing Logic**
to find t he address of an element at index i, we use `addr = base + index * elem_size`

RV32 is byte-addressed, therefore if we have an array of integers, each index is 4 bytes
^ Why? because `each int is 1 word = 4 bytes`

Thus,
- `arr[0] = base`
- `arr[1] = base + 4`
- `arr[2] = base + 8`
- Notice it multiplies by 2 each time, this is why we use **Shift**

**Assembly Implementation**
to load `arr[i]` into register,
1. calculate the offset by shifting the index left by 2 (same as multiplying by 4 bc 2^2 = 4) via `slli t1, s1, 2 (assuming s1 is index)`
2. add the offset to the base register via `add t1, t1, s0 (if s0 is base address)`
3. load via `lw t2, 0(t1)`

## Control Flow | Jump and Branching

in RV32I, the program counter  (PC) increments by 4 to execute instructions sequentially; control flow instructions break the sequence to implement loops, if else, and function calls

**Conditional Branches (B-Type)**
branches evaluate condition between two registers
- if true, PC jumps to specific label, but if false, the program continues to the next sequential instruction
Equality: beq (branch if equal); bne (branch if not equal)
Comparisons: blt (branch if less than); bge (branch if greater than)
- no ble or bgt in standard RISC-V

**Unconditional Jumps (J and I Type)**
jumps can happen without condition; they link the `ra` (return addr) so the hardware knows where to go back to once subroutine finishes