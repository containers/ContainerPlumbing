# Let's Fix Logging Once and For All 

**Presenters**: Peter Portante (Red Hat, Inc)

**Session Type:** Presentation (25min)

**Topics**: Container Runtimes, Container OSes, eBPF, conmon

## Session Details:

Do you know of an operating system in existence today which accepts a byte stream of data through an API, reads every byte of that data stream to determine how to add data to it and change its own operational behavior based on the contents?  The container logging sub-systems today do exactly that (see https://github.com/containers/conmon/issues/262).  We'll propose a fix for the "logging problem" using eBPF to solve this problem once and for all.  This will be an updated version of https://www.p99conf.io/session/lets-fix-logging-once-and-for-all/.
