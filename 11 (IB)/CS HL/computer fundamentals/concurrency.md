<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">Pipelining and parallel processing
- We always aim to make program execution faster
- Two techniques exist for speeding up program execution:
  - Pipelining
  - Parallel processing

## <span style="color:#fabd2f">Pipelining
- Allows multiple instructions to be processed simultaneously by `overlaying the different stages`
- 
- E.g: Fetch instruction 2, while decoding instruction 1, etc.

## <span style="color:#fabd2f">Parallel processing
- We can try to "multitask" and divide our tasks into different parts to process them simultaneously
### <span style="color:#fabd2f">Multithreading
- Single core running a "fake" parallel process, making it look like several cores were processing (not truly parallel)
### <span style="color:#fabd2f">Multi-core architecture
- Multiple independent CPU cores get different tasks --> True parallel processing
### <span style="color:#fabd2f">Amdahl's law
- The performance speedup from multiple cores is strictly limited by the sequential portion of the program


## <span style="color:#fabd2f">Parallel processing hazards
- An instruction can `depend` on the result of the previous instruction (=> Dependant instruction)
- Sometimes the required instruction hasn't finished yet

### <span style="color:#fabd2f">Solution 1
- CU stops the `dependant instruction` until the required instruction is finished
- Creates 'bubbles'[^1] in the pipeline
[^1]: Empty cycles where nothing is done

### <span style="color:#fabd2f">Solution 2 -- Data forwarding
- If we know the next step relies on the previous step, we can reroute the result into the input immediately
- ALU output `rerouted` into ALU output, skipping registers

## <span style="color:#fabd2f">Control Hazards
- CPU doesn't know next instruction address until branching condition is decided

### <span style="color:#fabd2f">Solution 1 -- Pipeline flush
- Simply continue execution, if we find later that we loaded the wrong instruction, simply discard them, and load the correct one

### <span style="color:#fabd2f">Solution 2 -- Branch prediction
- Processor tries to `predict the result` of the branch instruction
- Uses the prediction to `decide which instruction to load`
- If it makes a mistake, loading the wrong instruction:
  - Just do pipeline flush


## <span style="color:#fabd2f">Hazards of concurrency (threading)
- Threads often have to work on the same data
### <span style="color:#fabd2f">Race condition:
- Two different threads write to the same memory
- The value isn't updates for thread 2 while thread 1 is writing to it
- The value of the thread results on timing, and "who gets there first"
  
Solution:
- Use `Locks` --> Lock the variable we want to change until we're finished, and only then let the other thread use it
### <span style="color:#fabd2f">Deadlock:
- `Thread A` has `Lock X`, waiting for `Lock Y`
- `Thread B` has `Lock Y`, waiting for `Lock X`
- Result: Two threads will `wait forever`