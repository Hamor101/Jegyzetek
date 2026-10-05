# Homework 2

## Outline two differences between ROM and RAM
- ROM cannot be electronically ovewritten, while ram ca neb
- ROM is not volatile, while ram is

## Explain why ROM rather than RAM is used to store the instructions a computer needs at startup
- Because the ROM is non-volatile, and cannot be changed by the software

## State what EEPROM stands for and name two of its applications
- Stands for: Electronically Erasable Programmable Read Only Memory
- Used for:
  - Storing the BIOS in a computer
  - Storing things that can identify the hardware of the computer

## Explain why cache memory is important for CPU perofmrance and how different levels of cache memory vary in terms of speed and size
- Cache speeds up fetching of data, by saving frequently used data in the cache, which is physically closer, or inside the CPU.
- Speed vs Size:
  - L1: Fastest, smallest
  - L2: Medium speed, medium size
  - L3: Slowest cache, largest size

## Explain the difference between a cache hit and a cache miss, and why a higher hit rate improves performance
- Cache hit: the cpu requests some piece of data from the cache. Since the cache has it, it gets loaded into the CPU
- Cache miss: the CPU request some piece of data from the cache. The cache does not have this piece of data, so the data must be retrieved from RAM. This is slower than a cache hit.
- A higher hit rate means higher performance, because fetching more data from the cache inherently means higher performance