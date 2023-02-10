# Lazy Distribution of Container Images on Podman and CRI-O With Additional Layer Store Plugin 

**Presenters**: Kohei Tokunaga (NTT)

**Session Type:** Presentation (25min)

**Topics**: Container Runtimes, Image Building, Image formats & standards, Image transports, - Podman
- CRI-O
- Stargz Snapshotter/Stargz Store
- Kubernetes

## Session Details:

Pulling images is one of the most time-consuming steps in the container lifecycle. In this session, Kohei will talk about faster image distribution leveraging "Additional Layer Store" plugin of Podman/CRI-O with eStargz and zstd:chunked image formats. They are OCI-alternative but OCI-compatible image formats enabling "lazy pulling": starting up containers before the entire contents become locally available. The talk will share how Podman and CRI-O's Additional Layer Store plugin can leverage these formats for faster container startup. We will also cover recent efforts for the related tools including image creation. Through this session, we hope to encourage discussion about the plugin and image formats in the community for further improvement and adoption. People can learn about the latest status of lazy pulling and how they can leverage Additional Layer Store plugin for faster image distribution.
