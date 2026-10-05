<span style="font-family:'cascadia code'">

# <span style="color:#fabd2f">The Operating System

- Computers run programs
- The most important program the computer runs is the `Operating System`

## <span style="color:#fabd2f">Main functions of the operating system
- Controls hardware resources
- Provides services for programs
- `Intermediary` between applications and the hardware

## <span style="color:#fabd2f">Operating System Services (Why do we need an OS?)
- `Memory` management
- `Data` management
- `Device` management
- `Scheduling` management
- `Resource monitoring`
- `Virtualization`
- `Networking`
- `Security`
- `Error detection`/recovery

## <span style="color:#fabd2f">Memory management
- OS is `responsible for all available memory` in the computer
- When a new program starts
  -  OS `assigns some amount of memory` to the program
  - `Maintains a program's place` in memory while it is running
- OS tracks available memory

## <span style="color:#fabd2f">Disk access
- To start an application --> We must find it in `secondary storage`
- Organize data into files and directories[^1]
- Optimize storage space (e.g Defragmenting the disk)
- Keep track of where files are in secondary memory, so they don't get overwritten
[^1]: Basically folders

## <span style="color:#fabd2f">Device management
- Communicate with `peripherals`[^2]
- Communication is done via `device drivers` (small programs that tell the OS how to communicate with the peripheral)

## <span style="color:#fabd2f"> Scheduling
- Multitasking --> When programs `run in parallel`
- Many programs run at the same time --> `Processor time must be divided` between them
- OS must `decide which program can run` and for how long
- Scheduling allows more programs to run, speeds up response time

## <span style="color:#fabd2f">Resource monitoring
- OS tracks the amount of memory/storage/processor time a program uses

## <span style="color:#fabd2f"> Virtualization
- Multiple operating systems can be run at the same time on the same computer
- Programs interact with virtual "fake" hardware pieces
- Useful `mainly in professional life`, not so much in private computer usage

## <span style="color:#fabd2f"> Networking
- `Manage interactions` with networks
- Allows sharing of resources between computers
- Translate requests to network devices

## <span style="color:#fabd2f"> Security
- Identification services (e.g password)
- Manage user accounts
- Create `log files`

## <span style="color:#fabd2f">Error detection
- Close erroneous programs
- Make sure faulty programs don't damage the system
- Create `memory dumps`


[^2]:hardware devices outside the computer (e.g Mouse, keyboard, monitor, printer)