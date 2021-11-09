from cipher_ha2573 import cipher_ha2573
import pytest

@pytest.mark.parametrize("example_text, example_shift, expected", [
    ('Waystar RoyCo', 2, 'YcAuvct TqAEq'),
    ('vaulter', 1, 'wbvmufs'),
    ('STEWY', 17, 'jkVnp'),
    ('Argestes', -10, 'qhWUijUi')])
def test_cipher_encript(example_text, example_shift, expected):
    result = cipher_ha2573.cipher(example_text, example_shift)
    assert result == expected

@pytest.mark.parametrize("example_text, example_shift, expected", [
    ('roman', -1, 'qnlZm'),
    ('kendall', -27, 'JDMCzKK'),
    ('shiv', -56, 'oder'),
    ('logan', -100, 'psker')])
def test_cipher_negative(example_text, example_shift, expected):
    result = cipher_ha2573.cipher(example_text, example_shift)
    assert result == expected
    
    
@pytest.mark.parametrize("example_text, example_shift, expected", [
    ('gerri!', 3, 'jhuul!'),
    ('tom?', 105, 'upn?'),
    ('*jess', 27, '*KFTT')])
def test_cipher_symbol(example_text, example_shift, expected):
    result = cipher_ha2573.cipher(example_text, example_shift)
    assert result == expected
