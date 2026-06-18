"""Tests for core module."""
import pytest
from snappdf.core import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello" in captured.out
