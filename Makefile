
debian:
	sudo apt-get install make python-pygame

run:
	sh ./scripts/run.sh

clean:
	find . -name *.pyc -delete

