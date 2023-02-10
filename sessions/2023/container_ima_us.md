# Container IMA using eBPF 

**Presenters**: Avery Blanchard, Lily Sturmann (Red Hat)

**Session Type:** Presentation (25min)

**Topics**: cGroups, Namespaces, Kernel, eBPF, Container Integrity, Security , Container IMA

## Session Details:

With the ubiquity of container-based virtualization, the ability to ensure trust in a container is a pertinent security issue. The mechanism in the Linux kernel for measuring integrity within a system, Integrity Measurement Architecture IMA, does not support Linux containers. This leaves a substantial gap in container integrity and trust. I present a solution to this problem by implementing a run-time solution for continuous integrity monitoring of Linux containers without changes to the kernel. I extend the Integrity Measurement Architecture to Linux containers through the use of a loadable kernel module, software emulated TPMs, and eBPF. This presentation explores the design, implementation, and future work to be done to measure container integrity.
