# Text Processing Utils

## awk
- a powerful text processing tool
- uses extended [[2026-01-29 Regular Expression Metacharacters|regular expressions]] to find lines that match criteria

`awk '{print $3, $1, $2}' students_gpa.txt`
- prints 3rd, 1st, and 2nd columns of a file (in that order)

`awk '$3>3 {print $3, $2' students_gpa.txt`
If the val at column 3 is greater than 3, print column 3 and column 2

Can algo integrate with regex:
`awk '/fuz/ {print $3, $2}' students_gpa.txt`
Prints 3rd and 2nd columns of the lines that contain 'fuz'

awk program in separate file (file ext = .awk)
`awk -f awk_script.awk student_gpa.csv`
```
BEGIN {FS = ","

print "Students Name and GPA:"

print "------------------"}

{print $1}

END {print "----------------"}
```

Output:
```
bash-3.2$ awk -f awk_parser.awk students_gpa.txt 

Students Name and GPA:

------------------

Luigi Breehhh 3.1

  

Luigi Brehhhh 3.1

  

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

  

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

  

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

  

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

Luigi Brehhhh 3.1

  

  

  

  

----------------

bash-3.2$
```

Revision:
```BEGIN {FS = ","

print "Students Name and GPA:"

print "------------------"}

$3>3 {print $1, $3}
/fuz/ {print $1, $3}

END {print "----------------"}
```
-> prints top (conditional) OR bottom (regex)
same as:
```
BEGIN {FS = ","

print "Students Name and GPA:"

print "------------------"}

($3>3 || /fuz/) {print $1, $3}

END {print "----------------"}
```

## Shell Programming (see [[2026-01-20 Unix Shell Commands|shell commands]] for command basics)
Executes shell script to do many tasks at once (runs many commands at once)

```
#!/bin/bash

for count in {1..10..2}
do
	echo $count
	mkdir dir$count
	rm -r dir$count
done
```
makes 10 directories