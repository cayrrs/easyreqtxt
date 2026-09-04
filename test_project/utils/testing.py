import pytest
import sys

try:
    import ujson as json_impl
except ImportError:
    import json as json_impl


def test_something():
    assert 1 + 1 == 2


@pytest.fixture
def sample_data():
    return {"key": "value"}
