include deps.mk

run: install-deps
	python $(SRC)/$(MAIN)

test:
	echo $@

install-deps:
	pip install -q -r $(WORKSPACE)/requirements.txt

package:
	echo $@

.PHONY: run test install-deps package
