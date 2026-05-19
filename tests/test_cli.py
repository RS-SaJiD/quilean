import unittest
from click.testing import CliRunner
from quilean.cli import main

class TestCLI(unittest.TestCase):

    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(main, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Quilean", result.output)

if __name__ == '__main__':
    unittest.main()
