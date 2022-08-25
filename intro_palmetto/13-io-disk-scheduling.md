
# I/O and Disks: Disk Scheduling"
teaching: 0
exercises: 0
questions:
- "How to access data on disk?"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"



> ## 1. Input/Output devices
> 
> - Critical to computer systems
>   - Without input: Same results every time.
>   - Without output: What’s the point?
> - How should I/O be integrated into systems?
> - What are the general mechanisms?
> - How can we make them efficient?
```


> ## 2. Classical system architecture
> 
> - Hierarchical structure due to the relationship between physics and costs:
>   - The faster the bus, the shorter it is. 
>   - The faster the bus, the more complex it is to design and build (hence more costly). 
> <img src="../fig/io/01.png" alt="classical system" style="height:400px">
```


> ## 3. Modern system architecture
> 
> - Specialized chipsets and faster point-to-point interconnects. 
>
> <img src="../fig/io/02.png" alt="modern system" style="height:400px">
```


> ## 4. Canonical device
> 
> - Interface: allowing system software to control the device's operations
> - Internal structure: implementing the abstraction presented to the system.  
> - Abbreviations:
>   - DMI: Direct Memory Interface
>   - ATA: IBM's PC AT Attachment. 
>   - SATA: Serial ATA
>   - eSATA: External Serial ATA
>   - PCIe: Peripheral Component Interconnect Express
>
> <img src="../fig/io/03.png" alt="canonical device" style="height:150px">
```


> ## 5. A simple canonical protocol
> 
> - Repeatedly read the register for READY status.
> - Send data to register (Programmed I/O - PIO).
> - Write a command to the command register to initiate device execution.
> - Wait until the device is done.  
> - What is a problem with this approach?
>
> <img src="../fig/io/04.png" alt="canonical device" style="height:300px">
```


> ## 6. Hardware interrupts
> 
> - Instead of polling the device, the OS can:
>   - After issue an I/O request, put the calling process to sleep and context switch 
>   to another.
>   -  When the request is finished, the device will raised a hardware interrupt to 
>   return CPU to the OS.
> - Predetermined interrupt service routine (ISR) - interrupt handler.
>   - This allows overlap of computation and I/O (recall CPU scheduling slides)
> - To avoid interrupts all the time, a hybrid model is employed (scheduling). 
>
> <img src="../fig/io/05.png" alt="canonical device" style="height:200px">
```


> ## 7. Programmed I/O overheads
>
> - Programmed I/O: I/O instructions that move data from storage into register
> for computation purposed. This requires the CPU's involvement in every transactions. 
> - With programmed I/O, the CPU spends too much time moving data to and from devices. 
> - How do we offload this work: Direct Memory Access (DMA) device
>   - Orchestrate transfer between devices and main memory without much CPU intervention.
> - Example: Intel Broadwell Crystal Beach DMA Application
>   - Supports write operations from memory to I/O, but not from I/O to memory
>   - Instantiated as a root complex integrated PCIe end-point device
>   - Chipset DMA that is controllable by software executing on the processor
>   - A standardized software interface for controlling and accessing DMA features
>   - There are eight software visible CB DMA engines, visible as PCI functions. 
>     - Each engine has one channel. 
>     - Each can be independently operated. 
>     - In a virtualized system, each can be independently assigned to a VM. 
> - Copying of data is handled by DMA controller. 
>
> <img src="../fig/io/06.png" alt="canonical device" style="height:200px">
```


> ## 8. Method of device interaction
>
> - First method 
>   - Explicit I/O instructions (privileged)
> - Second method
>   - Memory-mapped I/O
> - The hardware makes the device registers available as if they were memory 
> locations.
> - No clear advantages on either method
```


> ## 9. Device driver
>
> - How to fit various I/O devices with different interfaces into the OS 
> (which is supposed to be generic)?
> - Abstraction, abstraction and abstraction: device driver
> - 70% of OS code is found in device drivers.
> - Unofficial device drivers are often the cause for kernel crashes. 
> - Example:
>   - [AMD Device Driver for Vulkan](https://gpuopen.com/amd-open-source-driver-for-vulkan/)
>   - [API guide for Linux driver implementation](https://www.kernel.org/doc/html/v4.11/driver-api/index.html)
>
> <img src="../fig/io/07.png" alt="device driver" style="height:300px">
```


> ## 10. Disk Drive
>
> - Large number of sectors (512-byte blocks)
> - Sectors are numbered 0 to n-1 on disks with n sectors. This is the address space of 
> the drive. 
> - Multi-sector operations are possible (read or write 4K bytes at a time). 
> - Only a single 512-byte write is guaranteed atomic.
>
> <img src="../fig/io/08.png" alt="physical structure of hard drive" style="height:700px">
```


> ## 11. Seek, rotation, transfer
>
> - Seek: move the disk arm to the correct cylinder
>   - depends on how fast disk arm can move
>   - typical time: 1-15ms, depending on distance (average 5-6ms)
>   - improving very slowly: 7-10% per year
> - Rotation: waiting for the sector to rotate under the head
>   - depend on the rotation rate of the disk (7200 RPM SATA, 15K RPM SCSI)
>   - average latency of ½ rotation (~4ms for 7200 RPM disk)
>   - has not changed in recent years
> - Transfer: transferring data from surface into disk controller 
>  electronics, or the other way around
>   - depends on density, higher density, higher transfer rate
>   - ~100MB/s, average sector transfer time of ~5 microseconds
>   - improving rapidly (~40% per year)
```


> ## 12. Disk scheduling
>
> - The OS has a queue of disk requests, therefore there is a chance 
> to schedule these requests
> - We want to minimize seeking
```


> ## 13. Disk scheduling algorithms
>
> - FCFS (do nothing)
>   - reasonable when load is low, long waiting time when load is high
>
> <img src="../fig/io/09.png" alt="FCFS" style="height:400px">
>
> - SSTF (shortest seek time first)
>   - minimizes arm movement
>   - favors blocks in middle tracks, because they have more blocks nearby.
>
> <img src="../fig/io/10.png" alt="SSTF" style="height:400px">
>
> - SCAN (elevator)
>   - serve request in one direction until done, then reverse
>   - like an elevator, avoid going back and forth in the middle
>
> <img src="../fig/io/11.png" alt="SCAN" style="height:400px">
>
> - C-SCAN (typewriter)
>   - like SCAN, but only go in one direction (no reverse direction)
>
> - LOOK / C-LOOK
>   - like SCAN/C-SCAN, but only go as far as last request in each direction, 
>   instead of going full width of the disk. 
>
> <img src="../fig/io/12.png" alt="LOOK" style="height:400px">
>
> - Disk scheduling is important only when disk requests queue up
>   - important for servers
>   - not so much for PCs
> - Modern disks often do disk scheduling themselves
>   - Disks know their layout better than the OS, can optimize better
>   - on-disk scheduling ignores, undoes any scheduling done by the OS
>
```


{% include links.md %}

