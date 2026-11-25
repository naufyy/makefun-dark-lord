"""The Lighthouse Keeper's Oath.

A 100-word monologue for a fantasy villain who is secretly just very
tired. The entry is a fixed text: the program writes it to
/output/entry.txt, exactly as the competition requires.
"""

from pathlib import Path

ENTRY = (
    "They took my crown, my armies, my mountain, and left me this lighthouse, "
    "so here I stand turning the lamp for ships that never thank me. "
    "The sea does not kneel or bargain. It only arrives, again and again, "
    "the way heroes once arrived at my gates. "
    "You are the first visitor in eleven years, bringing a sword to a man "
    "whose greatest enemy is the gull that steals his lunch. "
    "Strike, then. Or do not. The lamp needs oil either way, the tide will "
    "not wait for our drama, and I have a kettle going and a chair that "
    "remembers me."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
