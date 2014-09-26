
debian:
	sudo apt-get install make python-pygame

run:
	sh ./src/run.sh

clean:
	find . -name "*.pyc" -delete

