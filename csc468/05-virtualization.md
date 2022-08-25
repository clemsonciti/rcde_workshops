
# Virtualization in Cloud Computing"
teaching: 0
exercises: 0
questions:
- "What is virtualization?"
- "Is it something specific to cloud?"
objectives:
- "Understand how the virtualization concepts in OS are extended toward cloud computing models"
keypoints:
- "Cloud computing is another way to abstract computing resources and infrastructures for users"


> ## 1. What is virtualization?    
>  
> - Operating System concept: The abstraction of available resources
> - **Virtualization technologies encompass a variety of mechanisms and techniques used to address 
> computer system problems such as security, performance, and reliability by decoupling the
> architecture and user-perceived behavior of hardware and software resources from their physical 
> implementation.** (*https:/www.computer.org/csdl/mags/co/2005/05/r5028.html/*)
>
> <img src="../fig/04-virtualization/01.png" style="height:150px">
```


> ## 2. Virtualization
>
> - [Formal requirements for virtualizeable third generation architectures](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.141.4815&rep=rep1&type=pdf)
> - A virtual machine is taken to be an efficient, isolated duplicate  of the real machine.
> - These notions can be explained through the idea of a **virtual machine monitor**. 
> - Essential characteristics of VMM:
>   - Essentially identical to the physical resource
>   - Efficiency
>   - Complete control of system resources (with regard to the processes running inside the VM)
>
> <img src="../fig/04-virtualization/02.png" style="height:300px">
>
```


> ## 3. Virtualization
>
> - Virtualization Layer: The Virtual Machine Monitor (or its modern name: **Hypervisor**) 
> provides an interface between hardware and virtual operating systems.
> - Type of hypervisors:
>   - Bare-metal
>   - Hosted
> 
> <img src="../fig/04-virtualization/03.png" style="height:300px">
>
```


> ## 4. Issues that virtualization can help with
>
> - Under-utilized resources
> - Complicated system management
> - Limited access to shared resources
> - Inefficient power consumption
> - Tight coupling with underlying resources
>
```


> ## 5. Virtualization versus multitasking versus multicore/hyperthreading
>
> <img src="../fig/04-virtualization/04.png" style="height:300px">
>
```


> ## 6. Types of virtualization
>
> - Platform Virtualization
> - Memory Virtualization
> - Desktop Virtualization
> - Application Virtualization
> - Network Virtualization
> - Storage Virtualization
>
```


> ## 7. Platform virtualization
>
> - Full Virtualization
> - Para Virtualization
> - Hardware assisted virtualization
> - OS level virtualization
>
```


> ## 8. Without virtualization
>
> - x86 offers four levels of privilege (Ring 0 through 3)
> - OS needs to have access to hardware and run on ring 0
> - Application runs on ring 3, gain access to hardware by trapping into kernel mode for 
> privileged instructions.
> - Virtualizing x86 requires a layer under OS (which already at lowest level) to create 
> and manage the VM
> - Sensitive instructions must be executed in ring 0 
>
> <img src="../fig/04-virtualization/05.png" style="height:300px">
>
```


> ## 9. Full virtualization
>
> - Guess OS is unaware of host OS.
>   - VMM provides virtual BIOS, virtual devices, and virtual memory management.
> - Non-critical instructions run directly on hardware.
> - Runtime translation of critical non-virtualizable instructions happens in the hypervisor.
> - Provide best isolation and security at the cost of performance.
>
> <img src="../fig/04-virtualization/06.png" style="height:300px">
>
```


> ## 10. Para virtualization
>
> - Thin layer interfaces between each guest OS and underlying hardware.
> - Need guest kernel modification.
> - No need of runtime translation for critical instructions.
> - Superior in performance.
> - Requires expertise to patch the kernels.
>
> <img src="../fig/04-virtualization/07.png" style="height:300px">
>
```


> ## 11. Hardware-assisted virtualization
>
> - Hardware provides support to run instructions independently.
>   - Intel Virtualization Technology (VT-x)
>   - AMD Virtualization Technology (AMD-V)
> - No need to patch the kernels.
> - Runtime translation not required.
> - Better performance in comparison to other variants.
> - Greater stability
>
> <img src="../fig/04-virtualization/08.png" style="height:300px">
>
```


> ## 12. Virtualization at OS level
>
> - Same OS for both host and guest machines.
> - User space is completely isolated.
> - High performance.
> - Extremely light-weight.
>
```


> ## 13. Memory virtualization
>
> - How to share physical system memory and dynamically allocating it to virtual machines.
> - Guess OS maps virtual memory space (of VM) to physical memory space (of VM).
> - VMM translates physical memory space (of VM) to physical memory space (of main machine), 
> but also enables direct mapping (shadow table) to avoid overhead.
>
> <img src="../fig/04-virtualization/09.png" style="height:300px">
>
```


> ## 14. Summary
>
> |  | Full Virtualization with Binary Translation | Hardware Assisted Virtualization | OS Assisted Virtualization/Para Virtualization |  
> | ----------- | -------------- | -------------- | ------- |  
> | Guest modification/Compatibility | Unmodified Guest OS, excellent compatibility | Unmodified Guest OS, excellent compatibility | Guest OS codified to run Hypercall, cannot run of native hardware or other hypervisors. Poort compatibility |  
> | Performance | Good              | Fair              | Better on certain cases       |  
> | Guest OS Hypervisor Independent | Yes              | Yes              | Xen Linux runs only on Xen Hypervisor. VMI-Linux is Hypervisor agnostic       |  
>
```


> ## 15. Desktop and application virtualization
>
> - Desktop and Applications run on servers.
> - Stateless thin clients connected to servers.
> - Efficient system management.
> - Requires high-end servers for system stability
>
```


> ## 16. Network and storage virtualization
>
> - Similar idea of providing an abstraction layer to the physical infrastructures
> - In networks, abstraction will
>   - Be at the level of routers, switches, gateway, firewalls, load balancers, …
>   - Enabled by software-defined networking
> - In storage, single storage backends can be used for different requirements
>   - Ephemeral
>   - Persistent
>   - Specialize storage backends
>
```


> ## 17. Virtualization: concept of overcommits
>
> - Allocating more than the available physical resources to the Guest OS
> - Common types of overcommit:
>   - CPU 
>   - Memory 
>   - Storage 
>
```


> ## 18. Virtualization: concept of overcommits
>
> - Advantages:
>   - Favorable economic model
>   - Efficient resource utilization
>   - Support green computing
> - Disadvantages:
>   - Performance loss or unstable system response
>   - Complex system understanding
>   - VM shutdown by the hypervisor
>
```


> ## 19. Virtualization: CPU and memory overcommits
>
> - Allows more virtual CPUs than physically available
>   - Openstack KVM: overcommit-number = 16.0
> - Allow more memory than physically available
>   - Overstack KVM: overcommit-number = 1.5GB
>
```


> ## 20. Virtualization hypervisors
>
> - Contribution from industry and academia
> - Xen: Project from Cambridge Computer Laboratory
> - VMware: Commercial product
>   - Also comes from academic research (see Mendel Rosenblum ACM)
> - KVM: Initiated by the Open Virtualization Alliance, later dissolved and is now managed 
> by the Linux Foundation
> - Qemu: Open source machine emulator and virtualizer
>
```


> ## 21. Virtualization in the cloud
>
> <img src="../fig/04-virtualization/10.png" style="height:300px">
>
```


> ## 22. Openstack: Compute
>
> <img src="../fig/04-virtualization/11.png" style="height:300px">
>
```


> ## 23. Openstack: Compute
>
> <img src="../fig/04-virtualization/12.png" style="height:500px">
>
```


> ## 24. Openstack: Cinder
>
> <img src="../fig/04-virtualization/13.png" style="height:300px">
>
```


> ## 25. Openstack: Neutron
>
> - Management: internal comm between OpenStack components, reachable only within the 
> data center.
> - Guest: Used for VM data communication within the Cloud Deployment.
> - External: Provide VM with Internet access.
> - API: Exposed all the Stack’s API to the public.
>
> <img src="../fig/04-virtualization/14.png" style="height:300px">
>
```



{% include links.md %}

