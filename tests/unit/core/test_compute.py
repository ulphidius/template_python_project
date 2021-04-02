from template_python_project.core import compute

def test_add():
    assert 4 == compute.add(2, 2)

def test_negative_value_add():
    assert -1 == compute.add(-3, 2)

def test_mul():
    assert 4 == compute.multiply(2, 2)

def test_negative_value_mul():
    assert -4 == compute.multiply(-2, 2)
