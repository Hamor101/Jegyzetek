<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">Information encoding
- In computer science, we often have to `encode information into binary`, such as:
  - `Numbers`
    - Integers --> Regular [decimal to binary](number-systems.md/#converting-decimal-to-binary) conversion, but pad with leading zeroes[^1] for a specified length (8, 16, 32, 64, 128 bits)[^2]
    - Non-integers
      - Float (can be 32/64 bits long) --> Uses the normal form (2.5*10<sup>6</sup>), except in binary. It stores (in one number): the sign (+/-), the mantissa, and the exponent
  - `Characters` (text)
  - `Colors`
  - `Sound`
  - `Videos`

## <span style="color:#fabd2f">Representing negative numbers, two's complement
- Regular binary numbers are good at representing positive numbers
- But how to represent negative numbers?
### Method one
- We can use 1 bit at the start to indicate the sign
- This is good, but difficult to calculate with
  - A better method is needed
### <span style="color:#fabd2f">Two's complement (the better method)
- If positive: simply convert to binary, and done :)
  - BUT make sure the `leftmost bit`[^4] is 0 (use padding, if needed)
- If negative:
    1. Convert to binary (-12 --> 1100 --> 00001100)
    2. Reverse each bit (00001100 --> 11110011) --> one's complement
    3. add 1 to the number (11110011 --> 11110100) --> two's complement 🥳🥳


[^1]: `Padding with zeroes`: Adding extra zeroes to the front of the number that don't change its value, but make it so that the binary number has a given length, like 16, e.g: 1101 (4-bit length) = 0000000000001101 (16-bit length, same value)
[^2]: This is called word length, it determines the size of one single compartment/number in memory
[^3]:The sign bit is 0 for positive numbers, 1 for negative
[^4]: Leftmost bit is the bit on the left, sometimes also called 'the most significant bit'