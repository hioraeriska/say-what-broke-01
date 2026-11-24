import os

ENTRY = "Save failed: the disk is full. Delete a file you love, preferably not this one, and try again."


def resolve_output_dir():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    return out


def get_entry():
    return ENTRY


def main():
    out = resolve_output_dir()
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(get_entry())


if __name__ == "__main__":
    main()
