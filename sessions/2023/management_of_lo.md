# Management of Long-lived Servers: The Missing Bits for Avoiding Config Drift with Declarative Configuration and Image-based Updates 

**Presenters**: Kai Lüke (Microsoft)

**Session Type:** Presentation (25min)

**Topics**: Container OSes, Flatcar Container Linux

## Session Details:

Rethinking the OS to improve server management in the era of containers and the cloud started a decade ago. The concepts present in container-optimized distributions aim for automation, declarative configuration, and reduced complexity. The user should gain reproducible server setups without config drifts. However, out of my experience in developing Flatcar Container Linux, I think the container-OS community did not fully solve this problem yet. There are some gaps to fill for reliable management of long-lived servers. Redeploying a whole cluster to apply a configuration change shouldn't be the final answer. What approaches could help to prevent config drift in the last areas where it's found? I think we should equip users with additional tools to control local state. The systemd project developed system extension (overlay) images which could play a foundational role. At the same time, distributions and upstream projects should make it easier to auto-update configuration files and ensure that default configuration is separate from user-supplied configuration. I will present some work-in-progress solutions but also hope for further explorations to happen. Only then can we address the traps and inconveniences with running manage long-lived servers.
