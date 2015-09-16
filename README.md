# fibber

A RESTful web service for generating Fibonacci numbers.

## Development

Check out the source code to a directory on your local machine.

    $ git clone https://github.com/jmckind/fibber.git
    $ cd fibber

Next, set up and activate a virtual environment.

    $ pip install virtualenv
    $ mkdir .venv
    $ virtualenv --prompt="(fibber) " .venv
    $ source .venv/bin/activate

Download and install the application dependencies.

    $ pip install -r requirements.txt

Once the dependencies have been installed, start the development server.

    $ cd fibber
    $ gunicorn fibber:app

This will start the development server on the local machine, listening on port 8000. You should be able to access the application at [http://localhost:8000/](http://localhost:8000).

## Testing

Run the application tests.

    $ nosetests -v --with-coverage --cover-package=fibber --cover-erase --cover-branches --cover-html tests.py

## Deployment

Deploy on Heroku...
