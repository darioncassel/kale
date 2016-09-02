# Kale, a lisp-like language built on Python

## About

This project is an experiment in creating a programming language without knowing any of the theory involved. I essentially wanted to see where tabula rasa would take me before I took any PL classes.

### Interesting things about Kale

- ~~Uses postfix notation: ```(1 2 +) # => 3 #```~~
    - Removed to facilitate easier disambiguation. Wasn't really a feature to begin with.
- Is entirely stack-based.
- Is only lisp-like because of the parenthesis; it doesn't actually use s-expressions.
- Is interpreted to some kind of custom bytecode and then run on a very very simple VM (the kvm?).
- Only supports integer input, but can output floats.

### What it does so far

- Comments (multiline):
```
# this is a multi
    line comment! #
(+ 1 2) # => 3 #
```
**Caveat:** Comments must have an end ```#```

- Calculator-like behavior
```
(/ (* (+ 1 2) 3) 2)
# => 4.5 #
```

- Variable definition
```
# Allocate a new variable, a #
(var a)
# Print out what a contains #
(val a)
# => None #
```

- Variable assignment
```
# Allocate a new variable, a #
(var a)
# Set a to 3 #
(set a 3)
# Print out a #
(val a)
# => 3 #
```

- Using variables in expressions
```
(var a)
(set a 1)
(var b)
(set b 2)
(+ (val a) (val b))
# => 3 #
```

### Requirements

- Python 3

### How to run:

```python3 src/kale.py test.kl```
