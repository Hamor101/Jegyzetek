<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">Computational (boolean) logic
- Computers are mainly made of `small logic circuits`
- Logic circuits are built up of `logic gates`

## <span style="color:#fabd2f"> Logic gates

### Order of logical operations
- When performing logical operations, there's an order just like with regular math
- Hierarchy:
  1. NOT
  2. AND = NAND
  3. NOR = OR = XOR = XNOR
- If two operations are on the same level, they are processed from left to right


### <span style="color:#fabd2f">NOT gate
- `Negates`[^1] the input
- Notation: Ā

|In|Out|
|-----|-----|
|0|1|
|1|0|

[^1]: Inverts


### <span style="color:#fabd2f"> AND gate
- Produces true output only if `ALL` inputs are true
- A • B

|A|B|Out|
|-----|-----|-----|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

### <span style="color:#fabd2f">OR gate
- Produces true, when `at least one` of the inputs are true
- A + B

|A|B|Out|
|-----|-----|-----|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

### <span style="color:#fabd2f">NOR gate
- "NOT OR" gate --> Take the OR gate and `invert its output`

|A|B|Out|
|-----|-----|-----|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|

### <span style="color:#fabd2f">NAND gate
- "NOT AND" gate --> Take the AND gate and `invert its output`

|A|B|Out|
|-----|-----|-----|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|

### <span style="color:#fabd2f">XOR Gate
- Produces true when only one of the inputs are true (= if the inputs are different from each other)
- A ⊕ B

|A|B|Out|
|-----|-----|-----|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

### <span style="color:#fabd2f">XNOR Gate
- NOT XOR gate --> take XOR gate and `invert its output` (=only true output if both inputs are the same: 0,0 or 1,1)

|A|B|Out|
|-----|-----|-----|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|