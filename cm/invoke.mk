include deps.mk

run: install-deps
	python $(SRC)/$(MAIN)

test: install-deps
	pytest $(TESTS)

install-deps:
	PIP_CONFIG_FILE=$(PIP_CONF) pip install -r $(REQ)

package:
	echo $@

clean:
	cd $(WORKSPACE) && rm -r venv __pycache__

.PHONY: run test install-deps package clean
