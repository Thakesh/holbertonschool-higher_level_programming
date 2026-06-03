def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
