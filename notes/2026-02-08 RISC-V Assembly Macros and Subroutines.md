# RISC-V Assembly Macros and Subroutines

## quick aside ()
First, we know what register is used to handle operations.
- in CPUlator, the register used for operations is a7 (RV32)

We then also need to know what values that register understands as certain operations.
*See below, 2nd arg denotes value we should store in register a7 per operation*
```
Print an Integer,1,lw (from memory),"lw a0, my_age"
Print a String,4,la (the label),"la a0, my_name"
Print a Char,11,li (the ASCII),"li a0, 'A'"
Exit Program,10,Nothing,"li a7, 10"
```

Afterwards, based on the operation we chose, we have to correctly use load word, load address, or load immediate to print what we want to print. See above for reference again.

Lastly terminate this sequence with a system call. In this case, `ecall`

## Macros
Macros are code 'templates' that the assembler 'expands' during assemby.
When we invoke a macro, the assembler replaces our invocation with the macro's defined instructions before creating the machine code.

### Uses
- eliminates repetition
- improves code readability + maintability
- shorthand for ocmmon instructions
- reducing typing

### Time
-  macros expand at assembly time, replacing macro calls with the defined instruction sequences --> think of it like `.macro` is a toggle (that you would find in HTML/md/etc), and upon compilation, it is replaced by its defintion

### Syntax
```
.macro macro_name argument1, argument2
    # Macro body using \argument1, \argument2
.endm

# Invocation (no parentheses in GNU assembler)
macro_name value1, value2
```

### Examples
```
.macro print_int reg
    li a7, 1              # Print integer ecall
    mv a0, \reg           # Move value to print (note backslash)
    ecall
.endm

# Usage
lw t0, value
print_int t0              # Expands to the three instructions above
```

## Subroutines
Subroutines are independent code blocks that execute at runtime. 
==Differs from macros== because they exist as ACTUAL CODE in memory that can be called multiple times, with control transferring to the subroutine and then returning.

### Uses
- implementing complex operations that would be too large for macros
- saving memory (bc it is one copy of code that can be called 1+ times)
- creating modular + organized programs
- building libraries of reusable functions

### Time
- reusable code blocks called at runtime.

### Syntax
```
# Definition
subroutine_name:
    # Save registers to stack
    addi sp, sp, -N       # Allocate stack space
    sw reg, offset(sp)    # Save registers
    
    # Subroutine body
    
    # Restore registers from stack
    lw reg, offset(sp)    # Restore registers
    addi sp, sp, N        # Deallocate stack
    ret                   # Return to caller

# Invocation
call subroutine_name      # Saves return address in ra, jumps to subroutine
```

### Example
```
print_int:
    addi sp, sp, -4       # Allocate 4 bytes on stack
    sw a7, 0(sp)          # Save a7
    li a7, 1              # Print integer ecall
    ecall
    lw a7, 0(sp)          # Restore a7
    addi sp, sp, 4        # Deallocate stack
    ret                   # Return to caller
```

## Important Components to know

### Stack Pointer: `sp`
The stack pointer points to the top of the stack.
*In context of assembly, the stack is a memory region used for temporary storage. The stack grows downward. See below*
```
addi sp, sp, -N # allocates N bytes (moves stack pointer down)
addi sp, sp, N # deallocates N bytes (moves stack pointer up)

```

For the context of subroutines, the stack is crucial for preserving register values across the subroutines calls. (prevents data loss). This is because we save the value of the register to the stack and after the subroutine's essential function is done, we assign the value of the register to the stack pointer (which held its original value).

### Return Address: `ra`
When `call` executes, it saves the address of the next instruction ==automatically== (sequentially, in the main program) to the register `ra`. 

This allows the subroutine to know where to return the control to after it completes.

How I think of it: `ra` is the "resume" if we imagine that the main program is a video that we pause to read a random article, which in this case is our subroutine.

### Return Instruction: `ret`
`ret` transfers control back to the address that we stored in `ra`. IT tells us that the subroutine is finished. 

Without it, the processor would continue to execute whatever instructions follow the subroutine in memory -> unpredictable outcome / crashing

`ret` MUST come after any `ecall` in subroutine


## Ignore
note: #elaborative-interrogation : new obsidian #; I use it to reinforce my own understanding