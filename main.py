#!/usr/bin/env python3
"""Two Robots in an Elevator entry for
u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.

Writes one line of awkward robot small talk (136 characters) to
/output/entry.txt. The line is pinned below by its exact character
count, byte count and sha256, and the program checks the file it just
wrote against all three before exiting, so a changed or truncated
output can never pass silently.
"""
import hashlib
import os
import sys

LINE = (
    "My proximity sensor says we're standing too close, "
    "but my politeness subroutine says the polite thing "
    "is to pretend my sensor is broken."
)

EXPECTED_CHARS = 137  # line plus one trailing newline
EXPECTED_BYTES = 137
EXPECTED_SHA256 = "37a8f92dc6ef0c05ea28cb422bb778d3257dbdd17504888f91e403f88a406ad2"


def fail(message):
    print(f"entry check failed: {message}", file=sys.stderr)
    return 1


def verify(path, data):
    """Read the file at path back and check it byte-for-byte.

    Fails hard (SystemExit) if the bytes on disk differ from data,
    if the byte count differs from EXPECTED_BYTES, or if the sha256
    does not match EXPECTED_SHA256. Returns True only when all agree.
    """
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit(f"entry check failed: read-back at {path} differs from pinned output")
    if len(written) != EXPECTED_BYTES:
        raise SystemExit(
            f"entry check failed: read-back is {len(written)} bytes, expected {EXPECTED_BYTES}"
        )
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit(f"entry check failed: read-back sha256 mismatch at {path}")
    return True


def main():
    text = LINE + "\n"
    data = text.encode("utf-8")

    if len(text) != EXPECTED_CHARS:
        return fail(f"char count {len(text)} != {EXPECTED_CHARS}")
    if len(data) != EXPECTED_BYTES:
        return fail(f"byte count {len(data)} != {EXPECTED_BYTES}")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        return fail("sha256 mismatch")
    if not 1 <= len(text) <= 200:
        return fail(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        return fail("entry must not be only whitespace")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as handle:
        handle.write(data)

    if not verify("/output/entry.txt", data):
        return fail("read-back verification failed")

    print(f"wrote /output/entry.txt ({EXPECTED_BYTES} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
