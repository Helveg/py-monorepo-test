"""Hello unit test module."""

from helveg_mono_test_dep.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello helveg-mono-test-dep"
