import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "Hello World"
        self.assertEqual(task.my_func(), expected)

    def test2(self):
        expected = "Hola World"
        self.assertEqual(task.my_func(), expected)
        
    def test3(self):
        expected = "Hello Monkey"
        self.assertIsNot(task.my_func(), expected)
    
    def test4(self):
        expected = "Hello Smurf"
        self.assertIsNot(task.my_func(), expected)


if __name__ == '__main__':
    unittest.main()
