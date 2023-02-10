# Windows containers: The forgotten stepchild 

**Presenters**: Jamie Magee (Microsoft)

**Session Type:** Presentation (25min)

**Topics**: Container OSes, Container/Image Security/SBOM, Containers on alternate OSes, All demo code will be released under MIT license. It is not part of an existing open source project

## Session Details:

When it comes to Linux containers, there are plenty of tools out there that can scan container images, generate Software Bill of Materials (SBOM), or list vulnerabilities. However, Windows container images are more like the forgotten stepchild in the container ecosystem. And that means we’re forgetting the countless developers using Windows containers, too.

Instead of allowing this gap to widen further, container tool authors—especially SBOM tools and vulnerability scanners—need to add support for Windows container images.

In this presentation I’ll show you how to extract version information from Windows containers images that can be used to generate SBOMs, as well as how to integrate with the Microsoft Security Updates API which can provide detailed vulnerability information.
