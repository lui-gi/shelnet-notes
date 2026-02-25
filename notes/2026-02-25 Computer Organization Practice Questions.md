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

Fraction bits = 00111
Fractional field is 23 bits long, add 0s as necessary

F = 00111000000000000000000

v) ADD S, E, F

S E F
1 10000001 00111000000000000000000

vi) HEX (IF NEEDED)

1100 0000 1001 1100 0000 0000 0000 0000
12   0.    9.   12.  0-->
C. 0 9 C 0000

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
**Breaking Down R-Type Instruction**
```
funct7  rs2.    rs1     funct3   rd      opcode
7 bits  5 bits  5 bits  3 bits   5 bits  7 bits
31-25   24-20   19-15   14-12    11-7    6-0
```

opcode:
- tells the CPU it is an R-type format