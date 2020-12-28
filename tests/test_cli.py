# 3rd party
from click.testing import CliRunner, Result
from domdf_python_tools.testing import check_file_regression
from pytest_regressions.file_regression import FileRegressionFixture

# this package
from rsc_on_this_day.__main__ import main


def test_cli(file_regression: FileRegressionFixture):

	runner = CliRunner()
	result: Result = runner.invoke(main, catch_exceptions=False, args=["13", "10"])

	assert result.exit_code == 0
	check_file_regression(result.stdout.rstrip(), file_regression)


def test_cli_clear_cache(file_regression: FileRegressionFixture):

	runner = CliRunner()
	result: Result = runner.invoke(main, catch_exceptions=False, args=["--clear-cache"])

	assert result.exit_code == 0
	check_file_regression(result.stdout.rstrip(), file_regression)
