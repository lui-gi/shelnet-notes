# Encoding Intro

What is it?
- converting one type on info to another type of info
- Why? so we can convert to more efficient formats for transmission or storage

Examples:
- color can be represented as a hex number
- characters --> ASCII
- mechanical encoding: piano player using paper roll

## Finite State Machine (FSM): a memoryless computer

example: vending machine
- 25 cents accepted only
- 50 cents needed to dispense item

```
Start: ---transition----> State 1
0 c                       25 c
0 coins                    1 coin
```
- inserting 1 quarter is a 'state transition'

```
State 1  ---transition--> State 2
25 c                       50 c
1 coin                    2 coins
```
- @ State 2 = transaction complete, reset to Start/"Original State"
```
State 2 ------end state-----> Start
50 c                             0c
2 coins      *dispense item      0 coins
```
- denote 'Start' with double circle, meaning we can start again from this "starting state"

Using Encoding:
- we can call 'Start' state 0, more abstractly, 0
- State 1 is 1, etc.
- we can use the same logic to represent state transitions
- "enumeration" is a form of encoding
Basically, converting a physical representation to an abstract identifier.

### Why does this matter?

In state 2, we are adding 25 and 25 together. We are adding 2 numbers together.

What if we build something more complicated?
We can use the essence of the FSM to build a general computer.

1837 Babbage Machine: manipulating the many gears to calculate very large numbers

Note G: a computer algorithm written by Ada Lovelace that was designed to calculate Bernoulli numbers using the hypothetical analytical engine by Babbage

Turing Machines: a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules
- read, write, move are the only operations this machine can perform
- move moves to another page/STATE, then continues the cycle
- one extremely long strip of paper, scanner/printer head
In summary, everything that is computable can be condensed into 3 different actions: read, move, write. Each "position" is a state.
- digitizing the Turing machine via transistors

## Digital Encoders

Recap: composition of semi-conductors; material that only functions when a certain amount of current flows through (allows us to control function/flow)
```
i (input) --->[material]-- i (output) --->
(must be in excited state)
```

Encoding: representing something physical -> enumerates it to abstract concept, like a number (for our own convenience)
- excited state = 1
- non-excited state = 0

We now have a device = Binary State Machine
--> This device is called a **transistor**

#look-up logic gates, transistors, encoders, read transistors in textbook, chap 4

## Abstraction in Modern Computer

Different layers of abstractions built on top of each other; altogether they can work to make something more complicated

High-level language
- level of abstraction closer to problem domain
- provides for productivity and portability
Assembly language
- textual representation of instructions
Hardware representation
- binary digits (bits)
- encoded instructions and data

**Human Language vs. Machine Language**
English vs. 0s and 1s
What is the connecting thing between these two?
--> Instruction sets: (add, move, ...)
- add --> 0001 (for example)
- move --> 0101
Could be hard wired as a function in our computer chips using logic circuits

'add', 'move', etc. is **hardware language**
- this is what programmers in the 70s had to learn

We need a unified language to govern/cross different platforms. 
- this is known as the ==**C** language.==
- one of the oldest, most maturely developed languages that interact with machine code

Python is not a compiler language, unlike C.
