
from logging import getLogger
import falcon, json

LOG = getLogger(__name__)

class FibonacciResource:
    """
    Resource to generate a Fibonacci sequence.
    """

    min_value = 1
    max_value = 1024

    def on_get(self, req, resp, n):
        """
        Handle HTTP GET requests.

        Args:
            req: the request object.
            resp: the response object.
            n: the number of Fibonacci numbers to calculate.
        """

        try:
            value = self._validate_input(n)
            seq = self._generate_sequence(value)
            result = self._generate_result(value, seq)
        except (TypeError, ValueError):
            raise falcon.HTTPBadRequest(
                'Invalid Number',
                "Please provide an integer between %s and %s in the URL."
                    % (self.min_value, self.max_value)
            )
        except Exception as e:
            print("Unexpected error for input [%s]: %s" % (n, e.message))
            raise falcon.HTTPInternalServerError(
                'Unexpected Error', 'An unexpected error has occurred.'
            )

        resp.body = json.dumps(result)


    def _validate_input(self, n):
        """
        Validate n is a number between the MIN and MAX.

        Args:
            n: the number to validate.
        Returns:
            n when valid.
        Raises:
            TypeError: if n is not a valid integer.
            ValueError: if n in not between the min and max values.
        """

        value = int(n)
        if value is None or value < self.min_value or value > self.max_value:
            raise ValueError()
        return value


    def _generate_sequence(self, n):
        """
        Generate a Fibonacci sequence.

        Args:
            n: the number of Fibonacci numbers to calculate.
        Returns:
            a list containing the Fibonacci numbers.
        """

        sequence = [0]
        x,y = 0,1

        for i in range(n-1):
            x,y = y,x+y
            sequence.append(x)

        return sequence


    def _generate_result(self, n, seq):
        """
        Generate a dictionary containing n and the sequence.

        Args:
            n: the number of Fibonacci numbers to calculate.
            seq: list containing the Fibonacci numbers
        Returns:
            the dictionary containing the calculated values.
        """

        return {
            'n': n,
            'sequence': ' '.join(str(s) for s in seq),
            'numbers': seq
        }


app = falcon.API()
app.add_route('/{n}', FibonacciResource())
