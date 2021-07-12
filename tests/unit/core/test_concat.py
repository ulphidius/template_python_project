from template_python_project.core import concat

def test_concat():
    assert concat.concat('first', 'sample') == 'first sample'

def test_concat_number():
    assert concat.concat(1, 'sample') == '1 sample'
    assert concat.concat('first', 2) == 'first 2'
