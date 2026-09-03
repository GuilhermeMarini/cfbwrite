# cfbwrite

Write a complete **MS-CFB v3** (Microsoft Compound File Binary) container from
Python — including streams that changed size.

`olefile` reads Compound Files well and can replace a stream only with data of
*exactly* the same length. That is enough to rearrange existing content and not
enough to add any, so anything that grows a stream needs the container
rebuilt. This library rebuilds it.

```python
from cfbwrite import rebuild

rebuild(src="original.rdb", dst="updated.rdb", replacements={
    ("Relays", "QPC1_TR1", "SET_D1.TXT"): new_bytes,   # any size
})
```

Two properties it is built around, because it came from a tool that writes
protection-relay settings files:

- **It verifies its own output.** The result is reopened and every stream
  compared against the source before it is handed over. A bug in the writer
  surfaces as a failed write, never as a silently corrupt file.
- **It writes atomically.** The container is built in a temporary file beside
  the destination and only then `os.replace`d into place, so a failure leaves
  the destination exactly as it was.

Extracted from [PAC CT](https://github.com/GuilhermeMarini/pac-ct).

> **Status: scaffold.** Code lands here per `docs/MIGRATION.md` §4.1 of PAC CT.

## Licence

AGPL-3.0-or-later — see [LICENSE](LICENSE).
