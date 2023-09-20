VENV_LOC=../venv/bin/activate

%:
	. $(VENV_LOC); $(MAKE) -f invoke.mk $@; deactivate
