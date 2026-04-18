# Computer Organization Final Review

# Content to Review
- Function calls & stack allocation
- recursion + stack frames
- Logic Circuits
- Single-cycle datapath / CPU control
- CPU pipelining
- RISC-V instructions (all)

## Function Calls + The Stack

**Concept Overview**
when function is called, CPU needs to do this:
1. `jump` to the function's code
2. `save state` so it can return correctly
3. `execute` the function
4. `restore state` and return

RISC-V uses the `stack` to do this
- `stack`: grows DOWNWARD in memory
- `[        < ---- stack ]`

**Key Registers to Know:**
```
x1 - ra - return address, where to go back after ret is called

x2 - sp - stack pointer, points to top of stack

x10-x11 - a0-a1 - return values

x10-x17 - a0-a7 - function arguments

x5-x7, x28-x31 - t0-t6 - temporaries, not saved across calls

x8-x9, x18-x27 - s0-s11 - saved registers, must be preserved
```

**General Calling Convention**
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
*Explanation of `N-4`*
-> n where n is any int, n(sp) means the memory address at sp + 12
- the reason we use `N-4`: first assume `N` is the total size of our stack frame
- `addi sp, sp, -N`: stack frame moves DOWN by `N` bytes
- initially, `sp = 1000 (assume)`. now, `sp = 1000 - N`
- we can now fill the frame from the top down
- `N-4` is the highest slot in the frame, right below where the old stack pointer `sp` used to be.
- in summary, we store `ra` in the topmost word slot of the stack frame of `N` size

**Question 1** 
```
A function foo is called by main. Inside foo, the programmer wants to use registers s0 and s1. foo also calls another function bar.
What registers must foo save on the stack, and why?
```
Answer: 
`foo` must save `ra` because it calls `bar`, which will overwrite `ra`. 

It also needs to save `s0` and `s1` because the calling convention requires callers to preserve `s` registers, since `main` might be relying on those values staying the same. 

Remember:
save `ra` if function calls anything else
save `s0-s11` for every `s`-register we use
never save `t` registers since they're volatile

**Question 2**
```
addi sp, sp, -16
sw   ra, 12(sp)
sw   s0, 8(sp)

Draw or describe the stack frame layout. What is at each address relative to sp?

(Hint: think about what offset 12(sp) and 8(sp) mean after sp has already moved down by 16.)
```
Answer:
```
High address (old sp) →  [  old sp  ]   ← where sp was before prologue
                         [    ra    ]   ← 12(sp)
                         [    s0    ]   ← 8(sp)
                         [  unused  ]   ← 4(sp)
Low address (new sp)  →  [  unused  ]   ← 0(sp)
```

Note:
there are 2 unused slots, we allocated 16 bytes (room for 4 words), but we only needed 8 bytes (since we used 2 words)

**Question 3**
```
foo:
    addi sp, sp, -16
    sw   ra, 12(sp)
    sw   s0, 8(sp)

    # ... body of foo ...

    # YOUR EPILOGUE HERE
```
Answer:
```
lw ra 12(sp)
lw s0 8(sp)
addi sp, sp, 16
ret
```

## Recursion

**Concept:**
Every recursive call gets its own `stack frame`. Each frame has its own `ra` and any `s`-registers.
- the stack naturally tracks the entire call chain

**Factorial in C**
```
int fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}

QUESTION:
If you call `fact(3)`, how many stack frames get created total, and what value of `n` is stored in each one?
```
Answer:
```
3 stack frames are created because there are 3 recursive calls

		Calls Further?
n = 3   Yes, saves ra
n = 2   Yes, saves ra
n = 1   No, doesn't have to save ra
```

Important Note!
- n = 1 does get a frame, but since it hits the base case immediately, it returns 1 immediately and never calls `fact` again.

**Factorial in RISC-V**
```
fact:
    addi sp, sp, -8
    sw   ra, 4(sp)
    sw   a0, 0(sp)       # save n (we'll need it after the recursive call)

    li   t0, 1
    bgt  a0, t0, recurse # if n > 1, recurse
    li   a0, 1           # base case: return 1
    j    done

recurse:
    addi a0, a0, -1      # n - 1
    jal  ra, fact        # fact(n-1), result in a0

    lw   t0, 0(sp)       # restore our n
    mul  a0, t0, a0      # n * fact(n-1)

done:
    lw   ra, 4(sp)
    addi sp, sp, 8
    ret
    
QUESTION
Why is a0 (the argument n) saved to the stack, even though a0 is not an s-register?

Think about what happens to a0 during the recursive call.
```
Answer:
`a0` is NOT saved simply because it is decremented.
`a0` is saved because `a0` is the return value register
- after `jal ra, fact` returns, `a0` is overwritten with the result of `fact(n-1)`

