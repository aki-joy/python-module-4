import sys
import typing


def read_file(args: list[str]) -> None:

    if len(args) < 2:
        return print("Usage: ft_ancient_text.py <file>")
    print("=== Cyber Archives Recovery ===")
    for arg in args[1:]:

        file: typing.IO[str]
        filename = arg
        print(f"Accessing file '{filename}'")

        try:
            file = open(filename, "r")
            content = file.read()
            print(f"---\n\n{content}\n\n---")
            file.close()
            print(f"File '{filename}' closed.")

        except OSError as e:
            print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    read_file(sys.argv)
