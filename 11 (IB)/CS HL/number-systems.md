<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">Number systems

## Data vs. Information
- `Data`:
  - Raw
  - Uninterpreted
- `Information`:
  - Interpreted
  - processed
  - put into  context
- In CS, we must often put information into a machine-processable state (=binary)

## <span style="color:#fabd2f">The binary system
- Decimal system:
  - Each digit can have 10 different values (0...9)
  - Local values are multiplied by powers of ten --> ones, tens, hundreds, etc.
    - e.g 156 = 1 * 10<sup>2</sup> + 5 * 10<sup>1</sup> + 6 * 10<sup>0</sup>
- Binary system:
  - Each digit can have `two different values` (0,1)
  - Difference between digits: powers of two

### <span style="color:#fabd2f">Hexadecimal system
- Each digit can `have 16 values` (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)
  
### <span style="color:#fabd2f">Converting binary to decimal
1. Write each digit as a multiple of a power of two, based on its position
2. Sum them up
3. Done!

- 1001 = (1 * 2<sup>3</sup>) + (0 * 2<sup>2</sup>) + (0 * 2<sup>1</sup>) + (1 * 2<sup>0</sup>) = 9

### <span style="color:#fabd2f">Converting decimal to binary
1. Repeatedly `divide by 2`
2. Read out the `remainders from top to bottom`
3. Done!
- 156<sub>10</sub> = 10011100<sub>2</sub>

|Result|Remainder|
|-----|-----|
|156|0|
|78|0|
|39|1|
|19|1|
|9|1|
|4|0|
|2|0|
|1|1|

### <span style="color:#fabd2f">Converting hexadecimal to decimal
- Similar method to binary
1. Write each digit as a multiple of a power of 16
- bab<sub>16</sub>
  - b --> 11
  - a --> 10
  - b --> 11
- (11 * 16<sup>2</sup>) + (10 * 16<sup>1</sup>) + (11 * 16<sup>0</sup>) = 2987<sub>10</sub>


### <span style="color:#fabd2f">Converting hexadecimal to binary
1. Take each digit, write it up as a binary number
2. Read them all out together
- 1224<sub>16</sub>
  - `1` --> 0001
  - `2` --> 0010
  - `2` --> 0010
  - `4` --> 0100
- 1224<sub>16</sub> --> \[0001\],\[0010\],\[0010\],\[0100\] --> 0001001000100100
- c1ca:
  - `c` --> 12 --> 1100
  - `1` --> 1 --> 0001
  - `c` --> 12 --> 1100
  - `a` --> 10 --> 1010 
- c1ca<sub>16</sub> --> \[1100\],\[0001\],\[1100\],\[1010\] --> 1100000111001010

<sub></sub>

### <span style="color:#fabd2f">Binary to Hexadecimal
- 1 hex digit --> 4 binary digits
  - therefore: 4 binary digits --> 1 hex digit
- 101010110110010101 --> \[10\] \[1010\] \[1101\] \[1001\] \[0101\]
  - `10` --> 0010<sub>2</sub>--> 2<sub>10</sub>--> 2<sub>16</sub>
  - `1010` --> 1010<sub>2</sub> --> 10<sub>10</sub> --> A<sub>16</sub>
  - `1101` --> 1101<sub>2</sub> --> 13<sub>10</sub> --> D<sub>16</sub>
  - `1001` --> 1001<sub>2</sub> --> 9<sub>10</sub> --> 9<sub>16</sub>
  - `0101` --> 0101<sub>2</sub> --> 5<sub>10</sub> --> 5<sub>16</sub>
- 101010110110010101<sub>2</sub> --> 2AD95<sub>16</sub>

### <span style="color:#fabd2f">Decimal to hexadecimal
- 2 ways:
  - Use same method as [decimal to binary](#converting-decimal-to-binary), but divide by 16 instead of 2
  - [convert to binary](#converting-decimal-to-binary), then [convert to hexadecimal](#binary-to-hexadecimal) (easier if you don't have a calculator)

- `Method 2`:
  
|Result|Remainder|
|-----|-----|
|2242|0|
|1121|1|
|560|0|
|280|0|
|140|0|
|70|0|
|35|1|
|17|1|
|8|0|
|4|0|
|2|0|
|1|1|
- 10011000010 --> \[1000]\[1100]\[0010]
    - 1000 --> 8 --> 8
    - 1100 --> 12 --> C
    - 0010 --> 2 --> 2
- 10011000010 --> 8c2<sub>16</sub>
