# Challenges of Using User Namespaces at Big Scale

**Schedule**: March 9 01:00-01:25 PM EST 18:00-18:25 UTC

**Presenters**: Mauricio Vásquez

**Topics**: cGroups, Namespaces, Kernel, containerd,crio,runc,kubernetes

[Join this session on HopIn](https://hopin.com/events/container-plumbing-days)

## Session Details:

Running a process as root inside containers is a security risk: if such a process is able to break out of the container into the host, it can cause considerable damage as it will be running as a privileged user there.

User namespaces are a solution for this problem as they isolate user and group IDs, a process running as root in a container runs as non-root in the host. The OCI specification and projects like runc, containerd and cri-o support them, but Kubernetes doesn’t.

In this talk, I’ll introduce user namespaces and how they make it safe to run containers as root. I’ll explain what are the challenges and the reasons why they’re not supported in Kubernetes yet. I’ll explain how id-mapped mounts support in the kernel will make it much easier to implement and the ideas we have to implement it before we have that support in the kernel.
