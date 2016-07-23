# Kale, a lisp-like language built on Python

## About

This project is an experiment in creating a programming language without knowing any of the theory involved. I essentially wanted to see where tabula rasa would take me before I took any PL classes. I'm probably going to look back at this in a few years and laugh.

**Warning:** This is a toy project.

### Interesting things about Kale

- Uses postfix notation: ```(1 2 +) # => 3 #```
- Is only lisp-like because of the parenthesis; it doesn't actually use s-expressions.
- Is interpreted to some kind of custom bytecode and then run on a very very simple VM (the kvm?).
- Only supports integer input, but can output floats.

### What it does so far

- Comments (multiline):
```
# this is a multi
    line comment! #
(1 2 +) # => 3 #
```
**Caveat:** Comments must have an end ```#```

- Calculator-like behavior
```
(((1 2 +) 3 * ) 2 /)
# => 4.5 #
```

- Variable definition
```
# Allocate a new variable, a #
(a var)
# Print out what a contains #
(a val)
# => None #
```

- Variable assignment
```
(a var)
# Set a to 3 #
(a 3 =)
# Print out a #
(a val)
# => 3 #
```

- Using variables in expressions
```
(a var)
(a 1 =)
(b var)
(b 2 =)
(a val b val +)
# => 3 #
```

### Requirements

- Python 3

### How to run:

```python3 src/kale.py test.kl```
