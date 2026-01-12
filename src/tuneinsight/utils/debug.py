"""Utilities to debug and communicate about issues and the state of a Tune Insight instance."""

from typing import Any, Optional
import jsonpickle


def dump(thing: Any, dest: Optional[str] = None) -> str:
    """Dumps the state of a Tune Insight object to a JSON string (and optionally to file).

    This dump can be sent to your administrator to shed light on issues that you may
    encounter while using the SDK.

    Args:
        thing (Any): any object of the SDK:
        dest (Optional[str], optional): If provided, the file to which the dump is saved.

    Returns:
        str: the JSON dump of the state of the object on the Tune Insight instance.
    """
    # Under the hood, this dump is either defined at the class-level through the debug_dump
    # method, or a generic (but powerful) JSON serializer is used.
    if hasattr(thing, "debug_dump"):
        json_dump = thing.debug_dump()
    else:
        json_dump = jsonpickle.dumps(thing, unpicklable=False)
    if dest is not None:
        with open(dest, "w", encoding="utf-8") as ff:
            ff.write(json_dump)
    return json_dump
