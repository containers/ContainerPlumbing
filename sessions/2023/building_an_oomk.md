# Building an oomkill-exporter powered by eBPF in 5 minutes 

**Presenters**: Krisztian Fekete (solo.io)

**Session Type:** Lightning Talk (5min)

**Topics**: Container Runtimes, cGroups, Namespaces, Kernel, Containers & Virtualization, eBPF, solo-io/bumblebee, Prometheus

## Session Details:

Catching oomkills is an essential, but not trivial thing to do, especially in Kubernetes clusters. Many of the existing solutions have various issues, or even limitations, and the infamous "invisible" oomkills are one the worst nightmares an SRE can possible have during on-call. Fortunately, eBPF is here to help! In this talk, we will build a Prometheus exporter, so you can sleep better at night, knowing that the oomkiller cannot get away killing your processes without triggering an alert!
