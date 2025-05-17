PREFIX ?= /usr/local

install:
	sudo pip3 install .

uninstall:
	pip3 uninstall -y osst
