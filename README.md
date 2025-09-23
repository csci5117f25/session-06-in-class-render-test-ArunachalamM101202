# Render-test
A basic website -- just enough to test out hooking things up to render, and not much more.

We will go over steps in lecture. You should fill out the following:

## What steps do I need to do when I download this repo to get it running?
I used a macbook and did the following steps

First to download the repo
```bash
git clone https://github.com/Learn-GenAI/homework-1-404-not-found.git
code homework-1-404-not-found # I like opening VS Code from terminal
```

Then to setup environment and get it running
```bash
pipenv shell
brew install python@3.10
pipenv install
flask --app server.py run
```

## What commands starts the server?

```bash
flask --app server.py run
```

## Before render

Before render you will need to set up a more production-grade backend server process. We will do this together in lecture, once that's done you should update the command above for starting the server to be the **production grade** server.

We can create the production server first as mentioned using
```bash
pipenv install gunicorn
gunicorn server:app
```

Website is deployed at https://arun-interactive-web-session-6.onrender.com/

For loading the .env files I used

```bash
pipenv run python
```
