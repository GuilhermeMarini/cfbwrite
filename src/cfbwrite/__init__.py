"""Write a complete MS-CFB v3 compound file, including streams that grew.

Two entry points:

``rebuild(src, dst, replacements)``
    ``dst`` is ``src`` with some streams replaced, at any size. The result is
    verified against the source stream by stream and moved into place
    atomically, so a failure leaves ``dst`` exactly as it was.

``write_ole(dst, root_children)``
    A container built from an ``Entry`` tree you construct yourself.

    >>> from cfbwrite import Entry, write_ole
    >>> write_ole("out.cfb", [
    ...     Entry(name="Storage", is_storage=True, size=0, read=None,
    ...           children=[Entry(name="s", is_storage=False, size=3,
    ...                           read=lambda: b"abc")]),
    ... ])

Both raise `CfbWriteError` and nothing else of their own.
"""

from __future__ import annotations

from cfbwrite._writer import (
    DIFAT_IN_HEADER,
    DIFAT_PER_SECTOR,
    DIFSECT,
    DIR_ENTRY_SIZE,
    DIR_PER_SECTOR,
    ENDOFCHAIN,
    FAT_PER_SECTOR,
    FATSECT,
    FREESECT,
    MINI_CUTOFF,
    MINI_SECTOR_SIZE,
    NOSTREAM,
    SECTOR_SIZE,
    CfbWriteError,
    Entry,
    rebuild,
    write_ole,
)

__all__ = [
    "CfbWriteError",
    "Entry",
    "rebuild",
    "write_ole",
    # The format's own constants, exported because a caller building an Entry
    # tree needs them to reason about what will land in the mini stream.
    "SECTOR_SIZE",
    "MINI_SECTOR_SIZE",
    "MINI_CUTOFF",
    "DIR_ENTRY_SIZE",
    "DIR_PER_SECTOR",
    "FAT_PER_SECTOR",
    "DIFAT_PER_SECTOR",
    "DIFAT_IN_HEADER",
    "DIFSECT",
    "FATSECT",
    "ENDOFCHAIN",
    "FREESECT",
    "NOSTREAM",
]

__version__ = "1.0.0"
