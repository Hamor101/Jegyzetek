<span style="font-family:'cascadia code'">

## <span style="color:#fabd2f">Basic idea of a computer
- Input --> Process --> Output --> Store
- Input:    
  - Comes from some input device
- Process:
  - the CPU is responsible for processing data
  - the CPU can only read data from `primary` memory (RAM) [^1]

[^1]: This means that when we wish to start a program, the entire program must be loaded from storage into `primary memory`

# <span style="color:#fabd2f">The CPU
## Basic tasks
- Carries out logical & mathematical operations
- Controls the memory
## <span style="color:#fabd2f">Structure
### Units
- [ALU](#arithmetic-logic-unit) --> Arithmetic Logic Unit
- [CU](#control-unit) --> Control Unit
### Registers
- General-purpose registers
- Special Registers:
  - Memory Address Register (MAR)
  - Memory Data Register (MDR)
  - Program Counter (PC)
  - Instruction Register (IR)
  - Accumulator (AC)
### Caches
- L1 cache
- L2 cache

## <span style="color:#fabd2f">Control Unit
- Organizes operation of CPU and other units
- How it works:
  1. Reads instruction from memory (FETCH)
  2. Decodes instruction (DECODE)
  3. Sends control signals (EXECUTE)

## <span style="color:#fabd2f"> Arithmetic Logic Unit
- Performs all basic `arithmetic and logic operations`
- Reads and writes data from/to `registers`, not from memory
- Operation result usually written to the Accumulator

## <span style="color:#fabd2f">Special registers
- Built-in storage locations `inside the CPU`
  - for 64-bit computers --> 1 register is 64-bit
- Why do we need registers? --> Faster to read from them than from RAM

### Program Counter (PC)
- Holds the `memory address` of the next instruction
### Instruction Register (IR)
- Holds the instruction currently being executed
### Memory Data Register (MDR)
- Holds the latest piece of data read from memory
### Memory Address Register (MAR)
- Holds the memory address of data about to be read
### Accumulator (AC)
- Holds the result of the ALU's operations