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

### Priming Quiz
```
**Q1.** What does this truth table represent?

|A|B|Output|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

What logic gate is this?
-> AND

**Q2.** A **multiplexer** has 4 inputs and 1 output. What does it do?
-> MUX is a selector. It picks one input to pass through

**Q3.** What is the difference between a **half adder** and a **full adder**?
-> Half adder: , Full Adder:

**Q4.** In one sentence — what does an **ALU** do?
-> An ALU performs arithmetic and logic operations (addition, subtraction, AND, OR, comparisons, etc.)

**Q5.** If I give you the expression `F = A AND B`, and A=1, B=0 — what is F?
-> 0

```

### Logic Gates

**AND**
```
|A|B|Output|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|
```
- Output is 1 when both inputs are 1
- Output is 0 otherwise

**OR**
- Output is 1 when at least one input is 1

**NOT**
- Flips the input
- 1 -> 0
- 0 -> 1

**NAND**
- AND, THEN flip the output

**XOR**
- Output is 1 when the inputs are different

### Components n stuff

**Half Adder**
- does one thing: adds two single bits together

When we add two bits, we get two outputs
- Sum: the result bit
- Carry: the overflow bit (if it exceeds 1)

Example
```
 1
+1
--
10 <- 2 in binary.

Sum = 0
Carry = 1
```

Truth Table
```
### The Truth Table

|A|B|Sum|Carry|
|0|0|0  |0    |
|0|1|1  |0    |
|1|0|1  |0    |
|1|1|0  |1    |

What gate produces the Sum output?
-> XOR

What gate produces the Carry output?
-> AND

Using the two gates, what is the output of a half adder when A = 1; B = 0?
-> Sum = 1 XOR 0 = 1
-> Carry = 1 AND 0 = 0
```

Remember pls:
`SUM = A XOR B`
`CARRY = A AND B`

**Full Adder**
- half adder can only add `two` bits
- issue with ^ is that binary addition chains multiple columns together
- each column can receive a `carry-in` from the column to its right

Thus, a `Full Adder` adds `three bits`: `A`, `B`, and `Cin` (carry-in)
- Still produces two outputs: `Sum` and `Cout` (carry-out)
- it is literally two `half adders` chained together with an `OR` gate for the carry

```
### Truth Table

|A|B|Cin|Sum|Cout|
|0|0|0  |0  |0   |
|0|0|1  |1  |0   |
|0|1|0  |1  |0   |
|0|1|1  |0  |1   |
|1|0|0  |1  |0   |
|1|0|1  |0  |1   |
|1|1|0  |0  |1   |
|1|1|1  |1  |1   |

**Q1.** Using the truth table, what is the output when A=1, B=1, Cin=1?
-> SUM = 1
-> Cout = 1

**Q2.** Why can't a half adder handle multi-bit addition on its own?
-> Because it has no carry-in bit, so it can't receive the overflow from a previous column

**Q3.** If you were adding two 4-bit numbers, how many full adders would you need?
-> Two full adders WRONG
Correct --> we need 4 ADDERS, 1 can be either full or half,
reason is because 4 bits means 4 columns to add; columns 2+ need a carry-in from the previous column

Column:   4    3    2    1
         FA   FA   FA   HA
          ↑    ↑    ↑
         Cout→Cin Cout→Cin Cout→Cin
         
Chain = ripple carry adder

```

Full Adder Build
```
Half Adder 1
A XOR B = intermediate sum (S1)
A AND B = intermediate carry (C1)

Half Adder 2
S1 XOR Cin = final sum
S1 AND Cin = intermediate carry (C2)

Final Cout
C1 OR C2 = Cout

Example [A = 1, B = 0, Cin = 1]

Half Adder 1
1 XOR 0 = 1 = S1
1 AND 0 = 0 = C1

Half Adder 2
1 XOR 1 = 0 = final sum
1 AND 1 = 1 = C2

Final Cout
0 or 1 = 1 = Cout
```
- `Sum = XOR -> XOR`
- `Cout = AND + AND -> OR`

**Multiplexer**
- Selector switch; takes multiple inputs and uses a select signal to choose exactly ONE to pass through to the output
- kinda like a TV remote: many channels (inputs), whatever number we select determines what shows up on screen (output)

