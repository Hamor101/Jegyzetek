<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">Information encoding
- In computer science, we often have to `encode information into binary`, such as:
  - `Numbers`
    - Integers --> Regular [decimal to binary](number-systems.md/#converting-decimal-to-binary) conversion, but pad with leading zeroes[^1] for a specified length (8, 16, 32, 64, 128 bits)[^2]
    - Non-integers
      - Float (can be 32/64 bits long) --> Uses scientific notation (2.5*10<sup>6</sup>), but in binary. It stores (in one number): the sign (+/-), the mantissa, and the exponent
  - `Characters` (text)
  - `Colors`
  - `Sound`
  - `Videos`
- General storage rule: n bits --> 2<sup>n</sup> values can be stored

# <span style="color:#fabd2f">Integers
## <span style="color:#fabd2f">Representing negative numbers, two's complement
- Regular binary numbers are good at representing positive numbers
- But how to represent negative numbers?
### Method one
- We can use 1 bit at the start to indicate the sign
- This is good, but difficult to calculate with
  - A better method is needed
### <span style="color:#fabd2f">Two's complement (the better method)
- If positive: simply convert to binary, and done :)
  - BUT make sure the `leftmost bit`[^4] is 0 (use padding, if needed), because negative numbers must start with 1
- If negative:
    1. Convert to binary (-12 --> 1100 --> 00001100)
    2. Reverse each bit (00001100 --> 11110011) --> one's complement
    3. add 1 to the number (11110011 --> 11110100) --> two's complement 🥳🥳


[^1]: `Padding with zeroes`: Adding extra zeroes to the front of the number that don't change its value, but make it so that the binary number has a given length, like 16, e.g: 1101 (4-bit length) = 0000000000001101 (16-bit length, same value)
[^2]: This is called word length, it determines the size of one single compartment/number in memory
[^3]:The sign bit is 0 for positive numbers, 1 for negative
[^4]: Leftmost bit is the bit on the left, sometimes also called 'the most significant bit'

# <span style="color:#fabd2f">Characters, strings
## <span style="color:#fabd2f">Characters
- Characters can be encoded using `code tables`
- Code tables define which number 'means' which letter
- Example: the [ASCII table](https://catonmat.net/images/ascii-cheat-sheet.png) -- Contains character codes for:
  - Mathematical symbols
  - Punctuation symbols
  - Characters of the english alphabet (upper- and lowercase) --> No other alphabets supported :(
  - Special characters (space, carriage return, NULL, etc.)
  - Some control characters
### <span style="color:#fabd2f">Unicode & UTF-8
- UTF-8: 8-32 bits of storage
- Its first 128 characters are the `same as ASCII` for compatibility


## <span style="color:#fabd2f">Strings
- Called string because it is a string of characters
- Contiguous in memory (the characters are stored after each other)
- Null-terminated --> last character is a so-called NULL character, so the computer knows where the last character in a string is
- E.g: nice
  - `n` --> 0110 1110
  - `i` --> 0110 1001
  - `c` --> 0110 0011
  - `e` --> 0110 0101

# <span style="color:#fabd2f">Colors
- RGB-encoding:
  - intensity of each color component (red,green,blue) represented on 8-bits
  - 1 pixel: 24 bits (8*3, because red, green, blue each need 8 bits)
  - Usually represented with HEX-codes
    - First two characters: How much red
    - Middle two characters: How much green
    - Last two characters: How much blue
    - #FF00FF --> <span style="background-color:#ffffff"><span style="color:#ff00ff">‎ ■‎ </span></span>‎ Purple
    - #000000 --> <span style="background-color:#ffffff"><span style="color:#000000">‎ ■‎ </span></span>‎ Black

# <span style="color:#fabd2f"> Sounds
- Sound is a continous, analogue signal
- Must be digitized
- Sound must be processed quickly
  - Specialized program is required to COde and DECode --> CODEC
### <span style="color:#fabd2f">Temporal digitization: Sampling
  - In a given amount of time, take X samples of sound
  - e.g: 44kHz --> 44 000 samples per second

### <span style="color:#fabd2f"> Volume digitization
- 16-bits --> 2<sup>16</sup> different levels of volume

# <span style="color:#fabd2f"> Video
- basically a `sequence of images + sound`
- Processing images and sound are both resource-intensive --> video CODEC needed
- But even a codec may be too slow
- Solution --> image keyframes:
  - Storing the difference between frames instead of the entire frames