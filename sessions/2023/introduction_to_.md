# Introduction to NRI 

**Presenters**: Krisztian Litkey, Peter Hunt, Redhat (Intel)

**Session Type:** Presentation (25min)

**Topics**: Container Runtimes, CRI-O, containerd, NRI

## Session Details:

The Node Resource Interface allows one to plug custom logic into NRI-enabled OCI-compatible runtimes and adjust the configuration of containers managed by that runtime. The recently released 0.2.0 version reworks how plugins communicate with the runtime, how plugins adjust container configuration, and what configuration parameters plugins can adjust through NRI. 0.2.0 is also the first version which is supported by the most commonly used container runtime implementations in Kubernetes: CRI-O and containerd.

While NRI is still experimental, this latest release already allows one to plug some interesting and useful functionality into runtimes. In our talk, we briefly discuss how NRI works and what kind of controls it provides over containers. Then we’ll demonstrate some of NRI’s current capabilities in practice using existing NRI plugins.
