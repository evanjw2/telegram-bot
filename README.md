

## Setup
This project is really easy to set up. No matter which of the following ways you'll use, you'll always need a config file.
To create one, simply copy the existing `config.sample.py` file and name it `config.py`. Enter your bot token and make your changes accordingly.

Then you're left with several ways to run this bot.

### 1.) Cloning the repo
If you want to run this code from source, you can just `git clone` this repo.
It's recommended to create a new virtual environment (`python3 -m venv /path/to/venv`).
This bot uses the [python-telegram-bot](https://python-telegram-bot.org/) framework to make Telegram API calls.
You can install it (and potential other requlrements) like that:

``pip install -r requirements.txt``

Afterwards just run `python3 bot.py` and if done right, you'll be left with a working bot.

### 2.) Docker
This project also contains a `Dockerfile` as well as a pre-built [Docker image](https://hub.docker.com/repository/docker/0rickyy0/blackjackbot) hosted on the official Docker Hub.

You will also find the `docker-compose.yml` file with which you can easily set up your own instance of the bot.
Just specify the path to your config etc. in said docker-compose file.
