"""Utility package to use time in a practical matter, using time as int values in nanoseconds."""

import time

# Constants to appropriately scale time values.
NANOSECOND: int = 1
MICROSECOND: int = 1000 * NANOSECOND
MILLISECOND: int = 1000 * MICROSECOND
SECOND: int = MILLISECOND * 1000
MINUTE: int = 60 * SECOND
HOUR: int = 60 * MINUTE
DAY: int = 24 * HOUR


def now() -> int:
    """Returns the current time since the epoch in nanoseconds."""
    return time.time_ns()


def since(oldTime: int) -> int:
    """Returns the time in nanoseconds between now and an older time."""
    return now() - oldTime


def sleep(nanoseconds: int):
    """Block the current thread for at least some number of nanoseconds."""
    return time.sleep(nanoseconds / SECOND)
