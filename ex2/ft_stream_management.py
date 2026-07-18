import sys
import typing


def read_file(args: list[str]) -> str | None:

    if len(args) < 2:
        return print("Usage: ft_stream_management.py <file>")

    filename = args[1]
    file: typing.IO[str]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    sys.stdout.flush()

    try:
        file = open(filename, "r")
        content = file.read()

        print(f"---\n\n{content}\n\n---")

        file.close()

        print(f"File '{filename}' closed.\n")
        return content

    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return None


def write_file(content: str) -> None:

    lines = content.splitlines()
    new_content = ""
    for line in lines:
        new_content += line + "#\n"

    print(f"Transform data:\n---\n\n{new_content}\n---")

    new_filename = get_new_file()
    if new_filename == "":
        return print("Not saving data.")
    print(f"Saving data to '{new_filename}'")
    sys.stdout.flush()
    try:
        file = open(new_filename, "w")
        file.write(new_content)
        print(f"Data saved in file '{new_filename}'.")
        file.close()

    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_filename}': {e}\n"
        )
        print("Data not saved.")


def get_new_file() -> str:

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().rstrip("\n")

    return new_filename


if __name__ == "__main__":
    content = read_file(sys.argv)

    if content is not None:
        write_file(content)
