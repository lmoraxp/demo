import io
import sys
import pytest
from src import main

def test_main_prints_hello_ci_cd(monkeypatch):
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    main.main()
    output = captured_output.getvalue().strip()
    assert output == "Hello, gorgeous!"
