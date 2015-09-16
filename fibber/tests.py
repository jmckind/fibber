from mock import Mock
from unittest import TestCase
import falcon, server

class TestFibonacciResource(TestCase):
    def setUp(self):
        self.fib = server.FibonacciResource()

    def test_min_value_is_set(self):
        assert self.fib.min_value is not None

    def test_max_value_is_set(self):
        assert self.fib.max_value is not None

    def test_max_value_is_greater_than_min_value(self):
        self.assertGreater(self.fib.max_value, self.fib.min_value)

    def test_validate_input_with_valid_integer(self):
        val = self.fib._validate_input(1)
        self.assertEqual(val, 1)

    def test_validate_input_with_none(self):
        with self.assertRaises(TypeError):
            self.fib._validate_input(None)

    def test_validate_input_with_negative_value(self):
        with self.assertRaises(ValueError):
            self.fib._validate_input(-1)

    def test_validate_input_less_than_min_value(self):
        with self.assertRaises(ValueError):
            self.fib._validate_input(0)

    def test_validate_input_greater_than_max_value(self):
        with self.assertRaises(ValueError):
            self.fib._validate_input(1025)

    def test_generate_sequence_with_min_value(self):
        seq = self.fib._generate_sequence(self.fib.min_value)
        self.assertListEqual(seq, [0])

    def test_generate_sequence_with_max_value(self):
        seq = self.fib._generate_sequence(self.fib.min_value)
        self.assertEqual(len(seq), self.fib.min_value)

    def test_generate_sequence_with_valid_input(self):
        seq = self.fib._generate_sequence(5)
        self.assertListEqual(seq, [0,1,1,2,3])

    def test_generate_sequence_with_invalid_input(self):
        with self.assertRaises(TypeError):
            self.fib._generate_sequence(None)

    def test_generate_sequence_with_negative_value(self):
        seq = self.fib._generate_sequence(-1)
        self.assertListEqual(seq, [0])

    def test_generate_result_with_valid_inputs(self):
        n, seq = (1, [0])
        expected = {
            'n': n,
            'sequence': '0',
            'numbers': seq
        }

        result = self.fib._generate_result(n, seq)
        self.assertDictEqual(expected, result)

    def test_generate_result_with_invalid_sequence(self):
        with self.assertRaises(TypeError):
            result = self.fib._generate_result(1, None)

    def test_on_get_with_valid_integer(self):
        mock_req = Mock(falcon.Request)
        mock_resp = Mock(falcon.Response)

        self.fib.on_get(mock_req, mock_resp, 1)
        self.assertEquals(
            '{"sequence": "0", "numbers": [0], "n": 1}',
            mock_resp.body
        )

    def test_on_get_with_invalid_integer(self):
        mock_req = Mock(falcon.Request)
        mock_resp = Mock(falcon.Response)

        with self.assertRaises(falcon.HTTPBadRequest):
            self.fib.on_get(mock_req, mock_resp, -1)

    def test_on_get_with_unexpected_error(self):
        mock_req = Mock(falcon.Request)
        mock_resp = Mock(falcon.Response)
        self.fib._generate_sequence = Mock(side_effect=Exception('Boom!'))

        with self.assertRaises(falcon.HTTPInternalServerError):
            self.fib.on_get(mock_req, mock_resp, 1)
