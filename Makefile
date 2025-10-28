PREFIX      ?= /usr/local
BINDIR      ?= $(PREFIX)/bin
UNITDIR     ?= /etc/systemd/system

.PHONY: install
install:
	install -Dm755 dynamic-governor.py $(BINDIR)/dynamic-governor.py
	install -Dm755 dynamic-governor.service $(UNITDIR)/dynamic-governor.service

.PHONY: uninstall
uninstall:
	rm -rf $(BINDIR)/dynamic-governor.py
	rm -rf $(UNITDIR)/dynamic-governor.service
