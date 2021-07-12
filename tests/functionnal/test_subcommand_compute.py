from click.testing import CliRunner

from template_python_project.main import main

def test_add():
    runner = CliRunner()
    result = runner.invoke(main, ['compute', '--compute-type', 'ADD', '--first', '2', '--second', '2'])
    
    assert int(result.output) == 4

def test_mul():
    runner = CliRunner()
    result = runner.invoke(main, ['compute', '--compute-type', 'MUL', '--first', '2', '--second', '2'])
    
    assert int(result.output) == 4

def test_compute_type_missing():
    expected_error_message = """Usage: main compute [OPTIONS]

Error: Missing option '--compute-type' / '-c'.  Choose from:
\tADD,
\tMUL.
"""
    runner = CliRunner()
    result = runner.invoke(main, ['compute', '--first', '2', '--second', '2'], catch_exceptions=True)
    
    assert result.exit_code == 2
    assert expected_error_message == result.stdout

def test_verbose_and_quiet():
    expected_error_message = """Usage: main [OPTIONS] COMMAND [ARGS]...
Try 'main --help' for help.

Error: The option quiet and verbose cannot be used together
"""
    runner = CliRunner()
    result = runner.invoke(main, ['--verbose', '--quiet', 'compute', '--compute-type', 'ADD', '--first', '2', '--second', '2'], catch_exceptions=True)
    
    assert result.exit_code == 2
    assert expected_error_message == result.stdout

def test_not_a_number_value():
    expected_error_message_second = """Usage: main compute [OPTIONS]

Error: Invalid value for '--second' / '-s': test is not a valid integer
"""
    expected_error_message_first = """Usage: main compute [OPTIONS]

Error: Invalid value for '--first' / '-f': test is not a valid integer
"""
    runner = CliRunner()
    result_second = runner.invoke(main, ['compute', '--compute-type', 'ADD', '--first', '2', '--second', 'test'], catch_exceptions=True)
    result_first = runner.invoke(main, ['compute', '--compute-type', 'ADD', '--first', 'test', '--second', '2'], catch_exceptions=True)

    assert result_second.exit_code == 2
    assert result_first.exit_code == 2
    assert expected_error_message_second == result_second.stdout
    assert expected_error_message_first == result_first.stdout

def test_missing_option():
    expected_error_message_second = """Usage: main compute [OPTIONS]

Error: Missing option '--second' / '-s'.
"""
    expected_error_message_first =  """Usage: main compute [OPTIONS]

Error: Missing option '--first' / '-f'.
"""
    runner = CliRunner()
    result_second = runner.invoke(main, ['compute', '--compute-type', 'ADD', '--first', '2'], catch_exceptions=True)
    result_first = runner.invoke(main, ['compute', '--compute-type', 'ADD', '--second', '2'], catch_exceptions=True)

    assert result_second.exit_code == 2
    assert result_first.exit_code == 2
    assert expected_error_message_second == result_second.stdout
    assert expected_error_message_first == result_first.stdout