MUX Structure:
- Basic 2-1 MUX has
- 2 data inputs - I0, I1
- 1 select line - S
- 1 output - Y

```
| S | Y |
|---|---|
| 0 | I0 |
| 1 | I1 |
```
- S = 0 picks I0, S = 1 picks I1
```
4-to-1 MUX | 4 inputs, 2 select lines (2 bits are neede to represent 4 choices)

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | I0 |
| 0  | 1  | I1 |
| 1  | 0  | I2 |
| 1  | 1  | I3 |

```
- the select lines = a binary number pointing to which input wins

Practice
```
You have a 4-to-1 MUX with these inputs:
I0 = 0
I1 = 1
I2 = 0
I3 = 1

**Q1.** What is the output when S1=0, S0=1?
-> Y = I1

**Q2.** What is the output when S1=1, S0=1?
-> Y = I3

**Q3.** In your own words — what is the job of the select lines?
-> The job of the select lines is to determine which single input gets passed through to the output

```


**Decoder**
- opposite of the MUX
- instead of selecting one input to pass through, it takes a single binary input and activates exactly one of many outputs
- kinda like a hotel elevator: we press floor 3 (input) and only floor 3's door opens (output), everything else stays closed

Decoder Structure
- a 2-to-4 decoder has
- 2 input lines - A and B
- 4 output lines, O0, O1, O2, O3
- exactly one output is 1 at a time, the rest have to be 0
```
Table

| A | B | O0 | O1 | O2 | O3 |
|---|---|----|----|----|-----|
| 0 | 0 | 1  | 0  | 0  | 0  |
| 0 | 1 | 0  | 1  | 0  | 0  |
| 1 | 0 | 0  | 0  | 1  | 0  |
| 1 | 1 | 0  | 0  | 0  | 1  |
```
- input AB is just a binary number pointing to which output fires

`N inputs -> 2^N outputs always`
```
2 inputs → 4 outputs
3 inputs → 8 outputs
4 inputs → 16 outputs
```

Practice
```
**Q1.** A decoder has 3 input lines. How many output lines does it have?
-> 3 inputs = 2^3 outputs = 8 outputs

**Q2.** Using the 2-to-4 truth table above, which output is active when A=1, B=0?
-> 10 = 2 = O2

**Q3.** What is the key difference between a MUX and a Decoder?
-> MUX determines which single input gets mapped to the output, but the decoder takes the single binary input and activates the one output
```


**Comparator**
- takes two binary inputs, tells us their relationship
- it tells us if A = B, A > B, A < B
- exactly one of those outputs is 1 at any given time

Comparator Structure
- 1 bit comparator has
- 2 inputs: A, B
- 3 outputs: EQ (equal), GT (greater than), LT (less than)

```
| A | B | EQ | GT | LT |
|---|---|----|----|----|
| 0 | 0 | 1  | 0  | 0  |
| 0 | 1 | 0  | 0  | 1  |
| 1 | 0 | 0  | 1  | 0  |
| 1 | 1 | 1  | 0  | 0  |
```

Comparator Gate Logic
- `EQ = XNOR(A,B) -> when both inputs are the same` | XNOR is just XOR flipped, outputs 1 when inputs are equal, 0 otherwise
- `GT = A AND NOT(B) -> 1 when A=1 and B-0`
- `LT = NOT(A) and B -> when A=0 and B=1`

Practice
```
**Q1.** What are the EQ, GT, LT outputs when A=1, B=0?
-> EQ = 0, GT = 1, LT = 0

**Q2.** What gate computes the EQ output and why does it make sense?
-> XNOR(A,B), this makes sense because this gate returns 1 if A and B are the same value

**Q3.** A branch instruction `blt a0, a1, label` branches if a0 < a1. Which comparator output does this rely on?
-> LT
```

**Register**
- stores bits over time, unlike the previous components (inputs -> outputs)
- has memory
- writes values, values stay until explicitly changed

How registers work:
- built from flip-flops; these store exactly 1 bit
- chain 32 flip flops -> 32 bit register

