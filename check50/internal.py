"""
Additional check50 internals exposed to extension writers in addition to the standard API
"""

from contextlib import contextmanager

# Directory containing the check and its associated files
check_dir = None

# Temporary directory in which check is being run
run_dir = None


class Register:
    def __init__(self):
        self._before_everies = set()
        self._after_everies = set()
        self._after_check = set()

    def after_check(self, func):
        """run func once at the end of the check, then discard func"""
        self._after_onces.add(func)

    def after_every(self, func):
        """run func at the end of every check"""
        self._after_everies.add(func)

    def before_every(self, func):
        """run func at the start of every check"""
        self._before_everies.add(func)

    def __enter__(self):
        for f in self._before_everies:
            f()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Only run 'afters' when check has passed
        if exc_type is not None:
            return

        while self._after_check:
            self._after_onces.pop()()

        for f in self._after_everies:
            f()


register = Register()

_data = {}
register.reset(_data.clear)

def data(**kwargs):
    _data.update(kwargs)
