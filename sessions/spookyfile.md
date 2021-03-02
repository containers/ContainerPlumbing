# Spooky Filesystems

**Schedule**: March 9 12:30-12:55 PM EST 17:30-17:55 UTC

**Presenters**: Tammer Saleh, SuperOrbital

**Topics**: cGroups, Namespaces, Kernel, Linux Kernel

[Join this session on HopIn](https://hopin.com/events/container-plumbing-days)

## Session Details:

When most people think of containers, they only think of namespaces and cgroups.  But there's a lot more fascinating kernel magic going on under the hood.  

In this talk we’ll explore some of the more interesting Linux file systems that are used throughout containers.  We’ll explore procfs, sysfs, tempfs, OverlayFS, Bind Mounts, Mount namespaces, and pivot_root.  Grasping these technologies is crucial to understanding how containerization systems like Docker and Kubernetes work under the hood.  

By the end of this talk, you'll learn how all of these file systems work together inside containers, what they're for, and how to use them at the lowest possible level.
