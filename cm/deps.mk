WORKSPACE="$(shell git rev-parse --show-toplevel)"
MAIN="$(shell cd $(WORKSPACE) && python -m setup --name)".py

SRC=$(WORKSPACE)/src
