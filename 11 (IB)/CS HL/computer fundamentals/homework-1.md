<span style="font-family:'cascadia code'">

# CS Homework 1
### 1.Draw the model of the CPU showing its parts and the special registers clearly
### 2. Name the primary functions of the arithmetic logic unit (ALU) in a computer's CPU.
   - To execute arithmetic and logic operations with data from the registers, and store the result in the accumulator
### 3. Describe the difference in function between the instruction register (IR) and the memory data register (MDR)
- The MDR:
  - Stores data last read from memory
  - Stores data about to be written to memory
- The IR:
  - Stores the instruction currently being executed by the CPU
### 4. How does the memory address register (MAR) work in conjunction with other CPU components to access memory?
- It stores the memory address which the CPU wants to access for reading or writing
- The Control Unit sends a read/write signal to the memory, along with the address stored in the MAR
  - When writing, the data in the Memory Data Register is written to the memory address stored in the MAR
  - When reading, the data is read from the memory address stored in the MAR and written to the Memory Data Register

### 5. Describe the difference between multi-core processors and single-core processors in handling tasks
- Multi-core:
  - Essentially "multiple CPUs" inside of one CPU
  - Allows for multi-threading --> multiple processes can run simultaneously
- Single-core:
  - Does not allow multi-threading --> Processes have to share processor time --> The processor has to queue up tasks and switch between executing different processes
### 6. Describe the special features of GPUs that make them efficient in handling video
- GPUs can perform the same operation on many different units (e.g pixels) at once, while CPUs would have to do so sequentially


## Page 27 questions
### 1. List the steps of the Machine Instruction Cycle
- Fetch
- Decode
- Execute
- Store
### 2. Describe the role of the address bus and the data bus during the fetch stage
- Address bus:
  - Carries the address of the next instruction to the memory
- Data bus:
  - Carries the data at the address carried by the address bus back to the CPU to be interpreted
### 3. During the execution of an instruction a value is copied from a register to the memory data register. State the type of memory operation that is going to follow this instruction
- Write to memory
### 4.Describe the role of the Program Counter in the Machine Instruction Cycle
- The program counter holds the memory address of the next instruction to be read by the CPU from memory
- After regular instructions it is incremented by the instruction's size
- When branching instructions are executed it can be overwritten
### 5. Describe the steps the CPU performs during the fetch stage of the fetch, decode, execute cycle
- Move memory address of next instruction from PC to MAR
- Send read signal to memory --> Move data from data bus to MDR
- Move data from MDR to IR
- Increment PC
### Outline what happens during the decode stage
- The CU takes the data stored in the IR and interprets it according to the instruction set of the given CPU architecture, yielding an instruction, and its operands which can be operated on.