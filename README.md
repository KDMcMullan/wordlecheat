# wordlecheat
A helper program for 5-letter Wordle-style puzzles.

There's no interface here: you need to modify the code to solve the puzzle.

Global: exclude
A global which contains a list of letters which must not appear in the answer.

Global: inpos
A set of 5 characters. A dash (minus sign) indicates that we don't know the character in this position.

Global: notinpos
A list of sets of 5 characters. A dash (minus sign) indicates that we don't know that a particular character is not in this position.

Global: avoidDupLetters
If true, does not list words which contain the same letter more than once.

Global: buildRequired
If true, the total list of characters from notinpos must appear somewhere in teh word.

Global: initialCount
If zero, runs with the above parameters. If nonzero, displays that number of random words.

Letters in the above strings must be capital.
