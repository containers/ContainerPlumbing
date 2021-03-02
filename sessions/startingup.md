# Starting up Containers Super Fast With Lazy Pulling of Images

**Schedule**: March 10 10:00-10:25AM EST 15:00-15:25 UTC

**Presenters**: Kohei Tokunaga,

**Topics**: Container Runtimes, Image formats & standards, containers/storage, containers/image, Podman, CRI-O, Stargz Snapshotter, containerd, Kubernetes

[Join this session on HopIn](https://hopin.com/events/container-plumbing-days)

## Session Details:

Pull is one of the time-consuming steps in the container lifecycle. One of the root causes is the current OCI Image Specification, because it cannot run containers before the entire image contents are locally available. To solve this issue, several OCI-alternative image formats have been proposed in the community for enabling "lazy pulling": starting up containers without waiting for the entire image. Instead, necessary chunks are fetched on-demand.

In this session, Kohei will talk about OCI-alternative but OCI-compatible lazy-pullable image formats discussed in the community and their current adoption status. This will include speed of image startup comparisons with containerd, Kubernetes, and eStargz image format.  Learn about our proposal for enabling lazy pulling on Podman and CRI-O leveraging eStargz and zstd:chunked image formats through the patch set of "additional layer store". We will also cover recent efforts to standardize a lazy-pullable image format in OCI. Through this talk, people can learn what lazy pulling is and how it can be leveraged with tools in the community.
