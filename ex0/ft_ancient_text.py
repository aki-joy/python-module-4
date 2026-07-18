import sys
import typing


def read_file(args: list[str]) -> None:

    if len(args) != 2:

        if len(args) > 2:
            print("Too many arguments provided.")

        return print("Usage: ft_ancient_text.py <file>")

    else:
        file: typing.IO[str]
        filename = args[1]
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
    print("=== Cyber Archives Recovery ===")
    read_file(sys.argv)
