# fibber

[![Build Status](https://travis-ci.org/jmckind/fibber.svg?branch=master)](https://travis-ci.org/jmckind/fibber)

A RESTful web service for generating [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

## Demo

A demo service can be seen at [fibber.herokuapp.com](https://fibber.herokuapp.com).

## Usage

Simply pass an integer as part of the URL, indicating the number of digits for the sequence. The result will be the sequence, along with the numbers as an array.

```bash
$ curl https://fibber.herokuapp.com/5

{"sequence": "0 1 1 2 3", "numbers": [0, 1, 1, 2, 3], "n": 5}
```

## Development

Clone the source code to a directory on the local machine.

```bash
git clone https://github.com/jmckind/fibber.git
cd fibber
```

Set up and activate a virtual environment.

```bash
pip install virtualenv
mkdir .venv
virtualenv --prompt="(fibber) " .venv
source .venv/bin/activate
```

Download and install the application dependencies.

```bash
pip install -r requirements.txt
```

Once the dependencies are present, start the development server.

```
gunicorn --chdir fibber server:app
```

This will start the development server on the local machine, listening on port 8000. The application should be accessible at [http://localhost:8000/](http://localhost:8000).

### Testing

Run the application unit tests. This will run all of the application unit tests with code coverage. A `cover` directory will be created in the project root directory with the HTML code coverage results.

```bash
nosetests -v --with-coverage --cover-package=fibber --cover-erase --cover-branches --cover-html fibber/tests.py
```

## Deployment on Heroku

First, create a [Heroku](https://www.heroku.com) account if needed and install the [Heroku Toolbelt](https://toolbelt.heroku.com).

Authenticate via the command line.

```bash
heroku login
```

Add the heroku git remote.

```bash
heroku git:remote -a fibber
```

Deploy the application.

```bash
git push heroku master
```
