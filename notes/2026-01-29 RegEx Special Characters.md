# RegEx Special Characters

## Characters
Any character on the keyboard except newline (\n)

Literals
- the characters represent themselves within a regex
Special chars
- the characters not represent themselves within a regex
- example: $ matches the end of a line only, or + * ?

Example: 
`noun + verb + noun`
noun, verb has a special meaning
`He eats food`
Each individual word has no special meaning.

In regex, literals can be treated as *words* and special characters can be treated as *grammar*

## Delimiters

- special characters used to mark the beginning and end of a regex
- any char can be used as a delimiter, however most often `/` is used
- delimiters are not used with `grep`

## Special Characters / Meta Characters 

- metacharacters with special meaning are `\ [] ^ $ . * | ? + ()`
- `-` is only considered a metacharacter within square brackets (when indicating a range)
  ex: ab- is literal, no extra meaning
  [a-b] has extra meaning

`{}`
- `{}` only considered as a metacharacter when it is part of repetition operator
- ex ^ (cat){1,3}, means repeat 1 to 3 times

Example:
(ab+){1,3}
ab -> ab, abab, ababab
abb -> abb, abbabb
abbb -> etc.
abbbbbbb
etc. -> etc.

`.` = match with any ==character==
- to match any single character, use .
- `.nd` follow any character that terminates with `nd`

`[]`
- to match any of the single characters in a range, use []
- [abc] == [a-c]
- other metacharacters lose their special meanings inside square bracket
- [A-Da-d] = ABCDabcd

`\`
- to convert a metacharacter into a literal, use a `\`
- `\.` = matches with `.` 

`$` / `^`
- $ matches the end of a line only
- ^ matches the beginning of a line only
`and i was here ah`
- `a.$` = ah
- `^.nd` = and
Exception: `[^abcd]` = exclude abcd

`?`
- ? matches ==zero or one== occurrence of the single preceding character
- ex:`ab?` -> a or ab only


`*`
- * matches ==zero or more== occurrences of the character that precedes it
- ex: `ab*` = a ab abbbb ...
- ex: a(bc)* = a abc abcbc abcbcbcbcbc ...

`+`
- + matches ==one or more== occurrences of the single preceding character
- ex: `ab+` = ab abb abbb abbbbbb abbbbbb ...

`()`
- () group the matched string by regex inside it

`|`
- | matches either expression (acts like 'or')

Other examples:
(ab){1,2}c = ababc abc

## Character Classes

- \s = White space
- \S =

## grep
Find all lines containing the word 'error' in a log file:
`grep "error" /var/log/syslog`

Find all lines that start with the word "error"
`grep "^error /var/log/syslog`

Find all words that do not contain the word "success"
`grep -v "success" file.txt`
- -v flag: invert

#look-up Practices (phone #, MDY format, passwords, etc.)

`[a-z\s]*hello`
- hello
- yhello
- h hello
- say hello
