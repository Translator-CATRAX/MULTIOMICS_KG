import unittest


class TestKgConfigParser(unittest.TestCase):

    def test_check_kg_subconfigs(self) -> None:
        """
        Tests the check_kg_subconfigs() function.

        Verifies that the check_kg_subconfigs() function raises a ValueError
        exception when the given kg_config is invalid, and does not raise an
        exception when the given kg_config is valid.
        """
        # Test that check_kg_subconfigs does not raise an exception when the
        # given kg_config is valid
        valid_kg_config = {
            "knowledge_graph_name": "test",
            "version_number": "1.0",
            "max_workers": 4,
            "p_value_cutoff": 0.05,
            "config_directories": [],
            "override_sqlite": "",
            "supplement_sqlite": "",
            "babel_sqlite": "",
            "kg2_sqlite": "",
            "progress_handler_timeout": 10,
            "predicates_sqlite": "",
            "confidence_model": "",
            "tfidf_vectorizer": ""
        }
        self.assertEqual(
            kgConfigParser.check_kg_subconfigs(valid_kg_config), None)
        # Test that check_kg_subconfigs raises a ValueError exception when the
        # given kg_config is invalid
        invalid_kg_config = {
            "knowledge_graph_name": "test",
            "version_number": "1.0",
            "max_workers": 4,
            "config_directories": [],
            "override_sqlite": "",
            "supplement_sqlite": "",
            "babel_sqlite": "",
            "kg2_sqlite": "",
            "progress_handler_timeout": 10,
            "predicates_sqlite": "",
            "confidence_model": "",
        }
        with self.assertRaises(ValueError):
            kgConfigParser.check_kg_subconfigs(invalid_kg_config)

    def test_check_int(self) -> None:
        self.assertEqual(
            kgConfigParser.check_int(1, ""), None)
        with self.assertRaises(ValueError):
            kgConfigParser.check_int(["list"], "")

    def test_check_float(self) -> None:
        self.assertEqual(
            kgConfigParser.check_float(1.0, ""), None)
        with self.assertRaises(ValueError):
            kgConfigParser.check_float(["list"], "")

    def test_check_str(self) -> None:
        self.assertEqual(
            kgConfigParser.check_str("str", ""), None)
        with self.assertRaises(ValueError):
            kgConfigParser.check_str(["list"], "")

    def test_check_pkl(self) -> None:
        with self.assertRaises(ValueError):
            kgConfigParser.check_pkl(r"file.xlsx", "")


class TestToolkit(unittest.TestCase):

    def test_fast_extension(self) -> None:
        self.assertEqual(
            toolkit.fast_extension("file.txt"), ".txt")
        self.assertNotEqual(
            toolkit.fast_extension("file.yaml"), ".yaml")


class TestArguments(unittest.TestCase):

    def test_length(self) -> None:
        self.assertEqual(arguments.check_len_args([1]), None)
        with self.assertRaises(IndexError):
            arguments.check_len_args([1, 2, 3])

    def test_extensions(self) -> None:
        self.assertEqual(arguments.check_config_extension([".YmL"]), None)
        with self.assertRaises(ValueError):
            arguments.check_config_extension(["AamL"])
            arguments.check_config_extension(["YYML"])


def main() -> None:
    """
    Runs all the unit tests in the given test classes.

    This function does not take any arguments and returns nothing.
    It creates a suite of tests from a list of test classes and runs them.
    Note: unittest.main() does not work with the setup.py
    """
    test_classes: list[type] = [
        TestArguments, TestKgConfigParser, TestToolkit]
    suite: unittest.TestSuite = unittest.TestSuite()
    for test_class in test_classes:
        suite.addTests(
            unittest.defaultTestLoader.loadTestsFromTestCase(test_class))
    unittest.TextTestRunner().run(suite)
