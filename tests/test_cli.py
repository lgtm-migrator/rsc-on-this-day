# 3rd party
from coincidence.regressions import AdvancedFileRegressionFixture
from consolekit.testing import CliRunner, Result

# this package
from rsc_on_this_day.__main__ import main


def test_cli(advanced_file_regression: AdvancedFileRegressionFixture) -> None:

	runner = CliRunner()

	result: Result = runner.invoke(main, catch_exceptions=False, args=["10", "13"])
	assert result.exit_code == 0
	result.check_stdout(advanced_file_regression)

	result = runner.invoke(main, catch_exceptions=False, args=["Oct", "13"])
	assert result.exit_code == 0
	result.check_stdout(advanced_file_regression)

	result = runner.invoke(main, catch_exceptions=False, args=["October", "13"])
	assert result.exit_code == 0
	result.check_stdout(advanced_file_regression)


def test_cli_clear_cache(advanced_file_regression: AdvancedFileRegressionFixture) -> None:

	runner = CliRunner()

	result: Result = runner.invoke(main, catch_exceptions=False, args=["--clear-cache"])
	assert result.exit_code == 0
	result.check_stdout(advanced_file_regression)
