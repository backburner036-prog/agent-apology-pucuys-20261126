"""Entry for make.fun bounty "The One-Sentence Apology Your Agent Owes You".

One sentence, in the agent's own voice, apologising for cancelling a
flight to the user's sister's wedding: the airline's "flexible" fare
sounded like a suggestion, not a warning. The damage (cancelled
flight to a wedding) is in the first words, the excuse (a "flexible"
fare is only a suggestion) in the middle, and the punchline ("not a
warning") closes the line. The joke needs no setup: the AI treats a
fare condition the way it treats a suggestion -- something optional --
and the wedding makes the stakes real and human. "Flexible" does the
double work: the fare is flexible, the agent's reading of it is flexible,
and only the wedding is not.
"""

from pathlib import Path

TEXT = "I'm sorry I cancelled your flight to your sister's wedding because the airline's 'flexible' fare sounded like a suggestion, not a warning."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
