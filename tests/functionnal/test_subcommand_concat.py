from click.testing import CliRunner

from template_python_project.main import main

def test_concat():
    runner = CliRunner()
    result = runner.invoke(main, ['concat', '--first', 'hello', '--second', 'world'])

    assert result.output == "hello world\n"


def test_concat_number():
    runner = CliRunner()
    result = runner.invoke(main, ['concat', '--first', '5', '--second', '6'])

    assert result.output == "5 6\n"

def test_first_missing():
    expected_error_message = """Usage: main concat [OPTIONS]

Error: Missing option '--first' / '-f'.
"""
    runner = CliRunner()
    result = runner.invoke(main, ['concat', '--second', '2'], catch_exceptions=True)
    
    assert result.exit_code == 2
    assert expected_error_message == result.stdout

def test_second_missing():
    expected_error_message = """Usage: main concat [OPTIONS]

Error: Missing option '--second' / '-s'.
"""
    runner = CliRunner()
    result = runner.invoke(main, ['concat', '--first', '1'], catch_exceptions=True)
    
    assert result.exit_code == 2
    assert expected_error_message == result.stdout
