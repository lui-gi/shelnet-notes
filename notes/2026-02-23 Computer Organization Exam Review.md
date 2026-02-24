# Computer Organization Midterm Review

## Topics
- Signed and Unsigned Numbers
- Floating Points
- Representing Instructions in Computer
- Memory Allocation, Arrays
- Control Flow (jumps, branching)
- RISC-V Instructions: Arithmetic, Bitwise Logic, Shift, Load Immediate, Load and Store, Jump and Function, Branch

See https://projectf.io/posts/riscv-cheat-sheet/

### Signed and Unsigned Numbers
Unsigned integers can only represent non-negative numbers; all bits will be used.
- an n-bit unsigned integer can represent the values from 0 to 2^n - 1.

Signed integers represent negative numbers by using the most significant bit as the **sign** bit.
- an n-bit signed integer ranges from -2^n-1 to 2^n-1 - 1
###  One's and Two's Complement
to find the one's complement of a number, invert all the bits

to find the **two's complement**, (the standard for signed numbers), invert all the bits and add 1

### Extension
- for when we are loading a smaller data type into a 32-bit register:

Sign Extension (for signed numbers): replicate the most significant bit to fill the upper bits
Zero Extension (for unsigned): fill the upper bits with 0s

### Conversion
Signed <-> Unsigned
- use two's complement

Decimal -> Binary
Binary -> Hex
etc.

### Floating Point
IEEE 754 Standard: 32-bit Single Precision format
Sum of below:
`2^-1 + 2^-2 + 2^-3 + ... + 2^-n`
 
Order: top to bottom

To mitigate repeating digits, we specify precision in code
-> Floating point numbers are **approximations**

Thus, floating point is not real in binary, however we have special cases such as 0.75
`0.75 = 0.11`

```
0.75/0.5 == 1.5 R1
0.5/0.5 = 1.0 R1
0/0.5 = 0.0 R0
```


### Representing Instructions in the Computer
RISC-V uses standard 32-bit instruction formats:
- register
- immediate
- store
- branch
- jump

R-type (register): used for arithmetic/logic
I-Type (immediate): used for immediate arithmetic and loads
S-Type (store): immediates are split, used for stores
B-Type (branch): similar to s-type but used for PC-relative branching
J-type: used for large immediates and jumps

### Memory Allocation, Arrays
**Byte Addressing:** Memory is an array of bytes, since RV32I uses 4-byte words (32-bits), consecutive word addresses differ by 4

**Array Access**; thus to access array at i, we need to calculate the offset. usually we just use `slli` (shift left logical immediate) by 2 to multiple the index by 4 quickly

RISC-V is Little-Endian, therefore the LSB of a word is stored at the lowest memory address

### Big Endian vs Little Endian

**Big Endian**: MSB at lowest addr.
`Most Significant Byte -- other -- > Least Signifcant Byte`

**Little Endian (RV)**: MSB at highest addr.
`Least Significant Byte -- other -- > Most Significant Byte`

### Control Flow - Jump and Branch
Conditionals (if else)
- handles using branch instructions (`beq`, `bne`, `bge`, etc.)
- if condition is met, the **PC (Program Counter)** jumps to the target label; otherwise, falls through to next instruction

Loops (While for)
- require a conditional branch to check the exit condition and an uncoditional jump (j or jalx0) at the end of the loop body to return to the condition check

PC-Relative Addressing
- branches jump to addresses relative to the current PC. 

# Practice Quiz

## Questions

**Signed and Unsigned Numbers**
1. What is the 8-bit two's complement binary representation of the decimal number **-25**?
2. What is the decimal value of the 8-bit two's complement binary number `11111100`?
3. If you have an 8-bit unsigned integer, what is the maximum decimal value it can represent?

**Floating Points (IEEE 754 Single Precision)**
4. In IEEE 754 single-precision format, how many bits are allocated for the exponent and how many for the fraction (mantissa)?
5. What is the exponent bias used in IEEE 754 single-precision floating-point format?

**Representing Instructions**
6. Which RISC-V instruction format is used for the `addi` instruction?
7. The instruction `sw x10, 12(x11)` belongs to which instruction format?
8. In an R-type instruction, what are the names of the two fields used alongside the `opcode` to specify the exact arithmetic/logic operation?

**Memory Allocation & Arrays**
9. Assuming byte-addressable memory and 32-bit integers, if an array starts at base memory address `0x4000`, what is the exact hexadecimal memory address of `array[6]`?
10. Write the RISC-V assembly instruction to load a 32-bit word from the memory address stored in `x15` into register `x10` (assume a 0 offset).

**Control Flow & RISC-V Instructions**
11. What mathematical operation does the instruction `slli x10, x11, 2` effectively perform on the value in `x11`?
12. Which branch instruction would you use to jump to the label `Loop` if the value in `x5` is strictly less than the value in `x6`?
13. What is the hardwired, unchangeable value stored in RISC-V register `x0`?
14. If you want to isolate (keep) only the lowest 8 bits of register `x5` and clear all upper bits to zero, which bitwise logic instruction and immediate value should you use?
15. What is the primary difference between the `srl` (Shift Right Logical) and `sra` (Shift Right Arithmetic) instructions?

---
---

## Answer Key

1. **`11100111`** *(Breakdown: +25 is `00011001`. Invert bits: `11100110`. Add 1: `11100111`)*
2. **-4** *(Breakdown: Sign bit is 1, so it's negative. Invert bits: `00000011`. Add 1: `00000100` which is 4. Apply sign: -4)*
3. **255** *(Formula: $2^n - 1 \rightarrow 2^8 - 1 = 256 - 1 = 255$)*
4. **Exponent: 8 bits | Fraction: 23 bits** *(The remaining 1 bit is the sign bit, totaling 32 bits)*
5. **127**
6. **I-Type** (Immediate)
7. **S-Type** (Store)
8. **`funct3` and `funct7`**
9. **`0x4018`** *(Breakdown: 6th index * 4 bytes per word = 24 bytes offset. 24 in decimal is `0x18` in hexadecimal. `0x4000` + `0x18` = `0x4018`)*
10. **`lw x10, 0(x15)`**
11. **It multiplies the value by 4.** *(Shifting left by 1 multiplies by 2; shifting left by 2 multiplies by $2^2=4$. This is commonly used for array offsets).*
12. **`blt x5, x6, Loop`** (Branch if Less Than)
13. **0** (Zero)
14. **`andi x5, x5, 0xFF`** (or `255` in decimal). 
    *(The `AND` operation with 1s preserves bits, `AND` with 0s clears them).*
15. **`srl` fills the most significant (leftmost) bits with zeros, while `sra` replicates the sign bit.** *(Use `srl` for unsigned numbers and `sra` for signed numbers to preserve their positive/negative value).*