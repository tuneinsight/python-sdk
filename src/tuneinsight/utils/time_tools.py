import time

# Utility package to use time in a practical matter, using time as int values in nanoseconds

nanosecond: int = 1
microsecond: int = 1000 * nanosecond
millisecond: int = 1000 * microsecond
second : int = millisecond * 1000
minute: int = 60 * second
hour: int = 60 * minute
day: int = 24 * hour


def now() -> int:
    return time.time_ns()


def since(oldTime: int) -> int:
    return now() - oldTime


def sleep(nanoseconds: int):
    return time.sleep(nanoseconds / second)
