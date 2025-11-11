import unittest
import task


class TestMyFunc(unittest.TestCase):

    def test_my_func(self):
        expected = "Hello World"
        self.assertEqual(task.my_func(), expected)


if __name__ == '__main__':
    unittest.main()
