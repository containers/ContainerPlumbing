# Testing Container Images with Python and Pytest 

**Presenters**: Dan Čermák (SUSE)

**Session Type:** Presentation (25min)

**Topics**: Testing, CI & QA, python, pytest, pytest_container

## Session Details:

To ease the pain of testing container images, we've developed the pytest_container plugin for pytest. The plugin makes it possible to use pytest to perform tests on containers and software inside containers. You don't have to take care of pulling images, building them, or picking ports on the host. You just describe your container setup and pass it to a test function. In return, the plugin gives you a connection to the container. Using the connection, you can verify the container's state using the testinfra python framework. The plugin even cleans up after itself when you're done.

In short, pytest_container makes it possible to write tests in Python: no need to build your own framework from scratch or worry about the boring container plumbing tasks.

Join this talk to see pytest_container in action and learn how it can make your life easier!
