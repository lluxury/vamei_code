import unittest

import hello_world


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class HelloWorldTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world.hello(), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()


#第一课, test测的是模块的返回值,不是控制台的输出值,请牢记