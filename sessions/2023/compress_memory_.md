# Compress memory you do not need 

**Presenters**: Antti Kervinen, Alexander Kanevskiy (Intel)

**Session Type:** Presentation (25min)

**Topics**: Container Runtimes, cGroups, Namespaces, Kernel, Containers & Virtualization, github.com/intel/cri-resource-manager

## Session Details:

Many workloads actively use only a fraction of the memory they allocate. This opens up possibilities to use RAM smarter. Memtierd is an open source tool that runs in user space, tracks memory activity of processes in Linux cgroups, and takes actions based on detected activity and given configuration. Actions include moving memory between NUMA nodes and swapping it in or out. In our demo we use memtierd for compressing inactive application memory into RAM, resulting in more free memory for other applications and the operating system. We also use memtierd for inspecting how much of the memory of a process is in different activity levels, and we share our learnings on how user space tools in general can track memory, control moving it around and page out memory of other processes in Linux.
