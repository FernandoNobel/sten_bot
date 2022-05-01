# Install locally the Python Package.
install:
	pip3 install -e .

# Pull changes from GitHub.
pull:
	git pull origin master

# Build the container.
build:
	-docker rmi sten-bot
	docker build -t sten-bot .

# Run the container detached.
run:
	docker run -d --name sten-bot-container sten-bot 

# Stop the container.
stop:
	docker stop sten-bot-container
	docker rm sten-bot-container

all: pull build run
