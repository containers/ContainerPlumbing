# Killing in the name of eBPF 

**Presenters**: Holger Gantikow, Cedric Casper (science+computing AG, an Atos company)

**Session Type:** Lightning Talk (5min)

**Topics**: eBPF, eBPF, Podman

## Session Details:

In environments open to bring-your-own-code scenarios, user-provided containers are often given a lower trust status and additional safeguards are enabled. These include Seccomp profiles.
Seccomp can be used to restrict processes in a container, by providing the possibility to deny actions on a system call basis. To extend these capabilities we have written a service based on eBPF that detects corresponding violations and reliably terminates the corresponding Podman container. Filters can be applied to monitor only specific users or containers.
