WORKSPACE="$(shell git rev-parse --show-toplevel)"
MAIN="$(shell cd $(WORKSPACE) && python -m setup --name)".py

SRC=$(WORKSPACE)/src
TESTS=$(WORKSPACE)/tests
CM=$(WORKSPACE)/cm

REQ=$(WORKSPACE)/requirements.txt

PIP_CONF=$(CM)/pip.conf
