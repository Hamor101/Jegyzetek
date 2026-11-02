<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">Programming
- Programming: Writing sequences of instructions for a computer to execute

## <span style="color:#fabd2f">Evolution of programming
- Programming languages are classified into `five generations`

### <span style="color:#fabd2f">First generation ~1940s --> Machine code
- Writing pure machine code by hand (0s and 1s)
- `Lowest level` of programming
- `No translation` required
- Very efficient, but `platform-specific`[^1]
- Very uncomfortable for humans to use

### <span style="color:#fabd2f">Second generation ~1950s --> Assembly
- Introduced `mnemonics`[^2] (e.g ADD, MOV, SUB, CMP)
- `More readable` than first-generation languages
- `Translation required` --> Assembler: Program that translates assembly into 0s and 1s
- Still platform-specific, but now only the assembler needs to change between machines
- Control structures were introduced: `sequence, jump, conditional jump, return`

### <span style="color:#fabd2f">Third generation ~1950s-present --> High-level/Procedural languages
- These languages are the `most similar to human language`
- Allows use of english-like words, mathematical symbols to write instructions
- `platform-independent` --> Can be used with any machine BUT requires a compiler/interpreter for translation
- New features:
  - `Variables`
  - `Sequences, selection, iteration` --> Control structures
  - Object-Oriented Programming support --> basically very cool[^3]

### <span style="color:#fabd2f"> Fourth generation ~1970s-present --> Non-procedural languages
- Does not specify step-by-step logic, but rather an outcome

### <span style="color:#fabd2f"> Fifth generation ~1980s-present --> Constraint-based languages
- Neural networks and such systems use these



[^3]: Programmers can create abstract data types which have their own methods and functions
[^2]: Short words that replace the zeroes and ones so the code is more readable

[^1]: Runs only on the one kind of computer that it was written on; if you want to run it on another computer, you have to rewrite the program