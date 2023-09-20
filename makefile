MAIN=`python -m setup --name`.py

%:
	$(MAKE) -s -C ./cm -f wrapper.mk $@
