# fibber

[![Build Status](https://travis-ci.org/jmckind/fibber.svg?branch=master)](https://travis-ci.org/jmckind/fibber)

A RESTful web service for generating Fibonacci numbers.

## Demo

A demo service can be seen at [fibber.herokuapp.com](https://fibber.herokuapp.com).

##### curl

    $ curl https://fibber.herokuapp.com/5

    {"sequence": "0 1 1 2 3", "numbers": [0, 1, 1, 2, 3], "n": 5}


##### httpie

    $ http https://fibber.herokuapp.com/5

    HTTP/1.1 200 OK
    Connection: keep-alive
    Content-Length: 61
    Content-Type: application/json; charset=utf-8
    Date: Wed, 16 Sep 2015 20:02:53 GMT
    Server: gunicorn/19.3.0
    Via: 1.1 vegur

    {
        "n": 5,
        "numbers": [
            0,
            1,
            1,
            2,
            3
        ],
        "sequence": "0 1 1 2 3"
    }

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

    $ gunicorn --chdir fibber server:app

This will start the development server on the local machine, listening on port 8000. You should be able to access the application at [http://localhost:8000/](http://localhost:8000).

## Usage

Once the application is running, hit the root URL with a number. This is size of the Fibonacci sequence.

##### curl

    $ curl localhost:8000/5

    {"sequence": "0 1 1 2 3", "numbers": [0, 1, 1, 2, 3], "n": 5}


##### httpie

    $ http localhost:8000/5

    HTTP/1.1 200 OK
    Connection: close
    Date: Wed, 16 Sep 2015 18:59:35 GMT
    Server: gunicorn/19.3.0
    content-length: 61
    content-type: application/json; charset=utf-8

    {
        "n": 5,
        "numbers": [
            0,
            1,
            1,
            2,
            3
        ],
        "sequence": "0 1 1 2 3"
    }

## Testing

Run the application unit tests.

    $ nosetests -v --with-coverage --cover-package=fibber --cover-erase --cover-branches --cover-html fibber/tests.py

This will run all of the application unit tests with code coverage. A `cover` directory will be created in the project root directory with the HTML code coverage results.

    test_generate_result_with_invalid_sequence (fibber.tests.TestFibonacciResource) ... ok
    test_generate_result_with_valid_inputs (fibber.tests.TestFibonacciResource) ... ok
    test_generate_sequence_with_invalid_input (fibber.tests.TestFibonacciResource) ... ok
    test_generate_sequence_with_max_value (fibber.tests.TestFibonacciResource) ... ok
    test_generate_sequence_with_min_value (fibber.tests.TestFibonacciResource) ... ok
    test_generate_sequence_with_negative_value (fibber.tests.TestFibonacciResource) ... ok
    test_generate_sequence_with_valid_input (fibber.tests.TestFibonacciResource) ... ok
    test_max_value_is_greater_than_min_value (fibber.tests.TestFibonacciResource) ... ok
    test_max_value_is_set (fibber.tests.TestFibonacciResource) ... ok
    test_min_value_is_set (fibber.tests.TestFibonacciResource) ... ok
    test_on_get_with_invalid_integer (fibber.tests.TestFibonacciResource) ... ok
    test_on_get_with_unexpected_error (fibber.tests.TestFibonacciResource) ... ok
    test_on_get_with_valid_integer (fibber.tests.TestFibonacciResource) ... ok
    test_validate_input_greater_than_max_value (fibber.tests.TestFibonacciResource) ... ok
    test_validate_input_less_than_min_value (fibber.tests.TestFibonacciResource) ... ok
    test_validate_input_with_negative_value (fibber.tests.TestFibonacciResource) ... ok
    test_validate_input_with_none (fibber.tests.TestFibonacciResource) ... ok
    test_validate_input_with_valid_integer (fibber.tests.TestFibonacciResource) ... ok

    Name            Stmts   Miss Branch BrMiss  Cover   Missing
    -----------------------------------------------------------
    fibber              0      0      0      0   100%
    fibber.server      33      0      6      0   100%
    -----------------------------------------------------------
    TOTAL              33      0      6      0   100%
    ----------------------------------------------------------------------
    Ran 18 tests in 0.007s

    OK

## Heroku Deployment

First, create a [Heroku](https://www.heroku.com) account if needed and install the [Heroku Toolbelt](https://toolbelt.heroku.com).

Next, log in via the command line.

    $ heroku login

Add the heroku git remote.

    $ heroku git:remote -a fibber

Finally, deploy the application.

    $ git push heroku master
