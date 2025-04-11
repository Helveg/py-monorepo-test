"""Hello unit test module."""

from helveg_mono_test.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello helveg-mono-test"
