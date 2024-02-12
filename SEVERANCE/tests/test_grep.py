from src.grep import grep
import pytest


def test_grep():
    assert grep('^Author') == 'mbox.txt had 1798 lines that matched ^Author'
    assert grep('^X-') == 'mbox.txt had 14368 lines that matched ^X-'
