# Why was nerdctl made? 

**Presenters**: Akihiro Suda (NTT)

**Session Type:** Presentation (25min)

**Topics**: Container Runtimes, Container/Image Security/SBOM, Image Building, Image formats & standards, Image transports, Containers and filesystem storage, nerdctl, containerd, stargz snapshotter, ocicrypt, cosign, bypass4netns, buildg, and more

## Session Details:

nerdctl (contaiNERD CTL) was made to facilitate development of new technologies in the containerd platform.

Such technologies include:
- Lazy-pulling with Stargz/Nydus/OverlayBD
- P2P image distribution with IPFS
- Image encryption with OCIcrypt
- Image signing with Cosign
- "Real" read-only mounts with mount_setattr
- Slirp-less rootless containers with bypass4netns
- Interactive debugging of Dockerfiles, with buildg

nerdctl is also useful for debugging Kubernetes nodes that are running containerd.

Through this session, the audiences will learn these functionalities of nerdctl, relevant projects, and the roadmap for the future.
