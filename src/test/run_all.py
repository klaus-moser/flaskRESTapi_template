import unittest


def load_tests(loader, tests, pattern):
    """
    Discover and load all unit tests in all files named ``test_*.py`` in ``./test/``
    """
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('test', pattern='test_*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite


if __name__ == '__main__':
    unittest.main()