Register have:
- D - data input (what we want to store)
- Q - data output (what's currently stored)
- CLK - clock signal (controls WHEN data gets written)
- Write Enable  | WE - controls IF data gets written

```
| WE | CLK edge | What happens       |
|----|----------|--------------------|
| 0  | ↑        | Q holds old value  |
| 1  | ↑        | Q updates to D     |
```

Edge Triggered
- register only updates on the rising edge of the clock (when CLK goes from 0 to 1)
- register not updated continuously, only @ that one moment per cycle
- one clock tick at a time, keeps updates in sync

Registers in the CPU
- register file in RISC V: `x0-x31`: `32 registers`
- Program Counter | PC - a register
- pipeline stages use registers to hold values between stages

Practice
```
**Q1.** A flip-flop stores 1 bit. How many flip-flops do you need for a 32-bit register?
-> 32 bits

**Q2.** If WE=0, what happens to Q when the clock ticks?
-> Q does not change

**Q3.** Why does a register need a clock signal but a MUX does not?
-> Registers need to be organized in order for the CPU to work properly. Thus, they have to abide by the clock ticks. However, combinational logic like MUX can output at whatever time without consequence.
i.e. MUX is combinational -> output changes immediately with input, no timing needed
Register -> sequential -> needs clock to control when state changes

```

**Arithmetic Logic Unit | ALU**
- the calculator of the CPU
- all arithmetic and logic operation the program needs runs thru the ALU
- takes two inputs and a control signal that tells it what operation to perform, then produces one output 

ALU Structure:
- ALU has
- A, B - two data inputs
- ALU control - tells ALU which operation to perform
- Result - output
- Zero flag - a 1-bit output that is 1 when result=0 (for branch instructions)

```
| ALU Control | Operation  |
|-------------|------------|
| 0000        | AND        |
| 0001        | OR         |
| 0010        | ADD        |
| 0110        | SUB        |
| 0111        | SLT (set less than) |
| 1100        | NOR        |

ALU built with these:
Full Adder  → handles ADD and SUB
Comparator  → handles SLT and the Zero flag
AND/OR gates → handle bitwise logic
MUX         → selects which result to output based on control signal

+The control signal feeds into a MUX that picks which operation's result becomes the final output.
```

Zero Flag
- after a subtraction,
- A = B -> Result=0 -> Zero flag=1
- `beq` checks if Zero=1 to decide whether to branch

Practice
```
**Q1.** The ALU receives A=5, B=5, ALU Control = 0110 (SUB). What is the Result and what is the Zero flag?
-> Result = 0
-> Zero flag = 1

**Q2.** Which internal component of the ALU selects which operation's result becomes the output?
-> Multiplexer / MUX

**Q3.** A `beq` instruction compares two registers. Which ALU operation does it actually perform under the hood, and why?
-> it performs XNOR(x1,x2): this is the comparator EQ logic
more correct -> ALU subtracts A - B; if the result is 0, Zero flag=1; CPU then checks the zero flag to decide whether to branch
```


## Single-Cycle Datapath and CPU Control

-> How does the CPU actually execute an instruction from start to finish?
- the single-cycle datapath: the full path an instruction travels through the CPU (from the moment it is fetched to the moment the result is written)

**Instruction: 5 Stages**
```
1. Instruction Fetch - IF
2. Instruction Decode - ID
   
3. Execute - EX

4. Memory Access - MEM
   
5. Write Back - WB
```

**Stages Explained**
```
| Stage | What happens                          | Key component        |
|-------|---------------------------------------|----------------------|
| IF    | Fetch the instruction from memory     | PC, Instruction Memory|
| ID    | Decode the instruction, read registers| Register File, Control Unit|
| EX    | Perform the operation                 | ALU                  |
| MEM   | Read or write data memory             | Data Memory          |
| WB    | Write result back to register file    | Register File        |
```

**Single Cycle**
- in a single cycle CPU, one instruction completes all 5 stages in one clock cycle
- clock cycles must be long enough for the slowest instruction to finish

**Practice**
```
lw t0, 0(s0)   # load word: read memory at address s0+0, store in t0

**Q1.** What happens at the IF stage for this instruction?
-> the instruction for lw using two registers is loaded from the computer's memory
-> more corect -> the instruction is fetched from instruction memory using the PC

**Q2.** What happens at the EX stage? What does the ALU compute?
-> at the EX stage, ALU computes base address + offset to get the memory address
-> it does not load the value yet. that is the job for MEM

**Q3.** What happens at the MEM stage?
-> at the MEM stage, the value at 0(s0) is read.

**Q4.** What happens at the WB stage?
-> the value of 0(s0) is written to t0

**Q5.** Does a `sw` (store word) instruction use the WB stage? Why or why not?
-> no, because sw stores given values in memory, not to a register
```

```
add t0, t1, t2   # t0 = t1 + t2

**Q1.** What does the ALU compute at EX?
-> The ALU computes t1 + t2 = new value to store into t0

**Q2.** Does this instruction use the MEM stage? Why or why not?
-> no, no data is being read from memory. we are only working with registers

**Q3.** Where does the result end up at WB?
-> WB writes the value computed by the ALU into register t0

Key:
lw  → uses ALU (address calc) + MEM (read) + WB (write to register)
sw  → uses ALU (address calc) + MEM (write) — skips WB
add → uses ALU (compute)— skips MEM + writes result at WB
beq → uses ALU (subtract) — skips MEM and WB
```

**The Control Unit**
- brain of the CPU
- looks at opcode of the instruction and generates control signals that tell every component what to do

```
| Signal   | What it controls                              |
|----------|-----------------------------------------------|
| RegWrite | Should we write to a register? (WB stage)     |
| MemRead  | Should we read from data memory? (MEM stage)  |
| MemWrite | Should we write to data memory? (MEM stage)   |
| MemToReg | Should WB come from memory or ALU result?     |
| ALUSrc   | Should ALU use a register or immediate value? |
| Branch   | Is this a branch instruction?                 |
```

Practice
```
| Signal   | add | lw | sw | beq |
|----------|-----|----|----|-----|
| RegWrite | ?   | ?  | ?  | ?   |
| MemRead  | ?   | ?  | ?  | ?   |
| MemWrite | ?   | ?  | ?  | ?   |
| MemToReg | ?   | ?  | ?  | ?   |
| Branch   | ?   | ?  | ?  | ?   |

Use 1 for yes/active and 0 for no/inactive. Think through each instruction's datapath and reason it out.

<--------- Ans -------->
| Signal   | add | lw | sw | beq |
|----------|-----|----|----|-----|
| RegWrite | 1   | 1  | 0  | 0   |
| MemRead  | 0   | 1  | 0  | 0   |
| MemWrite | 0   | 0  | 1  | 0   |
| MemToReg | 0   | 1  | 0  | 0   |
| Branch   | 0   | 0  | 0  | 1   |

Note: lw rd, 0(rs1)
yes, 2 registers, but one register contains a memory address, which is why MemRead uses lw

Corrected:
RegWrite = 1 → result goes TO a register (add, lw)
MemRead  = 1 → we READ from memory (lw only)
MemWrite = 1 → we WRITE to memory (sw only)
MemToReg = 1 → value coming from memory, not ALU (lw only)
Branch   = 1 → beq only

For a `sw` instruction — which signals are active and which are not, and why?
-> MemWrite only
-> sw doesn't write to register, RegWrite = 0
-> sw doesn't read from memory, MemRead = 0
-> sw DOES write to memoery, MemWrite = 1
-> no val going to reg, MemToReg = 0
-> no branching, Branch = 0

```


## CPU Pipelining
**Why CPU pipelining?**
- single-cycle has problems
- ^ single-cycle CPU, while instruction 1 is at the EX stage,  the IF, ID, MEM, and WB hardware is idle
- being idle = being wasteful
- `pipelining fixes this by overlapping instruction execution`

**CPU Pipelining Core Idea**
- like a car wash with 5 stations
- rather than waiting for one car to finish all 5 stations before the next car enters, we push a new car into station 1 as soon as the previous car moves to station 2
- see below for visual
```
Cycle:  1    2    3    4    5    6    7
I1:     IF   ID   EX   MEM  WB
I2:          IF   ID   EX   MEM  WB
I3:               IF   ID   EX   MEM  WB
I4:                    IF   ID   EX   MEM  WB
```
- thus, every cycle, a new instruction enters the pipeline, so all 5 stages are busy simultaneously

**Benefit of CPU Pipelining**
- pipelining improves `throughput`
- (how many instructions finish per unit time)
- does NOT make any single instruction faster

**Issues with CPU Pipelining**
- `Hazards`: conflicts due to pipelining
- there are three types of hazards
- `Structural`: two instructions need the 
- `Data`
- `Control`

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
