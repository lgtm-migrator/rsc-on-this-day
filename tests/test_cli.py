# 3rd party
from coincidence import check_file_regression
from consolekit.testing import CliRunner, Result
from pytest_regressions.file_regression import FileRegressionFixture

# this package
from rsc_on_this_day.__main__ import main


def test_cli(file_regression: FileRegressionFixture):

	runner = CliRunner()

	result: Result = runner.invoke(main, catch_exceptions=False, args=["10", "13"])
	assert result.exit_code == 0
	result.check_stdout(file_regression)

	result = runner.invoke(main, catch_exceptions=False, args=["Oct", "13"])
	assert result.exit_code == 0
	result.check_stdout(file_regression)

	result = runner.invoke(main, catch_exceptions=False, args=["October", "13"])
	assert result.exit_code == 0
	result.check_stdout(file_regression)


def test_cli_clear_cache(file_regression: FileRegressionFixture):

	runner = CliRunner()

	result: Result = runner.invoke(main, catch_exceptions=False, args=["--clear-cache"])
	assert result.exit_code == 0
	result.check_stdout(file_regression)
