import unittest

loader = unittest.TestLoader()
suite = loader.discover("app/tests", pattern="test*.py")

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite)
