import os

import unittest
loader = unittest.TestLoader()
start_dir = os.getcwd() + '/test'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)