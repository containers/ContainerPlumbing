# Zero Trust: Running Confidential Computing Containers

**Schedule**: March 10 11:30-11:55 AM EST 16:30-16:55 UTC

**Presenters**: Samuel Ortiz, Intel

**Topics**: Container Runtimes, Container/Image Security, Containers & Virtualization, Image formats & standards, containerd, CRI-O, Kata Containers, QEMU, Cloud Hypervisor

[video](https://www.youtube.com/watch?v=o0ScKmPRAeQ)

## Session Details:

Today’s containers run in wildly heterogeneous environments. When deployed on multi-tenant clouds, they can span across nodes, regions, and multiple Cloud Service Providers (CSPs) while sharing CSP-owned resources between tenants. In such hostile environments, protecting containers data and code is a challenge and requires full trust on the CSP stack. Confidential computing leverages emerging hardware technologies to protect cloud code and data at rest, in transit and in use, allowing tenants to trust no one but themselves.

In this presentation, we will describe cloud native gaps for supporting confidential computing through memory encryption, authenticated launch and application attestability.  Attendees will learn about the proposed Kata Containers-based architecture to bring confidential computing to cloud native workloads. We also hope that this session will help initiate a wider community driven effort towards defining and implementing an end-to-end solution for cloud native confidential computing.