## Logic Circuits and Combinational Logic

**Decoder**
- takes an N-bit input, activates `exactly one` of `2^N` output lines
- 

## CPU Pipelining

**Concept Overview:**
NON-pipelined CPU simply executes one instruction `FULLY` before starting the next. 

a PIPELINED CPU `overlaps` the execution of multiple instructions like an assembly line

**RISC-V CPU Pipeline**
```
(Top to Bottom)

IF - Instruction Fetch
ID - Instruction Decode / Register Read
EX - Execute (ALU Operation)
MEM - Memory Access (load/store)
WB - Write Back (write result to register)
```

**Why Pipelining?**
- without pipelining, if each stage takes 1 cycle, then one single instruction takes 5 cycles
- WITH pipelining, we take 5 cycles for the `first` instruction, but afterwards, we can complete one instruction per cycle

**Pipelining Diagram**
```
Cycle:   1    2    3    4    5    6    7
I1:     IF   ID   EX  MEM   WB
I2:          IF   ID   EX  MEM   WB
I3:               IF   ID   EX  MEM   WB
```
- each instruction is one stage further behind the previous one, thus at cycle 5, all 5 stages are busy simultaneously

**Hazards**
sometimes the pipeline runs into issues, called hazards

```
Structural - Two instructions need the same hardware at the same time

Data - an instruction needs a result that hasn't been computed yet

Control - a branch changes the PC before we know which instruction comes next
```

**Question 1**
```
Instruction I2 needs the result of I1, but I1 hasn't finished EX yet when I2 reaches EX.
What type of hazard is this, and what are the two main ways to resolve it?
```
Answer: 
Type: Data Hazard

Resolving Data Hazards (2 Methods)
1. Stalling / inserting a bubble
2. Forwarding / Bypassing

`Stalling`:
- the pipeline is paused, so I2 is held back from EX until I1's result is available
```
Cycle:   1    2    3    4    5    6    7    8
I1:     IF   ID   EX  MEM   WB
I2:          IF   ID  NOP  NOP   EX  MEM   WB
                       ↑↑
                    bubbles (stalls)
```
- NOP = no operation
- works but wastes cycles because the pipeline is sitting idle waiting
- slower but simpler than forwarding

`Forwarding`:
- rather than waiting for `I1` to reach `WB` to write its result to a register, we forward the result directly from the output of `EX` (or `MEM`) to the input of the next `EX` stage
```
I1:     IF   ID   EX  MEM   WB
                   ↘
I2:          IF   ID   EX  MEM   WB
                        ↑
               result forwarded here
```
- no stall needed, therefore the result is grabbed straight off the pipeline wire before it ever reaches `WB`
- faster than stalling but requires extra hardware paths

**Question 2**
```
What type of hazard do branches create, and what are two ways a CPU can handle them?
```
Answer:
Type: Control Hazard
- when a branch instruction is in the pipeline, the CPU does not know which instruction to fetch until the branch outcome is determine at the EX stage

Resolving Control Hazards (2)
1. Stalling
2. Branch Prediction

`Stalling`:
- inserts NOPs after the branch
- waits until the outcome is known before fetching the next instruction

`Branch Prediction`:
- guess which way the branch goes and keep fetching
- if guess is correct, no penalty
- if wrong, we flush the incorrectly fetched instructions and restart from the correct path

**Question 3**
```
The CPU uses predict not taken. The branch is taken.
What happens to I2 and I3, and what does the CPU execute next?
```
Answer:
I2 and I3 are flushed
- they were fetched speculatively under the wrong assumption and are discarded before they can write any results
- the CPU fetches I4 (and) from LABEL and resumes correct execution from there
- this costs 2 wasted cycles, see below

```
Cycle:   1    2    3    4    5    6    7
beq:    IF   ID   EX  MEM   WB
add:         IF   ID  ███  ← flushed
sub:              IF  ███  ← flushed
and:                   IF   ID   EX  ...  ← correct path, fetched after flush
```

### Additional Notes:
`caller`: function that makes the call
`callee`: function that gets called

**Saved Questions:**
Why do we save registers to the stack when we call a function?
```
The function that makes the call might overwrite the registers that the caller was still using for its own values.

For example, if we were in the main function and we were using s0 and s1 for some arithmetic, but we call function foo which also uses s0 and s1 for something, we may mess up what we had goin on in main().

So basically the stack is a scratch pad.
```
