# New Kernel Features for Containers

**Schedule**: March 9 10:00-10:55 AM EST 15:00-15:55 UTC

**Presenters**: Giuseppe Scrivano, Red Hat, Kir Kolyshin, Red Hat, Dan Walsh, Red Hat

**Topics**: cGroups, Namespaces, Kernel, Linux, crun, runc

[video](https://youtu.be/eyPkTye-D0U)

## Session Details:

Join us for a discussion that summarizes our recent experience working on low level container runtimes (crun and runc), including, but not limited to, bringing in the latest and greatest Linux kernel features.
We will cover the following:
* cgroup v2 unified hierarchy: this fixes a lot of issues with cgroup v1, but the userspace support was sub-par.
* getting information about mounts: done via reading /proc/self/mountinfo, which appears to be problematic on many levels, especially with containers.
* overlay "volatile" feature: for some classes of containers storage persistence is not necessary, and these containers can take advantage of the new mount option,
* seccomp notifications: an extension for seccomp that let an external process take care of syscalls on behalf of the container.
* pidfd: a new kernel feature that helps eliminate TOCTOU issue when sending signals.
* close_range: let close a range of file descriptors with a single call.
* openat2: an extension for openat that adds new features to safely resolve a path.
