
debian:
	sudo apt-get install make python3-pygame

run:
	sh ./src/run.sh

clean:
	find . -name "*.pyc" -delete

test:
	sh ./src/run.sh test

