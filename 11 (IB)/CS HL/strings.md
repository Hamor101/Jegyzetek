<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">Representing characters/strings
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