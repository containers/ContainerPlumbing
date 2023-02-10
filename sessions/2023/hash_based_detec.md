# Hash-based detection of confidential files in container images 

**Presenters**: Holger Gantikow, Kevin Kaftan (science+computing AG, an Atos company)

**Session Type:** Lightning Talk (5min)

**Topics**: Container/Image Security/SBOM, Trivy

## Session Details:

The risk of unintentional disclosure of confidential data increases when container images are passed on to third parties or are made publicly available.

To minimize this risk, we have extended the Trivy security scanner by a plugin that can be used to detect appropriately classified files. For this purpose, an external database is used as the data source, which contains the corresponding classifications.
